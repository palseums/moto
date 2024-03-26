import boto3

def bucket_exists(session:boto3.session,name:str):
    s3 = session.client("s3")
    response = s3.list_buckets()
    buckets = [bucket["Name"] for bucket in response["Buckets"]]
    return name in buckets
