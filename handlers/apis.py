# -*- coding: utf-8 -*-
from flask import jsonify, request
from handlers import api
from handlers.users import user_info
from test_res import task1, task2, task3, task4, task5, task6, task7, task8, task9, task10, task11, task12, task13, \
    task14, task15, task16, task17, task18, task19, task20, task21, task22, task23
from utils.models import Test
from utils.util import use_api


@api.route('/api/carousel', methods=['GET'])
def carousel():
    t = Test()
    t.email = 'haha'
    t.first_name = 'lala'
    t.last_name = 'hehe'
    t.save()
    return jsonify(task1)


@api.route('/api/search', methods=['POST'])
def search():
    label = request.args.get('label', '')
    keyword = request.args.get('keyword', '')
    title = request.args.get('title', '')
    lecturer = request.args.get('lecturer', '')
    return jsonify(task2)


@api.route('/api/classification', methods=['GET'])
def classification():
    return jsonify(task3)


@api.route('/api/courseList', methods=['GET'])
def course_list():
    return jsonify(task4)


@api.route('/api/collection', methods=['POST'])
def collection():
    return jsonify(task5)


@api.route('/api/chapter', methods=['POST'])
def chapter():
    courseId = request.args.get('courseId', '')
    return jsonify(task6)


@api.route('/api/download', methods=['POST'])
def download():
    id = request.args.get('id', '')
    return jsonify(task7)


@api.route('/api/comment', methods=['POST'])
def comment():
    courseId = request.args.get('courseId', '')
    userId = request.args.get('userId', '')
    return jsonify(task8)


@api.route('/api/question', methods=['POST'])
def question():
    return jsonify(task9)


@api.route('/api/PostNew', methods=['POST'])
def post_new():
    userid = request.args.get('userid', '')
    label = request.args.get('label', '')
    postImg = request.args.get('postImg', '')
    postVoice = request.args.get('postVoice', '')
    return jsonify(task10)


@api.route('/api/searchQuestion', methods=['POST'])
def search_question():
    label = request.args.get('labeld', '')
    keyword = request.args.get('keyword', '')
    title = request.args.get('title', '')
    postName = request.args.get('postName', '')
    return jsonify(task11)


@api.route('/api/addlookNum', methods=['POST'])
def add_look_num():
    postId = request.args.get('postId', '')
    userId = request.args.get('userId', '')
    return jsonify(task12)


@api.route('/api/addLike', methods=['POST'])
def add_like():
    postId = request.args.get('postId', '')
    userId = request.args.get('userId', '')
    return jsonify(task13)


@api.route('/api/QuestionDetail', methods=['POST'])
def question_detail():
    postId = request.args.get('postId', '')
    return jsonify(task14)


@api.route('/api/Addcomment', methods=['POST'])
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


@api.route('/api/Saveuserinfo', methods=['POST'])
def save_user_info():
    userid = request.args.get('userid', '')
    userName = request.args.get('userName', '')
    platfromName = request.args.get('platfromName', '')
    nickName = request.args.get('nickName', '')
    usid = request.args.get('usid', '')
    iconUrl = request.args.get('iconUrl', '')
    accessToken = request.args.get('accessToken', '')
    return jsonify(task17)


@api.route('/api/Getranking', methods=['POST'])
def get_ranking():
    userid = request.args.get('userid', '')
    return jsonify(task18)


@api.route('/api/GetPerDetail', methods=['POST'])
def get_per_detail():
    userid = request.args.get('userid', '')
    return jsonify(task19)


@api.route('/api/myQuestion', methods=['POST'])
def my_question():
    userid = request.args.get('userid', '')
    return jsonify(task20)


@api.route('/api/delPost', methods=['POST'])
def del_post():
    userid = request.args.get('userid', '')
    postId = request.args.get('postId', '')
    return jsonify(task21)


@api.route('/api/Feedback', methods=['POST'])
def feed_back():
    userid = request.args.get('userid', '')
    content = request.args.get('content', '')
    return jsonify(task22)


@api.route('/api/index', methods=['GET'])
def index():
    return jsonify(task23)