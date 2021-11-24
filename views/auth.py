from flask_restx import Resource, Namespace
from flask import jsonify, request, abort
from implemented import user_service
from errors import NoContentError
from pydantic import BaseModel
from flask_pydantic import validate

auth_ns = Namespace('auth', description="Авторизация")


class TokenRequest(BaseModel):
    login: str
    password: str


class TokenResponse(BaseModel):
    access_token: str
    refresh_token: str


@auth_ns.route('/')
class AuthsView(Resource):
    @staticmethod
    @auth_ns.response(201, 'Created', headers={'Location': 'auth_auth_view'})
    @validate()
    def post(body: TokenRequest):
        """
        Generate tokens
        """
        if user_service.check_password(username=body.login, password=body.password):
            data = body.dict()
            return TokenResponse(access_token=user_service.gen_token(data),
                                 refresh_token=user_service.gen_token(data)), 201

        return "", 401

    # @staticmethod
    # @auth_ns.response(204, 'Updated', headers={'Location': 'auths_auth_view'})
    # def put():
    #     """
    #     Refresh tokens
    #     """
    #     # obj = auth_service.create(auth_ns.payload)
    #     # return "", 201, {'Location': obj.id}
    #     pass
