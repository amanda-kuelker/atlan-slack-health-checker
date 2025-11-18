import json

def handler(event, context):
    """Health check endpoint for Netlify"""
    
    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Allow-Methods': 'GET, POST, OPTIONS'
        },
        'body': json.dumps({
            "status": "healthy",
            "service": "Atlan Professional Health Check with MCP Integration - Netlify",
            "version": "3.0.0-netlify",
            "platform": "Netlify Functions"
        })
    }
