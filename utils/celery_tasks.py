# -*- coding: utf-8 -*-
from celery import Celery
from utils.conf import FLASK_MONGO_ENGINE_CONF

MONGODB = FLASK_MONGO_ENGINE_CONF.get('MONGODB_SETTINGS')

app = Celery(broker=MONGODB.get('host'))
app.conf.update(
    CELERY_ACCEPT_CONTENT=['pickle', 'json', 'msgpack', 'yaml'],
    CELERY_RESULT_BACKEND=MONGODB.get('host'),
    CELERY_MONGODB_BACKEND_SETTINGS={
        'database': 'one_night_test',
        'taskmeta_collection': 'one_night_test',
    },
    CELERY_IMPORTS=("utils.celery_task", ),
)