# -*- coding: utf-8 -*-


def obj2dict(obj, obj2=None, include=None):
    if not isinstance(obj, object):
        return {'code': 'not object'}
    if not isinstance(include, tuple):
        return {'code': 'not tuple'}

    base_dir = dir(obj)
    if obj2:
        base_dir += dir(obj2)
    include_tuple = include
    ret_dict = {}

    for i in base_dir:
        if i in include_tuple:
            ret_dict[i] = getattr(obj, i)
        else:
            print 'not' + i

    return ret_dict
