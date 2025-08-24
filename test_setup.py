#!/usr/bin/env python3
"""
Portia Uptime Agent - Setup Test Script (Gemini AI)
Tests all configurations and dependencies for hackathon demo
"""

import os
import sys
from dotenv import load_dotenv

def print_header(title):
    """Print a formatted header"""
    print(f"\n{'='*60}")
    print(f"  {title}")
    print(f"{'='*60}")

def test_python_version():
    """Test Python version compatibility"""
    print_header("🐍 Python Version Check")
    
    version = sys.version_info
    print(f"   Python Version: {version.major}.{version.minor}.{version.micro}")
    
    if version.major == 3 and version.minor >= 11:
        print("   ✅ Python 3.11+ detected - Compatible")
        return True
    else:
        print("   ❌ Python 3.11+ required - Please upgrade")
        return False

def test_dependencies():
    """Test if all required packages are installed"""
    print_header("📦 Dependencies Check")
    
    required_packages = [
        ("requests", "HTTP requests"),
        ("python-dotenv", "Environment management"),
        ("PyGithub", "GitHub integration"),
        ("google-generativeai", "Google Gemini AI"),
        ("gitpython", "Git operations"),
        ("pyyaml", "YAML processing"),
        ("jinja2", "Template engine")
    ]
    
    all_installed = True
    
    for package, description in required_packages:
        try:
            __import__(package.replace("-", "_"))
            print(f"   ✅ {package} - {description}")
        except ImportError:
            print(f"   ❌ {package} - {description} (Missing)")
            all_installed = False
    
    return all_installed

def test_environment_config():
    """Test environment configuration"""
    print_header("🔧 Environment Configuration")
    
    # Load environment variables
    load_dotenv()
    
    required_vars = [
        ("MONITORED_URL", "Website to monitor"),
        ("GITHUB_TOKEN", "GitHub personal access token"),
        ("GITHUB_REPO_OWNER", "GitHub repository owner"),
        ("GITHUB_REPO_NAME", "GitHub repository name"),
        ("GOOGLE_AI_API_KEY", "Google Gemini API key"),
        ("TELEGRAM_BOT_TOKEN", "Telegram bot token"),
        ("TELEGRAM_CHAT_ID", "Telegram chat ID")
    ]
    
    optional_vars = [
        ("MONITORING_INTERVAL", "Monitoring interval (default: 5)"),
        ("RETRY_ATTEMPTS", "Retry attempts (default: 3)"),
        ("DOWN_THRESHOLD", "Down threshold (default: 2)")
    ]
    
    all_required = True
    
    print("   Required Variables:")
    for var, description in required_vars:
        value = os.getenv(var)
        if value:
            # Mask sensitive values
            if "TOKEN" in var or "KEY" in var:
                masked_value = value[:8] + "..." if len(value) > 8 else "***"
                print(f"     ✅ {var}: {masked_value} - {description}")
            else:
                print(f"     ✅ {var}: {value} - {description}")
        else:
            print(f"     ❌ {var}: Not set - {description}")
            all_required = False
    
    print("\n   Optional Variables:")
    for var, description in optional_vars:
        value = os.getenv(var)
        if value:
            print(f"     ✅ {var}: {value} - {description}")
        else:
            print(f"     ⚠️  {var}: Not set - {description} (using default)")
    
    return all_required

def test_github_connection():
    """Test GitHub API connection"""
    print_header("🔗 GitHub Connection Test")
    
    try:
        from github import Github
        token = os.getenv("GITHUB_TOKEN")
        owner = os.getenv("GITHUB_REPO_OWNER")
        repo_name = os.getenv("GITHUB_REPO_NAME")
        
        if not all([token, owner, repo_name]):
            print("   ❌ GitHub configuration incomplete")
            return False
        
        github = Github(token)
        user = github.get_user()
        print(f"   ✅ GitHub authenticated as: {user.login}")
        
        try:
            repo = github.get_repo(f"{owner}/{repo_name}")
            print(f"   ✅ Repository access: {repo.full_name}")
            print(f"   ✅ Repository visibility: {repo.visibility}")
            print(f"   ✅ Default branch: {repo.default_branch}")
            return True
        except Exception as e:
            print(f"   ❌ Repository access failed: {e}")
            return False
            
    except ImportError:
        print("   ❌ PyGithub not installed")
        return False
    except Exception as e:
        print(f"   ❌ GitHub connection failed: {e}")
        return False

def test_gemini_connection():
    """Test Google Gemini API connection"""
    print_header("🤖 Google Gemini Connection Test")
    
    try:
        import google.generativeai as genai
        api_key = os.getenv("GOOGLE_AI_API_KEY")
        
        if not api_key:
            print("   ❌ Google Gemini API key not set")
            return False
        
        # Test with a simple API call
        genai.configure(api_key=api_key)
        print("   🔍 Testing Gemini API connection...")
        
        try:
            model = genai.GenerativeModel('gemini-1.5-flash')
            response = model.generate_content("Hello, this is a test.")
            print("   ✅ Gemini API key configured and working")
            print("   💰 Using FREE Gemini tier - No costs!")
            return True
        except Exception as e:
            print(f"   ❌ Gemini API test failed: {e}")
            return False
        
    except ImportError:
        print("   ❌ Google Generative AI package not installed")
        return False
    except Exception as e:
        print(f"   ❌ Gemini test failed: {e}")
        return False

