# -*- coding: utf-8 -*-
import functools
from flask import session
import flask
from main import app


def use_api(f_base):
    def wrap_agr(f):
        @functools.wraps(f)
        def wrap(*args, **kwargs):
            if app.use_api:
                return f_base()
            return f(*args, **kwargs)
        return wrap
    return wrap_agr


def acquire_admin(f):
    @functools.wraps(f)
    def wrap(*args, **kwargs):
        if 'role' not in session or session['role'] != 'admin':
            return flask.redirect(flask.url_for('view.login'))
        return f(*args, **kwargs)
    return wrap