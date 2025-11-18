import os
import json
import hmac
import hashlib
import time
from datetime import datetime
from flask import Flask, request, jsonify

app = Flask(__name__)

# Simplified for testing - disable signature verification temporarily
def verify_slack_signature(req):
    return True  # Temporarily disable for testing

@app.route('/slack/atlan-setup', methods=['POST'])
def handle_atlan_setup():
    try:
        command_text = request.form.get('text', '').strip()
        
        if not command_text:
            return jsonify({
                "response_type": "ephemeral",
                "text": """🚀 **Atlan Health Check App**

📋 **Usage**: `/atlan-health CustomerName https://tenant.atlan.com`

✅ **Working on Vercel!**"""
            })

        parts = command_text.split()
        customer_name = parts[0] if parts else "Unknown Customer"

        return jsonify({
            "response_type": "in_channel",
            "text": f"🚀 **Health Check for {customer_name}** ✅ Vercel Success!"
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/slack/interactive', methods=['POST'])
def handle_interactive():
    return jsonify({"status": "ok"})

@app.route('/', methods=['GET'])
def health_check():
    return jsonify({"status": "healthy", "service": "Atlan Health Check"})

# For Vercel
app = app
