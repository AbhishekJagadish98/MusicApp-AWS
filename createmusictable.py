import boto3


dynamodb = boto3.resource('dynamodb',
                          region_name = 'us-east-1',
                          aws_access_key_id='Enter-your-own',
                          aws_secret_access_key='Enter-your-own',
                          aws_session_token='Enter-your-own')
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



    
