

import os
import requests
import json
import time
from dotenv import load_dotenv
from github import Github
import git
import google.generativeai as genai
from datetime import datetime
import yaml
import jinja2

# Load environment variables
load_dotenv()

# Configuration
MONITORED_URL = os.getenv("MONITORED_URL", "https://example.com")
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")
GOOGLE_AI_API_KEY = os.getenv("GOOGLE_AI_API_KEY")
PORTIA_API_KEY = os.getenv("PORTIA_API_KEY")

# GitHub Configuration
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
GITHUB_REPO_OWNER = os.getenv("GITHUB_REPO_OWNER")
GITHUB_REPO_NAME = os.getenv("GITHUB_REPO_NAME")
GITHUB_BRANCH = os.getenv("GITHUB_BRANCH", "main")

# Monitoring Configuration
RETRY_ATTEMPTS = int(os.getenv("RETRY_ATTEMPTS", "3"))
DOWN_THRESHOLD = int(os.getenv("DOWN_THRESHOLD", "2"))

class GitHubManager:
    def __init__(self):
        if not all([GITHUB_TOKEN, GITHUB_REPO_OWNER, GITHUB_REPO_NAME]):
            raise ValueError("GitHub configuration incomplete")
        
        self.github = Github(GITHUB_TOKEN)
        self.repo = self.github.get_repo(f"{GITHUB_REPO_OWNER}/{GITHUB_REPO_NAME}")
        self.repo_path = f"temp_repo_{int(time.time())}"
        
    def clone_repository(self):
        """Clone the repository to local workspace"""
        try:
            print(f"[GITHUB] Cloning repository {self.repo.full_name}...")
            git.Repo.clone_from(
                f"https://{GITHUB_TOKEN}@github.com/{GITHUB_REPO_OWNER}/{GITHUB_REPO_NAME}.git",
                self.repo_path
            )
            print(f"[GITHUB] Repository cloned successfully to {self.repo_path}")
            return True
        except Exception as e:
            print(f"[ERROR] Failed to clone repository: {e}")
            return False
    
    def create_branch(self, branch_name):
        """Create a new branch for the fix"""
        try:
            repo = git.Repo(self.repo_path)
            new_branch = repo.create_head(branch_name)
            new_branch.checkout()
            print(f"[GITHUB] Created and switched to branch: {branch_name}")
            return True
        except Exception as e:
            print(f"[ERROR] Failed to create branch: {e}")
            return False
    
    def commit_and_push(self, commit_message):
        """Commit changes and push to remote"""
        try:
            repo = git.Repo(self.repo_path)
            repo.git.add(".")
            repo.index.commit(commit_message)
            repo.remote().push()
            print(f"[GITHUB] Changes committed and pushed: {commit_message}")
            return True
        except Exception as e:
            print(f"[ERROR] Failed to commit and push: {e}")
            return False
    
    def create_pull_request(self, title, body, branch_name):
        """Create a pull request"""
        try:
            pr = self.repo.create_pull(
                title=title,
                body=body,
                head=branch_name,
                base=self.repo.default_branch
            )
            print(f"[GITHUB] Pull request created: #{pr.number}")
            return pr
        except Exception as e:
            print(f"[ERROR] Failed to create pull request: {e}")
            return None
    
    def cleanup(self):
        """Clean up temporary repository"""
        try:
            import shutil
            if os.path.exists(self.repo_path):
                shutil.rmtree(self.repo_path)
                print(f"[GITHUB] Cleaned up temporary repository")
        except Exception as e:
            print(f"[WARNING] Failed to cleanup: {e}")

