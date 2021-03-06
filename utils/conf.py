import os

__author__ = 'dengjing'

INNER_IP = '0.0.0.0'
port = 8888

try:
    if int(os.getenv('PR')) == 1:
        DEBUG = False
except TypeError:
    DEBUG = True
else:
    DEBUG = True

UPLOAD_FOLDER = os.path.abspath(os.path.join(os.path.abspath(__file__), os.path.pardir+'/../media/'))

DBS = {
    'MONGODB_SETTINGS': {
        # 'host': 'mongodb://one:123456@oforever.net:27017/one_night'
        'host': 'mongodb://localhost:27017/one_night'
    },
    'MONGODB_SETTINGS_TEST': {
        # 'host': 'mongodb://one:123456@oforever.net:27017/one_night_test'
        'host': 'mongodb://localhost:27017/one_night_test'
        # 'host': 'mongodb://one:123456@oforever.net:27017/one_night'
    }
}

FLASK_MONGO_ENGINE_CONF = {
    'SECRET_KEY': '\x01\xcf\x12\\\x95\xbb\xc0\xc4\x03\xb8\xde\x198\x04\xd7\x88\xfe\x82\xfc\xf73\xf1v\xa3',
    'MONGODB_SETTINGS': DBS['MONGODB_SETTINGS']
}

if DEBUG:
    FLASK_MONGO_ENGINE_CONF.update({'MONGODB_SETTINGS': DBS['MONGODB_SETTINGS_TEST']})
    # print 'a'

import logging
LOGGING_FORMAT = '[%(levelname)1.1s %(asctime)s %(module)s:%(lineno)d] %(message)s'
DATE_FORMAT = '%Y-%m-%d %H:%M:%S'
logging.basicConfig(
    level=logging.NOTSET,
    format=LOGGING_FORMAT,
    datefmt=DATE_FORMAT
)
root_logger = logging.getLogger()