from flask_restx import Resource, Namespace

from dao.model.place import PlaceSchema
from implemented import place_service

place_ns = Namespace('places')


@place_ns.route('/')
class PlaceView(Resource):
    def get(self):
        places = place_service.get_all()
        return PlaceSchema(many=True).dumps(places), 200


@place_ns.route('/<int:pid>')
class PlacesViews(Resource):
    def get(self, pid):
        place = place_service.get_one(pid)
        return PlaceSchema().dumps(place)
