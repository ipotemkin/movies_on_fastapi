from service.basic import BasicService
import jwt
from constants import JWT_KEY, JWT_METHOD

# from implemented import user_service


class RTokenService(BasicService):
    def del_expired(self):
        tokens = self.dao.get_all(raise_errors=False)
        for token in tokens:
            try:
                jwt.decode(token['token'], JWT_KEY, JWT_METHOD)
            except Exception as e:
                print(f"Token with ID={token['id']} status {e}")
                self.dao.delete(token['id'])
