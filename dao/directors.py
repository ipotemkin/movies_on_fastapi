# это файл для классов доступа к данным (Data Access Object). Здесь должен быть класс с методами доступа к данным
# здесь в методах можно построить сложные запросы к БД

# Например
from dao.model.directors import Director, DirectorBM
from setup_db import db
from errors import NotFoundError, NoContentError, BadRequestError, DatabaseError


class DirectorDAO:
    @staticmethod
    def get_all():
        if not (directors := Director.query.all()):
            raise NotFoundError
        # return DirectorSchema(many=True).dump(directors)
        return [DirectorBM.from_orm(director).dict() for director in directors]

    @staticmethod
    def get_one(did: int):
        if not (director := Director.query.get(did)):
            raise NotFoundError
        # return DirectorSchema().dump(director)
        return DirectorBM.from_orm(director).dict()

    @staticmethod
    def create(new_director: dict):
        if not new_director:
            raise NoContentError
        try:
            director = Director(**new_director)
        except Exception:
            raise BadRequestError
        try:
            db.session.add(director)
            db.session.commit()
        except Exception:
            raise DatabaseError

    @staticmethod
    def update(new_director: dict, did: int):
        if not new_director:
            raise NoContentError
        if not (director := Director.query.get(did)):
            raise NotFoundError
        if ('id' in new_director) and (did != new_director['id']):
            raise BadRequestError
        if 'name' in new_director:
            director.name = new_director['name']
        try:
            db.session.add(director)
            db.session.commit()
        except Exception:
            raise DatabaseError

    @staticmethod
    def delete(did: int):
        if not (director := Director.query.get(did)):
            raise NotFoundError
        try:
            db.session.delete(director)
            db.session.commit()
        except Exception:
            raise DatabaseError
