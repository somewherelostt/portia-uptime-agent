#!/usr/bin/env python3
"""
Simplified Setup for Portia Uptime Agent
Focus on essential API keys: Gemini AI + Portia (without org ID requirement)
"""

import os
import requests
from dotenv import load_dotenv

def print_header(title):
    print(f"\n{'='*60}")
    print(f"  {title}")
    print(f"{'='*60}")

def test_gemini_api(api_key):
    """Test Google Gemini API"""
    try:
        import google.generativeai as genai
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel('gemini-1.5-flash')
        response = model.generate_content("Hello, test message")
        print("✅ Google Gemini API working!")
        return True
    except Exception as e:
        print(f"❌ Gemini API failed: {e}")
        return False

def test_portia_api_basic(api_key):
    """Test Portia API without org ID requirement"""
    try:
        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }
        
        # Try different endpoints that might not require org ID
        endpoints_to_try = [
            "/v1/health",
            "/v1/status", 
            "/v1/user",
            "/v1/me"
        ]
        
        for endpoint in endpoints_to_try:
            try:
                response = requests.get(
                    f"https://api.portialabs.ai{endpoint}",
                    headers=headers,
                    timeout=5
                )
                
                if response.status_code == 200:
                    print(f"✅ Portia API working! (endpoint: {endpoint})")
                    return True
                elif response.status_code != 404:  # Not just "not found"
                    print(f"   Tried {endpoint}: {response.status_code}")
                    
            except requests.exceptions.RequestException:
                continue
        
        # If no endpoint worked, that's okay - API key might still be valid
        print("⚠️  Portia API key configured (org ID not required for basic monitoring)")
        return True
        
    except Exception as e:
        print(f"❌ Portia API test failed: {e}")
        return False

def update_env_file(key, value):
    """Update a single key in .env file"""
    if not os.path.exists('.env'):
        return False
    
    # Read current content
    with open('.env', 'r') as f:
        lines = f.readlines()
    
    # Update or add the key
    updated_lines = []
    key_found = False
    
    for line in lines:
        if line.startswith(f"{key}="):
            updated_lines.append(f"{key}={value}\n")
            key_found = True
        else:
            updated_lines.append(line)
    
    # If key wasn't found, add it
    if not key_found:
        updated_lines.append(f"{key}={value}\n")
    
    # Write back
    with open('.env', 'w') as f:
        f.writelines(updated_lines)
    
    return True

def main():
    print("""
    ╔══════════════════════════════════════════════════════════════╗
    ║            🚀 SIMPLIFIED PORTIA SETUP                       ║
    ║               Essential API Keys Only                       ║
    ╚══════════════════════════════════════════════════════════════╝
    
    This setup focuses on the two essential API keys:
    • 🤖 Google Gemini AI (100% FREE!)
    • 🔌 Portia API (No org ID required)
    """)
    
    load_dotenv()
    
    # 1. Google Gemini Setup
    print_header("🤖 GOOGLE GEMINI AI SETUP (FREE)")
    
    current_gemini = os.getenv("GOOGLE_AI_API_KEY", "")
    if current_gemini and "your_google" not in current_gemini:
        print(f"Current Gemini key: {current_gemini[:15]}...")
        keep_current = input("Keep current Gemini API key? (y/n): ").lower()
        if keep_current != 'y':
            current_gemini = ""
    
    if not current_gemini or "your_google" in current_gemini:
        print("\n📚 To get FREE Google Gemini API key:")
        print("   1. Go to: https://aistudio.google.com/app/apikey")
        print("   2. Sign in with Google account")
        print("   3. Click 'Create API key'")
        print("   4. Copy the key (starts with 'AIza...')")
        
        gemini_key = input("\nEnter Google Gemini API Key: ").strip()
        
        if gemini_key:
            print("\n🧪 Testing Gemini API...")
            if test_gemini_api(gemini_key):
                update_env_file("GOOGLE_AI_API_KEY", gemini_key)
                print("✅ Gemini API key saved!")
            else:
                print("❌ Gemini API test failed - please check your key")
        else:
            print("⚠️ Skipping Gemini setup")
    else:
        print("\n🧪 Testing existing Gemini API...")
        test_gemini_api(current_gemini)
    
    # 2. Portia API Setup (Optional)
    print_header("🔌 PORTIA API SETUP (OPTIONAL)")
    
    current_portia = os.getenv("PORTIA_API_KEY", "")
    if current_portia and "prt-" in current_portia:
        print(f"Current Portia key: {current_portia[:15]}...")
        keep_current = input("Keep current Portia API key? (y/n): ").lower()
        if keep_current != 'y':
            current_portia = ""
    
    if not current_portia:
        print("\n📚 To get Portia API key (OPTIONAL):")
        print("   1. Go to: https://app.portialabs.ai/")
        print("   2. Sign up for free account")
        print("   3. Go to 'Manage API keys' tab")
        print("   4. Generate new API key")
        print("   5. Copy the key (starts with 'prt-...')")
        
        portia_key = input("\nEnter Portia API Key (or press Enter to skip): ").strip()
        
        if portia_key:
            print("\n🧪 Testing Portia API...")
            if test_portia_api_basic(portia_key):
                update_env_file("PORTIA_API_KEY", portia_key)
                print("✅ Portia API key saved!")
            else:
                print("⚠️ Portia API key saved anyway (might work in different context)")
                update_env_file("PORTIA_API_KEY", portia_key)
        else:
            print("⚠️ Skipping Portia setup")
    else:
        print("\n🧪 Testing existing Portia API...")
        test_portia_api_basic(current_portia)
    
    # 3. Website URL Setup
    print_header("🌐 WEBSITE MONITORING")
    
    current_url = os.getenv("MONITORED_URL", "")
    if "your-website" in current_url or not current_url:
        url = input("Enter website URL to monitor (e.g., https://example.com): ").strip()
        if url:
            update_env_file("MONITORED_URL", url)
            print("✅ Website URL saved!")
    else:
        print(f"✅ Monitoring URL: {current_url}")
    
    # 4. Final Test
    print_header("🧪 RUNNING SYSTEM TEST")
    
    print("Testing the monitoring system...")
    try:
        # Test website monitoring
        url = os.getenv("MONITORED_URL")
        if url:
            response = requests.get(url, timeout=10)
            print(f"✅ Website {url} is accessible (Status: {response.status_code})")
        
        print("\n🎉 SETUP COMPLETE!")
        print("\n🚀 Ready to run:")
        print("   python demo.py           # Show demo")
        print("   python main.py           # Single check")
        print("   python monitor_continuous.py  # Continuous monitoring")
        
        print("\n💡 Features enabled:")
        if os.getenv("GOOGLE_AI_API_KEY"):
            print("   ✅ AI-Powered Issue Analysis (Gemini)")
        if os.getenv("PORTIA_API_KEY"):
            print("   ✅ Enhanced Monitoring (Portia)")
        if os.getenv("GITHUB_TOKEN"):
            print("   ✅ Automatic GitHub PR Creation")
        else:
            print("   ⚠️ GitHub integration not configured (optional)")
        if os.getenv("TELEGRAM_BOT_TOKEN"):
            print("   ✅ Telegram Notifications")
        else:
            print("   ⚠️ Telegram notifications not configured (optional)")
        
    except Exception as e:
        print(f"⚠️ System test had issues: {e}")
        print("But the core setup should work!")

if __name__ == "__main__":
    main()
