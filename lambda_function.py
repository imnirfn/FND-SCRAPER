import json
import boto3
from botocore.config import Config
from botocore.exceptions import ClientError


GLOBAL_CONFIG = Config(
    region_name = 'us-east-1',
    signature_version = 'v4',
    retries = {
        'max_attempts': 5,
        'mode': 'standard'
    }
)


def getDataFromDynamoDB(tblName, searchFor, operator):

    client = boto3.client("dynamodb", config = GLOBAL_CONFIG)

    response = { "Items": [] }

    try:
        response = client.scan(TableName = tblName, Select = 'ALL_ATTRIBUTES', 
            ScanFilter = {
                "CardHolder": {
                    "AttributeValueList": [
                        {
                            "S": searchFor
                        }
                    ],
                    "ComparisonOperator": operator
                }
            }
        )
    except:
        return { "error": "some exception occured!" }

    return response["Items"]


def lambda_handler(event, context):

    response = None

    params = json.loads(event["body"])

    if params == None:
        response = { "msg": "error: missing parameters" }

    else:
        CardHolder = None
        TableName = "CardDetails"
        Operator = "EQ"


        if "CardHolder" in params:
            CardHolder = params["CardHolder"]

        else:
            response = { "msg": "error: missing parameters: CardHolder (required)" }


        if response == None:
            response = getDataFromDynamoDB(tblName = TableName, searchFor = CardHolder, operator = Operator)

    # Won't happen for sure!
    if response == None:
        response = { "msg": "no records found" }

    return {
        "statusCode": 200,
        "body": json.dumps(response)
    }