# здесь модель SQLAlchemy для сущности, также могут быть дополнительные методы работы с моделью
# (но не с базой, с базой мы работает в классе DAO)

from setup_db import db
from dao.model.directors import DirectorBM
from dao.model.genres import GenreBM
from pydantic import BaseModel
from typing import Optional


class Movie(db.Model):
    __tablename__ = 'movie'
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String, nullable=False)
    director_id = db.Column(db.Integer, db.ForeignKey('director.id'), nullable=False)
    genre_id = db.Column(db.Integer, db.ForeignKey('genre.id'), nullable=False)
    rating = db.Column(db.Float, default=0.0)
    title = db.Column(db.String, nullable=False)
    trailer = db.Column(db.String, default="#")
    year = db.Column(db.Integer, nullable=False)
    director = db.relationship('Director')
    genre = db.relationship('Genre')

    def __repr__(self):
        return f"<Movie {self.title}>"


class MovieBMSimple(BaseModel):
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


class MovieBM(MovieBMSimple):
    director: DirectorBM
    genre: GenreBM
