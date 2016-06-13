# -*- coding: utf-8 -*-
from flask import request, jsonify
from handlers import other
from mongoengine import ValidationError, DoesNotExist
from mongoengine.queryset import Q
from s3.get_url import get_url_qiniu
from test_res import task22, task1, task2, task3
from utils.extmodels.ext_models import Feedback, OauthUser, Course
from utils.models import Upload
from utils.obj2dict import obj2dict
from utils.util import test_api, handle_request_post_arguments


@other.route('/feed_back', methods=['POST', 'GET'])
def feed_back():
    test_api(request)

    args_list = ['user_id', 'content']
    args = handle_request_post_arguments(request, args_list)
    ret_dict = task22

    # update the last args
    user_id = args.pop('user_id')
    try:
        args['user'] = OauthUser.objects.get(user_id=user_id)
    except DoesNotExist as e:
        ret_dict['status'] = 0
        ret_dict['info'] = 'argument is DoesNotExist ' + e.message
        return jsonify(ret_dict)

    o_feed_back = Feedback()
    for k in args.keys():
        setattr(o_feed_back, k, args[k])
    try:
        o_feed_back.save()
    except ValidationError as e:
        ret_dict['status'] = 0
        ret_dict['info'] = 'argument ValidationError ' + e.message

    return jsonify(ret_dict)


@other.route('/get_carousel', methods=['POST', 'GET'])
def get_carousel():
    test_api(request)

    ret_dict = task1

    cobs = Course.objects
    course_list = []
    for o in cobs:
        uo = o['base_info']
        obj_dict = obj2dict(o, uo, include=('picture', 'video', 'course_name', 'class_name', 'class_uuid',
                                            'browse_count', 'download_count', 'course_type',
                                            'teacher_name', 'class_summary', 'class_time', 'is_over'))
        img_key = 'img-' + obj_dict['class_name'] + '.' + obj_dict['picture'][:-14].split('.')[-1]
        video_key = 'video-' + obj_dict['class_name'] + '.' + obj_dict['video'][:-14].split('.')[-1]
        obj_dict['picture_url'] = get_url_qiniu(img_key)
        obj_dict['video_url'] = get_url_qiniu(video_key)
        course_list.append(obj_dict)
    ret_dict['data'] = course_list

    return jsonify(ret_dict)


@other.route('/search_course', methods=['POST', 'GET'])
def search_course():
    test_api(request)

    args_list = ['keyword']
    args = handle_request_post_arguments(request, args_list)
    ret_dict = task2

    q = args.get('keyword', '')
    if not q == '':
        obs = Upload.objects(
            Q(class_summary__icontains=q) | Q(class_name__icontains=q) | Q(course_name__icontains=q) | Q(
                teacher_name__icontains=q))
    else:
        obs = Upload.objects()
    ret_dicts = []

    for o in obs:
        ret_dic = obj2dict(o, include=('picture', 'video', 'course_name', 'class_name',
                                       'teacher_name', 'class_summary', 'class_time', 'is_over'))
        img_key = 'img-' + ret_dic['class_name'] + '.' + ret_dic['picture'][:-14].split('.')[-1]
        video_key = 'video-' + ret_dic['class_name'] + '.' + ret_dic['video'][:-14].split('.')[-1]
        ret_dic['picture_url'] = get_url_qiniu(img_key)
        ret_dic['video_url'] = get_url_qiniu(video_key)
        ret_dicts.append(ret_dic)
    ret_dict['data'] = ret_dicts

    return jsonify(ret_dict)


@other.route('/classification_course', methods=['POST', 'GET'])
def classification_course():
    test_api(request)

    ret_dict = task3

    obs = Upload.objects
    course_list = []
    for o in obs:
        obj_dict = obj2dict(o, include=('picture', 'video', 'course_name', 'class_name',
                                        'teacher_name', 'class_summary', 'class_time', 'is_over'))
        img_key = 'img-' + obj_dict['class_name'] + '.' + obj_dict['picture'][:-14].split('.')[-1]
        video_key = 'video-' + obj_dict['class_name'] + '.' + obj_dict['video'][:-14].split('.')[-1]
        obj_dict['picture_url'] = get_url_qiniu(img_key)
        obj_dict['video_url'] = get_url_qiniu(video_key)
        course_list.append(obj_dict)
    ret_dict['data'] = course_list

    return jsonify(ret_dict)

