from .database import Base
from sqlalchemy import Column,Integer,String,TIMESTAMP,ForeignKey
from sqlalchemy.sql.expression import text
from sqlalchemy.orm import relationship

class Post(Base):
    __tablename__="Posts"

    ID=Column(Integer,primary_key=True,nullable=False)
    title=Column(String,nullable=False)
    content=Column(String,nullable=False)
    created_at=Column(TIMESTAMP(timezone=True),nullable=False,server_default=text('now()'))
    user_id=Column(Integer,ForeignKey("User.ID",ondelete="CASCADE"),nullable=False)
    owner=relationship("User")

class User(Base):
    __tablename__="User"

    ID=Column(Integer,nullable=False,primary_key=True)
    email=Column(String,nullable=False,unique=True)
    password=Column(String,nullable=False,unique=True)
    created_at=Column(TIMESTAMP(timezone=True),nullable=False,server_default=text('now()'))
    phone_number=Column(String)

class Votes(Base):
    __tablename__="votes"
    user_id=Column(Integer,ForeignKey("User.ID",ondelete="CASCADE"),primary_key=True)
    post_id=Column(Integer,ForeignKey("Posts.ID",ondelete="CASCADE"),primary_key=True)