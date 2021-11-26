# здесь контроллеры/хендлеры/представления для обработки запросов (flask ручки).
# сюда импортируются сервисы из пакета service

from flask import request
from flask_restx import Resource, Namespace
from implemented import genre_service
from utils import auth_required, admin_required

genre_ns = Namespace('genres', description="Жанры")


@genre_ns.route('/')
class GenresView(Resource):
    @staticmethod
    @auth_required
    def get():
        """
        Get all genres
        """
        return genre_service.get_all()

    @staticmethod
    @genre_ns.response(201, 'Created', headers={'Location': 'genres_genre_view'})
    @admin_required
    def post():
        """
        Add a new genre
        """
        obj = genre_service.create(genre_ns.payload)
        return "", 201, {'Location': obj.id}


@genre_ns.route('/<int:gid>')
@genre_ns.doc(params={'gid': 'Идентификатор жанра'})
class GenreView(Resource):
    @staticmethod
    @auth_required
    def get(gid: int):
        """
        Get a genre with the given gid
        """
        return genre_service.get_one(gid)

    @staticmethod
    @admin_required
    def patch(gid: int):
        """
        Update a genre with the given gid
        """
        genre_service.update(request.json, gid)
        return "", 204

    @staticmethod
    @admin_required
    def delete(gid: int):
        """
        Delete a genre with the given gid
        """
        genre_service.delete(gid)
        return "", 204