def test_telegram_connection():
    """Test Telegram bot connection"""
    print_header("📱 Telegram Connection Test")
    
    try:
        import requests
        token = os.getenv("TELEGRAM_BOT_TOKEN")
        chat_id = os.getenv("TELEGRAM_CHAT_ID")
        
        if not all([token, chat_id]):
            print("   ❌ Telegram configuration incomplete")
            return False
        
        # Test bot info
        url = f"https://api.telegram.org/bot{token}/getMe"
        response = requests.get(url, timeout=10)
        
        if response.status_code == 200:
            bot_info = response.json()
            if bot_info.get("ok"):
                bot_name = bot_info["result"]["first_name"]
                bot_username = bot_info["result"]["username"]
                print(f"   ✅ Bot connected: {bot_name} (@{bot_username})")
                print(f"   ✅ Chat ID: {chat_id}")
                return True
            else:
                print(f"   ❌ Bot API error: {bot_info}")
                return False
        else:
            print(f"   ❌ Bot connection failed: {response.status_code}")
            return False
            
    except ImportError:
        print("   ❌ Requests package not installed")
        return False
    except Exception as e:
        print(f"   ❌ Telegram test failed: {e}")
        return False

def test_website_accessibility():
    """Test if monitored website is accessible"""
    print_header("🌐 Website Accessibility Test")
    
    try:
        import requests
        url = os.getenv("MONITORED_URL")
        
        if not url:
            print("   ❌ No website URL configured")
            return False
        
        print(f"   🔍 Testing access to: {url}")
        response = requests.get(url, timeout=10)
        
        print(f"   ✅ Status Code: {response.status_code}")
        print(f"   ✅ Response Time: {response.elapsed.total_seconds():.2f}s")
        print(f"   ✅ Content Length: {len(response.content)} bytes")
        
        if response.status_code == 200:
            print("   ✅ Website is accessible")
        else:
            print(f"   ⚠️  Website returned status {response.status_code}")
        
        return True
        
    except ImportError:
        print("   ❌ Requests package not installed")
        return False
    except requests.exceptions.Timeout:
        print("   ❌ Website timeout - may be slow or down")
        return False
    except requests.exceptions.ConnectionError:
        print("   ❌ Website connection failed - may be down")
        return False
    except Exception as e:
        print(f"   ❌ Website test failed: {e}")
        return False

def run_demo_test():
    """Test if the demo script can run"""
    print_header("🎬 Demo Script Test")
    
    try:
        # Try to import demo components
        from demo import print_banner, check_configuration
        
        print("   ✅ Demo script imports successfully")
        print("   ✅ Demo functions available")
        
        # Test banner function
        print("   🔍 Testing demo banner...")
        print_banner()
        
        return True
        
    except ImportError as e:
        print(f"   ❌ Demo script import failed: {e}")
        return False
    except Exception as e:
        print(f"   ❌ Demo script test failed: {e}")
        return False

def main():
    """Main test function"""
    print("🚀 Portia Uptime Agent - Setup Test (Gemini AI)")
    print("Testing all configurations for hackathon demo...")
    print("💡 Using Google Gemini AI - 100% FREE tier!")
    
    tests = [
        ("Python Version", test_python_version),
        ("Dependencies", test_dependencies),
        ("Environment Config", test_environment_config),
        ("GitHub Connection", test_github_connection),
        ("Gemini AI Connection", test_gemini_connection),
        ("Telegram Connection", test_telegram_connection),
        ("Website Accessibility", test_website_accessibility),
        ("Demo Script", run_demo_test)
    ]
    
    results = []
    
    for test_name, test_func in tests:
        try:
            result = test_func()
            results.append((test_name, result))
        except Exception as e:
            print(f"   ❌ {test_name} test crashed: {e}")
            results.append((test_name, False))
    
    # Summary
    print_header("📊 Test Summary")
    
    passed = sum(1 for _, result in results if result)
    total = len(results)
    
    print(f"   Tests Passed: {passed}/{total}")
    
    for test_name, result in results:
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"     {status} - {test_name}")
    
    if passed == total:
        print("\n🎉 All tests passed! Your system is ready for the hackathon demo!")
        print("\n🚀 Next steps:")
        print("   1. Run: python demo.py")
        print("   2. Show judges the features")
        print("   3. Demonstrate live monitoring: python main.py")
        print("\n💡 Key Advantage: ZERO AI API costs with Gemini free tier!")
    else:
        print(f"\n⚠️  {total - passed} test(s) failed. Please fix the issues above.")
        print("\n🔧 Common fixes:")
        print("   1. Install missing packages: pip install -r requirements.txt")
        print("   2. Set up your .env file with required credentials")
        print("   3. Get FREE Gemini API key from: https://aistudio.google.com/app/apikey")
        print("   4. Check API keys and permissions")
    
    print(f"\n🏆 Good luck with your hackathon submission!")
    print("💰 Remember: Gemini AI is completely FREE for your demo!")

if __name__ == "__main__":
    main()
