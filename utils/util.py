# -*- coding: utf-8 -*-
import functools
import time
from flask import session
import flask
from main import app
from utils.models import TestEverything


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


def test_api(request):
    test_everything = TestEverything()
    if request.method == 'GET':
        test_everything.t1 = 'GET' + request.base_url
        test_everything.t2 = str(request.args)
        test_everything.t3 = time.strftime("%Y/%y/%d %H:%M:%S", time.localtime(time.time()))
    elif request.method == 'POST':
        test_everything.t1 = 'POST' + request.base_url
        test_everything.t2 = request.data
        test_everything.t3 = time.strftime("%Y/%y/%d %H:%M:%S", time.localtime(time.time()))
    else:
        test_everything.t1 = 'unknown method'
        test_everything.t2 = 'unknown method'
        test_everything.t3 = time.strftime("%Y/%y/%d %H:%M:%S", time.localtime(time.time()))
    test_everything.save()