from flask_restx import Resource
from implemented import director_service, directors_model, director_ns, auth_parser
from utils import auth_required, admin_required


@director_ns.route('/')
@director_ns.expect(auth_parser)
class DirectorsView(Resource):
    @staticmethod
    @auth_required
    @director_ns.marshal_list_with(directors_model)
    def get():
        """
        Получить всех режиссеров / Get all directors
        """
        return director_service.get_all()

    @staticmethod
    @director_ns.response(201, 'Created', headers={'Location': 'directors_director_view'})
    @admin_required
    def post():
        """
        Добавить нового режиссера / Add a new director
        """
        obj = director_service.create(director_ns.payload)
        return "", 201, {'Location': obj.id}


@director_ns.route('/<int:did>')
@director_ns.expect(auth_parser)
@director_ns.doc(params={'did': 'Идентификатор режиссера'})
class DirectorView(Resource):
    @staticmethod
    @auth_required
    @director_ns.marshal_with(directors_model)
    def get(did: int):
        """
        Получить режиссера с указанным ID / Get a director with the given did
        """
        return director_service.get_one(did)

    @staticmethod
    @admin_required
    def patch(did: int):
        """
        Обновить режиссера с указанным ID / Update a director with the given did
        """
        return director_service.update(director_ns.payload, did), 204

    @staticmethod
    @admin_required
    def delete(did: int):
        """
        Удалить режиссера с указанным ID / Delete a director with the given did
        """
        return director_service.delete(did), 204
