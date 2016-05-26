# -*- coding: utf-8 -*-
from conf import FLASK_MONGO_ENGINE_CONF
from flask import Blueprint
from flask import Flask
from flask.ext.bootstrap import Bootstrap
from utils.models import engine


app = Flask(__name__, template_folder='../templates')
app.config.update(FLASK_MONGO_ENGINE_CONF)
engine.init_app(app)
bootstrap = Bootstrap(app)

app.use_api = True
# app.use_api = False


api = Blueprint('api', __name__)
user = Blueprint('user', __name__)
other = Blueprint('other', __name__)
view = Blueprint('view', __name__)

import users
import others
import apis
import views


app.register_blueprint(api)
app.register_blueprint(user, url_prefix='/user')
app.register_blueprint(other, url_prefix='/other')
# 后面非API
app.register_blueprint(view)