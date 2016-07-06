# -*- coding: utf-8 -*-
import os
import uuid
from flask import request, jsonify
from handlers import support
from mongoengine import DoesNotExist
from mongoengine.queryset import Q
from s3.get_url import get_url_qiniu
from test_res import task5, task6, task7, task8, task9, task10, task11, task12, task13, task14
from utils.conf import UPLOAD_FOLDER
from utils.extmodels.ext_models import Course, OauthUser, Collection, Comment, Post, PostLikeLog
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
        ret_dict['data'] = [ret_dic]

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
        ret_dict['data'] = [ret_dic]

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

    _images = request.files.getlist('image')
    _voices = request.files.getlist('voice')

    args_list = ['userId', 'content', 'label', 'post_title']
    args = handle_request_post_arguments(request, args_list)
    ret_dict = task10

    try:
        o_user = OauthUser.objects.get(user_id=args['userId'])
    except DoesNotExist as e:
        ret_dict['status'] = 0
        ret_dict['info'] = 'argument is DoesNotExist ' + e.message

    post_id = str(uuid.uuid1())

    images = []
    voices = []

    for i in _images:
        file_id = post_id + '_' + i.filename
        i.save(os.path.join(UPLOAD_FOLDER, file_id + '_tmp'))
        images.append(get_url_qiniu(file_id))

    for i in _voices:
        file_id = post_id + '_' + i.filename
        i.save(os.path.join(UPLOAD_FOLDER, file_id + '_tmp'))
        voices.append(get_url_qiniu(file_id))

    if ret_dict['status'] == 1:
        Post(user=o_user, post=args['content'], label=args['label'], post_title=args['post_title'],
             post_id=post_id, post_img=images, post_voice=voices).save()

    return jsonify(ret_dict)


@support.route('/search_question', methods=['POST', 'GET'])
def search_question():
    test_api(request)

    args_list = ['keyword']
    args = handle_request_post_arguments(request, args_list)
    ret_dict = task11

    q = args.get('keyword', '')
    if not q == '':
        obs = Post.objects(Q(post__icontains=q) | Q(post_id__icontains=q))
    else:
        obs = Post.objects()
    ret_dicts = []

    for o in obs:
        ret_dic = obj2dict(o, include=('course', 'user', 'post', 'post_id', 'comment_count', 'c_time',
                                       'post_img', 'post_voice', 'like_count', 'browse_count'))
        ret_dicts.append(ret_dic)
    ret_dict['data'] = ret_dicts

    return jsonify(ret_dict)


@support.route('/add_look_num', methods=['POST', 'GET'])
def add_look_num():
    test_api(request)

    # args_list = ['postId', 'userId']
    args_list = ['postId']
    args = handle_request_post_arguments(request, args_list)
    ret_dict = task12

    try:
        o_post = Post.objects.get(post_id=args['postId'])
    except DoesNotExist as e:
        ret_dict['status'] = 0
        ret_dict['info'] = 'argument is DoesNotExist ' + e.message

    if ret_dict['status'] == 1:
        if not o_post.browse_count:
            o_post.browse_count = '1'
            o_post.save()
        else:
            o_post.browse_count = str(int(o_post.browse_count) + 1)
            o_post.save()

    return jsonify(ret_dict)


@support.route('/add_like', methods=['POST', 'GET'])
def add_like():
    test_api(request)

    args_list = ['postId', 'userId', 'cancel']
    args = handle_request_post_arguments(request, args_list)
    ret_dict = task13

    try:
        cancel = str(int(args.get('cancel', '0')))
    except ValueError as e:
        ret_dict['status'] = 0
        ret_dict['info'] = 'argument is ValueError ' + e.message

    try:
        o_post = Post.objects.get(post_id=args['postId'])
        o_user = OauthUser.objects.get(user_id=args['userId'])
    except DoesNotExist as e:
        ret_dict['status'] = 0
        ret_dict['info'] = 'argument is DoesNotExist ' + e.message

    if ret_dict['status'] == 1:
        PostLikeLog(post=o_post, user=o_user, cancel=cancel).save()
        if cancel == '0':
            if not o_post.like_count:
                o_post.like_count = '1'
                o_post.save()
            else:
                o_post.like_count = str(int(o_post.like_count) + 1)
                o_post.save()
        elif cancel == '1':
            if o_post.like_count:
                o_post.like_count = str(int(o_post.like_count) - 1)
                o_post.save()

    return jsonify(ret_dict)


@support.route('/question_detail', methods=['POST', 'GET'])
def question_detail():
    test_api(request)

    args_list = ['postId']
    args = handle_request_post_arguments(request, args_list)
    ret_dict = task14

    try:
        o_post = Post.objects(post_id=args['postId'])
    except DoesNotExist as e:
        ret_dict['status'] = 0
        ret_dict['info'] = 'argument is DoesNotExist ' + e.message

    if ret_dict['status'] == 1:
        ret_dic = obj2dict(o_post, include=('course', 'user', 'post', 'post_id', 'comment_count', 'c_time',
                                            'post_img', 'post_voice', 'like_count', 'browse_count'))
        ret_dict['data'] = [ret_dic]

    return jsonify(ret_dict)
