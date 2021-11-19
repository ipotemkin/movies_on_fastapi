# здесь бизнес логика, в виде классов или методов. сюда импортируются DAO классы из пакета dao и модели из dao.model
# некоторые методы могут оказаться просто прослойкой между dao и views,
# но чаще всего будет какая-то логика обработки данных сейчас или в будущем.

# Пример

# class BookService:
#
#     def __init__(self, book_dao: BookDAO):
#         self.book_dao = book_dao
#
#     def get_books(self) -> List["Book"]:
#         return self.book_dao.get_books()

from dao.model.movies import Movie
from dao.movies import MovieDAO


class MovieService:

    def __init__(self, movie_dao):
        self.movie_dao = movie_dao

    def get_all(self):
        return self.movie_dao.get_all()

    def get_one(self, mid: int):
        return self.movie_dao.get_one(mid)

    def create(self, new_obj_d: dict):
        return self.movie_dao.create(new_obj_d)

    def update(self, new_obj_d: dict, mid: int):
        return self.movie_dao.update(new_obj_d, mid)

    def part_update(self):
        pass

    def delete(self, mid: int):
        self.movie_dao.delete(mid)

    def get_all_by_filter(self, director_id, genre_id, year):
        return self.movie_dao.get_all_by_filter(director_id, genre_id, year)
