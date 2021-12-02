from setup_db import db
from pydantic import BaseModel
from typing import Optional


class RToken(db.Model):
    __tablename__ = 'r_token'
    id = db.Column(db.Integer, primary_key=True)
    token = db.Column(db.String, nullable=False, unique=True)


class RTokenBM(BaseModel):
    id: Optional[int]
    token: str

    class Config:
        orm_mode = True
