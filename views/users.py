# здесь контроллеры/хендлеры/представления для обработки запросов (flask ручки).
# сюда импортируются сервисы из пакета service

from flask import request
from flask_restx import Resource, Namespace
from implemented import user_service

user_ns = Namespace('users', description="Пользователи")


@user_ns.route('/')
class UsersView(Resource):
    @staticmethod
    def get():
        """
        Get all users
        """
        return user_service.get_all()

    @staticmethod
    @user_ns.response(201, 'Created', headers={'Location': 'users_user_view'})
    def post():
        """
        Add a new user
        """
        obj = user_service.create(user_ns.payload)
        return "", 201, {'Location': obj.id}


@user_ns.route('/<int:did>')
class UserView(Resource):
    @staticmethod
    def get(did: int):
        """
        Get a user with the given did
        """
        return user_service.get_one(did)

    @staticmethod
    def patch(did: int):
        """
        Update a user with the given did
        """
        return user_service.update(request.json, did), 204

    @staticmethod
    def delete(did: int):
        """
        Delete a user with the given did
        """
        return user_service.delete(did), 204
