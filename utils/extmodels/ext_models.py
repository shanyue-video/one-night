# -*- coding: utf-8 -*-
from datetime import datetime
from utils.models import engine, Upload


class OauthUser(engine.Document):
    user_id = engine.StringField(required=True, max_length=20, unique=False, verbose_name=u'第三方id',
                                 help_text=u'第三方用户id, 必须的')
    user_name = engine.StringField(required=True, max_length=20, unique=False, verbose_name=u'课程名称',
                                   help_text=u'第三方用户名,必填')
    platform_name = engine.StringField(required=True, max_length=20, verbose_name=u'平台名称',
                                       help_text=u'平台名称中文,必填')
    nick_name = engine.StringField(required=False, max_length=20, verbose_name=u'昵称',
                                   help_text=u'昵称可空')
    icon_url = engine.URLField(required=False, max_length=40, verbose_name=u'头像url',
                               help_text=u'头像url， 具体什么类型存')
    access_token = engine.StringField(required=True, max_length=200, verbose_name=u'oauth的值',
                                      help_text=u'oauth值，必填')
    role = engine.StringField(required=True, default='user',
                              choices=(('user', u'普通用户'), ('admin', u'管理员')),
                              verbose_name=u'角色')

    def __unicode__(self):
        return self.access_token


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
    user = engine.ReferenceField(OauthUser)
    c_time = engine.DateTimeField(default=datetime.now, verbose_name=u'创建时间')

    def __unicode__(self):
        return self.course


class Post(engine.Document):  # 对应question
    course = engine.ReferenceField(Course)  # 应该是1v多
    user = engine.ReferenceField(OauthUser)
    post = engine.StringField(required=False, max_length=20, verbose_name=u'帖子内容', help_text=u'帖子内容')
    post_id = engine.StringField(required=False, max_length=20, verbose_name=u'帖子id', help_text=u'帖子id')
    post_img = engine.StringField(required=False, max_length=20, verbose_name=u'帖子图片', help_text=u'帖子图片')
    like_count = engine.StringField(required=False, max_length=20, verbose_name=u'帖子点赞数', help_text=u'帖子点赞数')
    browse_count = engine.StringField(required=False, max_length=20, verbose_name=u'帖子浏览量', help_text=u'帖子浏览量')
    comment_count = engine.StringField(required=False, max_length=20, verbose_name=u'帖子评论量', help_text=u'帖子评论量')
    c_time = engine.DateTimeField(default=datetime.now, verbose_name=u'创建时间')

    def __unicode__(self):
        return self.post


class Comment(engine.Document):
    course = engine.ReferenceField(Course)  # 应该是1v多
    user = engine.ReferenceField(OauthUser)
    post = engine.ReferenceField(Post)
    comment = engine.StringField(required=False, max_length=20, verbose_name=u'评论内容', help_text=u'评论内容')
    c_time = engine.DateTimeField(default=datetime.now, verbose_name=u'创建时间')

    def __unicode__(self):
        return self.comment


class Feedback(engine.Document):
    user = engine.ReferenceField(OauthUser)
    content = engine.StringField(required=False, max_length=20, verbose_name=u'帖子内容', help_text=u'帖子内容')
    c_time = engine.DateTimeField(default=datetime.now, verbose_name=u'创建时间')

    def __unicode__(self):
        return self.content


class LearningHistory(engine.Document):
    user = engine.ReferenceField(OauthUser)
    # ranking = engine.StringField(required=False, max_length=20, verbose_name=u'排名', help_text=u'排名')
    study_time = engine.StringField(required=False, max_length=20, verbose_name=u'学习时长', help_text=u'学习时长')
    c_time = engine.DateTimeField(default=datetime.now, verbose_name=u'创建时间')

    def __unicode__(self):
        return self.content

