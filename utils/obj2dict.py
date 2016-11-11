# -*- coding: utf-8 -*-
import datetime


def obj2dict(obj, obj2=None, include=None):
    """
    加个注释，已经不记得什么意思了
    :param obj:
    :param obj2:
    :param include:
    :return: 把给定的几个对象中的字段 按需输出
    """
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
            if i in dir(obj):
                tmp = getattr(obj, i)
                if tmp == '':
                    continue
                if isinstance(tmp, datetime.datetime):
                    tmp = tmp.strftime('%Y-%m-%d %H:%M:%S')
                ret_dict[i] = tmp
            if i in dir(obj2):
                tmp = getattr(obj, i)
                if tmp == '':
                    continue
                if isinstance(tmp, datetime.datetime):
                    tmp = tmp.strftime('%Y-%m-%d %H:%M:%S')
                ret_dict[i] = tmp

    return ret_dict
