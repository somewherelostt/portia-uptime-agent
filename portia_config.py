#!/usr/bin/env python3
"""
Portia API Configuration
Configuration file for Portia API integration
"""

import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def get_portia_config():
    """Get Portia API configuration"""
    return {
        "base_url": os.getenv("PORTIA_BASE_URL", "https://api.portialabs.ai"),
        "api_key": os.getenv("PORTIA_API_KEY"),
        "endpoints": {
            "monitor_status": "/v1/monitors/status",
            "incident_report": "/v1/incidents/report",
            "create_incident": "/v1/incidents/create",
            "update_incident": "/v1/incidents/update",
            "get_incident": "/v1/incidents/get",
            "list_incidents": "/v1/incidents/list",
            "monitor_create": "/v1/monitors/create",
            "monitor_update": "/v1/monitors/update",
            "monitor_delete": "/v1/monitors/delete",
            "monitor_list": "/v1/monitors/list"
        },
        "timeout": int(os.getenv("PORTIA_TIMEOUT", "30")),
        "retry_attempts": int(os.getenv("PORTIA_RETRY_ATTEMPTS", "3")),
        "webhook_url": os.getenv("PORTIA_WEBHOOK_URL"),
        "notification_channels": os.getenv("PORTIA_NOTIFICATION_CHANNELS", "telegram,email").split(",")
    }

def get_portia_headers():
    """Get standard headers for Portia API requests"""
    config = get_portia_config()
    headers = {
        "Authorization": f"Bearer {config['api_key']}",
        "Content-Type": "application/json",
        "User-Agent": "Portia-Uptime-Agent/1.0",
        "Accept": "application/json"
    }
    
    # Add org ID header if available (optional)
    org_id = os.getenv("PORTIA_ORG_ID")
    if org_id and org_id != "your_actual_org_id_from_dashboard":
        headers["X-Portia-Org-ID"] = org_id
    
    return headers

def validate_portia_config():
    """Validate Portia configuration"""
    config = get_portia_config()
    
    if not config["api_key"]:
        print("[WARNING] PORTIA_API_KEY not set - Portia features will be disabled")
        return False
    
    if not config["base_url"]:
        print("[WARNING] PORTIA_BASE_URL not set - using default")
        return False
    
    print(f"[PORTIA] Configuration validated:")
    print(f"   Base URL: {config['base_url']}")
    print(f"   API Key: {config['api_key'][:10]}...")
    print(f"   Timeout: {config['timeout']}s")
    print(f"   Retry Attempts: {config['retry_attempts']}")
    
    return True

if __name__ == "__main__":
    validate_portia_config()
