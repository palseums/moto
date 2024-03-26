import boto3.session
import moto
import pytest
from bucket_main import bucket_exists

EXISTING_BUCKET = "my_bucket"
REGION = "us-west-2"

@pytest.fixture()
def mock_session():
    with moto.mock_aws():
        session = boto3.session.Session(aws_access_key_id="FAKE_KEY",aws_secret_access_key="FAKE_SECRET")
        bucket_name = EXISTING_BUCKET
        s3_client = session.client("s3")
        s3_client.create_bucket(Bucket=bucket_name)
        yield session


def test_bucket_does_not_exists(mock_session):
    assert not bucket_exists(mock_session,"my_bucket_doesnot")


def test_bucket_exists(mock_session):
    assert bucket_exists(mock_session,"my_bucket")
