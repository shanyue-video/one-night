# -*- coding: utf-8 -*-
from utils.conf import port

# port = '8888'
task23 = {
    "status": 1,  # 状态标识 1表示成功，0表示失败
    "info": u"正常",  # 状态说明
    "data": [
        {
            'api': 'http://api.oforever.net:%s/api/carousel' % port,
            '1type': 'GET',
            'args': ''
        },
        {
            'api': 'http://api.oforever.net:%s/api/search' % port,
            '2type': 'POST',
            'args': 'keyword'
        },
        {
            'api': 'http://api.oforever.net:%s/api/classification' % port,
            '3type': 'GET',
            'args': ''
        },
        {
            'api': 'http://api.oforever.net:%s/api/courseList' % port,
            '4type': 'GET',
            'args': 'keyword'
        },
        {
            'api': 'http://api.oforever.net:%s/api/collection' % port,
            '5type': 'POST',
            'args': 'courseId, userId'
        },
        {
            'api': 'http://api.oforever.net:%s/api/chapter' % port,
            '6type': 'POST',
            'args': 'courseId'
        },
        {
            'api': 'http://api.oforever.net:%s/api/download' % port,
            '7type': 'POST',
            'args': u'courseId  和上一个接口的chapter一样'
        },
        {
            'api': 'http://api.oforever.net:%s/api/comment' % port,
            '8type': 'POST',
            'args': 'courseId, userId, comment_content'
        },
        {
            'api': 'http://api.oforever.net:%s/api/ListQuestion' % port,
            '9type': 'POST',
            'args': ''
        },
        {
            'api': 'http://api.oforever.net:%s/api/PostNew' % port,
            '10type': 'POST',
            'args': 'userId, content, post_title, label, image, voice'  # (image, voice 都是文件名)
        },
        {
            'api': 'http://api.oforever.net:%s/api/searchQuestion' % port,
            '11type': 'POST',
            'args': 'keyword'
        },
        {
            'api': 'http://api.oforever.net:%s/api/addlookNum' % port,
            '12type': 'POST',
            'args': 'postId, # 暂时逻辑上不加userId'
        },
        {
            'api': 'http://api.oforever.net:%s/api/addLike' % port,
            '13type': 'POST',
            'args': 'postId, userId, cancel #cancel为0时表示赞,为1时表示取消赞'
        },
        {
            'api': 'http://api.oforever.net:%s/api/QuestionDetail' % port,
            '14type': 'POST',
            'args': 'postId'
        },
        {
            'api': 'http://api.oforever.net:%s/api/Addcomment' % port,
            '15type': 'POST',
            'args': 'postId, userid, commentContent   # 这个暂时'
                    '和comment接口一样, commentImg, commentVoice, commentVideo'
        },
        {
            'api': 'http://api.oforever.net:%s/api/Userinfo' % port,
            '16type': 'POST',
            'args': 'user_id'
        },
        {
            'api': 'http://api.oforever.net:%s/api/Saveuserinfo' % port,
            '17type': 'POST',
            'args': 'user_id, user_name, platform_name, nick_name, icon_url, access_token'  # code 返回2 时 表示已存在
        },
        {
            'api': 'http://api.oforever.net:%s/api/Getranking' % port,
            '18type': 'POST',
            'args': 'userId   # 上传时长的接口还未设计'
        },
        {
            'api': 'http://api.oforever.net:%s/api/GetPerDetail' % port,
            '19type': 'POST',
            'args': 'userId   # 上传时长的接口还未设计'
        },
        {
            'api': 'http://api.oforever.net:%s/api/myQuestion' % port,
            '20type': 'POST',
            'args': 'userId'
        },
        {
            'api': 'http://api.oforever.net:%s/api/delPost' % port,
            '21type': 'POST',
            'args': 'userId, postId'
        },
        {
            'api': 'http://api.oforever.net:%s/api/Feedback' % port,
            '22type': 'POST',
            'args': 'user_id, content'
        },
        {
            'api': 'http://api.oforever.net:%s/api/postTime' % port,
            '23type': 'POST',
            'args': 'userId, datetime, studyTime'
        },
    ]
}


if __name__ == '__main__':
    print len(task23['data'])