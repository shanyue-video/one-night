# -*- coding: utf-8 -*-
from flask import Blueprint


api = Blueprint('api', __name__)
user = Blueprint('user', __name__)
other = Blueprint('other', __name__)
view = Blueprint('view', __name__)

import users
import others
import apis
import views