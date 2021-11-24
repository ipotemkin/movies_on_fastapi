import hashlib
import jwt
from constants import PWD_HASH_SALT, PWD_HASH_ITERATIONS
from service.basic import BasicService
from errors import BadRequestError, NotFoundError

# TODO: Нужно ли передавать пароль для генерации токена?
# TODO: Какую информацию о пользователе нужно передать для генерации токена
# TODO: Чем refresh_token отличается от access_token?
# TODO: Какой код возврата при генерации токенов?


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

    def check_password(self, username: str, password: str) -> bool:
        """
        Checks a user's password
        :param username: user name
        :param password: a password to check
        :return: True or False
        """
        if self.dao.get_all_by_filter({'username': username, 'password': password}):
            return True
        return False
