import json

def handler(event, context):
    """Test endpoint for Netlify"""
    
    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Allow-Methods': 'GET, POST, OPTIONS'
        },
        'body': json.dumps({
            "message": "Professional health check system ready on Netlify!",
            "mcp_integration": "Available",
            "platform": "Netlify Functions",
            "example": '/atlan-health "DPR Construction" https://dpr.atlan.com industry:construction tags:Safety,OSHA'
        })
    }
