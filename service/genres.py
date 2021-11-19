
class GenreService:
    def __init__(self, genre_dao):
        self.genre_dao = genre_dao

    def get_all(self):
        return self.genre_dao.get_all()

    def get_one(self, did: int):
        return self.genre_dao.get_one(did)

    def create(self, new_obj_d: dict):
        return self.genre_dao.create(new_obj_d)

    def update(self, new_obj_d: dict, did: int):
        return self.genre_dao.update(new_obj_d, did)

    def part_update(self):
        pass

    def delete(self, did: int):
        self.genre_dao.delete(did)
