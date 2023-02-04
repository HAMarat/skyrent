from sqlalchemy import and_

from dao.model.place import Place


class PlaceDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, pid):
        return self.session.query(Place).get(pid)

    def get_all(self):
        return self.session.query(Place).all()

    def get_by_city(self, city):
        return self.session.query(Place).filter(Place.city == city).all()

    def get_by_price(self, price_from, price_to):
        return self.session.query(Place).filter(Place.price.between(price_from, price_to)).all()

    def get_by_city_and_price(self, city, price_from, price_to):
        return self.session.query(Place).filter(and_(Place.city == city,
                                                     Place.price.between(price_from, price_to))).all()
