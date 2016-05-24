# -*- coding: utf-8 -*-
from flask.ext.mongoengine import MongoEngine

engine = MongoEngine()


class Test(engine.Document):
    email = engine.StringField(required=True)
    first_name = engine.StringField(max_length=50)
    last_name = engine.StringField(max_length=50)