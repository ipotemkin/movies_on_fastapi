# это файл для классов доступа к данным (Data Access Object). Здесь должен быть класс с методами доступа к данным
# здесь в методах можно построить сложные запросы к БД

from dao.basic import BasicDAO


class DirectorDAO(BasicDAO):

    def __repr__(self):
        return f'<DirectorDAO (model={self.model})>'
