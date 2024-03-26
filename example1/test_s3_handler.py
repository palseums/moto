from moto import mock_aws
from file4 import S3Handler
import boto3



@mock_aws
def test_upload_s3_file():
    s3_client = boto3.client("s3")
    s3_client.create_bucket(Bucket="mybucket")
    s3_handler = S3Handler()
    s3_handler.upload_s3_file()