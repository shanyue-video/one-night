# -*- coding: utf-8 -*-
from flask import request, jsonify
from handlers import other
from s3.get_url import get_url
from mongoengine.queryset import Q
from test_res import task22, task1
from utils.models import Upload
from utils.obj2dict import obj2dict


@other.route('/feed_back', methods=['POST', 'GET'])
def feed_back():
    userid = request.args.get('userid', '')
    content = request.args.get('content', '')
    return jsonify(task22)


@other.route('/get_carousel', methods=['POST', 'GET'])
def get_carousel():
    obs = Upload.objects
    ret_dicts = []
    for o in obs:
        ret_dic = obj2dict(o, include=('picture', 'video', 'course_name', 'class_name',
                                       'teacher_name', 'class_summary', 'class_time', 'is_over'))
        img_key = 'img-' + ret_dic['class_name'] + '.' + ret_dic['picture'][:-14].split('.')[-1]
        video_key = 'video-' + ret_dic['class_name'] + '.' + ret_dic['video'][:-14].split('.')[-1]
        ret_dic['picture_url'] = get_url(img_key)
        ret_dic['video_url'] = get_url(video_key)
        ret_dicts.append(ret_dic)
    task1['course'] = ret_dicts
    return jsonify(task1)


@other.route('/search_course', methods=['POST', 'GET'])
def search_course():
    label = request.args.get('label', '')
    key_word = request.args.get('keyword', '')
    title = request.args.get('title', '')
    lecturer = request.args.get('lecturer', '')
    q = label or key_word or title or lecturer
    if q == '':
        obs = Upload.objects(Q(class_summary__contains=q))
    else:
        obs = []
    ret_dicts = []
    for o in obs:
        ret_dic = obj2dict(o, include=('picture', 'video', 'course_name', 'class_name',
                                       'teacher_name', 'class_summary', 'class_time', 'is_over'))
        img_key = 'img-' + ret_dic['class_name'] + '.' + ret_dic['picture'][:-14].split('.')[-1]
        video_key = 'video-' + ret_dic['class_name'] + '.' + ret_dic['video'][:-14].split('.')[-1]
        ret_dic['picture_url'] = get_url(img_key)
        ret_dic['video_url'] = get_url(video_key)
        ret_dicts.append(ret_dic)
    task1['course'] = ret_dicts
    return jsonify(task1)


@other.route('/classification_course', methods=['POST', 'GET'])
def classification_course():
    obs = Upload.objects
    ret_dicts = []
    for o in obs:
        ret_dic = obj2dict(o, include=('picture', 'video', 'course_name', 'class_name',
                                       'teacher_name', 'class_summary', 'class_time', 'is_over'))
        img_key = 'img-' + ret_dic['class_name'] + '.' + ret_dic['picture'][:-14].split('.')[-1]
        video_key = 'video-' + ret_dic['class_name'] + '.' + ret_dic['video'][:-14].split('.')[-1]
        ret_dic['picture_url'] = get_url(img_key)
        ret_dic['video_url'] = get_url(video_key)
        ret_dicts.append(ret_dic)
    task1['course'] = ret_dicts
    return jsonify(task1)

