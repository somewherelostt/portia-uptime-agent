#!/usr/bin/env python3
"""
Install Google AI Studio dependencies for Portia Uptime Agent
"""

import subprocess
import sys

def install_package(package):
    """Install a Python package using pip"""
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])
        print(f"✅ Successfully installed {package}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to install {package}: {e}")
        return False

def main():
    print("🚀 Installing Google AI Studio dependencies for Portia Uptime Agent...")
    print("=" * 60)
    
    # Install required packages
    packages = [
        "google-generativeai>=0.3.0",
        "requests>=2.28.0",
        "python-dotenv>=1.0.0"
    ]
    
    success_count = 0
    for package in packages:
        if install_package(package):
            success_count += 1
    
    print("=" * 60)
    if success_count == len(packages):
        print("🎉 All dependencies installed successfully!")
        print("\nNext steps:")
        print("1. Copy env_template.txt to .env")
        print("2. Get your Google AI API key from: https://aistudio.google.com/app/u/0/apikey")
        print("3. Set GOOGLE_AI_API_KEY in your .env file")
        print("4. Run: python main.py")
    else:
        print(f"⚠️  {len(packages) - success_count} packages failed to install")
        print("Please check the errors above and try again")

if __name__ == "__main__":
    main()
