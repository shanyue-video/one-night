# coding=utf-8
from utils.conf import port


task1 = {
    "status": 1,  # 状态标识
    "info": u"正常",  # 状态说明
    "data": []
}

task2 = {
    "status": 1,  # 状态标识
    "info": u"正常",  # 状态说明
    "data": []
}

task3 = {
    "status": 1,  # 状态标识
    "info": u"正常",  # 状态说明
    "data": [
        {
            "classId": "12",  # 分类id
            "className": "场景设计",  # 分类名称
        }
    ]

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
    "data": []
}

task6 = {
    "status": 1,  # 状态标识
    "info": u"正常",  # 状态说明
    "data": [
        {
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
    ]

}

task7 = {
    "status": 1,  # 状态标识
    "info": u"正常",  # 状态说明
    "data": [
        {
            "chapter": {
                "chapterId": "12",  # 章节id
                "chapterName": "场景设计",  # 章节名称
                "chapterDownUrl": ""  # 章节视频地址
            }
        }
    ]
}

task8 = {
    "status": 1,  # 状态标识 1表示成功，0表示失败
    "info": u"正常",  # 状态说明
    "data": []
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
    "data": []
}

task13 = {
    "status": 1,  # 状态标识 1表示成功，0表示失败
    "info": u"正常",  # 状态说明
    "data": [
        {
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
    ]

}

task14 = {
    "status": 1,  # 状态标识 1表示成功，0表示失败
    "info": u"正常",  # 状态说明
    "data": [
        {
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
    ]
}

task15 = {
    "status": 1,  # 状态标识 1表示成功，0表示失败
    "info": u"正常",  # 状态说明
    "data": []
}

task16 = {
    "status": 1,  # 状态标识 1表示成功，0表示失败
    "info": u"正常",  # 状态说明
    "data": [
        {
            "userId": "",  # 用户id
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
    ]
}

task17 = {
    "status": 1,  # 状态标识 1表示成功，0表示失败
    "info": u"正常",  # 状态说明
    "data": []
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
    "data": [
        {
            "userid": "",  # 用户id
            "ranking": "",  # 名次
            "iconUrl": "",  # 头像
            "nickname": "",  # 呢称
            "isZan": "",  # 是否点赞
            "datetime": "2016-05-14",  # 哪一天
            "studyTime": "300",  # 学习时间 单位为分钟
        },
        {
            "userid": "",  # 用户id
            "ranking": "",  # 名次
            "iconUrl": "",  # 头像
            "nickname": "",  # 呢称
            "isZan": "",  # 是否点赞
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
    "info": u"正常",  # 状态说明
    "data": []
}

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
            'args': u'classId  和上一个接口的chapter一样'
        },
        {
            'api': 'http://api.oforever.net:%s/api/comment' % port,
            '8type': 'POST',
            'args': 'courseId, userId'
        },
        {
            'api': 'http://api.oforever.net:%s/api/ListQuestion' % port,
            '9type': 'POST',
            'args': ''
        },
        {
            'api': 'http://api.oforever.net:%s/api/PostNew' % port,
            '10type': 'POST',
            'args': 'userid, content, label, postImgs, postVoice   #多图片参数 需要再对'
        },
        {
            'api': 'http://api.oforever.net:%s/api/searchQuestion' % port,
            '11type': 'POST',
            'args': 'keyword'
        },
        {
            'api': 'http://api.oforever.net:%s/api/addlookNum' % port,
            '12type': 'POST',
            'args': 'postId, userId'
        },
        {
            'api': 'http://api.oforever.net:%s/api/addLike' % port,
            '13type': 'POST',
            'args': 'postId, userId, cancel'
        },
        {
            'api': 'http://api.oforever.net:%s/api/QuestionDetail' % port,
            '14type': 'POST',
            'args': 'postId'
        },
        {
            'api': 'http://api.oforever.net:%s/api/Addcomment' % port,
            '15type': 'POST',
            'args': 'postId, userid, commentContent, commentImg, commentVoice, commentVideo'
        },
        {
            'api': 'http://api.oforever.net:%s/api/Userinfo' % port,
            '16type': 'POST',
            'args': 'user_id'
        },
        {
            'api': 'http://api.oforever.net:%s/api/Saveuserinfo' % port,
            '17type': 'POST',
            'args': 'user_id, user_name, platform_name, nick_name, icon_url, access_token'
        },
        {
            'api': 'http://api.oforever.net:%s/api/Getranking' % port,
            '18type': 'POST',
            'args': 'userid   # 上传时长的接口还未设计'
        },
        {
            'api': 'http://api.oforever.net:%s/api/GetPerDetail' % port,
            '19type': 'POST',
            'args': 'userid   # 上传时长的接口还未设计'
        },
        {
            'api': 'http://api.oforever.net:%s/api/myQuestion' % port,
            '20type': 'POST',
            'args': 'userid'
        },
        {
            'api': 'http://api.oforever.net:%s/api/delPost' % port,
            '21type': 'POST',
            'args': 'userid, postId'
        },
        {
            'api': 'http://api.oforever.net:%s/api/Feedback' % port,
            '22type': 'POST',
            'args': 'userid, content'
        },
    ]
}

if __name__ == '__main__':
    print len(task23['data'])