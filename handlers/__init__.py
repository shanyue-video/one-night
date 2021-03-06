# -*- coding: utf-8 -*-
import os
from utils.conf import FLASK_MONGO_ENGINE_CONF
from flask import Blueprint
from flask import Flask
from flask.ext.bootstrap import Bootstrap
from utils.models import engine

tmp_dir = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../templates'))
# tmp_dir = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../media'))

app = Flask(__name__, template_folder=tmp_dir, static_folder='../static')
app.config.update(FLASK_MONGO_ENGINE_CONF)
engine.init_app(app)
bootstrap = Bootstrap(app)

app.use_api = True
# app.use_api = False


api = Blueprint('api', __name__)

user = Blueprint('user', __name__)
other = Blueprint('other', __name__)
support = Blueprint('support', __name__)

view = Blueprint('view', __name__)

import users
import others
import apis
import views
import supports


app.register_blueprint(api)
app.register_blueprint(user, url_prefix='/user')
app.register_blueprint(other, url_prefix='/other')
app.register_blueprint(support, url_prefix='/support')
# 后面非API
app.register_blueprint(view)