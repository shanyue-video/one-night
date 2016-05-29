# coding=utf-8
from utils.conf import port

__author__ = "dengjing"

'''
task1 = {
    "status": 1,  # 状态标识
    "info": u"正常",  # 状态说明
    "courseId": "12",  # 课程id
    "courseName": "场景设计",  # 课程名称
    "courseImg": "",  # 课程图片
    # "courseImg": "",                # 课程讲师
    "courseType": 1,  # 课程类型
}
'''

task1 = {
    "status": 1,  # 状态标识
    "info": u"正常",  # 状态说明
    "courses": "场景设计",  # 课程名称
}

task2 = {
    "status": 1,  # 状态标识
    "info": u"正常",  # 状态说明
    "data": [
        {
            "courseId": "12",  # 课程id
            "courseName": "场景设计",  # 课程名称
            "courseImg": "",  # 课程图片
            # "courseImg": "",  #课程讲师
            "browse": "",  # 浏览量
            "downNum": "",  # 下载量
            "courseType": "",  # 课程类型
        },
        {
            "courseId": "12",  # 课程id
            "courseName": "场景设计",  # 课程名称
            "courseImg": "",  # 课程图片
            # "courseImg": "",  #课程讲师
            "browse": "",  # 浏览量
            "downNum": "",  # 下载量
            "courseType": "",  # 课程类型
        }
    ]
}

task3 = {
    "status": 1,  # 状态标识
    "info": u"正常",  # 状态说明
    "classId": "12",  # 分类id
    "className": "场景设计",  # 分类名称
}

task4 = {
    "status": 1,  # 状态标识
    "info": u"正常",  # 状态说明
    "data": [
        {
            "courseId": "12",  # 课程id
            "courseName": "场景设计",  # 课程名称
            "courseImg": ""  # 课程图片
        }
    ]
}

task5 = {
    "status": 1,  # 状态标识
    "info": u"正常",  # 状态说明
}

task6 = {
    "status": 1,  # 状态标识
    "info": u"正常",  # 状态说明
    "courseId": "12",  # 课程id
    "courseName": "场景设计",  # 课程名称
    "courseImg": "",  # 课程图片
    "lecturerId": "",  # 课程讲师名称
    "lecturerName": "",  # 课程讲师名称
    "courseIntroduce": "",  # 课程介绍
    "browse": "",  # 浏览量
    "isCollection": "",  # 是否收藏
    "isDownload": "",  # 是否下载
    "commentList": [
        {
            "commentId": "12",  # 评论id
            "commentContent": "",  # 评论内容
            "userId": "",  # 评论人
            "userName": "",  # 评论名字
            "commentTime": "",  # 评论时间
        },
        {
            "commentId": "12",  # 评论id
            "commentContent": "",  # 评论内容
            "userId": "",  # 评论人
            "userName": "",  # 评论名字
            "commentTime": "",  # 评论时间
        },
    ],
    "chapter": [
        {
            "chapterId": "12",  # 章节id
            "chapterName": "场景设计",  # 章节名称
            "chapterUrl": "",  # 章节视频地址
            "chapterime": "",  # 章节时长
        },
        {
            "chapterId": "12",  # 章节id
            "chapterName": "场景设计",  # 章节名称
            "chapterUrl": "",  # 章节视频地址
            "chapterime": "",  # 章节时长
        }
    ]
}

task7 = {
    "status": 1,  # 状态标识
    "info": u"正常",  # 状态说明
    "chapter": {
        "chapterId": "12",  # 章节id
        "chapterName": "场景设计",  # 章节名称
        "chapterDownUrl": ""  # 章节视频地址
    }
}

task8 = {
    "status": 1,  # 状态标识 1表示成功，0表示失败
    "info": u"正常",  # 状态说明
}

task9 = {
    "status": 1,  # 状态标识 1表示成功，0表示失败
    "info": u"正常",  # 状态说明
    "data": [
        {
            "postId": "",  # 帖子id
            "userId": "",  # 发帖人id
            "postName": "",  # 帖子name
            "userName": "",  # 发帖人姓名
            "userImg": "",  # 发帖人头像
            "postTime": "",  # 发帖时间
            "postContent": "",  # 发帖内容
            "postImg": "",  # 发帖图片多张图片以分号分隔
            "likeNum": "12",  # 点赞数
            "browseNum": "16",  # 浏览量
            "commentNum": "20"  # 评论数
        },
        {
            "postId": "",  # 帖子id
            "userId": "",  # 发帖人id
            "postName": "",  # 帖子name
            "userName": "",  # 发帖人姓名
            "userImg": "",  # 发帖人头像
            "postTime": "",  # 发帖时间
            "postContent": "",  # 发帖内容
            "postImg": "",  # 发帖图片多张图片以分号分隔
            "likeNum": "12",  # 点赞数
            "browseNum": "16",  # 浏览量
            "commentNum": "20",  # 评论数
        },
    ]
}

