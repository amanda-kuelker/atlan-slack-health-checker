from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/slack/atlan-setup', methods=['POST'])
def handle_atlan_setup():
    """Handle /atlan-health slash command"""
    try:
        command_text = request.form.get('text', '').strip()
        
        if not command_text:
            return jsonify({
                "response_type": "ephemeral",
                "text": "🚀 **Atlan Health Check** - Ready to use!"
            })
        
        parts = command_text.split()
        customer_name = parts[0] if parts else "Unknown Customer"
        
        return jsonify({
            "response_type": "in_channel",
            "text": f"✅ Health Check for {customer_name} - Working on Vercel!"
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/slack/interactive', methods=['POST'])
def handle_interactive():
    return jsonify({"status": "ok"})

@app.route('/api/health', methods=['GET'])
@app.route('/', methods=['GET'])
def health_check():
    return jsonify({"status": "healthy", "service": "Atlan Health Check"})

# Vercel handler
handler = app
