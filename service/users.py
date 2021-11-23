# from dao.model.users import user
# from errors import BadRequestError
import hashlib
from constants import PWD_HASH_SALT, PWD_HASH_ITERATIONS


class UserService:
    def __init__(self, user_dao):
        self.user_dao = user_dao

    def get_all(self):
        return self.user_dao.get_all()

    def get_one(self, did: int):
        return self.user_dao.get_one(did)

    def create(self, new_obj_d: dict):
        return self.user_dao.create(new_obj_d)

    def update(self, new_obj_d: dict, did: int):
        return self.user_dao.update(new_obj_d, did)

    def part_update(self):
        pass

    def delete(self, did: int):
        self.user_dao.delete(did)

    @staticmethod
    def get_hash(password):
        return hashlib.pbkdf2_hmac(
            'sha256',
            password.encode('utf-8'),  # Convert the password to bytes
            PWD_HASH_SALT,
            PWD_HASH_ITERATIONS
        ).decode("utf-8", "ignore")
