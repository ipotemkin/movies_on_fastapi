# здесь контроллеры/хендлеры/представления для обработки запросов (flask ручки).
# сюда импортируются сервисы из пакета service

# Пример
from flask import request
from flask_restx import Resource, Namespace, reqparse
# from service.directors import directorService
from dao.directors import DirectorDAO
from errors import NoContentError

director_ns = Namespace('directors')


@director_ns.route('/')
class DirectorsView(Resource):
    @staticmethod
    def get():
        """
        Get all directors
        """
        # return DirectorService(DirectorDAO()).get_directors(), 200
        return DirectorDAO.get_all()

    @staticmethod
    def post():
        """
        Add a new director
        """
        if not (new_director_json := request.json):
            raise NoContentError
        DirectorDAO.create(new_director_json)
        return "", 201


@director_ns.route('/<int:did>')
class DirectorView(Resource):
    @staticmethod
    def get(did: int):
        """
        Get a director with the given did
        """
        # return DirectorService(DirectorDAO()).get_directors(), 200
        return DirectorDAO.get_one(did)

    @staticmethod
    def patch(did: int):
        """
        Update a director with the given did
        """
        update_director_json = request.json
        if not update_director_json:
            raise NoContentError
        return DirectorDAO.update(update_director_json, did), 204

    @staticmethod
    def delete(did: int):
        """
        Delete a director with the given did
        """
        return DirectorDAO.delete(did), 204
