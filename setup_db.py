# from flask_sqlalchemy import SQLAlchemy
#
# db = SQLAlchemy()

from sqlalchemy.orm import Session, declarative_base
from sqlalchemy import create_engine

engine = create_engine("sqlite:///movies.db",
                       connect_args={'check_same_thread': False})
session = Session(bind=engine)

Base = declarative_base()