class GeminiCodeAnalyzer:
    def __init__(self):
        if not GOOGLE_AI_API_KEY:
            raise ValueError("Google AI API key not configured")
        
        # Configure Google AI
        genai.configure(api_key=GOOGLE_AI_API_KEY)
        self.model = genai.GenerativeModel('gemini-1.5-flash')
    
    def analyze_website_issue(self, url, error_details):
        """Analyze website issues and suggest fixes using Gemini"""
        try:
            prompt = f"""
            You are an expert DevOps engineer and website monitoring specialist. 
            A website monitoring system detected that {url} is down.
            
            Error details: {error_details}
            
            Please analyze this issue and provide a JSON response with:
            1. Root cause analysis
            2. Specific code fixes needed
            3. Configuration changes required
            4. Priority level (HIGH/MEDIUM/LOW)
            
            Respond with ONLY a valid JSON object in this exact format:
            {{
                "root_cause": "detailed description of the root cause",
                "fixes": [
                    {{
                        "file": "filename.ext",
                        "changes": "description of what needs to be changed",
                        "code": "actual code to add/change"
                    }}
                ],
                "config_changes": ["list of configuration changes needed"],
                "priority": "HIGH",
                "estimated_time": "estimated time to fix"
            }}
            
            Be specific and provide actionable fixes. If you can't determine the issue, return:
            {{
                "root_cause": "Unable to determine root cause from provided information",
                "fixes": [],
                "config_changes": [],
                "priority": "UNKNOWN",
                "estimated_time": "Unknown"
            }}
            """
            
            response = self.model.generate_content(prompt)
            ai_response = response.text.strip()
            
            # Extract JSON from response
            try:
                # Find JSON in the response
                start = ai_response.find('{')
                end = ai_response.rfind('}') + 1
                if start != -1 and end != 0:
                    json_str = ai_response[start:end]
                    parsed = json.loads(json_str)
                    return parsed
                else:
                    print(f"[WARNING] Gemini response format unexpected: {ai_response}")
                    return None
                    
            except json.JSONDecodeError:
                print(f"[WARNING] Gemini response not valid JSON: {ai_response}")
                return None
            
        except Exception as e:
            print(f"[ERROR] Gemini analysis failed: {e}")
            return None
    
    def generate_fix_code(self, issue_analysis):
        """Generate actual code fixes based on Gemini analysis"""
        try:
            fixes = []
            for fix in issue_analysis.get("fixes", []):
                prompt = f"""
                You are an expert software developer. Generate the complete, corrected code for this fix:
                
                File: {fix['file']}
                Changes needed: {fix['changes']}
                
                Provide ONLY the corrected code, no explanations or markdown formatting.
                If this is a new file, provide the complete file content.
                If this is a modification, provide the complete corrected file.
                """
                
                response = self.model.generate_content(prompt)
                generated_code = response.text.strip()
                
                # Clean up the response (remove markdown if present)
                if generated_code.startswith('```'):
                    lines = generated_code.split('\n')
                    if len(lines) > 2:
                        generated_code = '\n'.join(lines[1:-1])
                
                fix["generated_code"] = generated_code
                fixes.append(fix)
            
            return fixes
            
        except Exception as e:
            print(f"[ERROR] Code generation failed: {e}")
            return []

class UptimeMonitor:
    def __init__(self):
        self.down_count = 0
        self.last_status = None
        
    def check_uptime(self, url):
        """Check website uptime with retries"""
        for attempt in range(RETRY_ATTEMPTS):
            try:
                print(f"[CHECK] Attempt {attempt + 1}/{RETRY_ATTEMPTS} for {url}")
                response = requests.get(url, timeout=10)
                
                if response.status_code == 200:
                    return {"status": "UP", "code": response.status_code, "response_time": response.elapsed.total_seconds()}
                else:
                    return {"status": "DOWN", "code": response.status_code, "error": f"HTTP {response.status_code}"}
                    
            except requests.exceptions.Timeout:
                return {"status": "DOWN", "error": "Timeout"}
            except requests.exceptions.ConnectionError:
                return {"status": "DOWN", "error": "Connection Error"}
        except Exception as e:
            return {"status": "DOWN", "error": str(e)}
        
        return {"status": "DOWN", "error": "All retry attempts failed"}

def send_telegram_alert(message):
    """Send Telegram alert"""
    if not TELEGRAM_BOT_TOKEN or not TELEGRAM_CHAT_ID:
        print("[WARNING] Telegram credentials missing")
        return False
    
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    try:
        resp = requests.post(url, data={"chat_id": TELEGRAM_CHAT_ID, "text": message}, timeout=10)
        if resp.status_code == 200:
            print("[SUCCESS] Telegram alert sent!")
            return True
        else:
            print(f"[ERROR] Telegram notification failed: {resp.status_code}")
            return False
    except Exception as e:
        print(f"[ERROR] Telegram notification error: {e}")
        return False

