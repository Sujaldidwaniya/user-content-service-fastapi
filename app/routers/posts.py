from fastapi import APIRouter, Depends, HTTPException, status, Response
from sqlalchemy.orm import Session
from typing import List,Optional
from .. import models, schemas, oauth2
from ..database import get_db

router = APIRouter(prefix="/posts", tags=["Posts"])


@router.get("/", response_model=List[schemas.Post])
def get_posts(db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user),limit:int=10,skip:int=0,search:Optional[str]=""):
    posts = db.query(models.Post).filter(models.Post.title.contains(search)).limit(limit).offset(skip).all()

    if not posts:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="No Posts found")
    
    return [
        {
            "ID": post.ID,
            "title": post.title,
            "content": post.content,
            "created_at":post.created_at,
            "owner_id": post.user_id,
            "owner":post.owner
        }
        for post in posts
    ]



@router.post("/", response_model=schemas.Post, status_code=status.HTTP_201_CREATED)
def create_post(post: schemas.PostCreate, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    new_post = models.Post(user_id=current_user.ID, **post.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)

    return {
        "ID": new_post.ID,
        "title": new_post.title,
        "content": new_post.content,
        "created_at":new_post.created_at,
        "owner_id": new_post.user_id,
        "owner":new_post.owner
    }


@router.get("/{id}", response_model=schemas.Post)
def get_post(id: int, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    post = db.query(models.Post).filter(models.Post.ID == id).first()

    if not post:
        raise HTTPException(status_code=404, detail="Post not found")

    return {
        "ID": post.ID,
        "title": post.title,
        "content": post.content,
        "created_at":post.created_at,
        "owner_id": post.user_id,
        "owner":post.owner
    }


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    post = db.query(models.Post).filter(models.Post.ID == id)

    if post.first() is None:
        raise HTTPException(status_code=404, detail="Post not found")

    post.delete(synchronize_session=False)
    db.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.put("/{id}", response_model=schemas.Post)
def update_post(id: int, updated_post: schemas.PostCreate, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    post_query = db.query(models.Post).filter(models.Post.ID == id)

    post = post_query.first()

    if post is None:
        raise HTTPException(status_code=404, detail="Post not found")

    post_query.update(updated_post.dict(), synchronize_session=False)
    db.commit()

    updated = post_query.first()

    return {
        "ID": updated.ID,
        "title": updated.title,
        "created_at":updated.created_at,
        "content": updated.content,
        "owner_id": updated.user_id,
        "owner":updated.owner
    }