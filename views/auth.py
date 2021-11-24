from flask_restx import Resource, Namespace
from flask import jsonify, request, abort
from implemented import user_service
from errors import NoContentError

auth_ns = Namespace('auth', description="Авторизация")


@auth_ns.route('/')
class AuthsView(Resource):
    @staticmethod
    @auth_ns.response(201, 'Created', headers={'Location': 'auth_auth_view'})
    def post():
        """
        Generate tokens
        """
        if not (data := auth_ns.payload):
            raise NoContentError
        print(data)

        user = user_service.check_password(id=data.get('id', None),
                                           username=data.get('login', None),
                                           password=data.get('password', None)
                                           )
        # user = user_service.check_password(data)

        return user
        # return jsonify(auth_ns.payload)
        # obj = auth_service.create(auth_ns.payload)
        # return "", 201, {'Location': obj.id}
        # pass

    # @staticmethod
    # @auth_ns.response(204, 'Updated', headers={'Location': 'auths_auth_view'})
    # def put():
    #     """
    #     Refresh tokens
    #     """
    #     # obj = auth_service.create(auth_ns.payload)
    #     # return "", 201, {'Location': obj.id}
    #     pass
