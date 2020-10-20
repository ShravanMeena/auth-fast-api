from sqlalchemy import Column, Integer, String, Boolean, ForeignKey,DateTime
from datetime import datetime
from sqlalchemy.orm import relationship

from auth.database import Base

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    full_name = Column(String, index=True)
    email = Column(String, index=True)
    password = Column(String)
    added = Column(DateTime, default=datetime.now)
    updated = Column(DateTime, default=datetime.now)
    last_logged_in = Column(DateTime, default=datetime.now)
    is_logged_in = Column(Boolean, default=False)
    is_active = Column(Boolean, default=False)
    is_agreed = Column(Boolean, default=False)

    activities = relationship('UserActivity', back_populates='users')


class UserActivity(Base):
    __tablename__ = "activities"

    id = Column(Integer, primary_key=True, index=True)
    activity_type = Column(String, index=True)
    description = Column(String)
    recorded = Column(DateTime, default=datetime.now)
    user_id = Column(Integer, ForeignKey('users.id'))

    users = relationship('User', back_populates='activities')