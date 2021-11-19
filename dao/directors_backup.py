# это файл для классов доступа к данным (Data Access Object). Здесь должен быть класс с методами доступа к данным
# здесь в методах можно построить сложные запросы к БД

# Например
from dao.model.directors import Director, DirectorBM
# from setup_db import db
from errors import NotFoundError, NoContentError, BadRequestError, DatabaseError


class DirectorDAO:
    def __init__(self, session):
        self.session = session

    def get_all(self):
        if not (directors := self.session.query(Director).all()):
            raise NotFoundError
        return [DirectorBM.from_orm(director).dict() for director in directors]

    def get_one(self, did: int):
        # if not (director := self.session.query(Director).get(did)):
        #     raise NotFoundError
        director = self.session.query(Director).get_or_404(did)
        return DirectorBM.from_orm(director).dict()

    def create(self, new_director: dict):
        if not new_director:
            raise NoContentError
        try:
            director = Director(**new_director)
        except Exception:
            raise BadRequestError
        try:
            self.session.add(director)
            self.session.commit()
        except Exception:
            raise DatabaseError

    def update(self, new_director: dict, did: int):
        if not new_director:
            raise NoContentError
        if not Director.query.get(did):
            raise NotFoundError
        if ('id' in new_director) and (did != new_director['id']):
            raise BadRequestError
        try:
            self.session.query(Director).filter(Director.id == did).update(new_director)
            self.session.commit()
        except Exception:
            raise DatabaseError

    def delete(self, did: int):
        director = self.session.query(Director).get_or_404(did)
        try:
            self.session.delete(director)
            self.session.commit()
        except Exception:
            raise DatabaseError
