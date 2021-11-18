# это файл для классов доступа к данным (Data Access Object). Здесь должен быть класс с методами доступа к данным
# здесь в методах можно построить сложные запросы к БД

# Например
from dao.model.movies import Movie, MovieBM, MovieBMSimple
from setup_db import db
from errors import NotFoundError, NoContentError, BadRequestError, DatabaseError


class MovieDAO:
    @staticmethod
    def get_all_movies():
        if not (movies := Movie.query.all()):
            raise NotFoundError
        # return MovieSchema(many=True).dump(movies)
        return [MovieBM.from_orm(movie).dict() for movie in movies]

    @staticmethod
    def get_movie_by_id(mid: int):
        if not (movie := Movie.query.get(mid)):
            raise NotFoundError
        # return MovieSchema().dump(movie)
        return MovieBM.from_orm(movie).dict()

    @staticmethod
    def get_movies_by_director_id(did: int):
        if not (movies := Movie.query.filter(Movie.director_id == did).all()):
            raise NotFoundError
        # return MovieSchema(many=True).dump(movies)
        return [MovieBM.from_orm(movie).dict() for movie in movies]

    @staticmethod
    def get_movies_by_genre_id(gid: int):
        if not (movies := Movie.query.filter(Movie.genre_id == gid).all()):
            raise NotFoundError
        # return MovieSchema(many=True).dump(movies)
        return [MovieBM.from_orm(movie).dict() for movie in movies]

    @staticmethod
    def get_movies_by_year(year: int):
        if not (movies := Movie.query.filter(Movie.year == year).all()):
            raise NotFoundError
        # return MovieSchema(many=True).dump(movies)
        return [MovieBM.from_orm(movie).dict() for movie in movies]

    @staticmethod
    def get_movies_by_filter(*, director_id=None, genre_id=None, year=None):
        """
        Get movies with a filter by director_id, genre_id, year using SQLAlchemy CORE.
        """
        sql = "select * from movie"
        sql_lst = []
        if director_id:
            sql_lst.append(f'director_id = {director_id}')
        if genre_id:
            sql_lst.append(f'genre_id = {genre_id}')
        if year:
            sql_lst.append(f'year = {year}')
        if sql_lst:
            sql += ' where ' + ' and '.join(sql_lst)

        if not (movies := db.engine.execute(sql).fetchall()):
            raise NotFoundError
        return [MovieBMSimple.from_orm(movie).dict() for movie in movies]

    @staticmethod
    def get_movies_by_filter_orm(*, director_id=None, genre_id=None, year=None):
        """
        Get movies with a filter by director_id, genre_id, year using SQLAlchemy ORM.
        """
        req = {}
        if director_id:
            req['director_id'] = director_id
        if genre_id:
            req['genre_id'] = genre_id
        if year:
            req['year'] = year

        if not (movies := Movie.query.filter_by(**req).all() if req else Movie.query.all()):
            raise NotFoundError
        return [MovieBM.from_orm(movie).dict() for movie in movies]

    @staticmethod
    def make_movie(new_movie: dict):
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
    def update_movie(new_movie: dict, mid: int):
        if not new_movie:
            raise NoContentError
        if not (movie := Movie.query.get(mid)):
            raise NotFoundError
        if ('id' in new_movie) and (mid != new_movie['id']):
            raise BadRequestError
        # if 'description' in new_movie:
        #     movie.description = new_movie['description']
        # if 'director_id' in new_movie:
        #     movie.director_id = new_movie['director_id']
        # if 'genre_id' in new_movie:
        #     movie.genre_id = new_movie['genre_id']
        # if 'rating' in new_movie:
        #     movie.rating = new_movie['rating']
        # if 'title' in new_movie:
        #     movie.title = new_movie['title']
        # if 'trailer' in new_movie:
        #     movie.trailer = new_movie['trailer']
        # if 'year' in new_movie:
        #     movie.year = new_movie['year']

        try:
            for field in new_movie.keys():
                if field != 'id':
                    setattr(movie, field, new_movie[field])
        except Exception:
            raise BadRequestError
        try:
            db.session.add(movie)
            db.session.commit()
        except Exception:
            raise DatabaseError

    @staticmethod
    def delete_movie(mid: int):
        if not (movie := Movie.query.get(mid)):
            raise NotFoundError
        try:
            db.session.delete(movie)
            db.session.commit()
        except Exception:
            raise DatabaseError
