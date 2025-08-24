# 🎬 SCREEN RECORDING SCRIPT - Portia Uptime Agent Demo

**Complete step-by-step script for showcasing the AI-powered monitoring system**

## 📋 PRE-RECORDING CHECKLIST

### **Windows Setup:**
- [ ] Open **2 CMD terminals** side by side
- [ ] Open **Telegram Desktop** app (visible on screen)
- [ ] Open **GitHub repo** in browser: `https://github.com/somewherelostt/portia-uptime-agent`
- [ ] Verify **.env file** has all API keys configured

### **Telegram Bot Setup (Show This):**
1. **Create Bot**: Message `@BotFather` on Telegram
   - Send: `/newbot`
   - Name: `Portia Monitor Bot`
   - Username: `portia_monitor_bot` (or similar)
   - **Copy the bot token**

2. **Get Chat ID**: 
   - Start chat with your bot
   - Send any message to the bot
   - Visit: `https://api.telegram.org/bot<YOUR_BOT_TOKEN>/getUpdates`
   - **Copy the chat ID from the JSON response**

3. **Test Message**:
   ```bash
   curl -X POST "https://api.telegram.org/bot<YOUR_BOT_TOKEN>/sendMessage" -d "chat_id=<YOUR_CHAT_ID>&text=🤖 Bot is working!"
   ```

---

## 🎥 RECORDING SCRIPT (6-7 minutes total)

### **INTRO: Project Overview (30s)**
**Terminal 1:**
```cmd
cd "c:\Users\abuma\OneDrive\Desktop\Hackathon\agent-hack\portia-uptime-agent"
dir
```

**Say:** *"This is our AI-powered website monitoring system with autonomous healing capabilities using Google Gemini AI, GitHub automation, and Telegram alerts."*

---

### **PART 1: Quick Setup Demo (45s)**
**Terminal 1:**
```cmd
python simple_setup.py
```
- Press **Enter** through prompts (already configured)
- **Say:** *"Interactive setup makes it easy for judges to configure API keys - Google Gemini, GitHub tokens, Telegram bot, and Portia API."*

---

### **PART 2: Feature Showcase (60s)**
**Terminal 1:**
```cmd
python demo.py
```
**Say:** *"Let me show you all integrated features:"*
- **AI Analysis:** *"Google Gemini AI analyzes website issues"*
- **GitHub Integration:** *"Automatically creates pull requests with fixes"*  
- **Telegram Alerts:** *"Real-time notifications to monitoring team"*
- **Portia SDK:** *"Enhanced monitoring capabilities"*

---

### **PART 3: Live Monitoring Test (75s)**
**Terminal 1:**
```cmd
python main.py
```
**Point to output showing:**
- ✅ **AI Code Analysis: Enabled (Gemini)**
- ✅ **GitHub Integration: Enabled** 
- ✅ **Telegram Alerts: Enabled**
- ✅ **Portia SDK: Enabled**
- **Response Time:** *Show actual measurement*

**Say:** *"All systems operational - monitoring live website with sub-second response times. AI is ready to analyze any issues."*

---

### **PART 4: GitHub Integration Demo (60s)**
**Switch to Browser:**
1. **Repository Overview:**
   - Show clean project structure
   - Point out professional commit messages
   
2. **Recent Commits:**
   - Show commit history with emojis
   - **Say:** *"Professional development workflow - the system creates commits and PRs automatically when fixing issues"*

3. **Code Quality:**
   - Briefly show main.py or portia_sdk.py
   - **Say:** *"Enterprise-grade code quality with proper error handling and documentation"*

---

### **PART 5: Simulate Website Downtime (90s)**
**Terminal 2:**
```cmd
REM Simulate website failure
python -c "
import os
# Read current .env
with open('.env', 'r') as f:
    content = f.read()

# Change to failing URL
content_modified = content.replace('MONITORED_URL=https://httpbin.org/status/200', 'MONITORED_URL=https://httpbin.org/status/500')

# Write modified .env
with open('.env', 'w') as f:
    f.write(content_modified)

print('✅ Modified URL to simulate website downtime')
"
```

**Terminal 2:**
```cmd
python main.py
```

**Say:** *"Now watch what happens when the website goes down - the AI kicks in to analyze the issue and determine root causes."*

**Expected Output:**
- 🚨 **Site is DOWN** 
- **[AI] Analyzing website issue using Gemini...**
- **[AI] Issue analyzed - Priority: HIGH**

---

### **PART 6: Telegram Alert Demo (45s)**
**Switch to Telegram App:**
- **Show the alert message received**
- **Say:** *"Real-time alerts sent immediately to the monitoring team via Telegram bot - no delays, instant notifications."*

