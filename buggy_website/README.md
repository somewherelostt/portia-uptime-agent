# Buggy Website for Portia Uptime Agent Testing

This is a deliberately broken website designed to test the Portia Uptime Agent's ability to detect and automatically fix website issues.

## 🎯 **How It Works**

1. **Website is DOWN**: The website returns a 500 error due to the API function
2. **Portia Detects**: Your uptime monitor will detect the website as "DOWN"
3. **Automatic Fix**: Portia will access your GitHub repo and fix the issues
4. **PR Created**: A Pull Request will be created with the fixes
5. **You Merge**: Review and merge the PR to restore the website

## 🚀 **Quick Setup**

### 1. Deploy to Vercel

```bash
# Push to your GitHub repo
git add .
git commit -m "Add buggy website that returns 500 errors"
git push origin main

# Deploy to Vercel
# The website will return 500 errors (DOWN)
```

### 2. Test with Portia Agent

```bash
# Run your Portia Uptime Agent
python main.py

# Set MONITORED_URL to your Vercel URL
# Example: https://your-buggy-website.vercel.app/
```

## 🔧 **What Portia Will Fix**

The agent will detect these issues and fix them:

1. **Remove the crash API function** that causes 500 errors
2. **Fix the JavaScript error** in `index.html`
3. **Restore the static file serving** in `vercel.json`
4. **Create a working website**

## 📁 **Files Structure**

```
buggy_website/
├── index.html          # Main page with JavaScript error
├── styles.css          # CSS with syntax errors
├── vercel.json         # Vercel config (routes to crash function)
├── api/crash.js        # Function that returns 500 error
└── README.md           # This file
```

## 🎪 **Demo for Judges**

1. **Show the broken website**: Visit your Vercel URL - it will return 500 error
2. **Run Portia Agent**: Execute `python main.py`
3. **Watch the magic**: Portia detects, analyzes, and creates a PR
4. **Merge the fix**: Accept the PR and watch the website come back online

## 🎯 **Expected Behavior**

- ✅ Website returns 500 errors (DOWN)
- ✅ Portia detects the downtime
- ✅ Agent analyzes the issues
- ✅ GitHub PR created with fixes
- ✅ Website restored after PR merge

Perfect for hackathon demos! 🚀
