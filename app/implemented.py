from setup_db import session

from app.dao.directors import DirectorDAO
from app.dao.model.directors import DirectorBM, Director
from app.service.directors import DirectorService

from app.dao.genres import GenreDAO
from app.dao.model.genres import GenreBM, Genre
from app.service.genres import GenreService

from app.dao.movies import MovieDAO
from app.dao.model.movies import MovieBM, Movie, MovieBMSimple
from app.service.movies import MovieService


director_dao = DirectorDAO(session=session, model=Director, schema=DirectorBM)
director_service = DirectorService(dao=director_dao)

genre_dao = GenreDAO(session=session, model=Genre, schema=GenreBM)
genre_service = GenreService(dao=genre_dao)

movie_dao = MovieDAO(session=session, model=Movie, schema=MovieBMSimple, nested_schema=MovieBM)
movie_service = MovieService(dao=movie_dao)
