# это файл для классов доступа к данным (Data Access Object). Здесь должен быть класс с методами доступа к данным
# здесь в методах можно построить сложные запросы к БД

from errors import NotFoundError
from dao.basic import BasicDAO


class MovieDAO(BasicDAO):

    def get_all_by_filter(self, director_id=None, genre_id=None, year=None):
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

        if not (movies := self.model.query.filter_by(**req).all() if req else self.model.query.all()):
            raise NotFoundError
        return [self.nested_schema.from_orm(movie).dict() for movie in movies]

    # @staticmethod
    # def make_movie(new_movie: dict):
    #     if not new_movie:
    #         raise NoContentError
    #     try:
    #         movie = Movie(**new_movie)
    #         MovieBMSimple.parse_obj(new_movie)  # to validate new data because I cannot migrate db
    #     except Exception as e:
    #         print(e)
    #         raise BadRequestError
    #     try:
    #         db.session.add(movie)
    #         db.session.commit()
    #     except Exception:
    #         raise DatabaseError
    #     # Movie.create(**new_movie)
    #
    # @staticmethod
    # def update_movie(new_movie: dict, mid: int):
    #     if not new_movie:
    #         raise NoContentError
    #     if not Movie.query.get(mid):
    #         raise NotFoundError
    #     if ('id' in new_movie) and (mid != new_movie['id']):
    #         raise BadRequestError
    #     # if 'description' in new_movie:
    #     #     movie.description = new_movie['description']
    #     # if 'director_id' in new_movie:
    #     #     movie.director_id = new_movie['director_id']
    #     # if 'genre_id' in new_movie:
    #     #     movie.genre_id = new_movie['genre_id']
    #     # if 'rating' in new_movie:
    #     #     movie.rating = new_movie['rating']
    #     # if 'title' in new_movie:
    #     #     movie.title = new_movie['title']
    #     # if 'trailer' in new_movie:
    #     #     movie.trailer = new_movie['trailer']
    #     # if 'year' in new_movie:
    #     #     movie.year = new_movie['year']
    #
    #     try:
    #         Movie.query.filter(Movie.id == mid).update(new_movie)
    #         # for field in new_movie.keys():
    #         #     if field != 'id':
    #         #         setattr(movie, field, new_movie[field])
    #     except Exception:
    #         raise BadRequestError
    #     try:
    #         # db.session.add(movie)
    #         db.session.commit()
    #     except Exception:
    #         raise DatabaseError
    #
    # @staticmethod
    # def delete_movie(mid: int):
    #     if not (movie := Movie.query.get(mid)):
    #         raise NotFoundError
    #     try:
    #         db.session.delete(movie)
    #         db.session.commit()
    #     except Exception:
    #         raise DatabaseError
