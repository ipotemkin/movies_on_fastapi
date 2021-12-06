from fastapi import APIRouter, status, Depends, HTTPException, Request
from fastapi.security import OAuth2PasswordRequestForm

from pydantic import BaseModel

from app.service.users import UserService
from app.dependency import get_db, jwt_decode
from sqlalchemy.orm import Session

from app.dependency import oauth2_scheme


# Models
class TokenRequest(BaseModel):
    username: str
    password: str

    class Config:
        orm_mode = True


class TokenResponse(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str

    class Config:
        orm_mode = True


class RefreshTokensRequest(BaseModel):
    refresh_token: str


router = APIRouter(prefix='/auth', tags=['auth'])


def authenticate_user(username: str, password: str, db: Session = Depends(get_db)):
    user = UserService(db).get_all_by_filter({'username': username})[0]
    if not user:
        return False

    password_hash = user.get('password', None)

    if password_hash is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="No password set",
            headers={"WWW-Authenticate": "Bearer"},
        )

    if not UserService(db).check_password_with_hash(user_password=password, password_hash=password_hash):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    # user = get_user(fake_db, username)
    # if not user:
    #     return False
    # if not verify_password(password, user.hashed_password):
    #     return False
    return user


def decoded_jwt(token: str = Depends(oauth2_scheme)):
    return jwt_decode(token)


# async def get_current_user(token: str = Depends(oauth2_scheme)):
#     credentials_exception = HTTPException(
#         status_code=status.HTTP_401_UNAUTHORIZED,
#         detail="Could not validate credentials",
#         headers={"WWW-Authenticate": "Bearer"},
#     )
#     try:
#         payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
#         username: str = payload.get("sub")
#         if username is None:
#             raise credentials_exception
#         token_data = TokenData(username=username)
#     except JWTError:
#         raise credentials_exception
#     user = get_user(fake_users_db, username=token_data.username)
#     if user is None:
#         raise credentials_exception
#     return user


@router.post('', response_model=TokenResponse, summary='Получить токены')
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    """
    Получить токены / Generate tokens
    """
    user = authenticate_user(form_data.username, form_data.password, db)
    return UserService(db).gen_jwt({'username': user['username'], 'role': user['role']})


# @router.put('', response_model=TokenResponse, summary='Обновить токены')
# async def refresh_tokens(body: RefreshTokensRequest, db: Session = Depends(get_db)):
#     """
#     Обновить токены / Refresh tokens
#     """
#     if not UserService(db).check_refresh_token(body.refresh_token):
#         raise HTTPException(
#                     status_code=status.HTTP_401_UNAUTHORIZED,
#                     detail="Refresh token non valid",
#                     headers={"WWW-Authenticate": "Bearer"},
#                 )
#
#     return UserService(db).refresh_jwt(body.refresh_token)

# @auth_ns.route('/')
# class AuthsView(Resource):
#     @staticmethod
#     @auth_ns.response(201, 'Updated', headers={'Location': 'auths_auth_view'})
#     @validate()
#     def put(body: RefreshTokensRequest):
#         """
#         Обновить токены / Refresh tokens
#         """
#         if not user_service.check_refresh_token(body.refresh_token):
#             abort(401, {'error': 'Refresh token non valid'})
#
#         return user_service.refresh_jwt(body.refresh_token), 201
