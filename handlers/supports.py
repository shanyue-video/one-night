# -*- coding: utf-8 -*-
from flask import request, jsonify
from handlers import support
from mongoengine import DoesNotExist
from s3.get_url import get_url_qiniu
from test_res import task5, task6, task7, task8
from utils.extmodels.ext_models import Course, OauthUser, Collection, Comment
from utils.obj2dict import obj2dict
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


@support.route('/chapter', methods=['POST', 'GET'])
def chapter():
    test_api(request)

    args_list = ['courseId']
    args = handle_request_post_arguments(request, args_list)
    ret_dict = task6

    try:
        o_course = Course.objects.get(class_uuid=args['courseId'])
    except DoesNotExist as e:
        ret_dict['status'] = 0
        ret_dict['info'] = 'argument is DoesNotExist ' + e.message

    if ret_dict['status'] == 1:
        o_upload = o_course['base_info']
        ret_dic = obj2dict(o_course, o_upload, include=('picture', 'video', 'course_name', 'class_name',
                                                        'class_uuid', 'browse_count', 'download_count',
                                                        'course_type', 'teacher_name', 'class_summary',
                                                        'class_time', 'is_over'))
        img_key = 'img-' + ret_dic['class_name'] + '.' + ret_dic['picture'][:-14].split('.')[-1]
        video_key = 'video-' + ret_dic['class_name'] + '.' + ret_dic['video'][:-14].split('.')[-1]
        ret_dic['picture_url'] = get_url_qiniu(img_key)
        ret_dic['video_url'] = get_url_qiniu(video_key)
        ret_dict['data'] = ret_dic

    return jsonify(ret_dict)


@support.route('/download', methods=['POST', 'GET'])
def download():
    test_api(request)

    args_list = ['courseId']
    args = handle_request_post_arguments(request, args_list)
    ret_dict = task7

    try:
        o_course = Course.objects.get(class_uuid=args['courseId'])
    except DoesNotExist as e:
        ret_dict['status'] = 0
        ret_dict['info'] = 'argument is DoesNotExist ' + e.message

    if ret_dict['status'] == 1:
        o_upload = o_course['base_info']
        ret_dic = obj2dict(o_course, o_upload, include=('picture', 'video', 'course_name', 'class_name',
                                                        'class_uuid', 'browse_count', 'download_count',
                                                        'course_type', 'teacher_name', 'class_summary',
                                                        'class_time', 'is_over'))
        img_key = 'img-' + ret_dic['class_name'] + '.' + ret_dic['picture'][:-14].split('.')[-1]
        video_key = 'video-' + ret_dic['class_name'] + '.' + ret_dic['video'][:-14].split('.')[-1]
        ret_dic['picture_url'] = get_url_qiniu(img_key)
        ret_dic['video_url'] = get_url_qiniu(video_key)
        ret_dict['data'] = ret_dic

    return jsonify(ret_dict)


@support.route('/comment', methods=['POST', 'GET'])
def comment():
    test_api(request)

    args_list = ['courseId', 'userId', 'comment_content']
    args = handle_request_post_arguments(request, args_list)
    ret_dict = task8

    try:
        o_course = Course.objects.get(class_uuid=args['courseId'])
        o_user = OauthUser.objects.get(user_id=args['userId'])
    except DoesNotExist as e:
        ret_dict['status'] = 0
        ret_dict['info'] = 'argument is DoesNotExist ' + e.message

    if ret_dict['status'] == 1:
        Comment(course=o_course, user=o_user, comment=args['comment_content']).save()

    return jsonify(ret_dict)