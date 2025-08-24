# 🏆 Portia Uptime Agent - Hackathon Setup Guide (Gemini AI)

## 🎯 What This System Does

**Portia Uptime Agent** is an autonomous website monitoring system that:

1. **Monitors websites** for uptime/downtime continuously
2. **Automatically detects** when websites go down
3. **AI-analyzes** the root cause of issues using **Google Gemini**
4. **Generates code fixes** using advanced AI models
5. **Creates GitHub PRs** automatically with fixes
6. **Notifies owners** via Telegram for review
7. **Self-heals** websites when owners merge the PRs
8. **💰 Costs ZERO** - Uses Gemini's generous free tier!

## 🚀 Quick Demo for Judges

### 1. Run the Demo Script

```bash
python demo.py
```

This will showcase all features without requiring full setup.

### 2. Show Live Monitoring

```bash
python main.py
```

This demonstrates the actual monitoring system.

## 🔧 Complete Setup for Full Demo

### Prerequisites

- Python 3.11+
- Git installed
- GitHub account with repository access
- **Google Gemini API key (FREE!)**
- Telegram bot token

### Step 1: Install Dependencies

```bash
# Create virtual environment
python -m venv venv
venv\Scripts\activate  # Windows
# or
source venv/bin/activate  # Linux/Mac

# Install packages
pip install -r requirements.txt
```

### Step 2: Configure Environment

```bash
# Copy environment template
copy env_template.txt .env

# Edit .env with your credentials
```

**Required Environment Variables:**

```env
# Website to monitor (your demo website)
MONITORED_URL=https://your-demo-website.com

# GitHub Integration
GITHUB_TOKEN=your_github_personal_access_token
GITHUB_REPO_OWNER=your_github_username
GITHUB_REPO_NAME=your_repository_name

# Google Gemini AI (for code analysis - FREE!)
GOOGLE_AI_API_KEY=your_google_ai_api_key

# Telegram Bot (for notifications)
TELEGRAM_BOT_TOKEN=your_bot_token
TELEGRAM_CHAT_ID=your_chat_id
```

### Step 3: GitHub Setup

1. **Create Personal Access Token:**
   - Go to GitHub Settings → Developer settings → Personal access tokens
   - Generate new token with `repo` permissions
   - Copy token to `.env` file

2. **Repository Access:**
   - Ensure your token has access to the repository
   - Repository should contain the website code you're monitoring

### Step 4: Google Gemini Setup (100% FREE!)

