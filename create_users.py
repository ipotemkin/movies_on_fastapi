# create_data.py

from flask import Flask, request
from flask_restx import Api, Resource
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movies.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String)
    password = db.Column(db.String)
    role = db.Column(db.String)

    def __repr__(self):
        return f"<User {self.username}>"


# db.drop_all()
db.create_all()

u1 = User(username="vasya", password="my_little_pony", role="user")
u2 = User(username="oleg", password="qwerty", role="user")
u3 = User(username="oleg", password="P@ssw0rd", role="admin")

with db.session.begin():
    db.session.add_all([u1, u2, u3])


res = User.query.all()
print(res)
