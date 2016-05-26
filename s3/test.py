# -*- coding: utf-8 -*-
import boto3
from botocore.config import Config


def main():
    s3_client = boto3.client('s3', 'us-west-2', config=Config(s3={'addressing_style': 'path'}))
    # s3.Bucket(Bucket='ones-night')
    # for bucket in s3.buckets.all():
    # for key in bucket.objects.all():
    #         print(key.key)
    # s3.Object('one-night', 'hello.txt').put(Body=open('/Users/dengjing/workplace/one-night/logs/a', 'rb'))
    # print s3.upload_file("/Users/dengjing/workplace/one-night/logs/a", "one-night", "tmp2.txt")
    # print s3.list_objects(Bucket='one-night')

    # o = s3_client.get_object(Bucket='one-night', Key='tmp.txt')
    # print o
    s3_resource = boto3.resource('s3')
    object_acl = s3_resource.ObjectAcl('one-night', 'tmp.txt')
    print object_acl

    down_url = s3_client.generate_presigned_url('get_object',
                                                Params={'Bucket': "one-night", 'Key': 'tmp.txt'}, ExpiresIn=3600)
    print down_url


def main2():
    s3_client = boto3.client('s3')
    # s3_resource = boto3.resource('s3')
    s = 'one-night'
    # s3_client.create_bucket(ACL='public-read-write', Bucket=s)
    s3_client.upload_file("/Users/dengjing/workplace/one-night/logs/a", s, "tmp3.txt")
    down_url = s3_client.generate_presigned_url('get_object',
                                                Params={'Bucket': s, 'Key': 'tmp3.txt'}, ExpiresIn=3600)
    print down_url


def main3():
    s3 = boto3.resource('s3')
    bucket_acl = s3.BucketAcl('test-nn')
    bucket_acl.put(
        ACL='public-read-write',
        AccessControlPolicy={
            'Grants': [
                {
                    'Grantee': {
                        'DisplayName': 'string',
                        'EmailAddress': 'string',
                        'ID': 'string',
                        'Type': 'CanonicalUser' | 'AmazonCustomerByEmail' | 'Group',
                        'URI': 'string'
                    },
                    'Permission': 'FULL_CONTROL'
                },
            ],
            'Owner': {
                'DisplayName': 'string',
                'ID': 'string'
            }
        },
        GrantFullControl='string',
        GrantRead='string',
        GrantReadACP='string',
        GrantWrite='string',
        GrantWriteACP='string'
    )


if __name__ == '__main__':
    main2()