# здесь контроллеры/хендлеры/представления для обработки запросов (flask ручки).
# сюда импортируются сервисы из пакета service

from flask import request
from flask_restx import Resource, Namespace
from implemented import director_service

director_ns = Namespace('directors', description="Режиссеры")


@director_ns.route('/')
class DirectorsView(Resource):
    @staticmethod
    def get():
        """
        Get all directors
        """
        return director_service.get_all()

    @staticmethod
    @director_ns.response(201, 'Created', headers={'Location': 'directors_director_view'})
    def post():
        """
        Add a new director
        """
        obj = director_service.create(director_ns.payload)
        return "", 201, {'Location': obj.id}


@director_ns.route('/<int:did>')
@director_ns.doc(params={'did': 'Идентификатор режиссера'})
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
