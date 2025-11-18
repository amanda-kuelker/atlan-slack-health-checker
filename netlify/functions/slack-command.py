import json
import sys
import os
import urllib.parse

# Add the project root to Python path to import our modules
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

from health_checker import (
    AtlanHealthChecker, 
    fetch_atlan_data_with_mcp, 
    generate_canvas_assessment
)

def handler(event, context):
    """Main Slack command handler for Netlify"""
    
    try:
        # Handle OPTIONS request for CORS
        if event.get('httpMethod') == 'OPTIONS':
            return {
                'statusCode': 200,
                'headers': {
                    'Access-Control-Allow-Origin': '*',
                    'Access-Control-Allow-Headers': 'Content-Type',
                    'Access-Control-Allow-Methods': 'GET, POST, OPTIONS'
                },
                'body': ''
            }
        
        # Parse the form data from Slack
        body = event.get('body', '')
        if event.get('isBase64Encoded'):
            import base64
            body = base64.b64decode(body).decode('utf-8')
        
        # Parse form-encoded data
        form_data = urllib.parse.parse_qs(body)
        
        # Extract Slack form parameters
        command_text = form_data.get('text', [''])[0].strip()
        user_name = form_data.get('user_name', ['Unknown User'])[0]
        
        print(f"🔍 Processing Slack command: {command_text}")
        print(f"👤 User: {user_name}")
        
        # Initialize health checker
        health_checker = AtlanHealthChecker()
        
        # Handle empty command
        if not command_text:
            return {
                'statusCode': 200,
                'headers': {'Content-Type': 'application/json'},
                'body': json.dumps({
                    "response_type": "ephemeral",
                    "text": """🏥 **Atlan Professional Health Check**

📋 **Usage:**
`/atlan-health "Company Name" https://tenant.atlan.com industry:construction tags:Safety,OSHA`

🎯 **Industries:** finance, healthcare, construction, retail, technology, manufacturing
🔍 **Filters:** tags, connections, certificate, asset_type"""
                })
            }
        
        # Parse the command
        parsed = health_checker.parse_command(command_text)
        if not parsed:
            return {
                'statusCode': 200,
                'headers': {'Content-Type': 'application/json'},
                'body': json.dumps({
                    "response_type": "ephemeral",
                    "text": "❌ Could not parse command. Please include company name and Atlan tenant URL."
                })
            }
        
        company_name = parsed['company_name']
        atlan_url = parsed['atlan_url']
        filters = parsed['filters']
        
        # Detect industry
        industry = health_checker.detect_industry(company_name, filters)
        
        print(f"🔍 Processing: {company_name} ({industry}) - {atlan_url}")
        print(f"🔧 Filters: {filters}")
        
        # Fetch data from Atlan using MCP
        atlan_data = fetch_atlan_data_with_mcp(atlan_url, filters)
        
        # Calculate health scores
        health_scores = health_checker.calculate_health_score(industry, atlan_data)
        
        # Generate Canvas assessment
        canvas_content = generate_canvas_assessment(
            company_name, industry, atlan_url, atlan_data, health_scores
        )
        
        # Return Canvas assessment to Slack
        max_length = 3800  # Slack message limit
        
        if len(canvas_content) <= max_length:
            response_body = {
                "response_type": "in_channel",
                "text": f"📋 **Professional Assessment Complete**\n\n```\n{canvas_content}\n```"
            }
        else:
            # Split into chunks for long assessments
            lines = canvas_content.split('\n')
            first_chunk = ""
            
            for line in lines:
                if len(first_chunk + line + '\n') > max_length:
                    break
                first_chunk += line + '\n'
            
            response_body = {
                "response_type": "in_channel",
                "text": f"📋 **{company_name} - Health Assessment**\n\n```\n{first_chunk}\n```\n\n*Health Score: {health_scores['overall_score']}/100*"
            }
        
        return {
            'statusCode': 200,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            },
            'body': json.dumps(response_body)
        }
        
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        import traceback
        traceback.print_exc()
        
        return {
            'statusCode': 200,
            'headers': {'Content-Type': 'application/json'},
            'body': json.dumps({
                "response_type": "ephemeral", 
                "text": f"❌ **Error**: {str(e)}\n\nPlease try again or contact support."
            })
        }
