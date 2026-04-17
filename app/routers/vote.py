from fastapi import FastAPI,HTTPException,APIRouter,status,Depends
from .. import schemas,models,database,oauth2
from sqlalchemy.orm import Session

router=APIRouter(
    prefix="/vote",
)

@router.post("/",status_code=status.HTTP_201_CREATED)
def votes(vote:schemas.Vote,db:Session=Depends(database.get_db),current_user:int=Depends(oauth2.get_current_user)):
    vote_query=db.query(models.Votes).filter(models.Votes.post_id==vote.post_id,models.Votes.user_id==current_user.ID)
    found_vote=vote_query.first()

    post=db.query(models.Post).filter(models.Post.ID==vote.post_id).first()

    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Post with id :{vote.post_id} does not exists")

    if (vote.dir==1):
        if found_vote:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=f"User with id :{current_user.ID} has already like the post {vote.post_id}")
        new_vote=models.Votes(post_id=vote.post_id,user_id=current_user.ID)

        db.add(new_vote)
        db.commit()
        return {"message" :"successfully added vote"}
    
    else:
        if not found_vote:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Vote does not exist")
        
        vote_query.delete(synchronize_session=False)
        db.commit()

        return {"message":"Vote successfully deleted"}
        