def handle_website_down(url, error_details):
    """Handle website downtime - analyze and create fixes"""
    print(f"[CRITICAL] Website {url} is DOWN - Initiating automatic fix process...")
    
    try:
        # Initialize Gemini analyzer
        ai_analyzer = GeminiCodeAnalyzer()
        
        # Analyze the issue
        print("[AI] Analyzing website issue using Gemini...")
        issue_analysis = ai_analyzer.analyze_website_issue(url, error_details)
        
        if not issue_analysis:
            print("[ERROR] Gemini analysis failed, cannot proceed with automatic fixes")
            return False
        
        print(f"[AI] Issue analyzed - Priority: {issue_analysis.get('priority', 'UNKNOWN')}")
        
        # Generate code fixes
        print("[AI] Generating code fixes...")
        fixes = ai_analyzer.generate_fix_code(issue_analysis)
        
        if not fixes:
            print("[ERROR] No code fixes generated")
            return False
        
        # Initialize GitHub manager
        github_manager = GitHubManager()
        
        # Clone repository
        if not github_manager.clone_repository():
            return False
        
        # Create fix branch
        branch_name = f"fix/website-downtime-{int(time.time())}"
        if not github_manager.create_branch(branch_name):
            return False
        
        # Apply fixes
        print("[GITHUB] Applying code fixes...")
        for fix in fixes:
            file_path = os.path.join(github_manager.repo_path, fix["file"])
            
            # Create directory if it doesn't exist
            os.makedirs(os.path.dirname(file_path), exist_ok=True)
            
            # Write the fixed code
            with open(file_path, 'w') as f:
                f.write(fix["generated_code"])
            
            print(f"[GITHUB] Applied fix to {fix['file']}")
        
        # Commit and push changes
        commit_message = f"🔧 Auto-fix: Website downtime issue detected and resolved\n\n- Root cause: {issue_analysis.get('root_cause', 'Unknown')}\n- Priority: {issue_analysis.get('priority', 'Unknown')}\n- Files modified: {len(fixes)}"
        
        if not github_manager.commit_and_push(commit_message):
            return False
        
        # Create pull request
        pr_title = f"🚨 Auto-Fix: Website Downtime Resolution - {datetime.now().strftime('%Y-%m-%d %H:%M')}"
        pr_body = f"""
## 🤖 Automatic Website Downtime Fix

**Website:** {url}
**Issue Detected:** {error_details}
**Priority:** {issue_analysis.get('priority', 'Unknown')}

### 🔍 Root Cause Analysis
{issue_analysis.get('root_cause', 'Analysis not available')}

### 🛠️ Applied Fixes
{chr(10).join([f"- **{fix['file']}**: {fix['changes']}" for fix in fixes])}

### ⚙️ Configuration Changes
{chr(10).join([f"- {change}" for change in issue_analysis.get('config_changes', [])])}

### ⏱️ Estimated Resolution Time
{issue_analysis.get('estimated_time', 'Unknown')}

---
*This PR was automatically generated by Portia Uptime Agent using Google Gemini AI when downtime was detected.*
        """
        
        pr = github_manager.create_pull_request(pr_title, pr_body, branch_name)
        
        if pr:
            print(f"[SUCCESS] Pull request created: #{pr.number}")
            
            # Send Telegram notification about PR creation
            telegram_message = f"""
🚨 WEBSITE DOWNTIME DETECTED!

Website: {url}
Status: DOWN
Error: {error_details}

🤖 Gemini AI Analysis Complete:
Priority: {issue_analysis.get('priority', 'Unknown')}
Root Cause: {issue_analysis.get('root_cause', 'Unknown')}

🔧 Automatic Fix Applied:
- Files Modified: {len(fixes)}
- Pull Request: #{pr.number}
- Branch: {branch_name}

Review and merge the PR to restore website functionality.
            """
            
            send_telegram_alert(telegram_message)
            
            # Cleanup
            github_manager.cleanup()
            return True
        
        return False
            
    except Exception as e:
        print(f"[ERROR] Automatic fix process failed: {e}")
        return False

