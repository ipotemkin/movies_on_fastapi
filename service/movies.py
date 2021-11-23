# здесь бизнес логика, в виде классов или методов. сюда импортируются DAO классы из пакета dao и модели из dao.model
# некоторые методы могут оказаться просто прослойкой между dao и views,
# но чаще всего будет какая-то логика обработки данных сейчас или в будущем.

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

    def get_all_by_filter(self, *args, **kwargs):
        return self.movie_dao.get_all_by_filter(*args, **kwargs)
