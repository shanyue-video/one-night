# -*- coding: utf-8 -*-
import boto3


Bucket = 'one-night-1'
# base_url = 'http://o7z6eyjps.bkt.clouddn.com/'
base_url = 'http://obsk2aox1.bkt.clouddn.com/'


def get_url(key):
    s3_client = boto3.client('s3')
    down_url = s3_client.generate_presigned_url('get_object',
                                                Params={'Bucket': Bucket, 'Key': key}, ExpiresIn=3600)
    return down_url


def get_url_qiniu(key):
    if key:
        return base_url + key
    else:
        return ''