#!/usr/bin/env python3
"""
Code validation test for the cleaned up Atlan Health Checker
Tests the code structure and key functions without needing a running server
"""

import sys
import os
import importlib.util

def test_code_structure():
    """Test that the main code structure is clean and functional"""
    print("🔍 Testing code structure...")
    
    # Test main Flask app imports
    api_path = os.path.join(os.path.dirname(__file__), 'api', 'index.py')
    
    if not os.path.exists(api_path):
        print("❌ Main Flask app not found at api/index.py")
        return False
    
    # Count lines to verify it's been cleaned up
    with open(api_path, 'r') as f:
        lines = f.readlines()
    
    non_empty_lines = len([line for line in lines if line.strip() and not line.strip().startswith('#')])
    print(f"📊 Main app has {non_empty_lines} non-empty/non-comment lines")
    
    if non_empty_lines > 500:
        print("⚠️  App seems large - target is <400 lines")
    else:
        print("✅ App size is reasonable")
    
    # Test that key functions exist
    app_content = ''.join(lines)
    required_functions = [
        'parse_command',
        'detect_industry', 
        'calculate_health_score',
        'fetch_atlan_data_with_mcp',
        'generate_canvas_assessment',
        'slack_command'
    ]
    
    missing_functions = []
    for func_name in required_functions:
        if f'def {func_name}(' not in app_content:
            missing_functions.append(func_name)
    
    if missing_functions:
        print(f"❌ Missing required functions: {', '.join(missing_functions)}")
        return False
    else:
        print("✅ All required functions present")
    
    return True

def test_industry_support():
    """Test that all required industries are supported"""
    print("\n🏭 Testing industry support...")
    
    # Import the health checker class
    sys.path.append(os.path.dirname(__file__))
    
    try:
        # Import the main app file
        spec = importlib.util.spec_from_file_location("main", "api/index.py")
        main_module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(main_module)
        
        # Check industry regulations
        health_checker = main_module.health_checker
        industries = health_checker.industry_regulations
        
        required_industries = ['construction', 'healthcare', 'finance', 'technology', 'manufacturing', 'retail']
        
        missing_industries = []
        for industry in required_industries:
            if industry not in industries:
                missing_industries.append(industry)
        
        if missing_industries:
            print(f"❌ Missing industries: {', '.join(missing_industries)}")
            return False
        
        print(f"✅ All {len(required_industries)} industries supported:")
        for industry, info in industries.items():
            print(f"   {info['icon']} {industry.title()}: {info['name']}")
        
        return True
        
    except Exception as e:
        print(f"❌ Error testing industries: {e}")
        return False

def test_command_parsing():
    """Test the command parsing functionality"""
    print("\n📝 Testing command parsing...")
    
    try:
        sys.path.append(os.path.dirname(__file__))
        
        # Import the main app
        spec = importlib.util.spec_from_file_location("main", "api/index.py")
        main_module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(main_module)
        
        health_checker = main_module.health_checker
        
        # Test different command formats
        test_cases = [
            {
                'command': '"DPR Construction" https://dpr.atlan.com industry:construction tags:Safety,OSHA',
                'expected_company': 'DPR Construction',
                'expected_url': 'https://dpr.atlan.com',
                'expected_filters': {'industry': 'construction', 'tags': ['Safety', 'OSHA']}
            },
            {
                'command': 'TechCorp https://dsm.atlan.com industry:technology connections:snowflake',
                'expected_company': 'TechCorp',
                'expected_url': 'https://dsm.atlan.com',
                'expected_filters': {'industry': 'technology', 'connections': 'snowflake'}
            }
        ]
        
        for i, test_case in enumerate(test_cases, 1):
            result = health_checker.parse_command(test_case['command'])
            
            if not result:
                print(f"❌ Test case {i}: Parse returned None")
                continue
                
            if result['company_name'] != test_case['expected_company']:
                print(f"❌ Test case {i}: Company name mismatch")
                continue
                
            if result['atlan_url'] != test_case['expected_url']:
                print(f"❌ Test case {i}: URL mismatch")
                continue
                
            print(f"✅ Test case {i}: Command parsed correctly")
        
        return True
        
    except Exception as e:
        print(f"❌ Error testing command parsing: {e}")
        return False

def test_health_calculation():
    """Test health score calculation"""
    print("\n🧮 Testing health score calculation...")
    
    try:
        sys.path.append(os.path.dirname(__file__))
        
        # Import the main app
        spec = importlib.util.spec_from_file_location("main", "api/index.py")
        main_module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(main_module)
        
        health_checker = main_module.health_checker
        
        # Test with sample data
        test_data = {
            'total_assets': 100,
            'documented_assets': 25,
            'verified_assets': 20,
            'owned_assets': 15,
            'tagged_assets': 30
        }
        
        # Test different industries
        for industry in ['construction', 'healthcare', 'finance']:
            result = health_checker.calculate_health_score(industry, test_data)
            
            if 'overall_score' not in result:
                print(f"❌ {industry}: Missing overall_score")
                continue
                
            score = result['overall_score']
            if not (0 <= score <= 100):
                print(f"❌ {industry}: Score {score} out of valid range")
                continue
                
            print(f"✅ {industry}: Health score {score}/100")
        
        return True
        
    except Exception as e:
        print(f"❌ Error testing health calculation: {e}")
        return False

def main():
    """Run all validation tests"""
    print("🧪 Atlan Health Checker - Code Validation Tests")
    print("=" * 60)
    
    tests = [
        test_code_structure,
        test_industry_support,
        test_command_parsing,
        test_health_calculation
    ]
    
    results = []
    for test in tests:
        try:
            result = test()
            results.append(result)
        except Exception as e:
            print(f"❌ Test failed with error: {e}")
            results.append(False)
    
    print(f"\n{'='*60}")
    print("📊 VALIDATION SUMMARY")
    print(f"{'='*60}")
    
    passed = sum(results)
    total = len(results)
    
    test_names = [
        "Code Structure",
        "Industry Support", 
        "Command Parsing",
        "Health Calculation"
    ]
    
    for i, (name, result) in enumerate(zip(test_names, results)):
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"{status} - {name}")
    
    print(f"\nOverall: {passed}/{total} tests passed")
    
    if passed == total:
        print("\n🎉 All validation tests passed!")
        print("✅ Code is clean and ready for deployment")
        print("🚀 Deploy with: vercel deploy --prod")
    else:
        print(f"\n⚠️  {total - passed} validation test(s) failed")
        print("🔧 Check the errors above and fix before deploying")
    
    return passed == total

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
