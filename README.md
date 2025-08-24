# 🚀 Portia Uptime Agent - AI-Powered Website Monitoring

**An autonomous website monitoring system that uses AI to detect and fix issues automatically.**

## ✅ WORKING FEATURES (Verified & Ready for Demo)
- demo video https://www.youtube.com/watch?v=7GYWjlkbHP4

### **🤖 AI-Powered Analysis**
- **Google Gemini AI Integration** - 100% FREE tier (15 requests/min)
- **Automatic Root Cause Analysis** - AI identifies website issues
- **Code Fix Generation** - AI creates specific solutions

### **📊 Real-Time Monitoring**
- **Website Uptime Checking** - Monitors any URL with retry logic
- **Response Time Tracking** - Measures performance metrics
- **Down Threshold Detection** - Configurable failure limits (default: 2)

### **🔗 Automatic Integrations**
- **GitHub PR Creation** - Auto-creates pull requests with fixes
- **Telegram Notifications** - Real-time alerts for downtime/recovery
- **Portia API Integration** - Enhanced monitoring capabilities

### **🛠️ Self-Healing System**
- **Issue Detection** - Identifies when websites go down
- **AI Analysis** - Gemini analyzes the problem
- **Fix Generation** - Creates code solutions automatically
- **PR Creation** - Submits fixes via GitHub

## 🚀 QUICK START (30 seconds)

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Configure API Keys
Edit `.env` file with your keys:
```env
# Required for AI features
GOOGLE_AI_API_KEY=your_gemini_api_key

# Required for monitoring  
MONITORED_URL=https://your-website.com

# Optional integrations
GITHUB_TOKEN=your_github_token
TELEGRAM_BOT_TOKEN=your_bot_token
PORTIA_API_KEY=your_portia_key
```

### 3. Run Demo
```bash
python demo.py          # Interactive demo
python main.py          # Single monitoring check
python simple_setup.py  # Guided setup
```

## 📋 DEMO COMMANDS FOR JUDGES

### **Show All Features**
```bash
python demo.py
```
*Displays complete feature overview and capabilities*

### **Live Monitoring Test**
```bash
python main.py
```
*Runs actual website monitoring with AI analysis*

### **Continuous Monitoring**
```bash
python monitor_continuous.py
```
*Monitors website every 5 minutes automatically*

### **Quick Setup**
```bash
python simple_setup.py
```
*Interactive setup for API keys and configuration*

## 🎯 WHAT JUDGES WILL SEE

### **Successful Run Output:**
```
🚀 Portia Uptime Agent - Enhanced Hackathon Version
📊 Monitoring: https://your-website.com
🤖 AI Code Analysis: ✅ Enabled (Gemini)
🔗 GitHub Integration: ✅ Enabled
📱 Telegram Alerts: ✅ Enabled
🔌 Portia SDK: ✅ Enabled

🔍 Checking uptime...
📊 Status: UP
✅ Response Time: 1.1s
[SUCCESS] Site is UP
```

### **When Website Goes Down:**
```
🚨 Site is DOWN (Count: 2/2)
[AI] Analyzing website issue using Gemini...
[AI] Issue analyzed - Priority: HIGH
[GITHUB] Creating pull request with fixes...
[SUCCESS] PR #42 created with automatic fixes
[TELEGRAM] Alert sent to monitoring team
```

## 💡 KEY SELLING POINTS

### **💰 Cost-Effective**
- **$0 AI Costs** - Google Gemini free tier
- **$0 Basic Monitoring** - No subscription required
- **$0 Notifications** - Free Telegram bot

### **🔥 Technical Innovation**
- **AI-Powered Root Cause Analysis** - Uses latest Gemini model
- **Self-Healing Architecture** - Automatically fixes detected issues
- **Enterprise Integration** - GitHub, Telegram, Portia APIs

### **📈 Business Value**
- **Reduced Downtime** - Proactive monitoring and fixes
- **Team Efficiency** - Automatic issue resolution
- **Scalable Solution** - Monitor multiple websites

## 🗂️ PROJECT STRUCTURE

```
portia-uptime-agent/
├── demo.py              # Feature demonstration
├── main.py              # Core monitoring system
├── simple_setup.py      # Interactive setup
├── monitor_continuous.py # Continuous monitoring
├── portia_sdk.py        # Portia API integration
├── portia_config.py     # Configuration management
├── requirements.txt     # Dependencies
├── .env                 # API keys and config
└── README.md           # This file
```

## ⚡ TECHNICAL REQUIREMENTS

- **Python 3.11+** (Currently running 3.12)
- **Internet Connection** (for API calls)
- **API Keys** (Google Gemini required, others optional)

## 🏆 READY FOR HACKATHON

This project demonstrates:
- ✅ **AI Integration** - Cutting-edge Gemini AI
- ✅ **Practical Application** - Real website monitoring
- ✅ **Professional Quality** - Enterprise-grade features
- ✅ **Innovation** - Self-healing infrastructure
- ✅ **Cost Efficiency** - Free tier utilization

**Status: FULLY FUNCTIONAL** 🎉

---

*Built with Google Gemini AI, Portia SDK, and modern Python architecture*
