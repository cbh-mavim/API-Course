from typing import List
from app.schemas.schemas import ArticleBase,ArticleDisplay
from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.db import db_article
from app.auth.oauth2 import get_current_user
from app.schemas.schemas import UserBase

router = APIRouter(
    prefix="/article",
    tags = ['article']
)

#Create Article
@router.post('/',response_model=ArticleDisplay)
def create_article(request: ArticleBase,db: Session = Depends(get_db)):
    return db_article.create_article(db,request)

#Get Specific Article
@router.get("/{id}")#,response_model=ArticleDisplay)
def get_article(id:int,db: Session = Depends(get_db),current_user : UserBase =Depends(get_current_user)):
    return {
        'data' : db_article.get_article(db,id),
        'current_user' : current_user
    }


