from flask import Flask, request, jsonify

app = Flask(__name__)

def handler(request):
    """Vercel serverless function handler"""
    
    if request.method == 'POST':
        # Parse Slack slash command
        command_text = request.form.get('text', '').strip()
        user_id = request.form.get('user_id')
        
        if not command_text:
            return {
                "response_type": "ephemeral",
                "text": """🚀 **Atlan Health Check App - Working!**

📋 **Usage**: `/atlan-health CustomerName https://tenant.atlan.com`

**Examples**:
- `/atlan-health "Demo Corp" https://demo.atlan.com`
- `/atlan-health "MegaBank" https://megabank.atlan.com`

✅ **Deployed successfully on Vercel!**"""
            }
        
        # Simple response
        parts = command_text.split()
        customer_name = parts[0] if parts else "Unknown Customer"
        
        return {
            "response_type": "in_channel",
            "text": f"🚀 **Health Check for {customer_name}** ✅ Working on Vercel!"
        }
    
    # GET request - health check
    return {"status": "healthy", "message": "Atlan Health Check API is running!"}
