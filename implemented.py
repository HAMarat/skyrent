from dao.place import PlaceDAO
from service.place import PlaceService
from setup_db import db

place_dao = PlaceDAO(session=db.session)
place_service = PlaceService(dao=place_dao)
