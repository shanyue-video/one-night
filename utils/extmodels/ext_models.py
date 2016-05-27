# -*- coding: utf-8 -*-
from datetime import datetime
from utils.models import engine, Upload, User


class Course(engine.Document):
    base_info = engine.ReferenceField(Upload)  # 应该是一一对应关系吧
    class_uuid = engine.StringField(required=True, max_length=20, unique=True, verbose_name=u'课程名称',
                                    help_text=u'不超过20个字符串，且唯一，建议按照一定格式填写，例如"课件名称-课程名称-1"')
    browse_count = engine.StringField(required=False, max_length=20, verbose_name=u'浏览量',
                                      help_text=u'浏览量')
    download_count = engine.StringField(required=False, max_length=20, verbose_name=u'下载量',
                                        help_text=u'下载量')
    course_type = engine.StringField(required=False, max_length=20, verbose_name=u'课程类型',
                                     help_text=u'课程类型')

    def __unicode__(self):
        return self.class_uuid


class Collection(engine.Document):
    course = engine.ReferenceField(Course)  # 应该是1v多
    user = engine.ReferenceField(User)
    c_time = engine.DateTimeField(default=datetime.now, verbose_name=u'创建时间')

    def __unicode__(self):
        return self.course


class Comment(engine.Document):
    course = engine.ReferenceField(Course)  # 应该是1v多
    user = engine.ReferenceField(User)
    post = engine.ReferenceField(Post)
    comment = engine.StringField(required=False, max_length=20, verbose_name=u'评论内容', help_text=u'评论内容')
    c_time = engine.DateTimeField(default=datetime.now, verbose_name=u'创建时间')

    def __unicode__(self):
        return self.comment


class Post(engine.Document):  # 对应question
    course = engine.ReferenceField(Course)  # 应该是1v多
    user = engine.ReferenceField(User)
    post = engine.StringField(required=False, max_length=20, verbose_name=u'帖子内容', help_text=u'帖子内容')
    post_id = engine.StringField(required=False, max_length=20, verbose_name=u'帖子id', help_text=u'帖子id')
    post_img = engine.StringField(required=False, max_length=20, verbose_name=u'帖子图片', help_text=u'帖子图片')
    like_count = engine.StringField(required=False, max_length=20, verbose_name=u'帖子点赞数', help_text=u'帖子点赞数')
    browse_count = engine.StringField(required=False, max_length=20, verbose_name=u'帖子浏览量', help_text=u'帖子浏览量')
    comment_count = engine.StringField(required=False, max_length=20, verbose_name=u'帖子评论量', help_text=u'帖子评论量')
    c_time = engine.DateTimeField(default=datetime.now, verbose_name=u'创建时间')

    def __unicode__(self):
        return self.post


class Feedback(engine.Document):
    user = engine.ReferenceField(User)
    content = engine.StringField(required=False, max_length=20, verbose_name=u'帖子内容', help_text=u'帖子内容')
    c_time = engine.DateTimeField(default=datetime.now, verbose_name=u'创建时间')

    def __unicode__(self):
        return self.content


class LearningHistory(engine.Document):
    user = engine.ReferenceField(User)
    # ranking = engine.StringField(required=False, max_length=20, verbose_name=u'排名', help_text=u'排名')
    study_time = engine.StringField(required=False, max_length=20, verbose_name=u'学习时长', help_text=u'学习时长')
    c_time = engine.DateTimeField(default=datetime.now, verbose_name=u'创建时间')

    def __unicode__(self):
        return self.content

