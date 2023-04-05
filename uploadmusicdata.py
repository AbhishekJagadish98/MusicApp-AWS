import boto3
import json


dynamodb = boto3.resource('dynamodb',
                          region_name = 'us-east-1',
                          aws_access_key_id='Enter-your-own',
                          aws_secret_access_key='Enter-your-own',
                          aws_session_token='Enter-your-own')
tableName = 'music'

tablemusic = dynamodb.Table(tableName)

with open('a1.json') as file:
    data = json.load(file)
Writer = tablemusic.batch_writer()

for i in data['songs']:
    Writer.put_item(Item=i)

print(f"Finished Loading items into the {tableName} table")
