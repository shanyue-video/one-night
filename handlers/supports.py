# -*- coding: utf-8 -*-
import copy
import os
import uuid
from flask import request, jsonify
from handlers import support
from mongoengine import DoesNotExist
from mongoengine.queryset import Q
from s3.get_url import get_url_qiniu
from test_res import task5, task6, task7, task8, task9, task10, task11, task12, task13, task14, task15
from utils.conf import UPLOAD_FOLDER
from utils.extmodels.ext_models import Course, OauthUser, Collection, Comment, Post, PostLikeLog
from utils.obj2dict import obj2dict
from utils.util import test_api, handle_request_post_arguments, u_path


@support.route('/collection', methods=['POST', 'GET'])
def collection():
    test_api(request)

    args_list = ['courseId', 'userId']
    args = handle_request_post_arguments(request, args_list)
    ret_dict = copy.deepcopy(task5)

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
    ret_dict = copy.deepcopy(task6)

    try:
        o_course = Course.objects.get(class_uuid=args['courseId'])
    except DoesNotExist as e:
        ret_dict['status'] = 0
        ret_dict['info'] = 'Course argument is DoesNotExist ' + e.message

    try:
        o_comments = Comment.objects(course=o_course)
    except DoesNotExist as e:
        ret_dict['status'] = 0
        ret_dict['info'] = 'Comment argument is DoesNotExist ' + e.message

    if ret_dict['status'] == 1:
        o_upload = o_course['base_info']
        ret_dic = obj2dict(o_course, o_upload, include=('picture', 'video', 'course_name', 'class_name',
                                                        'class_uuid', 'browse_count', 'download_count',
                                                        'course_type', 'teacher_name', 'class_summary',
                                                        'class_time', 'is_over'))
        ret_coms = []
        for i in o_comments:
            ret_com = obj2dict(i, include=('user', 'post', 'comment', 'c_time'))
            ret_coms.append(ret_com)
        img_key = ret_dic['picture']
        video_key = ret_dic['video']
        ret_dic['commentList'] = ret_coms
        ret_dic['picture_url'] = get_url_qiniu(img_key)
        ret_dic['video_url'] = get_url_qiniu(video_key)
        ret_dict['data'] = [ret_dic]

    return jsonify(ret_dict)


@support.route('/download', methods=['POST', 'GET'])
def download():
    test_api(request)

    args_list = ['courseId']
    args = handle_request_post_arguments(request, args_list)
    ret_dict = copy.deepcopy(task7)

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
        img_key = ret_dic['picture']
        video_key = ret_dic['video']
        ret_dic['picture_url'] = get_url_qiniu(img_key)
        ret_dic['video_url'] = get_url_qiniu(video_key)
        ret_dict['data'] = [ret_dic]

    return jsonify(ret_dict)


@support.route('/comment', methods=['POST', 'GET'])
def comment():
    test_api(request)

    args_list = ['courseId', 'userId', 'comment_content']
    args = handle_request_post_arguments(request, args_list)
    ret_dict = copy.deepcopy(task8)

    try:
        o_course = Course.objects.get(class_uuid=args['courseId'])
        o_user = OauthUser.objects.get(user_id=args['userId'])
    except DoesNotExist as e:
        ret_dict['status'] = 0
        ret_dict['info'] = 'argument is DoesNotExist ' + e.message

    if ret_dict['status'] == 1:
        Comment(course=o_course, user=o_user, comment=args['comment_content']).save()

    return jsonify(ret_dict)


@support.route('/add_comment', methods=['POST', 'GET'])
def add_comment():
    test_api(request)

    args_list = ['postId', 'userId', 'comment_content']
    args = handle_request_post_arguments(request, args_list)
    ret_dict = copy.deepcopy(task15)

    try:
        default_course = Course.objects.get(class_uuid="1234")
        o_post = Post.objects.get(post_id=args['postId'])
        o_user = OauthUser.objects.get(user_id=args['userId'])
    except DoesNotExist as e:
        ret_dict['status'] = 0
        ret_dict['info'] = 'argument is DoesNotExist ' + e.message

    if ret_dict['status'] == 1:
        Comment(course=default_course, post=o_post, user=o_user, comment=args['comment_content']).save()

    return jsonify(ret_dict)


