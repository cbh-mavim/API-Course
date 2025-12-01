from fastapi import APIRouter, Depends
from app.schemas.schemas import UserDisplay,UserBase
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.db import db_user
from typing import List

router = APIRouter(
    prefix="/user",
    tags=["user"]
)

@router.post("/",response_model=UserDisplay)
def create_user(request: UserBase, db: Session = Depends(get_db)):
    return db_user.create_user(db, request)

#Read all users
@router.get("/",response_model=List[UserDisplay])
def get_all_users(db:Session = Depends(get_db)):
    return db_user.get_all_user(db)

@router.get('/{id}',response_model= UserDisplay)
def get_user(id: int,db:Session = Depends(get_db)):
    return db_user.get_user(db,id)

@router.post("/{id}/update",response_model=UserDisplay)
def update_user(id:int, request: UserBase, db:Session = Depends(get_db)):
    return db_user.update_user(db,id,request)

@router.delete("/{id}",response_model=UserDisplay)
def delete_user(id:int,db : Session = Depends(get_db)):
    return db_user.delete_user(db,id)

