# -*- coding: utf-8 -*-
from flask import jsonify, request
from handlers import api
from handlers.others import get_carousel, search_course, classification_course
from handlers.users import user_info, save_user_info
from test_res import task1, task2, task3, task4, task5, task6, task7, task8, task9, task10, task11, task12, task13, \
    task14, task15, task16, task17, task18, task19, task20, task21, task22, task23
from utils.util import use_api


@api.route('/api/carousel', methods=['GET'])
@use_api(get_carousel)
def carousel():
    return jsonify(task1)


@api.route('/api/search', methods=['POST', 'GET'])
@use_api(search_course)
def search():
    label = request.args.get('label', '')
    keyword = request.args.get('keyword', '')
    title = request.args.get('title', '')
    lecturer = request.args.get('lecturer', '')
    return jsonify(task2)


@api.route('/api/classification', methods=['GET'])
@use_api(classification_course)
def classification():
    return jsonify(task3)


@api.route('/api/courseList', methods=['GET'])
@use_api(get_carousel)
def course_list():
    return jsonify(task4)


@api.route('/api/collection', methods=['POST', 'GET'])
def collection():
    return jsonify(task5)


@api.route('/api/chapter', methods=['POST', 'GET'])
def chapter():
    courseId = request.args.get('courseId', '')
    return jsonify(task6)


@api.route('/api/download', methods=['POST', 'GET'])
def download():
    id = request.args.get('id', '')
    return jsonify(task7)


@api.route('/api/comment', methods=['POST', 'GET'])
def comment():
    courseId = request.args.get('courseId', '')
    userId = request.args.get('userId', '')
    return jsonify(task8)


@api.route('/api/question', methods=['POST', 'GET'])
def question():
    return jsonify(task9)


@api.route('/api/PostNew', methods=['POST', 'GET'])
def post_new():
    userid = request.args.get('userid', '')
    label = request.args.get('label', '')
    postImg = request.args.get('postImg', '')
    postVoice = request.args.get('postVoice', '')
    return jsonify(task10)


@api.route('/api/searchQuestion', methods=['POST', 'GET'])
def search_question():
    label = request.args.get('labeld', '')
    keyword = request.args.get('keyword', '')
    title = request.args.get('title', '')
    postName = request.args.get('postName', '')
    return jsonify(task11)


@api.route('/api/addlookNum', methods=['POST', 'GET'])
def add_look_num():
    postId = request.args.get('postId', '')
    userId = request.args.get('userId', '')
    return jsonify(task12)


@api.route('/api/addLike', methods=['POST', 'GET'])
def add_like():
    postId = request.args.get('postId', '')
    userId = request.args.get('userId', '')
    return jsonify(task13)


@api.route('/api/QuestionDetail', methods=['POST', 'GET'])
def question_detail():
    postId = request.args.get('postId', '')
    return jsonify(task14)


@api.route('/api/Addcomment', methods=['POST', 'GET'])
def add_comment():
    postId = request.args.get('postId', '')
    userid = request.args.get('userid', '')
    label = request.args.get('label', '')
    commentContent = request.args.get('commentContent', '')
    commentImg = request.args.get('commentImg', '')
    commentVoice = request.args.get('commentVoice', '')
    return jsonify(task15)


@api.route('/api/Userinfo', methods=['POST', 'GET'])
@use_api(user_info)
def user_info():
    userid = request.args.get('userid', '')
    return jsonify(task16)


@api.route('/api/Saveuserinfo', methods=['POST', 'GET'])
@use_api(save_user_info)
def save_user_info():
    userid = request.args.get('userid', '')
    userName = request.args.get('userName', '')
    platfromName = request.args.get('platfromName', '')
    nickName = request.args.get('nickName', '')
    usid = request.args.get('usid', '')
    iconUrl = request.args.get('iconUrl', '')
    accessToken = request.args.get('accessToken', '')
    return jsonify(task17)


@api.route('/api/Getranking', methods=['POST', 'GET'])
def get_ranking():
    userid = request.args.get('userid', '')
    return jsonify(task18)


@api.route('/api/GetPerDetail', methods=['POST', 'GET'])
def get_per_detail():
    userid = request.args.get('userid', '')
    return jsonify(task19)


@api.route('/api/myQuestion', methods=['POST', 'GET'])
def my_question():
    userid = request.args.get('userid', '')
    return jsonify(task20)


@api.route('/api/delPost', methods=['POST', 'GET'])
def del_post():
    userid = request.args.get('userid', '')
    postId = request.args.get('postId', '')
    return jsonify(task21)


@api.route('/api/Feedback', methods=['POST', 'GET'])
def feed_back():
    userid = request.args.get('userid', '')
    content = request.args.get('content', '')
    return jsonify(task22)


@api.route('/api/index', methods=['GET'])
def index():
    return jsonify(task23)