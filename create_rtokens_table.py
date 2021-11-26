from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from pydantic import BaseModel
from typing import Optional


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movies.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class RToken(db.Model):
    __tablename__ = 'r_token'
    id = db.Column(db.Integer, primary_key=True)
    token = db.Column(db.String, nullable=False, unique=True)


class RTokenBM(BaseModel):
    id: Optional[int]
    name: str

    class Config:
        orm_mode = True


db.create_all()

rt1 = RToken(token="trial_refresh_token")

with db.session.begin():
    db.session.add(rt1)
    db.session.commit()


res = RToken.query.all()
print(res)
