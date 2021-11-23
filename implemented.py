# файл для создания DAO и сервисов чтобы импортировать их везде

# book_dao = BookDAO(db.session)
# book_service = BookService(dao=book_dao)
#
# review_dao = ReviewDAO(db.session)
# review_service = ReviewService(dao=review_dao)
from dao.model.directors import Director, DirectorBM
from dao.directors import DirectorDAO
from service.directors import DirectorService

from dao.model.movies import Movie, MovieBM, MovieBMSimple
from dao.movies import MovieDAO
from service.movies import MovieService

from dao.model.genres import Genre, GenreBM
from dao.genres import GenreDAO
from service.genres import GenreService

from dao.model.users import User, UserBM
from dao.users import UserDAO
from service.users import UserService

from setup_db import db

director_dao = DirectorDAO(session=db.session, model=Director, schema=DirectorBM)
director_service = DirectorService(dao=director_dao)


genre_dao = GenreDAO(session=db.session, model=Genre, schema=GenreBM)
genre_service = GenreService(dao=genre_dao)


movie_dao = MovieDAO(session=db.session, model=Movie, schema=MovieBMSimple, nested_schema=MovieBM)
movie_service = MovieService(dao=movie_dao)

user_dao = UserDAO(session=db.session, model=User, schema=UserBM)
user_service = UserService(dao=user_dao)
