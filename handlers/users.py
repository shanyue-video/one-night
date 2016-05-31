# -*- coding: utf-8 -*-
from flask import request, jsonify
from handlers import user
from mongoengine import ValidationError, DoesNotExist
from test_res import task17, task16
from utils.extmodels.ext_models import OauthUser
from utils.obj2dict import obj2dict
from utils.util import test_api, handle_request_post_arguments


@user.route('/user_info', methods=['POST', 'GET'])
def user_info():
    test_api(request)

    args_list = ['user_id']
    args = handle_request_post_arguments(request, args_list)
    ret_dict = task16

    try:
        o_user = OauthUser.objects.get(user_id=args['user_id'])
    except DoesNotExist as e:
        ret_dict['status'] = 0
        ret_dict['info'] = 'argument is not enough' + e.message

    if ret_dict['status'] == 1:
        ret_dict = obj2dict(o_user, include=('user_id', 'user_name', 'platform_name',
                                             'nick_name', 'icon_url', 'access_token', 'role'))

    return jsonify(ret_dict)


@user.route('/save_user_info', methods=['POST', 'GET'])
def save_user_info():
    test_api(request)

    args_list = ['user_id', 'user_name', 'platform_name', 'nick_name', 'icon_url', 'access_token']
    args = handle_request_post_arguments(request, args_list)
    ret_dict = task17

    o_user = OauthUser()
    for k in args.keys():
        setattr(o_user, k, args[k])
    try:
        o_user.save()
        ret_dict['id'] = o_user.id
    except ValidationError as e:
        ret_dict['status'] = 0
        ret_dict['info'] = 'argument is not enough' + e.message

    return jsonify(ret_dict)