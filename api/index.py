import os
import json
import hmac
import hashlib
import time
from datetime import datetime
from flask import Flask, request, jsonify

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

@app.route('/api/slack/atlan-setup', methods=['POST'])
def handle_atlan_setup():
    if not verify_slack_signature(request):
        return jsonify({"error": "Unauthorized"}), 401

    try:
        command_text = request.form.get('text', '').strip()
        
        if not command_text:
            return jsonify({
                "response_type": "ephemeral",
                "text": "🚀 **Atlan Health Check App**\n\n📋 **Usage**: `/atlan-health CustomerName https://tenant.atlan.com`"
            })

        parts = command_text.split()
        customer_name = parts[0] if parts else "Unknown Customer"

        return jsonify({
            "response_type": "in_channel",
            "text": f"🚀 **Health Check Started for {customer_name}**\n\n✅ Working on Vercel!"
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/slack/interactive', methods=['POST'])
def handle_interactive():
    if not verify_slack_signature(request):
        return jsonify({"error": "Unauthorized"}), 401
    return jsonify({"status": "ok"})

@app.route('/', methods=['GET'])
@app.route('/api', methods=['GET'])
def health_check():
    return jsonify({
        "status": "healthy",
        "service": "Atlan Health Check App"
    })

# This is important for Vercel - no handler needed, just the app