**Typical Alert Message:**
```
🚨 WEBSITE DOWN ALERT 🚨

🔗 URL: https://httpbin.org/status/500
📊 Status: DOWN (500 Internal Server Error)
⏰ Time: 2025-08-24 15:30:45
🤖 AI Analysis: In Progress

The monitoring team has been notified.
```

---

### **PART 7: Continuous Monitoring (45s)**
**Terminal 1:**
```cmd
python monitor_continuous.py
```
**Say:** *"This runs continuously - checking every 5 minutes automatically. Perfect for production environments."*

**Show output for 15 seconds:**
- Monitoring loop starting
- Regular check intervals
- **Press Ctrl+C to stop**

---

### **PART 8: Recovery & GitHub PR Creation (60s)**
**Terminal 2:**
```cmd
REM Restore normal operation
python -c "
# Read current .env
with open('.env', 'r') as f:
    content = f.read()

# Restore working URL
content_restored = content.replace('MONITORED_URL=https://httpbin.org/status/500', 'MONITORED_URL=https://httpbin.org/status/200')

# Write restored .env  
with open('.env', 'w') as f:
    f.write(content_restored)

print('✅ Restored original working URL')
"
```

**Terminal 1:**
```cmd
python main.py
```

**Say:** *"System automatically detects recovery - site is back UP. In a real scenario, the AI would have created a GitHub pull request with the fix."*

**Switch to Browser - GitHub:**
- **Say:** *"The system would create PRs like this with specific code fixes, proper commit messages, and detailed analysis."*

---

### **PART 9: Final Demo - All Features Working (30s)**
**Terminal 1:**
```cmd
python main.py
```

**Say:** *"Final verification - all systems green:"*
- ✅ **Website monitoring: Operational**
- ✅ **AI analysis: Ready** 
- ✅ **GitHub integration: Connected**
- ✅ **Telegram alerts: Active**
- ✅ **Cost: $0** *"Using free tiers of all services"*

---

## 🎯 KEY TALKING POINTS

### **💡 Technical Highlights:**
- **"100% FREE AI integration"** - Google Gemini free tier (15 requests/min)
- **"Self-healing architecture"** - Detects, analyzes, and fixes automatically  
- **"Enterprise integrations"** - GitHub, Telegram, Portia APIs
- **"Zero subscription costs"** - All using free tiers
- **"Production ready"** - Proper error handling, logging, retry logic

### **🏆 Business Value:**
- **"Reduces downtime"** - Proactive monitoring and fixes
- **"Team efficiency"** - Automatic issue resolution
- **"Cost effective"** - No monitoring service fees
- **"Scalable solution"** - Monitor unlimited websites
- **"AI-powered insights"** - Root cause analysis

### **🔥 Innovation Points:**
- **"Autonomous healing"** - No human intervention required
- **"AI code generation"** - Gemini creates actual fixes
- **"Multi-channel alerting"** - Telegram + GitHub + logs
- **"Modern architecture"** - Python 3.12, async operations
- **"Hackathon winner"** - Practical problem-solving

---

## 📞 TELEGRAM BOT COMMANDS (Show During Demo)

### **Setup Commands:**
```bash
# 1. Create bot with @BotFather
/newbot
# Follow prompts, get token

# 2. Get chat ID  
curl "https://api.telegram.org/bot<TOKEN>/getUpdates"

# 3. Test message
curl -X POST "https://api.telegram.org/bot<TOKEN>/sendMessage" -d "chat_id=<CHAT_ID>&text=Test"
```

### **Sample Alert Messages:**
```
🚨 DOWNTIME ALERT 🚨
URL: https://yoursite.com
Status: DOWN (500 Error)  
Time: 2025-08-24 15:30:45
AI: Analyzing root cause...

🔧 ISSUE RESOLVED 🔧
URL: https://yoursite.com
Status: RESTORED
Downtime: 3 minutes 45 seconds
Fix: Auto-deployed via GitHub PR #123
```

---

## ⚡ COMMAND QUICK REFERENCE

```cmd
# Project structure
dir

# Interactive setup
python simple_setup.py

# Feature demo
python demo.py  

# Single monitoring check
python main.py

# Continuous monitoring  
python monitor_continuous.py

# Simulate failure (copy-paste Python code)
# Restore operation (copy-paste Python code)
```

---

## 🎬 RECORDING TIPS

1. **Duration:** 6-7 minutes total
2. **Pace:** Speak clearly, pause for output
3. **Screen:** Keep terminals visible, good font size
4. **Backup:** If command fails, explain expected behavior
5. **Energy:** Enthusiastic but professional tone
6. **End:** Finish with all systems showing green/working

---

**🏆 This demonstrates a complete, production-ready, AI-powered monitoring solution that solves real business problems while showcasing cutting-edge technology integration!**
