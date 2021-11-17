# здесь контроллеры/хендлеры/представления для обработки запросов (flask ручки).
# сюда импортируются сервисы из пакета service

# Пример
from flask import request
from flask_restx import Resource, Namespace, reqparse
from service.movies import MovieService
from dao.movies import MovieDAO
from errors import NoContentError

movie_ns = Namespace('movies')
parser = reqparse.RequestParser()
parser.add_argument('director_id', type=int)
parser.add_argument('genre_id', type=int)
parser.add_argument('year', type=int)


@movie_ns.route('/')
class MoviesView(Resource):
    @staticmethod
    @movie_ns.expect(parser)
    def get():
        """
        Get all movies
        """
        if director_id := parser.parse_args()['director_id']:
            return MovieDAO.get_all_movies_by_director_id(director_id)

        if genre_id := parser.parse_args()['genre_id']:
            return MovieDAO.get_all_movies_by_genre_id(genre_id)

        if year := parser.parse_args()['year']:
            return MovieDAO.get_all_movies_by_year(year)

        # return MovieService(MovieDAO()).get_movies(), 200
        return MovieDAO.get_all_movies()

    @staticmethod
    def post():
        """
        Add a new movie
        """
        if not (new_movie_json := request.json):
            raise NoContentError
        MovieDAO.make_movie(new_movie_json)
        return "", 201


@movie_ns.route('/<int:mid>')
class MovieView(Resource):
    @staticmethod
    def get(mid: int):
        """
        Get a movie with the given mid
        """
        # return MovieService(MovieDAO()).get_movies(), 200
        return MovieDAO.get_movie_by_id(mid)

    @staticmethod
    def patch(mid: int):
        """
        Update a movie with the given mid
        """
        update_movie_json = request.json
        if not update_movie_json:
            raise NoContentError
        return MovieDAO.update_movie(update_movie_json, mid), 204

    @staticmethod
    def delete(mid: int):
        """
        Delete a movie with the given mid
        """
        return MovieDAO.delete_movie(mid), 204
