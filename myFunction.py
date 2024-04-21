import json
import boto3
import botocore
from boto3.dynamodb.conditions import Key

dynamodb = boto3.client('dynamodb')

def lambda_handler(event, context):
    idprod = event['idproduto']
    response = dynamodb.get_item(
        TableName='produto',
        Key={
            'idProduto' : {'S': idprod}
        }
    )
    
    print(response['Item'])
   
    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps(response['Item'])
    }
