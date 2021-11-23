# здесь контроллеры/хендлеры/представления для обработки запросов (flask ручки).
# сюда импортируются сервисы из пакета service

from flask import request
from flask_restx import Resource, Namespace, reqparse
from implemented import genre_service

genre_ns = Namespace('genres', description="Жанры")


@genre_ns.route('/')
class GenresView(Resource):
    @staticmethod
    def get():
        """
        Get all genres
        """
        return genre_service.get_all()

    @staticmethod
    @genre_ns.response(201, 'Created', headers={'Location': 'genres_genre_view'})
    def post():
        """
        Add a new genre
        """
        obj = genre_service.create(genre_ns.payload)
        return "", 201, {'Location': obj.id}


@genre_ns.route('/<int:gid>')
class GenreView(Resource):
    @staticmethod
    def get(gid: int):
        """
        Get a genre with the given gid
        """
        return genre_service.get_one(gid)

    @staticmethod
    def patch(gid: int):
        """
        Update a genre with the given gid
        """
        genre_service.update(request.json, gid)
        return "", 204

    @staticmethod
    def delete(gid: int):
        """
        Delete a genre with the given gid
        """
        genre_service.delete(gid)
        return "", 204
