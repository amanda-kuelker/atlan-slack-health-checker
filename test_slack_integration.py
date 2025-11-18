#!/usr/bin/env python3
"""
Test script for Atlan Slack Health Checker
Tests the actual Slack webhook integration
"""

import requests
import json
import time

def test_slack_integration(base_url):
    """Test the Slack webhook endpoint directly"""
    
    test_data = {
        'text': 'TechCorp https://dsm.atlan.com industry:technology tags:Finance',
        'user_name': 'testuser',
        'channel_name': 'general',
        'response_url': 'https://httpbin.org/post'  # Test webhook URL
    }
    
    print(f"🧪 Testing Slack integration at: {base_url}/slack/atlan-setup")
    print(f"📋 Test data: {test_data}")
    
    try:
        # Send the test request
        response = requests.post(
            f"{base_url}/slack/atlan-setup",
            data=test_data,
            headers={'Content-Type': 'application/x-www-form-urlencoded'},
            timeout=30
        )
        
        print(f"✅ Status Code: {response.status_code}")
        print(f"📤 Response: {response.text}")
        
        if response.status_code == 200:
            print("🎉 Test successful! Check logs for Canvas output.")
            return True
        else:
            print(f"❌ Test failed with status {response.status_code}")
            return False
            
    except Exception as e:
        print(f"❌ Test error: {str(e)}")
        return False

def test_basic_endpoints(base_url):
    """Test basic endpoints"""
    
    print(f"🔍 Testing basic endpoints...")
    
    # Test health endpoint
    try:
        response = requests.get(f"{base_url}/", timeout=10)
        print(f"✅ Health endpoint: {response.status_code}")
    except Exception as e:
        print(f"❌ Health endpoint error: {e}")
    
    # Test test endpoint
    try:
        response = requests.get(f"{base_url}/test", timeout=10)
        print(f"✅ Test endpoint: {response.status_code}")
    except Exception as e:
        print(f"❌ Test endpoint error: {e}")

if __name__ == "__main__":
    # Test with your Vercel deployment
    BASE_URL = "https://atlan-slack-health-checker-dw1bxxcq0.vercel.app"
    
    print("🚀 Starting Atlan Slack Health Checker Tests")
    print("=" * 50)
    
    # Test basic endpoints first
    test_basic_endpoints(BASE_URL)
    
    print("\n" + "=" * 50)
    
    # Test Slack integration
    success = test_slack_integration(BASE_URL)
    
    if success:
        print("\n🎉 All tests passed!")
        print("💡 The Canvas assessment should now be sent back to Slack!")
    else:
        print("\n❌ Tests failed. Check the deployment.")
