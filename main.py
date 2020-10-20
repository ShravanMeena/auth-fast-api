from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from auth import models, schemas, handlers
from auth.database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/users/", response_model=schemas.UserShow)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_instance = handlers.user_info_by_username(db, username= user.username)
    if db_instance:
        raise HTTPException(status_code=400, detail="User already registered")
    return handlers.create_user(db, user)


@app.get("/users/")
def get_users(start: int = 0, end: int = 100, db: Session = Depends(get_db)):
    return handlers.user_info_all(db, skip=start, limit=end)