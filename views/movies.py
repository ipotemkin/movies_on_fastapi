# здесь контроллеры/хендлеры/представления для обработки запросов (flask ручки).
# сюда импортируются сервисы из пакета service

# Пример
from flask import request
from flask_restx import Resource, Namespace, reqparse
from implemented import movie_service

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
        You can additionally specify director_id, genre_id, year (any mix of these parameters)
        """
        director_id = parser.parse_args()['director_id']
        genre_id = parser.parse_args()['genre_id']
        year = parser.parse_args()['year']
        return movie_service.get_all_by_filter(director_id=director_id, genre_id=genre_id, year=year)

    @staticmethod
    def post():
        """
        Add a new movie
        """
        movie_service.create(request.json)
        return "", 201


@movie_ns.route('/<int:mid>')
class MovieView(Resource):
    @staticmethod
    def get(mid: int):
        """
        Get a movie with the given mid
        """
        return movie_service.get_one(mid)

    @staticmethod
    def patch(mid: int):
        """
        Update a movie with the given mid
        """
        movie_service.update(request.json, mid)
        return "", 204

    @staticmethod
    def delete(mid: int):
        """
        Delete a movie with the given mid
        """
        movie_service.delete(mid)
        return "", 204


# @movie_ns.route('/title')
# class MoviesTitleView(Resource):
#     @staticmethod
#     def get():
#         if not (what := request.args.get('s')):
#             raise NoContentError
#         return MovieDAO.search('title', what)
