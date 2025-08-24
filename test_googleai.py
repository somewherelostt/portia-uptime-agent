#!/usr/bin/env python3
"""
Test Google AI Studio integration for Portia Uptime Agent
"""

import os
import sys
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def test_googleai_api():
    """Test Google AI Studio API connectivity"""
    print("🧪 Testing Google AI Studio API Integration...")
    print("=" * 50)
    
    # Check if API key is set
    api_key = os.getenv("GOOGLE_AI_API_KEY")
    if not api_key:
        print("❌ GOOGLE_AI_API_KEY not found in environment variables")
        print("   Please set it in your .env file")
        return False
    
    print(f"✅ API Key found: {api_key[:10]}...{api_key[-4:]}")
    
    # Test API connectivity
    try:
        import google.generativeai as genai
        
        # Configure the API
        genai.configure(api_key=api_key)
        
        # Test with a simple prompt
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        print("🔄 Testing API call...")
        response = model.generate_content("Hello! Please respond with 'OK' if you can see this message.")
        
        if response and response.text:
            print(f"✅ API call successful!")
            print(f"   Response: {response.text.strip()}")
            return True
        else:
            print("❌ API call failed - no response received")
            return False
            
    except ImportError:
        print("❌ google-generativeai library not installed")
        print("   Run: pip install google-generativeai")
        return False
    except Exception as e:
        print(f"❌ API test failed: {e}")
        return False

def test_environment():
    """Test environment configuration"""
    print("\n🔧 Testing Environment Configuration...")
    print("=" * 50)
    
    required_vars = [
        "MONITORED_URL",
        "TELEGRAM_BOT_TOKEN", 
        "TELEGRAM_CHAT_ID"
    ]
    
    all_good = True
    for var in required_vars:
        value = os.getenv(var)
        if value:
            print(f"✅ {var}: {value[:20]}{'...' if len(value) > 20 else ''}")
        else:
            print(f"❌ {var}: Not set")
            all_good = False
    
    # Check Google AI API key
    google_ai_key = os.getenv("GOOGLE_AI_API_KEY")
    if google_ai_key:
        print(f"✅ GOOGLE_AI_API_KEY: {google_ai_key[:10]}...{google_ai_key[-4:]}")
    else:
        print("❌ GOOGLE_AI_API_KEY: Not set")
        all_good = False
    
    return all_good

def main():
    print("🚀 Google AI Studio Integration Test")
    print("=" * 50)
    
    # Test environment
    env_ok = test_environment()
    
    # Test Google AI API
    api_ok = test_googleai_api()
    
    print("\n" + "=" * 50)
    if env_ok and api_ok:
        print("🎉 All tests passed! Google AI Studio is ready to use.")
        print("\nNext steps:")
        print("1. Run: python main.py")
        print("2. Check your Telegram for notifications")
    else:
        print("⚠️  Some tests failed. Please fix the issues above.")
        if not env_ok:
            print("   - Check your .env file configuration")
        if not api_ok:
            print("   - Verify your Google AI API key")
            print("   - Ensure google-generativeai is installed")
    
    return env_ok and api_ok

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
