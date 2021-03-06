# -*- coding: utf-8 -*-
from datetime import datetime
from flask.ext.mongoengine import MongoEngine
from flask.ext.mongoengine.wtf import model_form

engine = MongoEngine()


class Test(engine.Document):
    email = engine.StringField(required=True)
    first_name = engine.StringField(max_length=50)
    last_name = engine.StringField(max_length=50)


class TestEverything(engine.Document):
    t1 = engine.StringField()
    t2 = engine.StringField()
    t3 = engine.StringField()


class User(engine.Document):
    username = engine.StringField(required=True, max_length=20, unique=True, verbose_name=u'用户名')
    password_hash = engine.StringField(max_length=255, required=True, verbose_name=u'密码')
    role = engine.StringField(required=True, default='user',
                              choices=(('user', u'普通用户'), ('admin', u'管理员')),
                              verbose_name=u'角色')

    def __unicode__(self):
        return self.username


class Upload(engine.Document):
    picture = engine.StringField(verbose_name=u'课程截图', help_text=u'视频截图，显示在当前课程首页的')
    picture_size = engine.StringField(default='', verbose_name=u'课程截图大小',
                                      help_text=u'视频截图，显示在当前课程首页的')
    video = engine.StringField(verbose_name=u'课程视频', help_text=u'视频文件')
    video_size = engine.StringField(default='', verbose_name=u'课程视频大小', help_text=u'视频文件')
    course_name = engine.StringField(required=True, max_length=40, unique=True, verbose_name=u'课件名称',
                                     help_text=u'不超过40个字符串且唯一')
    class_name = engine.StringField(required=True, max_length=40, unique=False, verbose_name=u'课程名称',
                                    help_text=u'不超过40个字符串，建议按照一定格式填写，例如"章节名称-1"')
    teacher_name = engine.StringField(max_length=40, required=False, verbose_name=u'老师名称',
                                      help_text=u'不超过40个字符串')
    class_summary = engine.StringField(required=False, max_length=2000, verbose_name=u'课程简介',
                                       help_text=u'不超过2000个字符串')
    class_time = engine.StringField(required=False, max_length=20, verbose_name=u'课程时长',
                                    help_text=u'视频长度，非精确，单位为秒，如写做"3:20"')
    is_over = engine.BooleanField(default=False, verbose_name=u'是否完结')
    user = engine.ReferenceField(User)
    c_time = engine.DateTimeField(default=datetime.now, verbose_name=u'创建时间')

    # def __unicode__(self):
    #     return self.class_name


UserForm = model_form(User, exclude=('role',))
UploadForm = model_form(Upload, exclude=('user', 'c_time', 'picture', 'video', 'class_summary',
                                         'picture_size', 'video_size'))


if __name__ == '__main__':
    from utils.obj2dict import obj2dict
    u = Upload()
    print obj2dict(u, include=('class_name',))
