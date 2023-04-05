import boto3
import json
import os
import urllib.request

#referenced https://www.geeksforgeeks.org/read-json-file-using-python/
with open('a1.json', 'r') as file:
    music = json.load(file)
#referenced https://boto3.amazonaws.com/v1/documentation/api/latest/guide/s3-uploading-files.html
s3 = boto3.resource('s3',
                          aws_access_key_id = "ASIAX6ND5WK3CAM56IWV",
                          aws_secret_access_key= "VtSc+9mKxfW44a5onwyDxIBlwZ46+L/o49Uflt5S",
                          region_name = 'us-east-1',
                          aws_session_token="FwoGZXIvYXdzEH0aDAD9FvFz0gAR+k/tiiLNAUL4jKSl7c2HP/Saeeu/3WbpiqEvcXmAi7SJ5QQ/iU4y0aEZGyNg9o6vvVIXtgjzubBVmtnn+DezZGXiKU7ElEiH3YY0YPY2iu3V0KQ5E19i1t0TpbelaCf82wTJnBgDDWX2YFTtLeF1g7nzcgqVB3r4hN9dHj3YbAb3Dg55lSWR40n+Tm2WN8fBUvvWUDOCKmdhk8Ap2BzUENHBjQoMDaAAnNyd+xJZv9oCDYt/0GtI+OYTnhJ0+tYOejKn63ntJ7Gco+QVeaEYLbaevaooxKWLoQYyLQw2tp/+d9nHdsm250CrwGinqNBcs648ZPo/XA0M9NXs6r61QuvTsp4zucEaUg==")

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
