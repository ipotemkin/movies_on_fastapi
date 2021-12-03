# from flask_sqlalchemy import SQLAlchemy
#
# db = SQLAlchemy()

from sqlalchemy.orm import Session
from sqlalchemy import create_engine

engine = create_engine("sqlite:///movies.db")
session = Session(bind=engine)
