# это файл для классов доступа к данным (Data Access Object). Здесь должен быть класс с методами доступа к данным
# здесь в методах можно построить сложные запросы к БД

# Например
from model.movies import Movie, MovieSchema
from setup_db import db
from errors import NotFoundError, NoContentError, BadRequestError, DatabaseError


class MovieDAO:
    @staticmethod
    def get_all_movies(self):
        if not (movies := Movie.query.all()):
            raise NotFoundError
        return MovieSchema(many=True).dump(movies)

    @staticmethod
    def get_movie_by_id(self, mid: int):
        if not (movie := Movie.query.get(mid)):
            raise NotFoundError
        return MovieSchema().dump(movie)

    @staticmethod
    def get_all_movies_by_director_id(self, did: int):
        if not (movies := Movie.query.filter(Movie.director_id == did).all()):
            raise NotFoundError
        return MovieSchema(many=True).dump(movies)

    @staticmethod
    def get_all_movies_by_genre_id(self, gid: int):
        if not (movies := Movie.query.filter(Movie.genre_id == gid).all()):
            raise NotFoundError
        return MovieSchema(many=True).dump(movies)

    @staticmethod
    def get_all_movies_by_year(self, year: int):
        if not (movies := Movie.query.filter(Movie.year == year).all()):
            raise NotFoundError
        return MovieSchema(many=True).dump(movies)

    @staticmethod
    def make_movie(self, new_movie: dict):
        if not new_movie:
            raise NoContentError
        try:
            movie = Movie(**new_movie)
        except Exception:
            raise BadRequestError
        try:
            db.session.add(movie)
            db.session.commit()
        except Exception:
            raise DatabaseError

    @staticmethod
    def update_movie(self, new_movie: dict):
        if not new_movie:
            raise NoContentError
        if not (movie := Movie.query.get(new_movie['id'])):
            raise NotFoundError
        try:
            for field in new_movie.keys():
                if field != 'id':
                    movie.__dict__[field] = new_movie[field]
        except Exception:
            raise BadRequestError
        try:
            db.session.add(movie)
            db.session.commit()
        except Exception:
            raise DatabaseError

    @staticmethod
    def delete_movie(self, mid: int):
        if not (movie := Movie.query.get(mid)):
            raise NotFoundError
        try:
            db.session.delete(movie)
            db.session.commit()
        except Exception:
            raise DatabaseError
