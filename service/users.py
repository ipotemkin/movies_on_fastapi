import hashlib
import jwt
from constants import PWD_HASH_SALT, PWD_HASH_ITERATIONS
from service.basic import BasicService
from errors import BadRequestError, NotFoundError

# TODO: Нужно ли передавать пароль для генерации токена?
# TODO: Какую информацию о пользователе нужно передать для генерации токена
# TODO: Чем refresh_token отличается от access_token?


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

    # def check_password(self, *, uid: int = None, username: str = None, password: str):
    def check_password(self, *args, **kwargs):
        """
        Checks a user's password
        :param id - user ID, username = user name, password - a password to check
        :return:
        """

        # opt 1
        # if uid:
        #     user = self.dao.get_one(uid)
        # elif not username:
        #     raise BadRequestError
        # else:
        #     user = self.dao.get_all_by_filter({'username': username})[0]

        # opt 2
        # req = {}
        # if uid:
        #     req['id'] = uid
        # if username:
        #     req['username'] = username
        # if not req:
        #     raise NotFoundError
        # user = self.dao.get_all_by_filter(req)[0]

        if not (req := {key: value for key, value in kwargs.items()
                        if (key in ('username', 'id', 'password')) and (value is not None)}):
            raise NotFoundError

        try:
            self.dao.get_all_by_filter(req)
        except Exception:
            return False

        return True
