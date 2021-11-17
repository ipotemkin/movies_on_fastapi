from error_handlers import reg_error_handlers
from setup_db import db
from flask import Flask
from flask_restx import Api
from config import Config
from views.movies import movie_ns
from views.directors import director_ns
from views.genres import genre_ns
from dao.model.movies import Movie
from dao.model.directors import Director
from dao.model.genres import Genre


# функция создания основного объекта app
def create_app(config_object):
    app_ = Flask(__name__)
    app_.config.from_object(config_object)
    register_extensions(app_)
    reg_error_handlers(app_)
    return app_


# функция подключения расширений (Flask-SQLAlchemy, Flask-RESTx, ...)
def register_extensions(app_):
    db.init_app(app_)
    api = Api(app_)
    api.add_namespace(movie_ns)
    api.add_namespace(director_ns)
    api.add_namespace(genre_ns)
    # create_data(app, db)


# функция
def create_data(app, db):
    with app.app_context():
        db.create_all()

        # создать несколько сущностей чтобы добавить их в БД

        # with db.session.begin():
        #     db.session.add_all(здесь список созданных объектов)


app = create_app(Config())
# app.debug = True

# m_dict = {
#     # "id": 22,
#     "description": "Владелец ранчо",
#     "director_id": 1,
#     "genre_id": 17,
#     "rating": 8.6,
#     "title": "Йеллоустоун",
#     "trailer": "https://www.youtube.com/watch?v=UKei_d0cbP4",
#     "year": 2018
# }
#
# with app.app_context():
#     m21 = Movie(**m_dict)
#     db.session.add(m21)
#     db.session.commit()
