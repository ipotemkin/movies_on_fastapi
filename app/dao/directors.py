from setup_db import db
from pydantic import BaseModel
from typing import Optional


class Director(db.Model):
    __tablename__ = 'director'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    # movies = db.relationship('Movie', lazy='dynamic')


class DirectorBM(BaseModel):
    id: Optional[int]
    name: str

    class Config:
        orm_mode = True