1. **Get API Key:**
   - Visit [Google AI Studio](https://aistudio.google.com/app/apikey)
   - Sign in with your Google account
   - Create a new API key
   - **No credit card required!**
   - **Free tier: 15 requests per minute**

2. **Why Gemini?**
   - **💰 Completely FREE** for hackathon demos
   - **🚀 Professional quality** - Same AI that powers Google
   - **⚡ Fast and reliable** - Enterprise-grade infrastructure
   - **🔒 Secure** - Google's security standards

### Step 5: Telegram Bot Setup

1. **Create Bot:**
   - Message [@BotFather](https://t.me/botfather) on Telegram
   - Send `/newbot` and follow the instructions
   - Save bot token

2. **Get Chat ID:**
   - Start chat with your bot
   - Send any message
   - Visit: `https://api.telegram.org/bot<TOKEN>/getUpdates`
   - Find your `chat_id` in response

## 🎬 Demo Scenarios for Judges

### Scenario 1: Website Goes Down

1. **Setup:** Configure monitoring for a test website
2. **Action:** Take the website offline (stop server, etc.)
3. **Result:** System detects downtime, Gemini AI analyzes issue, creates GitHub PR
4. **Show:** Pull request with AI-generated fixes

### Scenario 2: Configuration Issues

1. **Setup:** Introduce a configuration error in your website
2. **Action:** Run the monitoring system
3. **Result:** Gemini AI detects configuration issue, suggests fixes
4. **Show:** Generated configuration files and code changes

### Scenario 3: Code Errors

1. **Setup:** Introduce a bug in your website code
2. **Action:** Deploy the broken code
3. **Result:** System detects error, generates fix, creates PR
4. **Show:** Before/after code comparison

## 📊 What Judges Will See

### 1. **Real-time Monitoring Dashboard**

- Live uptime status
- Response time metrics
- Error detection logs

### 2. **Gemini AI Analysis Results**

- Root cause identification
- Issue prioritization
- Fix recommendations

### 3. **GitHub Integration**

- Automatic branch creation
- Code commits with fixes
- Pull request generation

### 4. **Telegram Notifications**

- Instant downtime alerts
- Fix progress updates
- PR creation confirmations

## 🏆 Key Selling Points for Judges

### **Innovation Factor**

- **Autonomous Problem Resolution:** System fixes issues without human intervention
- **Gemini AI-Powered Analysis:** Uses Google's latest AI for intelligent issue diagnosis
- **Self-Healing Infrastructure:** Websites automatically recover from failures

### **Technical Excellence**

- **Modern Tech Stack:** Python 3.11+, Google Gemini API, GitHub integration
- **Scalable Architecture:** Cloud-native, Docker-ready deployment
- **Security:** Secure API integration, environment-based configuration

### **Business Value**

- **Zero Downtime:** Continuous monitoring prevents service interruptions
- **Cost Reduction:** Eliminates manual troubleshooting time
- **User Experience:** Maintains website availability automatically
- **💰 Zero AI Costs:** Completely free using Gemini's generous free tier

### **Real-World Applicability**

- **Enterprise Ready:** Suitable for production environments
- **Multi-Platform:** Works with any website or web service
- **Extensible:** Easy to add new monitoring targets
- **Cost-Effective:** No ongoing AI API costs

## 💰 Cost Benefits for Judges

### **Gemini Free Tier**

- **🎯 15 requests per minute** - Perfect for demos
- **🚀 No credit card required** - Sign up with Google account
- **⚡ Professional quality** - Same AI that powers Google services
- **🔒 Enterprise security** - Google's infrastructure

### **Pro Tier (if needed)**

- **$0.0025 per 1K characters** - Extremely affordable
- **Unlimited requests** - Scale as needed
- **Priority support** - Google's enterprise support

## 🚨 Troubleshooting Common Issues

### **GitHub Authentication Failed**

- Check personal access token permissions
- Verify repository access
- Ensure token hasn't expired

### **Gemini API Errors**

- Verify API key is correct
- Check free tier limits (15 req/min)
- Ensure you're using the correct API endpoint

### **Telegram Notifications Not Working**

- Verify bot token
- Check chat ID
- Ensure bot is started

### **Website Monitoring Issues**

- Check URL accessibility
- Verify network connectivity
- Review firewall settings

## 📱 Demo Commands

```bash
# Show demo features
python demo.py

# Run single monitoring check
python main.py

# Start continuous monitoring
python monitor_continuous.py

# Check configuration
python test_setup.py
```

## 🎯 Judging Criteria Alignment

### **Innovation (25%)**

- Autonomous problem resolution
- Gemini AI-powered issue analysis
- Self-healing capabilities

### **Technical Implementation (25%)**

- Clean, maintainable code
- Modern technology stack
- Proper error handling

### **User Experience (20%)**

- Easy setup and configuration
- Clear notifications and alerts
- Intuitive monitoring interface

### **Business Impact (20%)**

- Reduces downtime costs
- Improves reliability
- Scalable solution
- **💰 Zero AI costs**

### **Presentation (10%)**

- Clear demonstration
- Professional documentation
- Effective communication

## 🚀 Next Steps After Hackathon

1. **Deploy to Production:** Set up on cloud infrastructure
2. **Add More Features:** Database monitoring, API health checks
3. **Scale Monitoring:** Multiple websites, team notifications
4. **Commercialize:** Offer as SaaS service with **free AI tier**
5. **Open Source:** Share with developer community

## 💡 Why This Will Impress Judges

### **Cost Innovation**

- **Traditional approach:** Pay per API call (OpenAI, etc.)
- **Your approach:** Completely free AI using Gemini
- **Result:** Sustainable, scalable solution

### **Technical Innovation**

- **Autonomous problem resolution** - Not just monitoring
- **AI-powered code generation** - Real fixes, not just alerts
- **GitHub integration** - Professional development workflow

### **Business Innovation**

- **Self-healing infrastructure** - Reduces manual intervention
- **Proactive monitoring** - Prevents issues before they impact users
- **Cost-effective scaling** - Free AI tier grows with your business

---

**Good luck with your hackathon submission! 🏆**

The Portia Uptime Agent represents the future of autonomous infrastructure management, all while keeping costs at **ZERO** thanks to Google Gemini's generous free tier.
