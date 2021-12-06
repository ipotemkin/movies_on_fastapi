from sqlalchemy.ext.declarative import declared_attr

from setup_db import db
from app.errors import NoContentError, DatabaseError, BadRequestError


class ApiMixin:

    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    id = db.Column(db.Integer, primary_key=True)

    @classmethod
    def create(cls, **kwargs):
        if not kwargs:
            raise NoContentError
        if not (obj := cls(**kwargs)):
            raise BadRequestError
        try:
            db.session.add(obj)
            db.session.commit()
        except Exception:
            raise DatabaseError
        return obj

    @classmethod
    def update_record(cls, pk: int, **kwargs):
        cls.query.filter_by(id=pk).update(kwargs)
        db.session.commit()
        return cls.query.get_or_404(pk)

    @classmethod
    def delete(cls, pk: int):
        obj = cls.query.get_or_404(pk)
        db.session.delete(obj)
        db.session.commit()
