# -*- coding: utf-8 -*-
import copy
from flask import request, jsonify
from handlers import other
from mongoengine import ValidationError, DoesNotExist
from mongoengine.queryset import Q
from s3.get_url import get_url_qiniu
from test_res import task22, task1, task2, task3, task18, task19, task20, task21, task24
from utils.conf import root_logger
from utils.extmodels.ext_models import Feedback, OauthUser, Course, Post, LearningHistory, Comment
from utils.models import Upload
from utils.obj2dict import obj2dict
from utils.util import test_api, handle_request_post_arguments
from datetime import datetime


@other.route('/feed_back', methods=['POST', 'GET'])
def feed_back():
    test_api(request)

    args_list = ['user_id', 'content']
    args = handle_request_post_arguments(request, args_list)
    ret_dict = copy.deepcopy(task22)

    # update the last args
    user_id = args.pop('user_id')
    try:
        args['user'] = OauthUser.objects.get(user_id=user_id)
    except DoesNotExist as e:
        ret_dict['status'] = 0
        ret_dict['info'] = 'argument is DoesNotExist ' + e.message
        root_logger.error(u'user cant find')
        return jsonify(ret_dict)

    o_feed_back = Feedback()
    for k in args.keys():
        setattr(o_feed_back, k, args[k])
    try:
        o_feed_back.save()
    except ValidationError as e:
        ret_dict['status'] = 0
        ret_dict['info'] = 'argument ValidationError ' + e.message
        root_logger.error(u'save feed_back save error')

    return jsonify(ret_dict)


@other.route('/get_carousel', methods=['POST', 'GET'])
def get_carousel():
    test_api(request)

    ret_dict = copy.deepcopy(task1)

    cobs = Course.objects(base_info__exists=True)
    course_list = []
    keys_course_list = set([])
    for o in cobs:
        uo = o['base_info']
        obj_dict = obj2dict(o, uo, include=('picture', 'video', 'course_name', 'class_name', 'class_uuid',
                                            'browse_count', 'download_count', 'course_type',
                                            'teacher_name', 'class_summary', 'class_time', 'is_over'))
        img_key = obj_dict['picture']
        video_key = obj_dict['video']
        obj_dict['picture_url'] = get_url_qiniu(img_key)
        obj_dict['video_url'] = get_url_qiniu(video_key)
        # course_list.append(obj_dict)
        if not obj_dict['class_name'] in keys_course_list:
            course_list.append(obj_dict)
            keys_course_list.add(obj_dict['class_name'])
    course_list = course_list[-5:]
    ret_dict['data'] = course_list

    return jsonify(ret_dict)


@other.route('/list_carousel', methods=['POST', 'GET'])
def list_carousel():
    test_api(request)

    args_list = ['index', 'rowCount']
    args = handle_request_post_arguments(request, args_list)
    ret_dict = copy.deepcopy(task1)

    cobs = Course.objects(base_info__exists=True)
    course_list = []
    keys_course_list = set([])
    for o in cobs:
        uo = o['base_info']
        obj_dict = obj2dict(o, uo, include=('picture', 'video', 'course_name', 'class_name', 'class_uuid',
                                            'browse_count', 'download_count', 'course_type',
                                            'teacher_name', 'class_summary', 'class_time', 'is_over'))
        img_key = obj_dict['picture']
        video_key = obj_dict['video']
        obj_dict['picture_url'] = get_url_qiniu(img_key)
        obj_dict['video_url'] = get_url_qiniu(video_key)
        if not obj_dict['class_name'] in keys_course_list:
            course_list.append(obj_dict)
            keys_course_list.add(obj_dict['class_name'])
    # ret_dict['data'] = course_list

    course_list.reverse()
    last_length = len(course_list)
    try:
        index = int(args['index'])
        rowCount = int(args['rowCount'])
        if (index - 1) * rowCount > last_length:
            ret_dict['data'] = u'超出长度'
            ret_dict['status'] = 0
        else:
            ret_dict['data'] = \
                course_list[(index - 1) * rowCount: index * rowCount if index * rowCount < last_length else last_length]
    except ValueError:
        ret_dict['data'] = u'输出正确数子'
        ret_dict['status'] = 0

    return jsonify(ret_dict)


@other.route('/search_course', methods=['POST', 'GET'])
def search_course():
    test_api(request)

    args_list = ['keyword']
    args = handle_request_post_arguments(request, args_list)
    ret_dict = copy.deepcopy(task2)

    q = args.get('keyword', '')
    if not q == '':
        obs = Upload.objects(
            Q(class_summary__icontains=q) | Q(class_name__icontains=q) | Q(course_name__icontains=q) | Q(
                teacher_name__icontains=q))
    else:
        obs = Upload.objects()
    ret_dicts = []

    for o in obs:
        ret_course = Course.objects.get(base_info=o.id)
        try:
            ret_comments = Comment.objects(course=ret_course)
            ret_dic = obj2dict(o, include=('picture', 'comment', 'video', 'course_name', 'class_name',
                                           'teacher_name', 'class_summary', 'class_time', 'is_over'))
            commentLists = []
            for ret_comment in ret_comments:
                commentLists.append(obj2dict(ret_comment, include=('user', 'post', 'comment', 'c_time')))
            ret_dic['commentList'] = commentLists
        except DoesNotExist:
            ret_dic = obj2dict(o, include=('picture', 'video', 'course_name', 'class_name',
                                           'teacher_name', 'class_summary', 'class_time', 'is_over'))
        img_key = ret_dic['picture']
        video_key = ret_dic['video']
        ret_dic['picture_url'] = get_url_qiniu(img_key)
        ret_dic['video_url'] = get_url_qiniu(video_key)
        ret_dicts.append(ret_dic)
    ret_dict['data'] = ret_dicts

    return jsonify(ret_dict)


