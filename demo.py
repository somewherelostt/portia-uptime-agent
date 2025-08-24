#!/usr/bin/env python3
"""
Portia Uptime Agent - Hackathon Demo Script (Gemini AI)
This script demonstrates the enhanced features for judges using Google Gemini
"""

import os
import time
import json
from datetime import datetime
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def print_banner():
    """Print a beautiful banner for the demo"""
    print("""
    ╔══════════════════════════════════════════════════════════════╗
    ║                    🚀 PORTIA UPTIME AGENT                   ║
    ║                    🏆 HACKATHON DEMO                        ║
    ║                    🤖 POWERED BY GEMINI AI                  ║
    ║                                                              ║
    ║  🤖 AI-Powered Website Monitoring                           ║
    ║  🔗 Automatic GitHub Integration                            ║
    ║  🛠️  Self-Healing Code Fixes                                ║
    ║  📱 Real-time Notifications                                 ║
    ║  💰 100% Free Tier (Google Gemini)                         ║
    ╚══════════════════════════════════════════════════════════════╝
    """)

def check_configuration():
    """Check if all required configurations are set"""
    print("🔧 Checking Configuration...")
    print("-" * 50)
    
    configs = {
        "Website Monitoring": os.getenv("MONITORED_URL"),
        "Telegram Bot": "✅" if os.getenv("TELEGRAM_BOT_TOKEN") else "❌",
        "GitHub Integration": "✅" if os.getenv("GITHUB_TOKEN") else "❌",
        "Google Gemini AI": "✅" if os.getenv("GOOGLE_AI_API_KEY") else "❌"
    }
    
    for key, value in configs.items():
        print(f"   {key}: {value}")
    
    print()
    return all([os.getenv("MONITORED_URL"), os.getenv("GITHUB_TOKEN"), os.getenv("GOOGLE_AI_API_KEY")])

def demo_uptime_check():
    """Demonstrate uptime checking capabilities"""
    print("🔍 Demo: Uptime Monitoring")
    print("-" * 50)
    
    url = os.getenv("MONITORED_URL", "https://example.com")
    print(f"   Monitoring URL: {url}")
    print(f"   Retry Attempts: {os.getenv('RETRY_ATTEMPTS', '3')}")
    print(f"   Down Threshold: {os.getenv('DOWN_THRESHOLD', '2')}")
    print()

def demo_ai_analysis():
    """Demonstrate AI-powered issue analysis"""
    print("🤖 Demo: Gemini AI-Powered Issue Analysis")
    print("-" * 50)
    
    print("   When a website goes down, Gemini AI will:")
    print("   1. Analyze the root cause")
    print("   2. Identify affected files")
    print("   3. Generate specific code fixes")
    print("   4. Prioritize the issue (HIGH/MEDIUM/LOW)")
    print("   5. Estimate resolution time")
    print("   💰 All using Google's FREE Gemini tier!")
    print()

def demo_github_integration():
    """Demonstrate GitHub integration features"""
    print("🔗 Demo: GitHub Integration")
    print("-" * 50)
    
    print("   Automatic GitHub Actions:")
    print("   1. Clone the repository")
    print("   2. Create a fix branch")
    print("   3. Apply Gemini-generated fixes")
    print("   4. Commit and push changes")
    print("   5. Create a pull request")
    print("   6. Clean up temporary files")
    print()

def demo_workflow():
    """Demonstrate the complete workflow"""
    print("🔄 Demo: Complete Workflow")
    print("-" * 50)
    
    workflow_steps = [
        "1. Website goes down",
        "2. Portia Agent detects downtime",
        "3. Sends immediate Telegram alert",
        "4. Gemini AI analyzes the issue",
        "5. Generates code fixes",
        "6. Creates GitHub PR automatically",
        "7. Owner reviews and merges",
        "8. Website is restored"
    ]
    
    for step in workflow_steps:
        print(f"   {step}")
        time.sleep(0.5)
    
    print()

def demo_features():
    """Showcase key features"""
    print("✨ Key Features for Hackathon")
    print("-" * 50)
    
    features = [
        "🚀 Zero-Downtime Monitoring",
        "🤖 Gemini AI-Powered Issue Resolution",
        "🔗 Automatic GitHub Integration",
        "📱 Real-time Notifications",
        "🛠️ Self-Healing Code",
        "⚡ Intelligent Retry Logic",
        "📊 Detailed Analytics",
        "🔒 Secure API Integration",
        "💰 100% Free AI (Gemini Tier)"
    ]
    
    for feature in features:
        print(f"   {feature}")
    
    print()