def main():
    print(f"🚀 Portia Uptime Agent - Enhanced Hackathon Version (Gemini AI + Portia SDK)")
    print(f"📊 Monitoring: {MONITORED_URL}")
    print(f"🤖 AI Code Analysis: {'✅ Enabled (Gemini)' if GOOGLE_AI_API_KEY else '❌ Disabled'}")
    print(f"🔗 GitHub Integration: {'✅ Enabled' if GITHUB_TOKEN else '❌ Disabled'}")
    print(f"📱 Telegram Alerts: {'✅ Enabled' if TELEGRAM_BOT_TOKEN else '❌ Disabled'}")
    print(f"🔌 Portia SDK: {'✅ Enabled' if PORTIA_API_KEY else '❌ Disabled'}")
    print("-" * 80)
    
    # Initialize monitor and Portia SDK
    monitor = UptimeMonitor()
    
    # Initialize Portia SDK if available
    portia_client = None
    if PORTIA_API_KEY:
        try:
            from portia_sdk import get_portia_client
            portia_client = get_portia_client()
            if portia_client.enabled:
                print(f"[PORTIA] SDK initialized successfully")
            else:
                print(f"[PORTIA] SDK disabled - check configuration")
        except ImportError:
            print(f"[WARNING] Portia SDK not available - using basic integration")
        except Exception as e:
            print(f"[WARNING] Portia SDK initialization failed: {e}")
    
    # Check uptime
    print(f"\n🔍 Checking uptime for {MONITORED_URL}...")
    result = monitor.check_uptime(MONITORED_URL)
    
    print(f"\n📊 Uptime Check Result:")
    print(f"   Status: {result.get('status', 'UNKNOWN')}")
    print(f"   Details: {result}")
    
    # Handle results
    if result.get('status') == "DOWN":
        monitor.down_count += 1
        print(f"[ALERT] Site is DOWN (Count: {monitor.down_count}/{DOWN_THRESHOLD})")
        
        # Send immediate alert
        alert_message = f"""
🚨 UPTIME ALERT

Website: {MONITORED_URL}
Status: DOWN
Error: {result.get('error', 'Unknown')}
Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

Attempting automatic resolution using Gemini AI...
        """
        send_telegram_alert(alert_message)
        
        # Send incident report to Portia API if available
        if portia_client and portia_client.enabled:
            try:
                incident_data = {
                    "status": "DOWN",
                    "error": result.get('error', 'Unknown'),
                    "response_time": result.get('response_time', 0),
                    "down_count": monitor.down_count,
                    "severity": "high" if monitor.down_count >= DOWN_THRESHOLD else "medium"
                }
                
                # Create incident in Portia
                incident_result = portia_client.create_incident(
                    monitor_id="uptime-agent",
                    title=f"Website Downtime: {MONITORED_URL}",
                    description=f"Website {MONITORED_URL} is down. Error: {result.get('error', 'Unknown')}",
                    severity="high" if monitor.down_count >= DOWN_THRESHOLD else "medium",
                    status="open"
                )
                
                if incident_result:
                    print(f"[PORTIA] Incident created successfully")
                else:
                    print(f"[PORTIA] Failed to create incident")
                    
            except Exception as e:
                print(f"[PORTIA] Error creating incident: {e}")
        
        # If threshold reached, initiate automatic fix
        if monitor.down_count >= DOWN_THRESHOLD:
            print(f"[CRITICAL] Down threshold reached ({DOWN_THRESHOLD}) - Starting automatic fix process...")
            if handle_website_down(MONITORED_URL, result.get('error', 'Unknown')):
                print("[SUCCESS] Automatic fix process completed successfully!")
            else:
                print("[ERROR] Automatic fix process failed")
        else:
            print(f"[INFO] Waiting for threshold ({DOWN_THRESHOLD}) before automatic fix...")
            
    elif result.get('status') == "UP":
        if monitor.down_count > 0:
            print(f"[RECOVERY] Site is back UP - Resetting down counter")
            monitor.down_count = 0
            
            # Update incident status in Portia if available
            if portia_client and portia_client.enabled:
                try:
                    # This would update the incident status to resolved
                    print(f"[PORTIA] Would update incident status to resolved")
                except Exception as e:
                    print(f"[PORTIA] Error updating incident: {e}")
            
            # Send recovery notification
            recovery_message = f"""
✅ WEBSITE RECOVERED!

Website: {MONITORED_URL}
Status: UP
Response Time: {result.get('response_time', 'Unknown')}s
Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

The website is now accessible again.
            """
            send_telegram_alert(recovery_message)
        else:
        print("[SUCCESS] Site is UP")
    
    monitor.last_status = result.get('status')

if __name__ == "__main__":
    main()
