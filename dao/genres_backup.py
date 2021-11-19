# это файл для классов доступа к данным (Data Access Object). Здесь должен быть класс с методами доступа к данным
# здесь в методах можно построить сложные запросы к БД

# Например
from dao.model.genres import Genre, GenreBM
from setup_db import db
from errors import NotFoundError, NoContentError, BadRequestError, DatabaseError


class GenreDAO:
    @staticmethod
    def get_all_genres():
        if not (genres := Genre.query.all()):
            raise NotFoundError
        # return GenreSchema(many=True).dump(genres)
        return [GenreBM.from_orm(genre).dict() for genre in genres]

    @staticmethod
    def get_genre_by_id(gid: int):
        if not (genre := Genre.query.get(gid)):
            raise NotFoundError
        # return GenreSchema().dump(genre)
        return GenreBM.from_orm(genre).dict()

    @staticmethod
    def make_genre(new_genre: dict):
        if not new_genre:
            raise NoContentError
        try:
            genre = Genre(**new_genre)
        except Exception:
            raise BadRequestError
        try:
            db.session.add(genre)
            db.session.commit()
        except Exception:
            raise DatabaseError

    @staticmethod
    def update_genre(new_genre: dict, gid: int):
        if not new_genre:
            raise NoContentError
        if not (genre := Genre.query.get(gid)):
            raise NotFoundError
        if ('id' in new_genre) and (gid != new_genre['id']):
            raise BadRequestError
        if 'name' in new_genre:
            genre.name = new_genre['name']
        try:
            db.session.add(genre)
            db.session.commit()
        except Exception:
            raise DatabaseError

    @staticmethod
    def delete_genre(gid: int):
        if not (genre := Genre.query.get(gid)):
            raise NotFoundError
        try:
            db.session.delete(genre)
            db.session.commit()
        except Exception:
            raise DatabaseError
