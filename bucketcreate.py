import boto3
s3 = boto3.resource('s3',
                          region_name = 'us-east-1',
                          aws_access_key_id='Enter-your-own',
                          aws_secret_access_key='Enter-your-own',
                          aws_session_token='Enter-your-own')


bucket_name = 's3911506'
s3.create_bucket(Bucket=bucket_name)