task10 = {
    "status": 1,  # 状态标识 1表示成功，0表示失败
    "info": u"正常",  # 状态说明
    "data": [
        {
            "postId": "",  # 发帖人id
            "postName": "",  # 发帖人name
            # "postImg": "",  # 发帖人头像
            "postTime": "",  # 发帖时间
            "postContent": "",  # 发帖内容
            "postImg": "",  # 发帖图片多张图片以分号分隔
            "likeNum": "12",  # 点赞数
            "browseNum": "16",  # 浏览量
            "commentNum": "20",  # 评论数
        }
    ]
}

task11 = {
    "status": 1,  # 状态标识 1表示成功，0表示失败
    "info": u"正常",  # 状态说明
    "data": [
        {
            "postId": "",  # 帖子id
            "userId": "",  # 发帖人id
            "postName": "",  # 帖子name
            "userName": "",  # 发帖人姓名
            "userImg": "",  # 发帖人头像
            "postTime": "",  # 发帖时间
            "postContent": "",  # 发帖内容
            "postImg": "",  # 发帖图片多张图片以分号分隔
            "likeNum": "12",  # 点赞数
            "browseNum": "16",  # 浏览量
            "commentNum": "20",  # 评论数
        },
        {
            "postId": "",  # 帖子id
            "userId": "",  # 发帖人id
            "postName": "",  # 帖子name
            "userName": "",  # 发帖人姓名
            "userImg": "",  # 发帖人头像
            "postTime": "",  # 发帖时间
            "postContent": "",  # 发帖内容
            "postImg": "",  # 发帖图片多张图片以分号分隔
            "likeNum": "12",  # 点赞数
            "browseNum": "16",  # 浏览量
            "commentNum": "20"  # 评论数
        },
    ]
}

task12 = {
    "status": 1,  # 状态标识 1表示成功，0表示失败
    "info": u"正常",  # 状态说明
}

task13 = {
    "status": 1,  # 状态标识 1表示成功，0表示失败
    "info": u"正常",  # 状态说明
    "post": {
        "postId": "",  # 帖子id
        "userId": "",  # 发帖人id
        "postName": "",  # 帖子name
        "userName": "",  # 发帖人姓名
        "userImg": "",  # 发帖人头像
        "postTime": "",  # 发帖时间
        "postContent": "",  # 发帖内容
        "postImg": "",  # 发帖图片多张图片以分号分隔
        "likeNum": "12",  # 点赞数
        "browseNum": "16",  # 浏览量
        "commentNum": "20",  # 评论数
        "commentList": [
            {
                "commentId": "12",  # 评论id
                "commentContent": "",  # 评论内容
                "userId": "",  # 评论人
                "userName": "",  # 评论名字
                "userImg": "",  # 评论头像
                "commentTime": "",  # 评论时间
                "userType": "",  # 评论人身份
            },
            {
                "commentId": "12",  # 评论id
                "commentContent": "",  # 评论内容
                "userId": "",  # 评论人
                "userName": "",  # 评论名字
                "userImg": "",  # 评论头像
                "commentTime": "",  # 评论时间
                "userType": "",  # 评论人身份
                "commentImg": "",  # 评论图片
                "commentVoice": "",  # 评论语音
            }
        ]
    }
}

task14 = {
    "status": 1,  # 状态标识 1表示成功，0表示失败
    "info": u"正常",  # 状态说明
    "post": {
        "postId": "",  # 帖子id
        "userId": "",  # 发帖人id
        "postName": "",  # 帖子name
        "userName": "",  # 发帖人姓名
        "userImg": "",  # 发帖人头像
        "postTime": "",  # 发帖时间
        "postContent": "",  # 发帖内容
        "postImg": "",  # 发帖图片多张图片以分号分隔
        "likeNum": "12",  # 点赞数
        "browseNum": "16",  # 浏览量
        "commentNum": "20",  # 评论数
        "commentList": [
            {
                "commentId": "12",  # 评论id
                "commentContent": "",  # 评论内容
                "userId": "",  # 评论人
                "userName": "",  # 评论名字
                "userImg": "",  # 评论头像
                "commentTime": "",  # 评论时间
                "userType": "",  # 评论人身份
            },
            {
                "commentId": "12",  # 评论id
                "commentContent": "",  # 评论内容
                "userId": "",  # 评论人
                "userName": "",  # 评论名字
                "userImg": "",  # 评论头像
                "commentTime": "",  # 评论时间
                "userType": "",  # 评论人身份
                "commentImg": "",  # 评论图片
                "commentVoice": "",  # 评论语音
            }
        ]
    }
}

