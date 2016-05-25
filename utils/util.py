# -*- coding: utf-8 -*-
import functools
import flask
from flask import request
from main import app


def use_api(f_base):
    def wrap_agr(f):
        @functools.wraps(f)
        def wrap(*args, **kwargs):
            if app.use_api:
                return f_base()
                # return flask.redirect(flask.url_for(route, args=request.args.to_dict()), code=307)
            return f(*args, **kwargs)
        return wrap
    return wrap_agr