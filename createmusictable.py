import boto3


dynamodb = boto3.resource('dynamodb',
                          aws_access_key_id = "ASIAX6ND5WK3CAM56IWV",
                          aws_secret_access_key= "VtSc+9mKxfW44a5onwyDxIBlwZ46+L/o49Uflt5S",
                          region_name = 'us-east-1',
                          aws_session_token="FwoGZXIvYXdzEH0aDAD9FvFz0gAR+k/tiiLNAUL4jKSl7c2HP/Saeeu/3WbpiqEvcXmAi7SJ5QQ/iU4y0aEZGyNg9o6vvVIXtgjzubBVmtnn+DezZGXiKU7ElEiH3YY0YPY2iu3V0KQ5E19i1t0TpbelaCf82wTJnBgDDWX2YFTtLeF1g7nzcgqVB3r4hN9dHj3YbAb3Dg55lSWR40n+Tm2WN8fBUvvWUDOCKmdhk8Ap2BzUENHBjQoMDaAAnNyd+xJZv9oCDYt/0GtI+OYTnhJ0+tYOejKn63ntJ7Gco+QVeaEYLbaevaooxKWLoQYyLQw2tp/+d9nHdsm250CrwGinqNBcs648ZPo/XA0M9NXs6r61QuvTsp4zucEaUg==")

tableName = 'music'
keys = [
    {
        'AttributeName':'title',
        'KeyType':'HASH'
    },

    {
        'AttributeName':'artist',
        'KeyType':'RANGE'
    }
]
attributes = [
    {
        'AttributeName':'title',
        'AttributeType':'S'
    },

    {
        'AttributeName':'artist',
        'AttributeType':'S'
    }
]
provisionedthroughput={
    'ReadCapacityUnits':10,
    'WriteCapacityUnits':10
}

tablemusic=dynamodb.create_table(
    TableName = tableName,
    KeySchema = keys,
    AttributeDefinitions=attributes,
    ProvisionedThroughput=provisionedthroughput
)

tablemusic.meta.client.get_waiter('table_exists').wait(TableName=tableName)



    
