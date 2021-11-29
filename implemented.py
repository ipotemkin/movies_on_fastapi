# файл для создания DAO и сервисов чтобы импортировать их везде

# book_dao = BookDAO(db.session)
# book_service = BookService(dao=book_dao)
#
# review_dao = ReviewDAO(db.session)
# review_service = ReviewService(dao=review_dao)
from dao.model.directors import Director, DirectorBM
from dao.directors import DirectorDAO
from service.directors import DirectorService

from dao.model.movies import Movie, MovieBM, MovieBMSimple
from dao.movies import MovieDAO
from service.movies import MovieService

from dao.model.genres import Genre, GenreBM
from dao.genres import GenreDAO
from service.genres import GenreService

from dao.model.users import User, UserBM
from dao.users import UserDAO
from service.users import UserService

# from dao.model.rtokens import RToken, RTokenBM
# from dao.rtokens import RTokenDAO
# from service.rtokens import RTokenService

from setup_db import db

from flask_restx import Namespace, fields

director_dao = DirectorDAO(session=db.session, model=Director, schema=DirectorBM)
director_service = DirectorService(dao=director_dao)


genre_dao = GenreDAO(session=db.session, model=Genre, schema=GenreBM)
genre_service = GenreService(dao=genre_dao)


movie_dao = MovieDAO(session=db.session, model=Movie, schema=MovieBMSimple, nested_schema=MovieBM)
movie_service = MovieService(dao=movie_dao)

user_dao = UserDAO(session=db.session, model=User, schema=UserBM)
user_service = UserService(dao=user_dao)

# rtoken_dao = RTokenDAO(session=db.session, model=RToken, schema=RTokenBM)
# rtoken_service = RTokenService(dao=rtoken_dao)

movie_ns = Namespace('movies', description="Фильмы")
director_ns = Namespace('directors', description="Режиссеры")
genre_ns = Namespace('genres', description="Жанры")

directors_model = movie_ns.model('DirectorsModel',
                                 {'id': fields.Integer(attribute='id', description='ID режиссера'),
                                  'name': fields.String(attribute='name', description='режиссер')})

genres_model = movie_ns.model('GenresModel',
                              {'id': fields.Integer(attribute='id', description='ID жанра'),
                               'name': fields.String(attribute='name', description='жанр')})

movies_model = movie_ns.model('MoviesModel',
                              {'id': fields.Integer(description='ID фильма'),
                               'title': fields.String(description='название фильма'),
                               'description': fields.String(description='описание сюжета'),
                               'rating': fields.Float(description='рейтинг'),
                               'year': fields.Integer(description='год выпуска'),
                               'director_id': fields.Integer(description='ID режиссера'),
                               'genre_id': fields.Integer(description='ID жанра'),
                               'trailer': fields.String(description='ссылка на трейлер'),
                               'director': fields.Nested(directors_model, description='словарь с именем режиссера'),
                               'genre': fields.Nested(genres_model, description='словарь с названием жанра')
                               })
