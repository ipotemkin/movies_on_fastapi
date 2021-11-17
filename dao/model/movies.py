# здесь модель SQLAlchemy для сущности, также могут быть дополнительные методы работы с моделью
# (но не с базой, с базой мы работает в классе DAO)

# Пример

from setup_db import db


class Movie(db.Model):
    __tablename__ = 'movie'
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String)
    director_id = db.Column(db.Integer)  # , db.ForeignKey('director.id'))
    genre_id = db.Column(db.Integer)  # , db.ForeignKey('genre.id'))
    rating = db.Column(db.Float)
    title = db.Column(db.String)
    trailer = db.Column(db.String)
    year = db.Column(db.Integer)
    # directors = db.relationship('Director')

    def __repr__(self):
        return f"<Movie({self.title})>"

# OPTION #1
from marshmallow import fields, Schema  # noqa


class MovieSchema(Schema):
    id = fields.Int(dump_only=True)
    description = fields.Str()
    director_id = fields.Int()
    genre_id = fields.Int()
    rating = fields.Float()
    title = fields.Str()
    trailer = fields.Str()
    year = fields.Int()


# OPTION #2
from pydantic import BaseModel  # noqa
from typing import Optional  # noqa


class MovieBM(BaseModel):
    id: Optional[int]
    description: str
    director_id: int
    genre_id: int
    rating: float
    title: str
    trailer: str
    year: int

    class Config:
        orm_mode = True
