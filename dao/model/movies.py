# здесь модель SQLAlchemy для сущности, также могут быть дополнительные методы работы с моделью
# (но не с базой, с базой мы работает в классе DAO)

# Пример

from setup_db import db
from marshmallow import fields, Schema


class Movie(db.Model):
    __tablename__ = 'movie'
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String)
    director_id = db.Column(db.Integer, db.ForeignKey('director.id'))
    genre_id = db.Column(db.Integer, db.ForeignKey('genre.id'))
    rating = db.Column(db.Float)
    title = db.Column(db.String)
    trailer = db.Column(db.String)
    year = db.Column(db.Integer)
    directors = db.relationship('Director')


class MovieSchema(Schema):
    id = fields.Int(dump_only=True)
    description = fields.Str()
    director_id = fields.Int()
    genre_id = fields.Int()
    rating = fields.Float()
    title = fields.Str()
    trailer = fields.Str()
    year = fields.Int()
