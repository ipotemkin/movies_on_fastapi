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

    def __init__(self, movie_dao: MovieDAO):
        self.movie_dao = movie_dao

    def get_movies(self) -> list["Movie"]:
        return self.movie_dao.get_all_movies()
