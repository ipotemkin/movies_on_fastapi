from flask_restx import Resource, Namespace
from implemented import user_service
from utils import auth_required, admin_required

user_ns = Namespace('users', description="Пользователи")


@user_ns.route('/')
class UsersView(Resource):
    @staticmethod
    # @auth_required
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
    @auth_required
    def get(uid: int):
        """
        Get a user with the given uid
        """
        return user_service.get_one(uid)

    @staticmethod
    @admin_required
    def patch(uid: int):
        """
        Update a user with the given uid
        """
        return user_service.update(user_ns.payload, uid), 204

    @staticmethod
    @admin_required
    def delete(uid: int):
        """
        Delete a user with the given uid
        """
        return user_service.delete(uid), 204
