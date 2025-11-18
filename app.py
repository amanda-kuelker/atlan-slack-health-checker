import os
import json
import hmac
import hashlib
import time
from datetime import datetime
from flask import Flask, request, jsonify
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

SLACK_SIGNING_SECRET = os.getenv('SLACK_SIGNING_SECRET', '')


def verify_slack_signature(req):
    """Verify that the request came from Slack"""
    if not SLACK_SIGNING_SECRET:
        print("WARNING: SLACK_SIGNING_SECRET not configured")
        return False

    slack_request_timestamp = req.headers.get('X-Slack-Request-Timestamp', '')
    slack_signature = req.headers.get('X-Slack-Signature', '')

    if not slack_request_timestamp or not slack_signature:
        return False

    try:
        request_timestamp = int(slack_request_timestamp)
    except (ValueError, TypeError):
        return False

    if abs(time.time() - request_timestamp) > 300:
        return False

    sig_basestring = f'v0:{slack_request_timestamp}:{req.get_data(as_text=True)}'
    my_signature = 'v0=' + hmac.new(
        SLACK_SIGNING_SECRET.encode(),
        sig_basestring.encode(),
        hashlib.sha256
    ).hexdigest()

    return hmac.compare_digest(my_signature, slack_signature)


@app.route('/slack/atlan-setup', methods=['POST'])
def handle_atlan_setup():
    """Handle /atlan-health slash command"""

    if not verify_slack_signature(request):
        return jsonify({"error": "Unauthorized"}), 401

    try:
        command_text = request.form.get('text', '').strip()
        user_id = request.form.get('user_id')
        team_id = request.form.get('team_id')

        if not command_text:
            return jsonify({
                "response_type": "ephemeral",
                "text": """🚀 **Atlan Health Check App**

📋 **Usage**: `/atlan-health CustomerName https://tenant.atlan.com`

**Examples**:
- `/atlan-health "Demo Corp" https://demo.atlan.com`
- `/atlan-health "MegaBank" https://megabank.atlan.com`
- `/atlan-health "General Hospital" https://hospital.atlan.com`

✅ **Your webhook is working perfectly!**
🔧 **Ready to analyze your data ecosystem...**"""
            })

        parts = command_text.split()
        customer_name = parts[0] if parts else "Unknown Customer"

        return jsonify({
            "response_type": "in_channel",
            "text": f"""🚀 **Health Check Started for {customer_name}**

✅ Webhook connection successful!
📊 Processing your data ecosystem...
🔧 Full industry analysis and Canvas generation coming online...

*This confirms your Slack app is properly connected!*"""
        })

    except Exception as e:
        print(f"Error in handle_atlan_setup: {str(e)}")
        return jsonify({
            "response_type": "ephemeral",
            "text": "❌ An error occurred processing your request"
        }), 500


@app.route('/slack/interactive', methods=['POST'])
def handle_interactive():
    """Handle interactive components"""

    if not verify_slack_signature(request):
        return jsonify({"error": "Unauthorized"}), 401

    try:
        return jsonify({"status": "ok"})
    except Exception as e:
        print(f"Error in handle_interactive: {str(e)}")
        return jsonify({"error": "Internal server error"}), 500


@app.route('/health', methods=['GET'])
@app.route('/', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({
        "status": "healthy",
        "service": "Atlan Health Check App",
        "version": "1.0.0",
        "timestamp": datetime.utcnow().isoformat()
    }), 200


if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
