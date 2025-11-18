#!/bin/bash

# Atlan Slack Health Checker - Deployment Script
echo "🚀 Atlan Slack Health Checker - Deployment Guide"
echo "================================================"

echo ""
echo "📋 Prerequisites:"
echo "- Vercel CLI installed: npm i -g vercel"
echo "- Git repository initialized"
echo "- Slack app configured"

echo ""
echo "🔧 Deployment Steps:"
echo ""
echo "1. Deploy to Vercel:"
echo "   vercel deploy"
echo ""
echo "2. For production deployment:"
echo "   vercel deploy --prod"
echo ""
echo "3. Configure Slack App:"
echo "   - Request URL: https://your-app-name.vercel.app/slack/atlan-setup"
echo "   - Command: /atlan-health"
echo "   - Method: POST"
echo ""
echo "4. Test with command:"
echo "   /atlan-health \"TechCorp\" https://dsm.atlan.com industry:technology tags:Finance"
echo ""

echo "🧪 Testing:"
echo "python3 test_slack_integration.py"

echo ""
echo "📊 Features:"
echo "✅ Real MCP integration with Atlan"
echo "✅ Canvas assessments sent back to Slack"
echo "✅ Industry-specific health scoring" 
echo "✅ Professional ROI projections"
echo "✅ Error handling and fallbacks"

echo ""
echo "🎯 The key fix: Canvas assessments are now sent back to Slack"
echo "   instead of only being printed to console logs!"

echo ""
echo "Ready to generate professional assessments! 🏥"
