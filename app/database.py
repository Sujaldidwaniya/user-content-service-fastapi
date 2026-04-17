from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from .config import settings
import os

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(
    DATABASE_URL,
    connect_args={"sslmode": "require"}
)

SessionLocal=sessionmaker(autoflush=False,autocommit=False,bind=engine)

Base=declarative_base()

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()


# while True:

#     try:
#         conn=psycopg2.connect(host='localhost',database='fastapi',user='postgres',password='Sujal@197899',cursor_factory=RealDictCursor)
#         cursor=conn.cursor()
#         print("Database connection is successfull")
#         break

#     except Exception as error:
#         print("Database connection failed")
#         print("Error is  :",error)
#         time.sleep(2)