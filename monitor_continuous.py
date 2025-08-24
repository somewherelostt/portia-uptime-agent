#!/usr/bin/env python3
"""
Simple continuous monitoring script for Portia Uptime Agent
Runs the main uptime check at regular intervals
"""

import time
import subprocess
import sys
import os

def main():
    print("🔄 Starting continuous monitoring...")
    print("Press Ctrl+C to stop")
    print("-" * 50)
    
    # Get monitoring interval from environment (default: 5 minutes)
    interval = int(os.getenv("MONITORING_INTERVAL", "5")) * 60
    
    try:
        while True:
            print(f"\n⏰ Running uptime check at {time.strftime('%H:%M:%S')}...")
            
            # Run the main uptime check
            result = subprocess.run([sys.executable, "main.py"], 
                                  capture_output=True, text=True)
            
            if result.returncode == 0:
                print("✅ Uptime check completed successfully")
            else:
                print("❌ Uptime check failed")
                if result.stderr:
                    print(f"Error: {result.stderr}")
            
            print(f"⏳ Waiting {interval//60} minutes until next check...")
            time.sleep(interval)
            
    except KeyboardInterrupt:
        print("\n🛑 Monitoring stopped by user")
    except Exception as e:
        print(f"\n❌ Monitoring error: {e}")

if __name__ == "__main__":
    main()
