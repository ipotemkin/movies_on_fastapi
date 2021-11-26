import hashlib
import hmac

import jwt
from constants import PWD_HASH_SALT, PWD_HASH_ITERATIONS
from constants import JWT_KEY, JWT_METHOD, AC_TOKEN_EXP_TIME_MIN, R_TOKEN_EXP_TIME_DAYS
from service.basic import BasicService
from errors import BadRequestError, NotFoundError
import datetime
import calendar
from pydantic import BaseModel

# TODO: Нужно ли передавать пароль для генерации токена?
# TODO: Какую информацию о пользователе нужно передать для генерации токена
# TODO: Чем refresh_token отличается от access_token?
# TODO: Какой код возврата при генерации токенов?


class UserForTokenModel(BaseModel):
    username: str
    role: str


class TokenModel(UserForTokenModel):
    exp: int


class UserService(BasicService):
    @staticmethod
    def get_hash(password):
        return hashlib.pbkdf2_hmac(
            'sha256',
            password.encode('utf-8'),  # Convert the password to bytes
            PWD_HASH_SALT,
            PWD_HASH_ITERATIONS
        ).decode("utf-8", "ignore")

    @staticmethod
    def gen_token(data):
        access_token = jwt.encode(data, 's3cR$eT', 'HS256')
        return access_token

    def check_access_token(self, access_token: str) -> bool:
        data = jwt.decode(access_token, JWT_KEY, JWT_METHOD)
        token_model = TokenModel.parse_obj(data)
        self.get_all_by_filter({'username': token_model.username})  # checking a user existence
        now_int = calendar.timegm(datetime.datetime.utcnow().timetuple())
        return token_model.exp > now_int

    def check_refresh_token(self, refresh_token: str) -> bool:
        return self.check_access_token(refresh_token)

    @staticmethod
    def gen_jwt(user_obj: dict):
        UserForTokenModel.parse_obj(user_obj)  # to validate the model

        ends_at = datetime.datetime.utcnow() + datetime.timedelta(minutes=AC_TOKEN_EXP_TIME_MIN)
        user_obj['exp'] = calendar.timegm(ends_at.timetuple())
        access_token = jwt.encode(user_obj, JWT_KEY, JWT_METHOD)

        ends_at = datetime.datetime.utcnow() + datetime.timedelta(days=R_TOKEN_EXP_TIME_DAYS)
        user_obj['exp'] = calendar.timegm(ends_at.timetuple())
        refresh_token = jwt.encode(user_obj, JWT_KEY, JWT_METHOD)

        return {'access_token': access_token, 'refresh_token': refresh_token}

    def refresh_jwt(self, refresh_token: str):
        data = jwt.decode(refresh_token, JWT_KEY, JWT_METHOD)
        return self.gen_jwt(data)

    def check_password(self, username: str, password: str) -> bool:
        """
        Checks a user's password
        :param username: user name
        :param password: a password to check
        :return: True or False
        """
        # if self.dao.get_all_by_filter({'username': username, 'password': password}):
        #     return True
        # return False
        password_hash = self.get_hash(password)
        print(password_hash)
        user_password = self.dao.get_all_by_filter({'username': username})[0]['password']
        print(user_password)
        return hmac.compare_digest(password_hash.encode('utf-8'), user_password.encode('utf-8'))

    def check_password_with_hash(self, user_password: str, password_hash: str) -> bool:
        """
        Compares a user's password with its hash in the database
        :param user_password: a user password (a decoded string)
        :param password_hash: a hashed password from the user record
        :return: True or False
        """
        user_password_hash = self.get_hash(user_password)
        return hmac.compare_digest(password_hash.encode('utf-8'), user_password_hash.encode('utf-8'))

    def create(self, new_obj: dict):
        if 'password' in new_obj:
            new_obj['password'] = self.get_hash(new_obj['password'])
        return super().create(new_obj)

    def update(self, new_obj: dict, uid: int):
        if 'password' in new_obj:
            new_obj['password'] = self.get_hash(new_obj['password'])
        super().update(new_obj, uid)
