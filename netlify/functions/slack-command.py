import json
import urllib.parse

def handler(event, context):
    """Simple Slack command function for Netlify"""
    
    # Parse Slack form data
    body = event.get('body', '')
    
    # Check if it's a Slack request
    if 'token=' in body and 'text=' in body:
        # Parse form data
        form_data = urllib.parse.parse_qs(body)
        command_text = form_data.get('text', [''])[0]
        
        # Simple response
        response = {
            "response_type": "in_channel",
            "text": f"🎉 **Python Functions Working!**\n\nReceived command: `{command_text}`\n\n✅ Netlify deployment successful!\n✅ Python functions active!\n✅ Slack integration working!\n\nReady for full health assessment integration."
        }
        
        return {
            "statusCode": 200,
            "headers": {"Content-Type": "application/json"},
            "body": json.dumps(response)
        }
    
    # Default response for browser requests
    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin": "*"
        },
        "body": json.dumps({
            "message": "Slack command handler ready!",
            "status": "working",
            "usage": "/atlan-health test"
        })
    }
