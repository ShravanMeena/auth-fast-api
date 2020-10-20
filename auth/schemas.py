from typing import Optional, List
from pydantic import BaseModel
from datetime import datetime


# user activities schemas

class UserActivity(BaseModel):
    activity_type: str
    description: str
    user_id: int


class UserActivityCreate(UserActivity):
    pass


class UserActivityShow(UserActivity):
    id: int
    recorded: datetime

    class Config:
        orm_mode = True

# user schemas
class User(BaseModel):
    username: str
    full_name: str
    email: str

class UserCreate(User):
    password: str
    pass


class UserShow(User):
    id: int
    added: datetime
    updated: datetime
    last_logged_in: datetime
    is_active: bool
    is_agreed: bool
    is_logged_in: bool
    activities: List[UserActivity] = []
    
    class Config:
        orm_mode= True
