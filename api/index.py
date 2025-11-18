from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "status": "healthy",
        "service": "Atlan Health Check App",
        "message": "Flask app is running on Vercel!"
    })

@app.route("/test")
def test():
    return jsonify({
        "message": "Test endpoint working!",
        "method": request.method,
        "path": request.path
    })

@app.route("/slack/atlan-setup", methods=["POST"])
def slack_command():
    try:
        # Get form data from Slack
        command_text = request.form.get("text", "").strip()
        
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

# Error handler
@app.errorhandler(404)
def not_found(e):
    return jsonify({
        "status": 404, 
        "message": "Not Found",
        "path": request.path,
        "available_routes": [
            "/",
            "/test", 
            "/slack/atlan-setup (POST)"
        ]
    }), 404

# Debug: Log all requests
@app.before_request
def log_request_info():
    print(f"Request: {request.method} {request.path}")
    print(f"Headers: {dict(request.headers)}")
    if request.method == "POST":
        print(f"Form data: {dict(request.form)}")
