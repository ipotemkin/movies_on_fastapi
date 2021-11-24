from setup_db import db
from pydantic import BaseModel
from typing import Optional


class User(db.Model):
    __tablename__ = 'user'
    # __bind_key__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String)
    role = db.Column(db.String)

    def __repr__(self):
        return f"<User: id={self.id}, username={self.username}, role={self.role}>"


class UserBM(BaseModel):
    id: Optional[int]
    username: str
    password: Optional[str]
    role: str

    class Config:
        orm_mode = True
