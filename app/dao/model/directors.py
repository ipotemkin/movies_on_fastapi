# from setup_db import db
from pydantic import BaseModel
from typing import Optional
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from setup_db import Base


class Director(Base):
    __tablename__ = 'director'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    # movies = db.relationship('Movie', lazy='dynamic')


class DirectorBM(BaseModel):
    id: Optional[int]
    name: str

    class Config:
        orm_mode = True


class DirectorUpdateBM(BaseModel):
    name: str

    class Config:
        orm_mode = True
