import boto3
s3 = boto3.resource('s3',
                          region_name = 'us-east-1',
                          aws_access_key_id='ASIAX6ND5WK3J3QRBNQQ',
                          aws_secret_access_key='t19L5j8+ygCsTcM8Ky2S8nBKBPy0Nhd6UKr/4UQr',
                          aws_session_token='FwoGZXIvYXdzEDQaDL//A7i0EAh9WZTc5SLNAVh7Ueigek814ireKLTolTbx8tr7sGiRZcwk8Qezs1lPvPtUMhZK29qboohCa9M35zfW3U4vTTP7CY3dMyDhSy/t4fXo/pugbMih+oXdrfQe41f0x1eGqmD3bhPXX8/0z2jA2zAOjKs6scpesVgVb+ddPeIalH0w57ItBGKEY4ozhLQJYjiPr+e1860XTiKxuvzI4nIXxkqPqlY1TtkTefNiF6ub2TI4zmf+0SpfA+JJ9I92Sq6T2DeEpZBwRMpi+YCleLx320duvjgCAJMotMKzoQYyLRPbs1wjnuhuJcElt5yKlIpLbUCGIOAmp0CqxHvOBToxsej/mS8v2cyDi3qg0A==')


bucket_name = 's3911506'
s3.create_bucket(Bucket=bucket_name)
