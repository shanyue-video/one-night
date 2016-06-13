# -*- coding: utf-8 -*-
from flask import jsonify
from handlers import api
from handlers.others import get_carousel, search_course, classification_course, feed_back
from handlers.supports import collection
from handlers.users import user_info, save_user_info
from test_res import task1, task2, task3, task4, task5, task6, task7, task8, task9, task10, task11, task12, task13, \
    task14, task15, task16, task17, task18, task19, task20, task21, task22, task23
from utils.util import use_api


@api.route('/api/carousel', methods=['GET'])
@use_api(get_carousel)
def carousel():
    return jsonify(task1)


@api.route('/api/search', methods=['POST'])
@use_api(search_course)
def search():
    return jsonify(task2)


@api.route('/api/classification', methods=['GET'])
@use_api(classification_course)
def classification():
    return jsonify(task3)


@api.route('/api/courseList', methods=['GET'])
@use_api(get_carousel)
def course_list():
    return jsonify(task4)


@api.route('/api/collection', methods=['POST'])
@use_api(collection)
def collection():
    return jsonify(task5)


@api.route('/api/chapter', methods=['POST'])
def chapter():
    return jsonify(task6)


@api.route('/api/download', methods=['POST'])
def download():
    return jsonify(task7)


@api.route('/api/comment', methods=['POST'])
def comment():
    return jsonify(task8)


@api.route('/api/ListQuestion', methods=['POST'])
def question():
    return jsonify(task9)


@api.route('/api/PostNew', methods=['POST'])
def post_new():
    return jsonify(task10)


@api.route('/api/searchQuestion', methods=['POST'])
def search_question():
    return jsonify(task11)


@api.route('/api/addlookNum', methods=['POST'])
def add_look_num():
    return jsonify(task12)


@api.route('/api/addLike', methods=['POST'])
def add_like():
    return jsonify(task13)


@api.route('/api/QuestionDetail', methods=['POST'])
def question_detail():
    return jsonify(task14)


@api.route('/api/Addcomment', methods=['POST'])
def add_comment():
    return jsonify(task15)


@api.route('/api/Userinfo', methods=['POST'])
@use_api(user_info)
def user_info():
    return jsonify(task16)


@api.route('/api/Saveuserinfo', methods=['POST'])
@use_api(save_user_info)
def save_user_info():
    return jsonify(task17)


@api.route('/api/Getranking', methods=['POST'])
def get_ranking():
    return jsonify(task18)


@api.route('/api/GetPerDetail', methods=['POST'])
def get_per_detail():
    return jsonify(task19)


@api.route('/api/myQuestion', methods=['POST'])
def my_question():
    return jsonify(task20)


@api.route('/api/delPost', methods=['POST'])
def del_post():
    return jsonify(task21)


@api.route('/api/Feedback', methods=['POST'])
@use_api(feed_back)
def feed_back():
    return jsonify(task22)


@api.route('/api/index', methods=['GET'])
def index():
    return jsonify(task23)