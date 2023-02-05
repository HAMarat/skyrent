from dao.place import PlaceDAO


class PlaceService:
    def __init__(self, dao: PlaceDAO):
        self.dao = dao

    def get_one(self, pik):
        return self.dao.get_one(pik)

    def get_all(self):
        return self.dao.get_all()

    def get_by_city(self, city):
        return self.dao.get_by_city(city)

    def get_by_price(self, price_from, price_to):
        if price_from == "":
            price_from = 0
        if price_to == "":
            price_to = 999999
        return self.dao.get_by_price(price_from, price_to)

    def get_by_city_and_price(self, city, price_from, price_to):
        return self.dao.get_by_city_and_price(city, price_from, price_to)
