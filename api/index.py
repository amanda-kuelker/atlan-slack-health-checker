import os
import json
import hmac
import hashlib
import time
import logging
from datetime import datetime
from flask import Flask, request, jsonify

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)

SLACK_SIGNING_SECRET = os.environ.get('SLACK_SIGNING_SECRET', '')

def verify_slack_signature(req):
    """Verify that the request came from Slack"""
    if not SLACK_SIGNING_SECRET:
        return False

    slack_request_timestamp = req.headers.get('X-Slack-Request-Timestamp', '')
    slack_signature = req.headers.get('X-Slack-Signature', '')

    if not slack_request_timestamp or not slack_signature:
        return False

    try:
        request_timestamp = int(slack_request_timestamp)
        if abs(time.time() - request_timestamp) > 300:
            return False
    except (ValueError, TypeError):
        return False

    sig_basestring = f'v0:{slack_request_timestamp}:{req.get_data(as_text=True)}'
    my_signature = 'v0=' + hmac.new(
        SLACK_SIGNING_SECRET.encode(),
        sig_basestring.encode(),
        hashlib.sha256
    ).hexdigest()

    return hmac.compare_digest(my_signature, slack_signature)

# Slack slash command endpoint
@app.route('/slack/atlan-setup', methods=['POST'])
def handle_atlan_setup():
    logger.info(f"Received request to /slack/atlan-setup")
    logger.info(f"Request method: {request.method}")
    logger.info(f"Request headers: {dict(request.headers)}")
    logger.info(f"Request form data: {dict(request.form)}")
    
    # Temporarily disable signature verification for debugging
    # if not verify_slack_signature(request):
    #     return jsonify({"error": "Unauthorized"}), 401

    try:
        command_text = request.form.get('text', '').strip()
        
        if not command_text:
            response = {
                "response_type": "ephemeral",
                "text": "🚀 **Atlan Health Check App**\n\n📋 **Usage**: `/atlan-health CustomerName https://tenant.atlan.com`"
            }
        else:
            parts = command_text.split()
            customer_name = parts[0] if parts else "Unknown Customer"
            response = {
                "response_type": "in_channel", 
                "text": f"🚀 **Health Check Started for {customer_name}**\n\n✅ Working on Vercel!"
            }
        
        logger.info(f"Sending response: {response}")
        return jsonify(response)

    except Exception as e:
        logger.error(f"Error in handle_atlan_setup: {str(e)}")
        return jsonify({"error": str(e)}), 500

@app.route('/slack/interactive', methods=['POST']) 
def handle_interactive():
    # Temporarily disable signature verification for debugging
    # if not verify_slack_signature(request):
    #     return jsonify({"error": "Unauthorized"}), 401
    return jsonify({"status": "ok"})

# Alternative routes that might be hit due to Vercel routing
@app.route('/api/slack/atlan-setup', methods=['POST'])
def handle_atlan_setup_alt():
    return handle_atlan_setup()

@app.route('/api/slack/interactive', methods=['POST'])
def handle_interactive_alt():
    return handle_interactive()

@app.route('/', methods=['GET'])
@app.route('/api', methods=['GET'])
def health_check():
    return jsonify({
        "status": "healthy",
        "service": "Atlan Health Check App",
        "timestamp": datetime.now().isoformat()
    })

@app.route('/test', methods=['GET', 'POST'])
@app.route('/api/test', methods=['GET', 'POST'])
def test_endpoint():
    return jsonify({
        "message": "Test endpoint working!",
        "method": request.method,
        "path": request.path,
        "timestamp": datetime.now().isoformat()
    })

# This is important for Vercel - no handler needed, just the app
