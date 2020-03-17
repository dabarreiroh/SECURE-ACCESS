import boto3
def upload(file,filename):
    S3_ACCESS_KEY = 'AKIAYMHNAO67RML26Q7F'
    S3_SECRET_KEY= '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'
    region = 'us-east-2'
    bucket = 'mlds-4-access-secure'
    client = boto3.client('s3', aws_access_key_id=S3_ACCESS_KEY, aws_secret_access_key=S3_SECRET_KEY, region_name=region)
    response = client.upload_file(file, bucket, filename)
    return response