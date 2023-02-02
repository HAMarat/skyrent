from dao.place import PlaceDAO


class PlaceService:
    def __init__(self, dao: PlaceDAO):
        self.dao = dao

    def get_one(self, pik):
        return self.dao.get_one(pik)

    def get_all(self):
        return self.dao.get_all()
