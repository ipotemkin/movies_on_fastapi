# from dao.model.directors import Director
# from errors import BadRequestError


class DirectorService:
    def __init__(self, director_dao):
        self.director_dao = director_dao

    def get_all(self):
        return self.director_dao.get_all()

    def get_one(self, did: int):
        return self.director_dao.get_one(did)

    def create(self, new_obj_d: dict):
        return self.director_dao.create(new_obj_d)

    def update(self, new_obj_d: dict, did: int):
        return self.director_dao.update(new_obj_d, did)

    def part_update(self):
        pass

    def delete(self, did: int):
        self.director_dao.delete(did)
