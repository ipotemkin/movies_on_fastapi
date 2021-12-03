from pydantic import BaseModel
from typing import Optional
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float, ForeignKey
# from app.dao.model.directors import Director
# from app.dao.model.genres import Genre
from sqlalchemy.orm import relationship

Base = declarative_base()


class Movie(Base):
    __tablename__ = 'movie'
    id = Column(Integer, primary_key=True)
    description = Column(String, nullable=False)
    director_id = Column(Integer, ForeignKey('director.id'), nullable=False)
    genre_id = Column(Integer, ForeignKey('genre.id'), nullable=False)
    rating = Column(Float, default=0.0)
    title = Column(String, nullable=False)
    trailer = Column(String, default="#")
    year = Column(Integer, nullable=False)
    # director = relationship('Director')
    # genre = relationship('Genre')

    def __repr__(self):
        return f"<Movie {self.title}>"


# пришлось добавить сюда описание классов Genre и Director, чтобы работал ForeignKey
class Genre(Base):
    __tablename__ = 'genre'
    id = Column(Integer, primary_key=True)
    name = Column(String)


class Director(Base):
    __tablename__ = 'director'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    # movies = db.relationship('Movie', lazy='dynamic')


class MovieUpdateBM(BaseModel):
    description: str
    director_id: int
    genre_id: int
    rating: float
    title: str
    trailer: Optional[str]
    year: int

    class Config:
        orm_mode = True


class MovieBMSimple(MovieUpdateBM):
    id: Optional[int]


class MovieBM(BaseModel):
    id: Optional[int]
    description: str
    director_id: int
    genre_id: int
    rating: float
    title: str
    trailer: Optional[str]
    year: int

    class Config:
        orm_mode = True

    # director: DirectorBM
    # genre: GenreBM

