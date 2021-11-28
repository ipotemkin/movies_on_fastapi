from flask_restx import Resource, Namespace, reqparse
from implemented import movie_service
from utils import admin_required, auth_required

movie_ns = Namespace('movies', description="Фильмы")
parser = reqparse.RequestParser()
parser.add_argument('director_id', type=int, help='Фильтрация по id режиссера')
parser.add_argument('genre_id', type=int, help='Фильтрация по id жанра')
parser.add_argument('year', type=int, help='Фильтрация по году выпуска')


@movie_ns.route('/')
class MoviesView(Resource):
    @staticmethod
    @movie_ns.expect(parser)
    @auth_required
    def get():
        """
        Получить все фильмы / Get all movies
        Можно фильтровать по режиссеру, жанру и году выпуска / You can additionally specify director_id, genre_id, year (any mix of these parameters)
        """
        req = {key: value for key, value in parser.parse_args().items() if value is not None}
        return movie_service.get_all_by_filter(req)

    @staticmethod
    # @movie_ns.response(201, 'Created', headers={'Location': 'movies_movie_view'})
    @movie_ns.response(201, 'Created', headers={'Location': 'url нового фильма'})
    @admin_required
    def post():
        """
        Добавить новый фильм / Add a new movie
        """
        obj = movie_service.create(movie_ns.payload)
        return "", 201, {'Location': obj.id}


@movie_ns.route('/<int:mid>')
@movie_ns.doc(params={'mid': 'Идентификатор фильма'})
class MovieView(Resource):
    @staticmethod
    @auth_required
    def get(mid: int):
        """
        Получить фильм с указанным ID / Get a movie with the given mid
        """
        return movie_service.get_one(mid)

    @staticmethod
    @movie_ns.response(204, 'Updated')
    @admin_required
    def patch(mid: int):
        """
        Обновить фильм с указанным ID / Update a movie with the given mid
        """
        movie_service.update(movie_ns.payload, mid)
        return {}, 204

    @staticmethod
    @movie_ns.response(204, 'Deleted')
    @admin_required
    def delete(mid: int):
        """
        Удалить фильм с указанным ID / Delete a movie with the given mid
        """
        movie_service.delete(mid)
        return "", 204
