import boto3
import json
import os
import urllib.request

#referenced https://www.geeksforgeeks.org/read-json-file-using-python/
with open('a1.json', 'r') as file:
    music = json.load(file)
#referenced https://boto3.amazonaws.com/v1/documentation/api/latest/guide/s3-uploading-files.html
s3 = boto3.resource('s3',
                          region_name = 'us-east-1',
                          aws_access_key_id='Enter-your-own',
                          aws_secret_access_key='Enter-your-own',
                          aws_session_token='Enter-your-own')
#extracts each song as value and saves artist and image url
for value in music['songs']:
    artist = value['artist']
    images = value['img_url']

    #urllib searches the web to retrieve image using url and downloads to the same path as this python file
    imagefile = os.path.basename(images)
    urllib.request.urlretrieve(images, imagefile)

    #uploads data to bucket specified in the folder format artists/'artist_name'/image.jpg
    bucket = 's3911506-test'
    s3key = f'artists/{artist}/{imagefile}'
    s3.Bucket(bucket).upload_file(imagefile, s3key)

    #removes the downloaded image in local system
    os.remove(imagefile)

    print(f'Finished {s3key}')
