# это файл для классов доступа к данным (Data Access Object). Здесь должен быть класс с методами доступа к данным
# здесь в методах можно построить сложные запросы к БД

# Например
from errors import NotFoundError, NoContentError, BadRequestError, DatabaseError


class BasicDAO:
    def __init__(self, session, model, schema, nested_schema=None):
        self.session = session
        self.model = model
        self.schema = schema
        self.nested_schema = nested_schema

    def get_all(self):
        if not (objs := self.session.query(self.model).all()):
            raise NotFoundError
        return [self.schema.from_orm(obj).dict() for obj in objs]

    def get_one(self, uid: int):
        # if not (obj := self.session.query(obj).get(uid)):
        #     raise NotFoundError
        obj = self.session.query(self.model).get_or_404(uid)
        return self.schema.from_orm(obj).dict()

    def create(self, new_obj: dict):
        if not new_obj:
            raise NoContentError
        try:
            obj = self.model(**new_obj)
        except Exception:
            raise BadRequestError
        try:
            self.session.add(obj)
            self.session.commit()
        except Exception:
            raise DatabaseError

    def update(self, new_obj: dict, uid: int):
        if not new_obj:
            raise NoContentError
        if not self.model.query.get(uid):
            raise NotFoundError
        if ('id' in new_obj) and (uid != new_obj['id']):
            raise BadRequestError
        try:
            self.session.query(self.model).filter(self.model.id == uid).update(new_obj)
            self.session.commit()
        except Exception:
            raise DatabaseError

    def delete(self, uid: int):
        obj = self.session.query(self.model).get_or_404(uid)
        try:
            self.session.delete(obj)
            self.session.commit()
        except Exception:
            raise DatabaseError