task15 = {
    "status": 1,  # 状态标识 1表示成功，0表示失败
    "info": u"正常",  # 状态说明
}

task16 = {
    "status": 1,  # 状态标识 1表示成功，0表示失败
    "info": u"正常",  # 状态说明
    " userId": "",  # 用户id
    "userName": "",  # 发帖人name
    "userType": "",  # 用户类型
    "birthday": "2015-09-10 00:00:00",
    "sex": "1",
    "mobile": "1354231321",
    "email": "",
    "iconUrl": "",  # 头像
    "nickName": "",  # 昵称
    "accessToken": "",  # 授权码
    "studyTime": "",  # 学习时间
    "ranking": ""  # 学习排名
}

task17 = {
    "status": 1,  # 状态标识 1表示成功，0表示失败
    "info": u"正常",  # 状态说明
}

task18 = {
    "status": 1,  # 状态标识 1表示成功，0表示失败
    "info": u"正常",  # 状态说明
    "data": [
        {
            "userid": "",  # 用户id
            "ranking": "",  # 名次
            "iconUrl": "",  # 头像
            "nickname": "",  # 呢称
            "studyTime": "",  # 学习时长
            "isZan": "",  # 是否点赞
        },
        {
            "ranking": "",  # 名次
            "iconUrl": "",  # 头像
            "nickname": "",  # 呢称
            "studyTime": "",  # 学习时长
            "isZan": ""  # 是否点赞
        }
    ]
}

task19 = {
    "status": 1,  # 状态标识 1表示成功，0表示失败
    "info": u"正常",  # 状态说明
    "userid": "",  # 用户id
    "ranking": "",  # 名次
    "iconUrl": "",  # 头像
    "nickname": "",  # 呢称
    "studyTime": "",  # 学习时长
    "isZan": "",  # 是否点赞
    "data": [
        {
            "datetime": "2016-05-14",  # 哪一天
            "studyTime": "300",  # 学习时间 单位为分钟
        },
        {
            "datetime": "2016-05-15",  # 哪一天
            "studyTime": "300",  # 学习时间 单位为分钟
        }
    ]
}

task20 = {
    "status": 1,  # 状态标识 1表示成功，0表示失败
    "info": u"正常",  # 状态说明
    "data": [
        {
            "postId": "",  # 帖子id
            "userId": "",  # 发帖人id
            "postName": "",  # 帖子name
            "userName": "",  # 发帖人姓名
            "userImg": "",  # 发帖人头像
            "postTime": "",  # 发帖时间
            "postContent": "",  # 发帖内容
            "postImg": "",  # 发帖图片多张图片以分号分隔
            "likeNum": "12",  # 点赞数
            "browseNum": "16",  # 浏览量
            "commentNum": "20",  # 评论数
        },
        {
            "postId": "",  # 帖子id
            "userId": "",  # 发帖人id
            "postName": "",  # 帖子name
            "userName": "",  # 发帖人姓名
            "userImg": "",  # 发帖人头像
            "postTime": "",  # 发帖时间
            "postContent": "",  # 发帖内容
            "postImg": "",  # 发帖图片多张图片以分号分隔
            "likeNum": "12",  # 点赞数
            "browseNum": "16",  # 浏览量
            "commentNum": "20",  # 评论数
        },
    ]
}

task21 = {
    "status": 1,  # 状态标识 1表示成功，0表示失败
    "info": u"正常",  # 状态说明
    "data": [
        {
            "  postId": "",  # 帖子id
            "userId": "",  # 发帖人id
            "postName": "",  # 帖子name
            "userName": "",  # 发帖人姓名
            "userImg": "",  # 发帖人头像
            "postTime": "",  # 发帖时间
            "postContent": "",  # 发帖内容
            "postImg": "",  # 发帖图片多张图片以分号分隔
            "likeNum": "12",  # 点赞数
            "browseNum": "16",  # 浏览量
            "commentNum": "20",  # 评论数
        },
        {
            "postId": "",  # 帖子id
            "userId": "",  # 发帖人id
            "postName": "",  # 帖子name
            "userName": "",  # 发帖人姓名
            "userImg": "",  # 发帖人头像
            "postTime": "",  # 发帖时间
            "postContent": "",  # 发帖内容
            "postImg": "",  # 发帖图片多张图片以分号分隔
            "likeNum": "12",  # 点赞数
            "browseNum": "16",  # 浏览量
            "commentNum": "20",  # 评论数
        },
    ]
}

