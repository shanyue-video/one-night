# -*- coding: utf-8 -*-
from flask import request, jsonify
from handlers import support
from mongoengine import DoesNotExist
from test_res import task5
from utils.extmodels.ext_models import Course, OauthUser, Collection
from utils.util import test_api, handle_request_post_arguments


@support.route('/collection', methods=['POST', 'GET'])
def collection():
    test_api(request)

    args_list = ['courseId', 'userId']
    args = handle_request_post_arguments(request, args_list)
    ret_dict = task5

    try:
        o_course = Course.objects.get(class_uuid=args['courseId'])
        o_user = OauthUser.objects.get(user_id=args['userId'])
    except DoesNotExist as e:
        ret_dict['status'] = 0
        ret_dict['info'] = 'argument is DoesNotExist ' + e.message

    if ret_dict['status'] == 1:
        Collection(course=o_course, user=o_user).save()

    return jsonify(ret_dict)
