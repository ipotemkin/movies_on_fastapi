from setup_db import db
from pydantic import BaseModel
from typing import Optional


class Genre(db.Model):
    __tablename__ = 'genre'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    # movies = db.relationship('Movie', lazy='dynamic')


class GenreBM(BaseModel):
    id: Optional[int]
    name: str

    class Config:
        orm_mode = True
