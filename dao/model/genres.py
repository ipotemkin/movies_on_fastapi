# здесь модель SQLAlchemy для сущности, также могут быть дополнительные методы работы с моделью
# (но не с базой, с базой мы работает в классе DAO)

# Пример

from setup_db import db
from marshmallow import fields, Schema


class Genre(db.Model):
    __tablename__ = 'genre'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    movies = db.relationship('Movie')


class GenreSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str()
