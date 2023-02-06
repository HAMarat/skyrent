from backend.dao.place import PlaceDAO
from backend.service.place import PlaceService
from backend.setup_db import db

place_dao = PlaceDAO(session=db.session)
place_service = PlaceService(dao=place_dao)
