from sqlalchemy.orm import Session
from app.schemas.schemas import UserBase
from app.models.models import DbUser
from app.db.hash import Hash
from fastapi import HTTPException, status

def create_user(db: Session, request: UserBase):
    new_user = DbUser(
        username=request.username,
        email=request.email,
        password=Hash.bcrypt(request.password)
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def get_all_user(db:Session):
    user = db.query(DbUser).all()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"There are no user's right now!")

def get_user(db:Session,id:int):
    user =  db.query(DbUser).filter(DbUser.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"The user with {id} was not found!")

def update_user(db:Session,id: int,request:UserBase):
    user = db.query(DbUser).filter(DbUser.id == id)
    if not user.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"The user with {id} was not found!")
    user.update(
        {
            DbUser.username: request.username,
            DbUser.email: request.email,
            DbUser.password: Hash.bcrypt(request.password)
        }
    )
    db.commit()

    return 'Ok'

def delete_user(db:Session,id:int):
    user = db.query(DbUser).filter(DbUser.id == id).first()
    if not user.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"The user with {id} was not found!")
    db.delete(user)
    db.commit()
    return "Ok"