task22 = {
    "status": 1,  # 状态标识 1表示成功，0表示失败
    "info": u"正常", 	# 状态说明
}

# port = '8888'
task23 = {
    "status": 1,  # 状态标识 1表示成功，0表示失败
    "info": u"正常",  # 状态说明
    "data": [
        {
            'api': 'http://api.oforever.net:%s/api/carousel' % port,
            'type': 'GET',
            'args': ''
        },
        {
            'api': 'http://api.oforever.net:%s/api/search' % port,
            'type': 'POST',
            'args': 'keyword'
        },
        {
            'api': 'http://api.oforever.net:%s/api/classification' % port,
            'type': 'GET',
            'args': ''
        },
        {
            'api': 'http://api.oforever.net:%s/api/courseList' % port,
            'type': 'GET',
            'args': 'keyword'
        },
        {
            'api': 'http://api.oforever.net:%s/api/collection' % port,
            'type': 'POST',
            'args': 'courseId, userId'
        },
        {
            'api': 'http://api.oforever.net:%s/api/chapter' % port,
            'type': 'POST',
            'args': 'courseId'
        },
        {
            'api': 'http://api.oforever.net:%s/api/download' % port,
            'type': 'POST',
            'args': u'classId  和上一个接口的chapter一样'
        },
        # {
        #     'api': 'http://api.oforever.net:%s/api/search' % port,
        #     'type': 'POST',
        #     'args': 'label, keyword, title, lecturer'
        # },
        {
            'api': 'http://api.oforever.net:%s/api/comment' % port,
            'type': 'POST',
            'args': 'courseId, userId'
        },
        {
            'api': 'http://api.oforever.net:%s/api/ListQuestion' % port,
            'type': 'POST',
            'args': ''
        },
        {
            'api': 'http://api.oforever.net:%s/api/PostNew' % port,
            'type': 'POST',
            'args': 'userid, content, label, postImgs, postVoice   #多图片参数 需要再对'
        },
        {
            'api': 'http://api.oforever.net:%s/api/searchQuestion' % port,
            'type': 'POST',
            'args': 'keyword'
        },
        {
            'api': 'http://api.oforever.net:%s/api/addlookNum' % port,
            'type': 'POST',
            'args': 'postId, userId'
        },
        {
            'api': 'http://api.oforever.net:%s/api/addLike' % port,
            'type': 'POST',
            'args': 'postId, userId, cancel'
        },
        {
            'api': 'http://api.oforever.net:%s/api/QuestionDetail' % port,
            'type': 'POST',
            'args': 'postId'
        },
        {
            'api': 'http://api.oforever.net:%s/api/Addcomment' % port,
            'type': 'POST',
            'args': 'postId, userid, commentContent, commentImg, commentVoice, commentVideo'
        },
        {
            'api': 'http://api.oforever.net:%s/api/Userinfo' % port,
            'type': 'POST',
            'args': 'userid'
        },
        {
            'api': 'http://api.oforever.net:%s/api/Saveuserinfo' % port,
            'type': 'POST',
            'args': 'userid, userName, platfromName, nickName, iconUrl, accessToken'
        },
        {
            'api': 'http://api.oforever.net:%s/api/Getranking' % port,
            'type': 'POST',
            'args': 'userid   # 上传时长的接口还未设计'
        },
        {
            'api': 'http://api.oforever.net:%s/api/GetPerDetail' % port,
            'type': 'POST',
            'args': 'userid   # 上传时长的接口还未设计'
        },
        {
            'api': 'http://api.oforever.net:%s/api/myQuestion' % port,
            'type': 'POST',
            'args': 'userid'
        },
        {
            'api': 'http://api.oforever.net:%s/api/delPost' % port,
            'type': 'POST',
            'args': 'userid, postId'
        },
        {
            'api': 'http://api.oforever.net:%s/api/Feedback' % port,
            'type': 'POST',
            'args': 'userid, content'
        },
    ]
}
