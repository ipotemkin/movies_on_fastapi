# здесь контроллеры/хендлеры/представления для обработки запросов (flask ручки).
# сюда импортируются сервисы из пакета service

# Пример
from flask import request
from flask_restx import Resource, Namespace  # , reqparse
# from service.directors import directorService
# from dao.directors import DirectorDAO
# from errors import NoContentError
from implemented import director_service

director_ns = Namespace('directors')


@director_ns.route('/')
class DirectorsView(Resource):
    @staticmethod
    def get():
        """
        Get all directors
        """
        return director_service.get_all()

    @staticmethod
    def post():
        """
        Add a new director
        """
        director_service.create(request.json)
        return "", 201


@director_ns.route('/<int:did>')
class DirectorView(Resource):
    @staticmethod
    def get(did: int):
        """
        Get a director with the given did
        """
        return director_service.get_one(did)

    @staticmethod
    def patch(did: int):
        """
        Update a director with the given did
        """
        return director_service.update(request.json, did), 204

    @staticmethod
    def delete(did: int):
        """
        Delete a director with the given did
        """
        return director_service.delete(did), 204
