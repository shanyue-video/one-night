# -*- coding: utf-8 -*-
import functools
import time
from flask import session
import flask
from handlers import app
import os
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
        test_everything.t3 = time.strftime("%Y/%m/%d %H:%M:%S", time.localtime(time.time()))
    elif request.method == 'POST':
        test_everything.t1 = 'POST' + request.base_url
        test_everything.t2 = request.data or str(request.form) + ' file:' + str(request.files)
        test_everything.t3 = time.strftime("%Y/%m/%d %H:%M:%S", time.localtime(time.time()))
    else:
        test_everything.t1 = 'unknown method'
        test_everything.t2 = 'unknown method'
        test_everything.t3 = time.strftime("%Y/%m/%d %H:%M:%S", time.localtime(time.time()))
    test_everything.save()


def handle_request_post_arguments(request, args_list):
    if request.method == 'POST':
        base_form = request.form
        base_dict = base_form.to_dict()
        ret = {}
        for arg in args_list:
            if base_dict.get(arg):
                ret[arg] = base_dict[arg]
        return ret
    if request.method == 'GET':
        base_form = request.values
        base_dict = base_form.to_dict()
        ret = {}
        for arg in args_list:
            if base_dict.get(arg):
                ret[arg] = base_dict[arg]
        return ret


def u_path(string):
    if isinstance(string, str):
        return os.path.abspath(string)
    else:
        raise AssertionError('u_path error')


if __name__ == '__main__':
    print time.strftime("%Y/%m/%d %H:%M:%S", time.localtime(time.time()))