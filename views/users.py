from flask import request, abort
from flask_restx import Resource, Namespace
from implemented import user_service
import jwt
from constants import JWT_KEY, JWT_METHOD

user_ns = Namespace('users', description="Пользователи")


def auth_required(func):
    def wrapper(*args, **kwargs):
        if 'Authorization' not in request.headers:
            abort(401, 'Authorization Error')
        token = request.headers['Authorization'].split('Bearer ')[-1]
        try:
            user = jwt.decode(token, JWT_KEY, JWT_METHOD)
        except Exception as e:
            abort(401, f'JWT Decode Exception: {e}')
        return func(*args, **kwargs)

    return wrapper


@user_ns.route('/')
class UsersView(Resource):
    @staticmethod
    @auth_required
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


@user_ns.route('/<int:uid>')
@user_ns.doc(params={'uid': 'Идентификатор пользователя'})
class UserView(Resource):
    @staticmethod
    # @auth_required
    def get(uid: int):
        """
        Get a user with the given uid
        """
        return user_service.get_one(uid)

    @staticmethod
    def patch(uid: int):
        """
        Update a user with the given uid
        """
        return user_service.update(request.json, uid), 204

    @staticmethod
    def delete(uid: int):
        """
        Delete a user with the given uid
        """
        return user_service.delete(uid), 204