def demo_tech_stack():
    """Showcase the technology stack"""
    print("🛠️ Technology Stack")
    print("-" * 50)
    
    tech_stack = {
        "Backend": "Python 3.11+",
        "AI/ML": "Google Gemini 1.5 Flash (FREE)",
        "Git Integration": "PyGithub, GitPython",
        "Monitoring": "Requests, Custom Uptime Logic",
        "Notifications": "Telegram Bot API",
        "Configuration": "Environment Variables, YAML",
        "Deployment": "Docker-ready, Cloud-native"
    }
    
    for category, tech in tech_stack.items():
        print(f"   {category}: {tech}")
    
    print()

def demo_cost_benefits():
    """Showcase cost benefits of using Gemini"""
    print("💰 Cost Benefits of Gemini AI")
    print("-" * 50)
    
    benefits = [
        "🎯 Free Tier: 15 requests per minute",
        "🚀 Pro Tier: $0.0025 per 1K characters",
        "⚡ Fast: Optimized for real-time analysis",
        "🔒 Secure: Google's enterprise-grade security",
        "🌐 Global: Multiple data center locations",
        "📊 Reliable: 99.9% uptime SLA",
        "🔄 Scalable: Handles high-volume requests"
    ]
    
    for benefit in benefits:
        print(f"   {benefit}")
    
    print()

def demo_use_cases():
    """Showcase real-world use cases"""
    print("🌍 Real-World Use Cases")
    print("-" * 50)
    
    use_cases = [
        "🏢 Enterprise Website Monitoring",
        "🛒 E-commerce Platform Uptime",
        "🏥 Healthcare System Reliability",
        "🏦 Financial Service Availability",
        "🎓 Educational Platform Monitoring",
        "📱 Mobile App Backend Health",
        "☁️ Cloud Service Monitoring",
        "🔧 DevOps Infrastructure Health"
    ]
    
    for use_case in use_cases:
        print(f"   {use_case}")
    
    print()

def demo_benefits():
    """Showcase business benefits"""
    print("💼 Business Benefits")
    print("-" * 50)
    
    benefits = [
        "💰 Reduced Downtime Costs",
        "👥 Improved User Experience",
        "🔧 Faster Issue Resolution",
        "🤖 Reduced Manual Intervention",
        "📊 Proactive Monitoring",
        "🔄 Continuous Improvement",
        "🛡️ Risk Mitigation",
        "📈 Increased Reliability",
        "💸 Zero AI API Costs (Free Tier)"
    ]
    
    for benefit in benefits:
        print(f"   {benefit}")
    
    print()

def run_live_demo():
    """Run a live demonstration"""
    print("🎬 Live Demo Mode")
    print("-" * 50)
    
    print("   Starting live uptime monitoring...")
    print("   (This would normally run the actual monitoring)")
    print()
    
    # Simulate monitoring
    for i in range(3):
        print(f"   🔍 Check {i+1}: Simulating uptime check...")
        time.sleep(1)
        print(f"   ✅ Status: UP (Demo Mode)")
        time.sleep(1)
    
    print("   🎯 Demo completed successfully!")
    print()

def main():
    """Main demo function"""
    print_banner()
    
    print("Welcome to the Portia Uptime Agent Hackathon Demo!")
    print("This system demonstrates autonomous website monitoring and self-healing capabilities.")
    print("🚀 Powered by Google Gemini AI - 100% FREE tier!")
    print()
    
    # Check configuration
    if not check_configuration():
        print("⚠️  Warning: Some configurations are missing.")
        print("   The demo will show features but may not work fully.")
        print()
    
    # Run demo sections
    demo_uptime_check()
    demo_ai_analysis()
    demo_github_integration()
    demo_workflow()
    demo_features()
    demo_tech_stack()
    demo_cost_benefits()
    demo_use_cases()
    demo_benefits()
    
    # Ask if user wants live demo
    try:
        response = input("🎬 Would you like to see a live demo? (y/n): ").lower()
        if response in ['y', 'yes']:
            run_live_demo()
    except KeyboardInterrupt:
        print("\n\n👋 Demo interrupted. Thank you for your interest!")
        return
    
    print("🎉 Demo completed!")
    print("\n🚀 To get started:")
    print("   1. Set up your .env file with required credentials")
    print("   2. Get FREE Google Gemini API key from: https://aistudio.google.com/app/apikey")
    print("   3. Run: python main.py")
    print("   4. For continuous monitoring: python monitor_continuous.py")
    print("\n📚 Check README.md for detailed setup instructions")
    print("\n💡 Key Advantage: ZERO AI API costs with Gemini free tier!")
    print("\n🏆 Good luck with your hackathon submission!")

if __name__ == "__main__":
    main()
