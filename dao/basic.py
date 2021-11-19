# это файл для классов доступа к данным (Data Access Object). Здесь должен быть класс с методами доступа к данным
# здесь в методах можно построить сложные запросы к БД

# Например
# from dao.model.directors import Director, DirectorBM
from errors import NotFoundError, NoContentError, BadRequestError, DatabaseError


class BasicDAO:
    def __init__(self, session, model, schema, nested_schema=None):
        self.session = session
        self.model = model
        self.schema = schema
        self.nested_schema = nested_schema

    def get_all(self):
        if not (directors := self.session.query(self.model).all()):
            raise NotFoundError
        return [self.schema.from_orm(director).dict() for director in directors]

    def get_one(self, did: int):
        # if not (director := self.session.query(Director).get(did)):
        #     raise NotFoundError
        director = self.session.query(self.model).get_or_404(did)
        return self.schema.from_orm(director).dict()

    def create(self, new_director: dict):
        if not new_director:
            raise NoContentError
        try:
            director = self.model(**new_director)
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
        if not self.model.query.get(did):
            raise NotFoundError
        if ('id' in new_director) and (did != new_director['id']):
            raise BadRequestError
        try:
            self.session.query(self.model).filter(self.model.id == did).update(new_director)
            self.session.commit()
        except Exception:
            raise DatabaseError

    def delete(self, did: int):
        director = self.session.query(self.model).get_or_404(did)
        try:
            self.session.delete(director)
            self.session.commit()
        except Exception:
            raise DatabaseError
