import json
import boto3
from decimal import Decimal

dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
table = dynamodb.Table('Properties')


def decimal_converter(obj):
    if isinstance(obj, Decimal):
        return int(obj) if obj % 1 == 0 else float(obj)
    raise TypeError


def lambda_handler(event, context):
    listing_id = event['pathParameters']['id']

    resp = table.get_item(
        Key={'L_ListingID': listing_id}
    )

    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json'
        },
        'body': json.dumps(
            resp.get('Item', {}),
            default=decimal_converter
        )
    }
