from dao.model.place import Place


class PlaceDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, pid):
        return self.session.query(Place).get(pid)

    def get_all(self):
        return self.session.query(Place).all()
