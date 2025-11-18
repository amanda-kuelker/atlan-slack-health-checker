#!/usr/bin/env python3
"""
Test script for the cleaned up Atlan Slack Health Checker
Tests both local and deployed versions
"""

import requests
import json
import sys

def test_health_endpoint(base_url):
    """Test the health endpoint"""
    try:
        response = requests.get(f"{base_url}/", timeout=10)
        print(f"✅ Health endpoint: {response.status_code}")
        if response.status_code == 200:
            data = response.json()
            print(f"   Version: {data.get('version', 'Unknown')}")
            return True
    except Exception as e:
        print(f"❌ Health endpoint error: {e}")
    return False

def test_slack_command(base_url, command_text):
    """Test the Slack command endpoint"""
    test_data = {
        'text': command_text,
        'user_name': 'testuser',
        'channel_name': 'general',
        'team_id': 'T1234567890',
        'user_id': 'U1234567890'
    }
    
    print(f"\n🧪 Testing command: {command_text}")
    
    try:
        response = requests.post(
            f"{base_url}/slack/atlan-setup",
            data=test_data,
            headers={'Content-Type': 'application/x-www-form-urlencoded'},
            timeout=30
        )
        
        print(f"📊 Status: {response.status_code}")
        
        if response.status_code == 200:
            try:
                result = response.json()
                response_type = result.get('response_type', 'unknown')
                text = result.get('text', '')
                
                print(f"📤 Response type: {response_type}")
                print(f"📝 Response length: {len(text)} chars")
                
                # Check if it contains Canvas assessment
                if 'Governance Health Score' in text and 'Strategic Recommendations' in text:
                    print("✅ Canvas assessment generated successfully!")
                    return True
                else:
                    print("⚠️  Response received but no Canvas assessment found")
                    print(f"First 200 chars: {text[:200]}...")
            except json.JSONDecodeError:
                print(f"📄 Raw response: {response.text[:200]}...")
        else:
            print(f"❌ Failed with status {response.status_code}")
            print(f"Response: {response.text[:200]}...")
            
    except Exception as e:
        print(f"❌ Request error: {e}")
    
    return False

def run_comprehensive_tests(base_url):
    """Run comprehensive tests"""
    print(f"🚀 Testing Atlan Health Checker at: {base_url}")
    print("=" * 60)
    
    # Test health endpoint
    if not test_health_endpoint(base_url):
        print("❌ Health check failed, aborting tests")
        return False
    
    # Test cases matching different industries and scenarios
    test_cases = [
        {
            'name': 'Construction Company (DPR-style)',
            'command': '"DPR Construction" https://dpr.atlan.com industry:construction tags:Safety,OSHA'
        },
        {
            'name': 'Healthcare Organization', 
            'command': '"Regional Medical" https://health.atlan.com industry:healthcare tags:PHI,HIPAA'
        },
        {
            'name': 'Financial Institution',
            'command': '"MegaBank Corp" https://bank.atlan.com industry:finance tags:PII,SOX'
        },
        {
            'name': 'Technology Company',
            'command': 'TechCorp https://dsm.atlan.com industry:technology connections:snowflake'
        },
        {
            'name': 'Simple Company Test',
            'command': 'TestCorp https://test.atlan.com'
        }
    ]
    
    results = []
    for test_case in test_cases:
        print(f"\n{'='*20} {test_case['name']} {'='*20}")
        success = test_slack_command(base_url, test_case['command'])
        results.append({'name': test_case['name'], 'success': success})
    
    # Summary
    print(f"\n{'='*60}")
    print("📊 TEST SUMMARY")
    print(f"{'='*60}")
    
    passed = sum(1 for r in results if r['success'])
    total = len(results)
    
    for result in results:
        status = "✅ PASS" if result['success'] else "❌ FAIL"
        print(f"{status} - {result['name']}")
    
    print(f"\nOverall: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All tests passed! The integration is working correctly.")
        return True
    else:
        print(f"⚠️  {total - passed} test(s) failed. Check the logs above.")
        return False

if __name__ == "__main__":
    # Determine which URL to test
    if len(sys.argv) > 1:
        base_url = sys.argv[1]
    else:
        # Default to local development
        base_url = "http://localhost:8080"
        print("💡 Testing local development server. Use: python test.py <URL> for deployed version")
    
    success = run_comprehensive_tests(base_url)
    
    if success:
        print("\n🎯 Ready for production! The Canvas assessments should now work in Slack.")
        print(f"📋 Slack webhook URL: {base_url}/slack/atlan-setup")
    else:
        print("\n🔧 Some tests failed. Check the implementation above.")
    
    sys.exit(0 if success else 1)
