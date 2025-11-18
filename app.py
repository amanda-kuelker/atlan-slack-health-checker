from flask import Flask, request, jsonify
import json

# Create Flask app
app = Flask(__name__)

@app.route('/slack/atlan-setup', methods=['POST'])
def handle_atlan_setup():
    """Handle /atlan-health slash command"""
    
    # Parse Slack slash command
    command_text = request.form.get('text', '').strip()
    user_id = request.form.get('user_id')
    
    if not command_text:
        return jsonify({
            "response_type": "ephemeral",
            "text": """🚀 **Atlan Health Check App - Demo Version**

📋 **Usage**: `/atlan-health CustomerName https://tenant.atlan.com`

**Examples**:
- `/atlan-health "Demo Corp" https://demo.atlan.com`
- `/atlan-health "MegaBank" https://megabank.atlan.com`
- `/atlan-health "General Hospital" https://hospital.atlan.com`

✅ **Your webhook is working perfectly!**
🔧 **Full industry analysis coming soon...**"""
        })
    
    # Simple response for testing
    parts = command_text.split()
    customer_name = parts[0] if parts else "Unknown Customer"
    
    return jsonify({
        "response_type": "in_channel",
        "text": f"""🚀 **Health Check Started for {customer_name}**

✅ Webhook connection successful!
📊 Demo mode: Basic functionality working
🔧 Full industry analysis and Canvas generation coming online...

*This confirms your Slack app is properly connected!*"""
    })

@app.route('/slack/interactive', methods=['POST'])
def handle_interactive():
    """Handle interactive components"""
    return jsonify({"status": "ok"})

@app.route('/test', methods=['GET'])
@app.route('/', methods=['GET'])
def test_endpoint():
    """Test endpoint to verify server is running"""
    return jsonify({
        "status": "healthy",
        "service": "Atlan Health Check App",
        "message": "Webhook server is running on Vercel!"
    })

# This is what Vercel needs
handler = app
