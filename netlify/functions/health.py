def handler(event, context):
    """Simple health check function for Netlify"""
    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin": "*"
        },
        "body": '{"status":"healthy","message":"Python function working","timestamp":"2025-11-18"}'
    }
