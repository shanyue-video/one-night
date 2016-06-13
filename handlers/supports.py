# -*- coding: utf-8 -*-
import uuid
from flask import request, jsonify
from handlers import support
from mongoengine import DoesNotExist
from s3.get_url import get_url_qiniu
from test_res import task5, task6, task7, task8, task9, task10
from utils.extmodels.ext_models import Course, OauthUser, Collection, Comment, Post
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


@support.route('/list_question', methods=['POST', 'GET'])
def list_question():
    test_api(request)

    # args_list = []
    # args = handle_request_post_arguments(request, args_list)
    ret_dict = task9

    p_obs = Post.objects
    course_list = []
    for o in p_obs:
        obj_dict = obj2dict(o, include=('course', 'user', 'post', 'post_id', 'post_img',
                                        'like_count', 'browse_count', 'comment_count',
                                        'c_time'))
        course_list.append(obj_dict)
    ret_dict['data'] = course_list

    return jsonify(ret_dict)


@support.route('/post_new', methods=['POST', 'GET'])
def post_new():
    test_api(request)

    args_list = ['userId', 'content', 'label', 'postImgs', 'postVoice']
    args = handle_request_post_arguments(request, args_list)
    ret_dict = task10

    try:
        o_user = OauthUser.objects.get(user_id=args['userId'])
    except DoesNotExist as e:
        ret_dict['status'] = 0
        ret_dict['info'] = 'argument is DoesNotExist ' + e.message

    if ret_dict['status'] == 1:
        Post(user=o_user, post=args['content'], post_id=str(uuid.uuid1()), post_img=args['postImgs'],
             post_voice=args['postVoice']).save()

    return jsonify(ret_dict)