# -*- coding: utf-8 -*-
from flask import request, jsonify
from handlers import user
from mongoengine import ValidationError
from test_res import task16, task17
from utils.extmodels.ext_models import OauthUser
from utils.util import test_api, handle_request_post_arguments


@user.route('/user_info', methods=['POST', 'GET'])
def user_info():
    test_api(request)
    return jsonify(task16)


@user.route('/save_user_info', methods=['POST', 'GET'])
def save_user_info():
    test_api(request)
    args_list = ['user_id', 'user_name', 'platform_name', 'nick_name', 'icon_url', 'access_token']
    args = handle_request_post_arguments(request, args_list)

    o_user = OauthUser()
    # o_user.user_id = args['user_id']
    # o_user.user_name = args['user_name']
    # o_user.platform_name = args['platform_name']
    # o_user.nick_name = args['nick_name']
    # o_user.icon_url = args['icon_url']
    # o_user.access_token = args['access_token']
    for k in args.keys():
        setattr(o_user, k, args[k])

    try:
        o_user.save()
    except ValidationError:
        task17['status'] = 0
        task17['info'] = 'argument is not enough'

    return jsonify(task17)