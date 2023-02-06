from flask_restx import Resource, Namespace
from flask import request

from backend.dao.model.place import PlaceSchema
from backend.implemented import place_service

place_ns = Namespace('places')


@place_ns.route('/')
class PlaceView(Resource):
    def get(self):
        filter_city = request.args.get('city')
        price_from = request.args.get('from', 0)
        if price_from == "":
            price_from = 0
        price_to = request.args.get('to', 999999)
        if price_to == "":
            price_to = 999999

        if filter_city is not None and filter_city != '':
            return PlaceSchema(many=True).dump(place_service.get_by_city_and_price(filter_city, price_from, price_to))

        if (price_from and price_to) is not None:
            return PlaceSchema(many=True).dump(place_service.get_by_price(price_from, price_to))

        places = place_service.get_all()
        return PlaceSchema(many=True).dump(places), 200


@place_ns.route('/<int:pid>')
class PlacesViews(Resource):
    def get(self, pid):
        place = place_service.get_one(pid)
        return PlaceSchema().dump(place)
