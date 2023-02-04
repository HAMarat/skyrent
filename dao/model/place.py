from marshmallow import Schema, fields
from marshmallow.fields import Str

from setup_db import db


class Place(db.Model):
    __tablename__ = 'place'
    pk = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    description = db.Column(db.String)
    picture_url = db.Column(db.String)
    price = db.Column(db.Integer)
    country = db.Column(db.String)
    city = db.Column(db.String)
    features_on = db.Column(db.String)
    features_off = db.Column(db.String)
    host_name = db.Column(db.String)
    host_phone = db.Column(db.String)
    host_location = db.Column(db.String)


class PlaceSchema(Schema):
    pk = fields.Int()
    title = fields.Str()
    description = fields.Str()
    picture_url = fields.Str()
    price = fields.Int()
    country = fields.Str()
    city = fields.Str()
    features_on = fields.Str()
    features_off = fields.Str()
    host_name = fields.Str()
    host_phone = fields.Str()
    host_location = fields.Str()
