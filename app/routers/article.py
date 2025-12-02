from typing import List
from app.schemas.schemas import ArticleBase,ArticleDisplay
from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.db import db_article

router = APIRouter(
    prefix="/article",
    tags = ['article']
)

#Create Article
@router.post('/',response_model=ArticleDisplay)
def create_article(request: ArticleBase,db: Session = Depends(get_db)):
    return db_article.create_article(db,request)

#Get Specific Article
@router.get("/{id}",response_model=ArticleDisplay)
def get_article(id:int,db: Session = Depends(get_db)):
    return db_article.get_article(db,id)


