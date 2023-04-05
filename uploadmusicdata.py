import boto3
import json


dynamodb = boto3.resource('dynamodb',
                          aws_access_key_id = "ASIAX6ND5WK3CAM56IWV",
                          aws_secret_access_key= "VtSc+9mKxfW44a5onwyDxIBlwZ46+L/o49Uflt5S",
                          region_name = 'us-east-1',
                          aws_session_token="FwoGZXIvYXdzEH0aDAD9FvFz0gAR+k/tiiLNAUL4jKSl7c2HP/Saeeu/3WbpiqEvcXmAi7SJ5QQ/iU4y0aEZGyNg9o6vvVIXtgjzubBVmtnn+DezZGXiKU7ElEiH3YY0YPY2iu3V0KQ5E19i1t0TpbelaCf82wTJnBgDDWX2YFTtLeF1g7nzcgqVB3r4hN9dHj3YbAb3Dg55lSWR40n+Tm2WN8fBUvvWUDOCKmdhk8Ap2BzUENHBjQoMDaAAnNyd+xJZv9oCDYt/0GtI+OYTnhJ0+tYOejKn63ntJ7Gco+QVeaEYLbaevaooxKWLoQYyLQw2tp/+d9nHdsm250CrwGinqNBcs648ZPo/XA0M9NXs6r61QuvTsp4zucEaUg==")

tableName = 'music'

tablemusic = dynamodb.Table(tableName)

with open('a1.json') as file:
    data = json.load(file)
Writer = tablemusic.batch_writer()

for i in data['songs']:
    Writer.put_item(Item=i)

print(f"Finished Loading items into the {tableName} table")
