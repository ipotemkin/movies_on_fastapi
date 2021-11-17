# здесь контроллеры/хендлеры/представления для обработки запросов (flask ручки).
# сюда импортируются сервисы из пакета service

# Пример
from flask_restx import Resource, Namespace
from service.movies import MovieService
from dao.movies import MovieDAO

movie_ns = Namespace('movies')


@movie_ns.route('/')
class MoviesView(Resource):
    @staticmethod
    def get():
        # movie_dao = MovieDAO()
        # movie_service = MovieService(movie_dao)
        # return MovieService(MovieDAO()).get_movies(), 200
        return MovieDAO.get_all_movies()

    # def post(self):
    #     return "", 201


@movie_ns.route('/<int:mid>')
class MovieView(Resource):
    @staticmethod
    def get(mid: int):
        # movie_dao = MovieDAO()
        # movie_service = MovieService(movie_dao)
        # return MovieService(MovieDAO()).get_movies(), 200
        return MovieDAO.get_movie_by_id(mid)
