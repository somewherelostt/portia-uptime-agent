# 🚀 Portia Uptime Agent - Enhanced Hackathon Version (Gemini AI)

A revolutionary, **AI-powered autonomous website monitoring system,** that not only detects downtime but **automatically fixes issues** by creating GitHub pull requests with AI-generated code fixes. **Powered by Google Gemini AI - 100% FREE tier!**

## ✨ Revolutionary Features

- 🤖 **Gemini AI-Powered Issue Resolution**: Uses Google Gemini 1.5 Flash for intelligent analysis and fixes
- 🔗 **Automatic GitHub Integration**: Creates PRs with fixes when issues are detected
- 🛠️ **Self-Healing Code**: Automatically generates and applies code fixes
- 📱 **Real-time Notifications**: Instant Telegram alerts for downtime and fixes
- ⚡ **Intelligent Monitoring**: Smart retry logic with configurable thresholds
- 🔒 **Secure & Scalable**: Enterprise-ready architecture with secure API integration
- 🔌 **Portia API Integration**: Enhanced monitoring with external API services
- 💰 **Zero AI Costs**: Completely free using Gemini's generous free tier

## 🎯 What Makes This Special

**Traditional monitoring systems** just tell you when something is wrong.
**Portia Uptime Agent** actually **fixes the problems automatically** using **free AI**!

### 🔄 Complete Autonomous Workflow

1. **Website goes down** → System detects it immediately
2. **Gemini AI analyzes the issue** → Identifies root cause and affected files
3. **Code fixes generated** → AI creates specific solutions
4. **GitHub PR created** → Automatic branch, commit, and pull request
5. **Owner reviews** → Human oversight of AI-generated fixes
6. **Merge and deploy** → Website automatically recovers

## 🚀 Quick Start

### 1. Clone and Setup

```bash
git clone <your-repo-url>
cd portia-uptime-agent
python -m venv venv
venv\Scripts\activate  # Windows
# or
source venv/bin/activate  # Linux/Mac
pip install -r requirements.txt
```

### 2. Environment Configuration

```bash
copy env_template.txt .env
```

Edit `.env` with your credentials:

```env
# Website to monitor
MONITORED_URL=https://your-website.com

# GitHub Integration (Required for automatic fixes)
GITHUB_TOKEN=your_github_personal_access_token
GITHUB_REPO_OWNER=your_github_username
GITHUB_REPO_NAME=your_repository_name

# Google Gemini AI (Required for AI analysis - FREE!)
GOOGLE_AI_API_KEY=your_google_ai_api_key

# Telegram Bot (Required for notifications)
TELEGRAM_BOT_TOKEN=your_bot_token
TELEGRAM_CHAT_ID=your_chat_id
```

### 3. Run the Demo

```bash
# Showcase all features for judges
python demo.py

# Test the monitoring system
python main.py

# Start continuous monitoring
python monitor_continuous.py
```

## 🔧 Setup Instructions

### GitHub Integration Setup

1. **Create Personal Access Token:**
   - Go to GitHub Settings → Developer settings → Personal access tokens
   - Generate new token with `repo` permissions
   - Copy token to `.env` file

2. **Repository Access:**
   - Ensure your token has access to the repository
   - Repository should contain the website code you're monitoring

### Google Gemini Setup (FREE!)

