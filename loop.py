# -*- coding: utf-8 -*-
import time
import boto3
import os
from qiniu import Auth, put_file
from utils.conf import UPLOAD_FOLDER

Bucket = 'one-night'

access_key = '4vtH5Qbea2P_qbji0mkxAqjEr4oulloHX4yDgnJP'
secret_key = 'no0C1cbm0nv26_zvVr8PPgFo2HmNk0DPtr_aDDKJ'

import sys

reload(sys)
sys.setdefaultencoding('utf-8')


def loop():
    while True:
        for f in os.listdir(UPLOAD_FOLDER):
            if not 'tmp' == f.split('_')[-1]:
                continue
            else:
                print 'start handle %s' % f
                f_path = os.path.join(UPLOAD_FOLDER, f)
                f_path_new = os.path.join(UPLOAD_FOLDER, f[:-4])
                s3_client = boto3.client('s3')
                s3_client.upload_file(f_path_new, Bucket, f[:-4])
                os.rename(f_path, f_path_new)
                print 'end handle %s' % f[:-4]
                print time.strftime("%Y/%y/%d %H:%M:%S", time.localtime(time.time()))


def loop_qiniu():
    while True:
        for f in os.listdir(UPLOAD_FOLDER):
            if not 'tmp' == f.split('_')[-1]:
                # os.remove(os.path.join(UPLOAD_FOLDER, f))
                pass
            else:
                print 'start handle %s' % f
                f_path = os.path.join(UPLOAD_FOLDER, f)
                f_path_new = os.path.join(UPLOAD_FOLDER, f[:-4])
                key = f[:-4]
                q = Auth(access_key, secret_key)
                token = q.upload_token(Bucket, key, 3600)
                local_file = f_path
                ret, _ = put_file(token, key, local_file)
                assert ret['key'] == key
                os.rename(f_path, f_path_new)
                print 'end handle %s' % key
                print time.strftime("%Y/%y/%d %H:%M:%S", time.localtime(time.time()))
    print 'pass this time while error', time.strftime("%Y/%y/%d %H:%M:%S", time.localtime(time.time()))


if __name__ == '__main__':
    loop_qiniu()