@other.route('/classification_course', methods=['POST', 'GET'])
def classification_course():
    test_api(request)

    ret_dict = copy.deepcopy(task3)

    cobs = Course.objects
    course_list = []
    for o in cobs:
        uo = o['base_info']
        obj_dict = obj2dict(o, uo, include=('picture', 'video', 'course_name', 'class_name', 'class_uuid',
                                            'browse_count', 'download_count', 'course_type',
                                            'teacher_name', 'class_summary', 'class_time', 'is_over'))
        img_key = obj_dict['picture']
        video_key = obj_dict['video']
        obj_dict['picture_url'] = get_url_qiniu(img_key)
        obj_dict['video_url'] = get_url_qiniu(video_key)
        course_list.append(obj_dict)
    ret_dict['data'] = course_list

    return jsonify(ret_dict)


@other.route('/get_ranking', methods=['POST', 'GET'])
def get_ranking():
    test_api(request)

    args_list = ['userId']
    args = handle_request_post_arguments(request, args_list)
    ret_dict = copy.deepcopy(task18)

    try:
        user = OauthUser.objects.get(user_id=args['userId'])
        histories = LearningHistory.objects(user=user)
    except DoesNotExist as e:
        ret_dict['status'] = 0
        ret_dict['info'] = 'argument is DoesNotExist ' + e.message

    data = []
    for history in histories:
        d_o = obj2dict(history, include=('study_time', 'user', 'c_time'))
        data.append(d_o)

    if ret_dict['status'] == 1:
        ret_dict['data'] = data

    return jsonify(ret_dict)


@other.route('/get_per_detail', methods=['POST', 'GET'])
def get_per_detail():
    test_api(request)

    args_list = ['userId']
    args = handle_request_post_arguments(request, args_list)
    ret_dict = copy.deepcopy(task19)

    try:
        user = OauthUser.objects.get(user_id=args['userId'])
        histories = LearningHistory.objects(user=user)
    except DoesNotExist as e:
        ret_dict['status'] = 0
        ret_dict['info'] = 'argument is DoesNotExist ' + e.message

    data = []
    for history in histories:
        d_o = obj2dict(history, include=('study_time', 'user', 'c_time'))
        data.append(d_o)

    if ret_dict['status'] == 1:
        ret_dict['data'] = data

    return jsonify(ret_dict)


@other.route('/my_question', methods=['POST', 'GET'])
def my_question():
    test_api(request)

    args_list = ['userId']
    args = handle_request_post_arguments(request, args_list)
    ret_dict = copy.deepcopy(task20)

    try:
        o_user = OauthUser.objects.get(user_id=args['userId'])
        o_posts = Post.objects(user=o_user)
    except DoesNotExist as e:
        ret_dict['status'] = 0
        ret_dict['info'] = 'argument is DoesNotExist ' + e.message

    if ret_dict['status'] == 1:
        re_list = []
        for o in o_posts:
            t_o = obj2dict(o, include=('course', 'user', 'post', 'post_id', 'comment_count', 'c_time',
                                       'post_img', 'post_voice', 'like_count', 'browse_count'))
            re_list.append(t_o)
        ret_dict['data'] = re_list

    return jsonify(ret_dict)


@other.route('/del_post', methods=['POST', 'GET'])
def del_post():
    test_api(request)

    args_list = ['userId', 'postId']
    args = handle_request_post_arguments(request, args_list)
    ret_dict = copy.deepcopy(task21)

    try:
        o_user = OauthUser.objects.get(user_id=args['userId'])
        o_post = Post.objects.get(user=o_user, post_id=args['postId'])
    except DoesNotExist as e:
        ret_dict['status'] = 0
        ret_dict['info'] = 'argument is DoesNotExist ' + e.message

    if ret_dict['status'] == 1:
        p_o = obj2dict(o_post, include=('course', 'user', 'post', 'post_id', 'comment_count', 'c_time',
                                        'post_img', 'post_voice', 'like_count', 'browse_count'))
        ret_dict['data'] = [p_o]
        o_post.delete()

    return jsonify(ret_dict)


@other.route('/post_time', methods=['POST', 'GET'])
def post_time():
    test_api(request)

    args_list = ['userId', 'datetime', 'studyTime']
    args = handle_request_post_arguments(request, args_list)
    ret_dict = copy.deepcopy(task24)

    try:
        c_time = datetime.strptime(args['datetime'], '%Y-%m-%d')
    except ValueError as e:
        ret_dict['status'] = 0
        ret_dict['info'] = 'argument of datetime isn`t correct format ' + e.message

    try:
        user = OauthUser.objects.get(user_id=args['userId'])
        LearningHistory(user=user, study_time=args['studyTime'], c_time=c_time).save()
    except DoesNotExist as e:
        ret_dict['status'] = 0
        ret_dict['info'] = 'argument is DoesNotExist ' + e.message

    if ret_dict['status'] == 1:
        pass

    return jsonify(ret_dict)