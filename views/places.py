from flask_restx import Resource, Namespace
from flask import request

from dao.model.place import PlaceSchema
from implemented import place_service

place_ns = Namespace('places')


@place_ns.route('/')
class PlaceView(Resource):
    def get(self):
        filter_city = request.args.get('city')
        if filter_city:
            return PlaceSchema(many=True).dump(place_service.get_by_city(filter_city))

        price_from = request.args.get('from')
        price_to = request.args.get('to')

        if price_from and price_to:
            return PlaceSchema(many=True).dump(place_service.get_by_price(price_from, price_to))

        places = place_service.get_all()
        return PlaceSchema(many=True).dump(places), 200


@place_ns.route('/<int:pid>')
class PlacesViews(Resource):
    def get(self, pid):
        place = place_service.get_one(pid)
        return PlaceSchema().dump(place)
