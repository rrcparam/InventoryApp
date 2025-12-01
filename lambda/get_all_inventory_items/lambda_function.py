import json
import boto3

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table("Inventory")


def response(status_code, body):
    return {
        "statusCode": status_code,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps(body),
    }


def lambda_handler(event, context):
    """
    GET /item
    Returns all inventory items.
    """
    try:
        result = table.scan()
        items = result.get("Items", [])

        return response(200, {
            "message": "All inventory items",
            "count": len(items),
            "items": items,
        })
    except Exception as e:
        return response(500, {"error": str(e)})

