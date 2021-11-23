import hashlib
from constants import PWD_HASH_SALT, PWD_HASH_ITERATIONS
from service.basic import BasicService


class UserService(BasicService):
    @staticmethod
    def get_hash(password):
        return hashlib.pbkdf2_hmac(
            'sha256',
            password.encode('utf-8'),  # Convert the password to bytes
            PWD_HASH_SALT,
            PWD_HASH_ITERATIONS
        ).decode("utf-8", "ignore")
