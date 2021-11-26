from flask_restx import Resource, Namespace
from flask import abort
from implemented import user_service
from pydantic import BaseModel
from flask_pydantic import validate

auth_ns = Namespace('auth', description="Авторизация")


class TokenRequest(BaseModel):
    username: str
    password: str

    class Config:
        orm_mode = True


class TokenResponse(BaseModel):
    access_token: str
    refresh_token: str

    class Config:
        orm_mode = True


class RefreshTokensRequest(BaseModel):
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
        user = user_service.get_all_by_filter({'username': body.username})[0]

        if (password_hash := user.get('password', None)) is None:
            return {'error': 'No password set'}, 400

        if not user_service.check_password_with_hash(user_password=body.password, password_hash=password_hash):
            abort(401, {'error': 'Wrong password'})

        return user_service.gen_jwt({'username': user['username'], 'role': user['role']}), 201

    @staticmethod
    @auth_ns.response(204, 'Updated', headers={'Location': 'auths_auth_view'})
    @validate()
    def put(body: RefreshTokensRequest):
        """
        Refresh tokens
        """
        if not user_service.check_refresh_token(body.refresh_token):
            abort(401, {'error': 'Refresh token non valid'})

        return user_service.refresh_jwt(body.refresh_token), 201
