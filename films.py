# основной файл приложения. здесь конфигурируется фласк, сервисы, SQLAlchemy и все остальное что требуется
# для приложения. этот файл часто является точкой входа в приложение

from flask import Flask
from flask_restx import Api
from setup_db import db
from config import Config
from error_handlers import reg_error_handlers

from dao.model.movies import Movie
from dao.model.directors import Director
from dao.model.genres import Genre
from dao.model.users import User
from dao.model.rtokens import RToken, RTokenBM
from dao.rtokens import RTokenDAO
from service.rtokens import RTokenService

from views.movies import movie_ns
from views.directors import director_ns
from views.genres import genre_ns
from views.users import user_ns
from views.auth import auth_ns

from flask_migrate import Migrate


# функция создания основного объекта app
def create_app(config_object):
    app_ = Flask(__name__)
    app_.config.from_object(config_object)
    app_.url_map.strict_slashes = False
    register_extensions(app_)
    reg_error_handlers(app_)

    # to delete obsolete refresh tokens from DB
    rtoken_dao = RTokenDAO(session=db.session, model=RToken, schema=RTokenBM)
    rtoken_service = RTokenService(dao=rtoken_dao)
    with app_.app_context():
        rtoken_service.del_expired()

    return app_


# функция подключения расширений (Flask-SQLAlchemy, Flask-RESTx, ...)
def register_extensions(app_):
    db.init_app(app_)
    migrate = Migrate(app_, db)

    # authorizations = {
    #     'apikey': {
    #         'type': 'apiKey',
    #         'in': 'header',
    #         'name': 'Authorization',
    #         'tokenUrl': '/auth',
    #         'flow': 'implicit',
    #         'authorizationUrl': 'localhost:10001/auth'
    #     },
    #     'admin_key': {
    #         'type': 'admin_key',
    #         'in': 'header',
    #         'name': 'Authorization'
    #     }
    # }
    # api = Api(authorizations=authorizations)

    api = Api()
    api.init_app(app_, vrsion='1.0', title='REST API on Flask')  # , authorizations=authorizations)
    api.add_namespace(movie_ns)
    api.add_namespace(director_ns)
    api.add_namespace(genre_ns)
    api.add_namespace(user_ns)
    api.add_namespace(auth_ns)

    # create_data(app, db)


def create_data(app, db):
    with app.app_context():
        db.create_all()

        # создать несколько сущностей чтобы добавить их в БД

        # with db.session.begin():
        #     db.session.add_all(здесь список созданных объектов)


app = create_app(Config())


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'Movie': Movie, 'Director': Director, 'Genre': Genre, 'User': User, 'RToken': RToken}


if __name__ == '__main__':
    app.run(host="localhost", port=10001, debug=True)
