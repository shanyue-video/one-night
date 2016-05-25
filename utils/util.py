# -*- coding: utf-8 -*-
import functools
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