1. **Get API Key:**
   - Visit [Google AI Studio](https://aistudio.google.com/app/apikey)
   - Sign in with your Google account
   - Create a new API key
   - **Completely FREE** - No credit card required!

### Telegram Bot Setup

1. **Create Bot:**
   - Message [@BotFather](https://t.me/botfather) on Telegram
   - Send `/newbot` and follow the instructions
   - Save your bot token

2. **Get Chat ID:**
   - Start a chat with your bot
   - Send any message to the bot
   - Visit: `https://api.telegram.org/bot<YOUR_BOT_TOKEN>/getUpdates`
   - Find your `chat_id` in the response

## 🎬 Demo Scenarios for Hackathon Judges

### Scenario 1: Website Downtime Detection & Auto-Fix

1. **Setup:** Configure monitoring for a test website
2. **Action:** Take the website offline (stop server, etc.)
3. **Result:** System detects downtime, Gemini AI analyzes issue, creates GitHub PR with fixes
4. **Show:** Pull request with AI-generated code changes

### Scenario 2: Configuration Error Resolution

1. **Setup:** Introduce a configuration error in your website
2. **Action:** Run the monitoring system
3. **Result:** Gemini AI detects configuration issue, generates corrected config files
4. **Show:** Before/after configuration comparison

### Scenario 3: Code Bug Auto-Fix

1. **Setup:** Introduce a bug in your website code
2. **Action:** Deploy the broken code
3. **Result:** System detects error, generates fix, creates PR
4. **Show:** Code diff with AI-generated fixes

## 📊 What You'll See

### Successful Monitoring

```
🚀 Portia Uptime Agent - Enhanced Hackathon Version (Gemini AI)
📊 Monitoring: https://your-website.com
🤖 AI Code Analysis: ✅ Enabled (Gemini)
🔗 GitHub Integration: ✅ Enabled
📱 Telegram Alerts: ✅ Enabled
--------------------------------------------------------------------------------

🔍 Checking uptime for https://your-website.com...
📊 Uptime Check Result:
   Status: UP
   Details: {'status': 'UP', 'code': 200, 'response_time': 0.45}
✅ Site is UP
```

### Website Down - Auto-Fix Process

```
🚨 Site is DOWN (Count: 2/2)
[CRITICAL] Down threshold reached (2) - Starting automatic fix process...
[AI] Analyzing website issue using Gemini...
[AI] Issue analyzed - Priority: HIGH
[AI] Generating code fixes...
[GITHUB] Cloning repository your-username/your-repo...
[GITHUB] Repository cloned successfully to temp_repo_1234567890
[GITHUB] Created and switched to branch: fix/website-downtime-1234567890
[GITHUB] Applied fix to src/main.py
[GITHUB] Changes committed and pushed: 🔧 Auto-fix: Website downtime issue detected and resolved
[GITHUB] Pull request created: #42
[SUCCESS] Automatic fix process completed successfully!
```

## 🏆 Key Innovation Points for Judges

### **Autonomous Problem Resolution**

- **Zero Human Intervention**: System fixes issues automatically
- **Gemini AI-Powered Analysis**: Uses Google's latest AI for intelligent issue diagnosis
- **Self-Healing Infrastructure**: Websites automatically recover from failures

### **Technical Excellence**

- **Modern Tech Stack**: Python 3.11+, Google Gemini API, GitHub integration
- **Scalable Architecture**: Cloud-native, Docker-ready deployment
- **Security**: Secure API integration, environment-based configuration

### **Business Value**

- **Zero Downtime**: Continuous monitoring prevents service interruptions
- **Cost Reduction**: Eliminates manual troubleshooting time
- **User Experience**: Maintains website availability automatically
- **💰 Zero AI Costs**: Completely free using Gemini's generous free tier

## 💰 Why Google Gemini AI?

### **Cost Benefits**

- **🎯 Free Tier**: 15 requests per minute - Perfect for demos!
- **🚀 Pro Tier**: $0.0025 per 1K characters (if you need more)
- **⚡ Fast**: Optimized for real-time analysis
- **🔒 Secure**: Google's enterprise-grade security
- **🌐 Global**: Multiple data center locations worldwide

### **Perfect for Hackathons**

- **No Credit Card Required**: Sign up with Google account
- **Generous Limits**: Free tier covers most demo scenarios
- **Professional Quality**: Same AI that powers Google's services
- **Easy Integration**: Simple Python library

## 📁 Project Structure

```
portia-uptime-agent/
├── main.py                    # Enhanced monitoring with Gemini AI fixes
├── monitor_continuous.py      # Continuous monitoring script
├── demo.py                    # Hackathon demo showcase
├── HACKATHON_SETUP.md         # Complete setup guide for judges
├── env_template.txt           # Environment configuration template
├── portia_config.py           # Portia API configuration
├── test_portia.py             # Portia API integration tests
├── PORTIA_API_README.md       # Portia API integration guide
├── README.md                  # This file
├── requirements.txt           # Enhanced dependencies
└── venv/                     # Virtual environment
```

## 🛠️ Enhanced Dependencies

- `google-generativeai>=0.3.0` - Google Gemini AI integration (FREE!)
- `PyGithub>=2.1.1` - GitHub API integration
- `gitpython>=3.1.0` - Git operations
- `requests>=2.28.0` - HTTP monitoring
- `python-dotenv>=1.0.0` - Environment management

## 🔌 Portia API Integration

The Portia Uptime Agent now includes **Portia API integration** for enhanced monitoring capabilities:

- **Enhanced Monitoring Data**: Get additional insights from Portia API
- **Automatic Incident Reporting**: Send downtime reports to Portia API
- **Configurable Endpoints**: Easy customization of API endpoints
- **Graceful Fallback**: Continues monitoring even if Portia API is unavailable

### Quick Portia API Setup

1. **Add your Portia API key to `.env`:**

   ```env
   PORTIA_API_KEY=prt-5XpKO1cC.2QG1alMXZRyvr7X7Ci8d4jDJ1y7LVQQ3
   ```

2. **Test the integration:**

   ```bash
   python test_portia.py
   ```

3. **Customize endpoints in `portia_config.py`**

See `PORTIA_API_README.md` for complete documentation.

## 🚨 Troubleshooting

### Common Issues

1. **GitHub Authentication Failed**
   - Check personal access token permissions
   - Verify repository access

2. **Gemini API Errors**
   - Verify API key is correct
   - Check free tier limits (15 req/min)

3. **Telegram Notifications Not Working**
   - Verify bot token and chat ID
   - Ensure bot is started

## 🎯 Judging Criteria Alignment

- **Innovation (25%)**: Autonomous problem resolution, Gemini AI-powered analysis
- **Technical Implementation (25%)**: Clean code, modern stack, error handling
- **User Experience (20%)**: Easy setup, clear notifications, intuitive interface
- **Business Impact (20%)**: Reduces costs, improves reliability, scalable, **ZERO AI costs**
- **Presentation (10%)**: Clear demo, professional docs, effective communication

## 🚀 Next Steps

1. **Deploy to Production**: Set up on cloud infrastructure
2. **Add More Features**: Database monitoring, API health checks
3. **Scale Monitoring**: Multiple websites, team notifications
4. **Commercialize**: Offer as SaaS service with **free AI tier**

---

**This is the future of autonomous infrastructure management - powered by FREE AI! 🚀**

The Portia Uptime Agent represents a paradigm shift from reactive monitoring to proactive, self-healing systems, all while keeping costs at **ZERO** thanks to Google Gemini's generous free tier.
