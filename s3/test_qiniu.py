# -*- coding: utf-8 -*-
import datetime
import os
from qiniu import Auth, put_file
from s3.get_url import get_url_qiniu
from utils.conf import UPLOAD_FOLDER
from qiniu import BucketManager


def main1():
    access_key = '4vtH5Qbea2P_qbji0mkxAqjEr4oulloHX4yDgnJP'
    secret_key = 'no0C1cbm0nv26_zvVr8PPgFo2HmNk0DPtr_aDDKJ'

    bucket_name = 'one-night'

    q = Auth(access_key, secret_key)

    key = 'a'

    token = q.upload_token(bucket_name, key, 3600)

    local_file = os.path.join(UPLOAD_FOLDER, 'a')

    ret, info = put_file(token, key, local_file)
    print(info)


def insert_sort(lst):
    n = len(lst)
    if n == 1:
        return lst
    for i in range(1, n):
        for j in range(i, 0, -1):
            if lst[j] < lst[j-1]:
                lst[j], lst[j-1] = lst[j-1], lst[j]
    return lst


def main():
    access_key = '4vtH5Qbea2P_qbji0mkxAqjEr4oulloHX4yDgnJP'
    secret_key = 'no0C1cbm0nv26_zvVr8PPgFo2HmNk0DPtr_aDDKJ'
    bucket_name = 'one-night-1'
    q = Auth(access_key, secret_key)
    bucket = BucketManager(q)
    ret, eof, info = bucket.list(bucket_name)
    ret_items = ret['items']
    r_s = sorted(ret_items, key=lambda x: x['putTime'])
    # print r_s
    count = 0
    for i in r_s:
        # print i
        # print datetime.datetime.fromtimestamp(i['putTime']/10000000)
        if 'video' in i['mimeType']:
            print get_url_qiniu(i['key'])
            count += 1
    print count

    '''
    sort_list = []
    for i in ret['items']:
        sort_list.append(i['putTime'])
    sort_list = insert_sort(sort_list)
    for i in sort_list:
        # print i
        print datetime.datetime.fromtimestamp(i/10000000)
        # print int(i['putTime'])/1000.000
    # print info
    '''

if __name__ == '__main__':
    # main1()
    main()