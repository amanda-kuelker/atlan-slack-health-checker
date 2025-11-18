import os
import json
import hmac
import hashlib
import time
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

SLACK_SIGNING_SECRET = os.getenv('SLACK_SIGNING_SECRET', '')


def verify_slack_signature(headers, body):
    """Verify that the request came from Slack"""
    if not SLACK_SIGNING_SECRET:
        print("WARNING: SLACK_SIGNING_SECRET not configured")
        return False

    slack_request_timestamp = headers.get('x-slack-request-timestamp', '')
    slack_signature = headers.get('x-slack-signature', '')

    if not slack_request_timestamp or not slack_signature:
        return False

    try:
        request_timestamp = int(slack_request_timestamp)
    except (ValueError, TypeError):
        return False

    if abs(time.time() - request_timestamp) > 300:
        return False

    sig_basestring = f'v0:{slack_request_timestamp}:{body}'
    my_signature = 'v0=' + hmac.new(
        SLACK_SIGNING_SECRET.encode(),
        sig_basestring.encode(),
        hashlib.sha256
    ).hexdigest()

    return hmac.compare_digest(my_signature, slack_signature)


def handler(event, context):
    """Netlify function handler"""

    headers = event.get('headers', {})
    method = event['httpMethod']
    path = event['path']
    body = event.get('body', '')

    cors_headers = {
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': 'GET, POST, OPTIONS',
        'Access-Control-Allow-Headers': 'Content-Type',
        'Content-Type': 'application/json'
    }

    if method == 'OPTIONS':
        return {
            'statusCode': 200,
            'headers': cors_headers,
            'body': ''
        }

    if path == '/health' and method == 'GET':
        return {
            'statusCode': 200,
            'headers': cors_headers,
            'body': json.dumps({
                'status': 'healthy',
                'service': 'Atlan Health Check App',
                'version': '1.0.0',
                'timestamp': datetime.utcnow().isoformat()
            })
        }

    if path == '/' and method == 'GET':
        return {
            'statusCode': 200,
            'headers': cors_headers,
            'body': json.dumps({
                'status': 'healthy',
                'service': 'Atlan Health Check App',
                'version': '1.0.0',
                'timestamp': datetime.utcnow().isoformat()
            })
        }

    if path == '/slack/atlan-setup' and method == 'POST':
        if not verify_slack_signature(headers, body):
            return {
                'statusCode': 401,
                'headers': cors_headers,
                'body': json.dumps({'error': 'Unauthorized'})
            }

        try:
            from urllib.parse import parse_qs
            params = parse_qs(body)
            command_text = params.get('text', [''])[0].strip()
            user_id = params.get('user_id', [''])[0]
            team_id = params.get('team_id', [''])[0]

            if not command_text:
                response = {
                    'response_type': 'ephemeral',
                    'text': """🚀 **Atlan Health Check App**

📋 **Usage**: `/atlan-health CustomerName https://tenant.atlan.com`

**Examples**:
- `/atlan-health "Demo Corp" https://demo.atlan.com`
- `/atlan-health "MegaBank" https://megabank.atlan.com`
- `/atlan-health "General Hospital" https://hospital.atlan.com`

✅ **Your webhook is working perfectly!**
🔧 **Ready to analyze your data ecosystem...**"""
                }
            else:
                parts = command_text.split()
                customer_name = parts[0] if parts else 'Unknown Customer'

                response = {
                    'response_type': 'in_channel',
                    'text': f"""🚀 **Health Check Started for {customer_name}**

✅ Webhook connection successful!
📊 Processing your data ecosystem...
🔧 Full industry analysis and Canvas generation coming online...

*This confirms your Slack app is properly connected!*"""
                }

            return {
                'statusCode': 200,
                'headers': cors_headers,
                'body': json.dumps(response)
            }

        except Exception as e:
            print(f"Error in handle_atlan_setup: {str(e)}")
            return {
                'statusCode': 500,
                'headers': cors_headers,
                'body': json.dumps({
                    'response_type': 'ephemeral',
                    'text': '❌ An error occurred processing your request'
                })
            }

    if path == '/slack/interactive' and method == 'POST':
        if not verify_slack_signature(headers, body):
            return {
                'statusCode': 401,
                'headers': cors_headers,
                'body': json.dumps({'error': 'Unauthorized'})
            }

        try:
            return {
                'statusCode': 200,
                'headers': cors_headers,
                'body': json.dumps({'status': 'ok'})
            }
        except Exception as e:
            print(f"Error in handle_interactive: {str(e)}")
            return {
                'statusCode': 500,
                'headers': cors_headers,
                'body': json.dumps({'error': 'Internal server error'})
            }

    return {
        'statusCode': 404,
        'headers': cors_headers,
        'body': json.dumps({'error': 'Not found'})
    }
