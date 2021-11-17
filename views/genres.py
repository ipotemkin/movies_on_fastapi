# здесь контроллеры/хендлеры/представления для обработки запросов (flask ручки).
# сюда импортируются сервисы из пакета service

# Пример
from flask import request
from flask_restx import Resource, Namespace, reqparse
# from service.genres import genreService
from dao.genres import GenreDAO
from errors import NoContentError

genre_ns = Namespace('genres')


@genre_ns.route('/')
class GenresView(Resource):
    @staticmethod
    def get():
        """
        Get all genres
        """
        # return GenreService(GenreDAO()).get_genres(), 200
        return GenreDAO.get_all_genres()

    @staticmethod
    def post():
        """
        Add a new genre
        """
        if not (new_genre_json := request.json):
            raise NoContentError
        GenreDAO.make_genre(new_genre_json)
        return "", 201


@genre_ns.route('/<int:gid>')
class GenreView(Resource):
    @staticmethod
    def get(gid: int):
        """
        Get a genre with the given gid
        """
        # return GenreService(GenreDAO()).get_genres(), 200
        return GenreDAO.get_genre_by_id(gid)

    @staticmethod
    def patch(gid: int):
        """
        Update a genre with the given gid
        """
        update_genre_json = request.json
        if not update_genre_json:
            raise NoContentError
        return GenreDAO.update_genre(update_genre_json, gid), 204

    @staticmethod
    def delete(gid: int):
        """
        Delete a genre with the given gid
        """
        return GenreDAO.delete_genre(gid), 204