@support.route('/list_question', methods=['POST', 'GET'])
def list_question():
    test_api(request)

    args_list = ['index', 'rowCount', 'userId']
    args = handle_request_post_arguments(request, args_list)
    ret_dict = copy.deepcopy(task9)

    try:
        o_user = OauthUser.objects.get(user_id=args['userId'])
    except DoesNotExist as e:
        o_user = None
    except KeyError as e:
        o_user = None

    if o_user:
        p_obs = [o for o in Post.objects(user=o_user)][::-1]
    else:
        p_obs = [o for o in Post.objects][::-1]

    course_list = []
    last_length = len(p_obs)
    try:
        index = int(args['index'])
        rowCount = int(args['rowCount'])
    except ValueError:
        ret_dict['data'] = u'输出正确数子'
        ret_dict['status'] = 0
        return jsonify(ret_dict)

    if (index - 1) * rowCount > last_length:
        ret_dict['info'] = u'超出长度'
        ret_dict['status'] = 0
        return jsonify(ret_dict)
    p_obs = p_obs[(index - 1) * rowCount: index * rowCount if index * rowCount < last_length else last_length]
    for o in p_obs:
        obj_dict = obj2dict(o, include=('course', 'post_title', 'label', 'user', 'post', 'post_id', 'post_img',
                                        'like_count', 'browse_count', 'comment_count',
                                        'c_time'))
        obj_dict.update(post_content=obj_dict.pop('post'))
        try:
            obj_dict.update(browse_count=int(obj_dict.pop('browse_count')))
        except TypeError:
            obj_dict.update(browse_count=None)
        try:
            obj_dict.update(like_count=int(obj_dict.pop('like_count')))
        except TypeError:
            obj_dict.update(like_count=None)

        o_post = Post.objects(post_id=obj_dict['post_id'])[0]
        o_comments = Comment.objects(post=o_post)

        o_like_logs = PostLikeLog.objects(post=o_post)
        like_logs = {}
        for o_like in o_like_logs:
            if o_like.user.id in like_logs.keys():
                like_logs[str(o_like.user.id)] += 1
            else:
                like_logs[str(o_like.user.id)] = 1
        like_user = []
        for k in like_logs:
            if like_logs[k] % 2 == 1:
                like_user.append(k)

        comment_count = 0
        for p in o_comments:
            comment_count += 1
        obj_dict['comment_count'] = comment_count
        obj_dict['like_user'] = like_user
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
    ret_dict = copy.deepcopy(task10)

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
        i.save(u_path(str(os.path.join(UPLOAD_FOLDER, file_id) + '_tmp')))
        images.append(get_url_qiniu(file_id))

    for i in _voices:
        file_id = post_id + '_' + i.filename
        i.save(u_path(str(os.path.join(UPLOAD_FOLDER, file_id) + '_tmp')))
        voices.append(get_url_qiniu(file_id))

    if ret_dict['status'] == 1:
        Post(user=o_user, post=args['content'], label=args['label'], post_title=args['post_title'],
             post_id=post_id, post_img=images, post_voice=voices).save()

    return jsonify(ret_dict)


@support.route('/search_question', methods=['POST', 'GET'])
def search_question():
    test_api(request)

    args_list = ['keyword', 'userId']
    args = handle_request_post_arguments(request, args_list)
    ret_dict = copy.deepcopy(task11)

    q = args.get('keyword', '')

    try:
        o_user = OauthUser.objects.get(user_id=args['userId'])
    except DoesNotExist as e:
        o_user = None
    except KeyError as e:
        o_user = None

    if q != '' and o_user:
        obs = Post.objects((Q(post__icontains=q) | Q(post_id__icontains=q)) & Q(user=o_user))
    elif q != '' and not o_user:
        obs = Post.objects((Q(post__icontains=q) | Q(post_id__icontains=q)))
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
    ret_dict = copy.deepcopy(task12)

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
    ret_dict = copy.deepcopy(task13)

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
        pll = PostLikeLog(post=o_post, user=o_user, cancel=cancel)
        pll.save()
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
        # ret_dict['data'][0] = obj2dict(pll, include=('post', 'user', 'cancel', 'post', 'c_time'))

    return jsonify(ret_dict)


@support.route('/question_detail', methods=['POST', 'GET'])
def question_detail():
    test_api(request)

    args_list = ['postId']
    args = handle_request_post_arguments(request, args_list)
    ret_dict = copy.deepcopy(task14)

    try:
        o_post = Post.objects(post_id=args['postId'])[0]
        o_comments = Comment.objects(post=o_post)
    except DoesNotExist as e:
        ret_dict['status'] = 0
        ret_dict['info'] = 'argument is DoesNotExist ' + e.message

    if ret_dict['status'] == 1:
        ret_dic = obj2dict(o_post, include=('course', 'user', 'post_title', 'post', 'post_id', 'comment_count',
                                            'c_time', 'post_img', 'post_voice', 'like_count', 'browse_count'))
        comment_list = []
        ret_dic['post_content'] = ret_dic['post']
        del ret_dic['post']
        comment_count = 0
        for c in o_comments:
            dic_c = obj2dict(c, include=('course', 'user', 'post', 'comment', 'c_time'))
            comment_count += 1
            comment_list.append(dic_c)

        o_like_logs = PostLikeLog.objects(post=o_post)
        like_logs = {}
        for o_like in o_like_logs:
            if o_like.user.id in like_logs.keys():
                like_logs[str(o_like.user.id)] += 1
            else:
                like_logs[str(o_like.user.id)] = 1
        like_user = []
        for k in like_logs:
            if like_logs[k] % 2 == 1:
                like_user.append(k)
        ret_dict['data'] = [ret_dic]
        ret_dict['data'][0]['like_user'] = like_user
        ret_dict['data'][0]['commentList'] = comment_list
        ret_dict['data'][0]['comment_count'] = comment_count

    return jsonify(ret_dict)
