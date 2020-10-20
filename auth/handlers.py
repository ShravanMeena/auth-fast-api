from sqlalchemy.orm import Session
from auth import models, schemas

def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = user.password + "bahothard"
    db_instance = models.User(username= user.username, full_name= user.full_name, email= user.full_name, password= hashed_password)
    db.add(db_instance)
    db.commit()
    db.refresh(db_instance)
    return db_instance

def create_user_activiy(db: Session, user_activity: schemas.UserActivityCreate, user_id: int):
    db_instance = models.UserActivity(**user_activity.dict(), user_id= user_id)
    db.add(db_instance)
    db.commit()
    db.refresh(db_instance)
    return db_instance


def user_info_all(db: Session, skip: int = 0, limit: int = 100):
    db_instance = db.query(models.User).offset(skip).limit(limit).all()
    return db_instance


def user_info_by_id(db: Session, user_id: int):
    db_instance = db.query(models.User).filter(models.User.id == user_id).first()
    return db_instance


def user_info_by_username(db: Session, username: str):
    db_instance = db.query(models.User).filter(models.User.username == username).first()
    return db_instance