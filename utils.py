from flask import request, abort
import jwt
from constants import JWT_KEY, JWT_METHOD


def jwt_decode():
    if 'Authorization' not in request.headers:
        abort(401, 'Authorization Error')
    token = request.headers['Authorization'].split('Bearer ')[-1]
    try:
        decoded_jwt = jwt.decode(token, JWT_KEY, JWT_METHOD)
    except Exception as e:
        abort(401, f'JWT Decode Exception: {e}')
    else:
        return decoded_jwt


def auth_required(func):
    def wrapper(*args, **kwargs):
        jwt_decode()
        return func(*args, **kwargs)
    return wrapper


def admin_required(func):
    def wrapper(*args, **kwargs):
        decoded_jwt = jwt_decode()
        role = decoded_jwt.get('role')
        if role != 'admin':
            abort(401, 'Admin Role Required')
        return func(*args, **kwargs)
    return wrapper
