from flask import Flask
from flask_restx import Api
from flask_cors import CORS

from backend.setup_db import db
from backend.config import Config
from backend.dao.model.place import Place
from backend.views.places import place_ns
from backend.utils import get_data_from_json


def create_app(config_object):
    application = Flask(__name__)
    application.config.from_object(config_object)
    registration_extensions(application)
    return application


def registration_extensions(application):
    db.init_app(application)
    api = Api(application)
    api.add_namespace(place_ns)
    create_data(application, db)


def create_data(application, db):
    with application.app_context():
        db.drop_all()
        db.create_all()

        for place in get_data_from_json():
            place_data = Place(**place)
            db.session.add(place_data)
            db.session.commit()


app = create_app(Config())


@app.errorhandler(404)
def error_404(error):
    """
    Вьюшка для обработки не найденной страницы
    """
    return f"Страница не найдена. Ошибка: {error}", 404


@app.errorhandler(Exception)
def error_handler(error):
    """
    Вьюшка для обработки ошибки на стороне сервера
    """
    return f"Ошибка сервера. Ошибка: {error}"


CORS(app)
cors = CORS(resources={
    r"/*": {"origins": '*'}
})

app.run(port=9000)
