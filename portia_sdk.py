#!/usr/bin/env python3
"""
Portia SDK Client
Comprehensive client for Portia API integration
"""

import requests
import json
import time
from datetime import datetime
from typing import Dict, List, Optional, Any
from portia_config import get_portia_config, get_portia_headers

class PortiaSDK:
    """Portia SDK client for API integration"""
    
    def __init__(self):
        self.config = get_portia_config()
        self.headers = get_portia_headers()
        self.session = requests.Session()
        self.session.headers.update(self.headers)
        
        if not self.config["api_key"]:
            print("[WARNING] Portia API key not configured - SDK disabled")
            self.enabled = False
        else:
            self.enabled = True
            print(f"[PORTIA] SDK initialized with API key: {self.config['api_key'][:10]}...")
    
    def _make_request(self, method: str, endpoint: str, data: Optional[Dict] = None, 
                     params: Optional[Dict] = None, retry: bool = True) -> Optional[Dict]:
        """Make HTTP request to Portia API with retry logic"""
        if not self.enabled:
            return None
        
        url = f"{self.config['base_url']}{endpoint}"
        attempts = 0
        max_attempts = self.config["retry_attempts"] if retry else 1
        
        while attempts < max_attempts:
            try:
                response = self.session.request(
                    method=method,
                    url=url,
                    json=data,
                    params=params,
                    timeout=self.config["timeout"]
                )
                
                if response.status_code == 200:
                    return response.json()
                elif response.status_code == 401:
                    print(f"[PORTIA] Authentication failed - check API key")
                    return None
                elif response.status_code == 429:
                    print(f"[PORTIA] Rate limited - waiting before retry")
                    time.sleep(2 ** attempts)  # Exponential backoff
                else:
                    print(f"[PORTIA] API request failed: {response.status_code} - {response.text}")
                    if not retry:
                        return None
                
            except requests.exceptions.Timeout:
                print(f"[PORTIA] Request timeout (attempt {attempts + 1}/{max_attempts})")
            except requests.exceptions.RequestException as e:
                print(f"[PORTIA] Request error: {e}")
            
            attempts += 1
            if attempts < max_attempts:
                time.sleep(1)  # Wait before retry
        
        print(f"[PORTIA] All {max_attempts} attempts failed")
        return None
    
    def create_monitor(self, name: str, url: str, check_interval: int = 60, 
                      alert_channels: Optional[List[str]] = None) -> Optional[Dict]:
        """Create a new monitoring endpoint"""
        endpoint = self.config["endpoints"]["monitor_create"]
        
        data = {
            "name": name,
            "url": url,
            "check_interval": check_interval,
            "alert_channels": alert_channels or ["telegram"],
            "created_at": datetime.now().isoformat()
        }
        
        result = self._make_request("POST", endpoint, data=data)
        if result:
            print(f"[PORTIA] Monitor created: {name} -> {url}")
        return result
    
    def update_monitor(self, monitor_id: str, **kwargs) -> Optional[Dict]:
        """Update an existing monitor"""
        endpoint = self.config["endpoints"]["monitor_update"]
        
        data = {
            "monitor_id": monitor_id,
            "updated_at": datetime.now().isoformat(),
            **kwargs
        }
        
        result = self._make_request("PUT", endpoint, data=data)
        if result:
            print(f"[PORTIA] Monitor updated: {monitor_id}")
        return result
    
    def delete_monitor(self, monitor_id: str) -> bool:
        """Delete a monitor"""
        endpoint = self.config["endpoints"]["monitor_delete"]
        
        data = {"monitor_id": monitor_id}
        result = self._make_request("DELETE", endpoint, data=data)
        
        if result:
            print(f"[PORTIA] Monitor deleted: {monitor_id}")
            return True
        return False
    
    def list_monitors(self) -> Optional[List[Dict]]:
        """List all monitors"""
        endpoint = self.config["endpoints"]["monitor_list"]
        
        result = self._make_request("GET", endpoint)
        if result:
            monitors = result.get("monitors", [])
            print(f"[PORTIA] Found {len(monitors)} monitors")
            return monitors
        return None
    
    def get_monitor_status(self, monitor_id: str) -> Optional[Dict]:
        """Get current status of a monitor"""
        endpoint = self.config["endpoints"]["monitor_status"]
        
        params = {"monitor_id": monitor_id}
        result = self._make_request("GET", endpoint, params=params)
        
        if result:
            status = result.get("status", "unknown")
            print(f"[PORTIA] Monitor {monitor_id} status: {status}")
        return result
    
    def create_incident(self, monitor_id: str, title: str, description: str, 
                       severity: str = "medium", status: str = "open") -> Optional[Dict]:
        """Create a new incident"""
        endpoint = self.config["endpoints"]["create_incident"]
        
        data = {
            "monitor_id": monitor_id,
            "title": title,
            "description": description,
            "severity": severity,
            "status": status,
            "created_at": datetime.now().isoformat(),
            "source": "portia-uptime-agent"
        }
        
        result = self._make_request("POST", endpoint, data=data)
        if result:
            incident_id = result.get("incident_id")
            print(f"[PORTIA] Incident created: {incident_id} - {title}")
        return result
    
    def update_incident(self, incident_id: str, **kwargs) -> Optional[Dict]:
        """Update an incident"""
        endpoint = self.config["endpoints"]["update_incident"]
        
        data = {
            "incident_id": incident_id,
            "updated_at": datetime.now().isoformat(),
            **kwargs
        }
        
        result = self._make_request("PUT", endpoint, data=data)
        if result:
            print(f"[PORTIA] Incident updated: {incident_id}")
        return result
    
    def get_incident(self, incident_id: str) -> Optional[Dict]:
        """Get incident details"""
        endpoint = self.config["endpoints"]["get_incident"]
        
        params = {"incident_id": incident_id}
        result = self._make_request("GET", endpoint, params=params)
        
        if result:
            title = result.get("title", "Unknown")
            print(f"[PORTIA] Retrieved incident: {incident_id} - {title}")
        return result
    
    def list_incidents(self, monitor_id: Optional[str] = None, 
                      status: Optional[str] = None, limit: int = 50) -> Optional[List[Dict]]:
        """List incidents with optional filtering"""
        endpoint = self.config["endpoints"]["list_incidents"]
        
        params = {"limit": limit}
        if monitor_id:
            params["monitor_id"] = monitor_id
        if status:
            params["status"] = status
        
        result = self._make_request("GET", endpoint, params=params)
        if result:
            incidents = result.get("incidents", [])
            print(f"[PORTIA] Found {len(incidents)} incidents")
            return incidents
        return None
    
    def report_incident(self, url: str, incident_data: Dict) -> bool:
        """Report an incident to Portia API"""
        endpoint = self.config["endpoints"]["incident_report"]
        
        payload = {
            "url": url,
            "incident": incident_data,
            "timestamp": datetime.now().isoformat(),
            "agent": "portia-uptime-agent",
            "version": "1.0.0"
        }
        
        result = self._make_request("POST", endpoint, data=payload)
        if result:
            print(f"[PORTIA] Incident report sent successfully for {url}")
            return True
        else:
            print(f"[PORTIA] Failed to send incident report for {url}")
            return False
    
    def get_enhanced_monitoring_data(self, url: str) -> Optional[Dict]:
        """Get enhanced monitoring data for a URL"""
        # This would integrate with Portia's monitoring data
        # For now, return basic structure
        return {
            "url": url,
            "portia_data": {
                "monitor_id": None,
                "last_check": datetime.now().isoformat(),
                "uptime_percentage": None,
                "average_response_time": None,
                "incident_count": 0
            }
        }
    
    def health_check(self) -> bool:
        """Check if Portia API is accessible"""
        try:
            # Try to list monitors as a health check
            result = self.list_monitors()
            return result is not None
        except Exception as e:
            print(f"[PORTIA] Health check failed: {e}")
            return False
    
    def get_api_info(self) -> Optional[Dict]:
        """Get Portia API information"""
        try:
            # This would be a dedicated endpoint in the real API
            return {
                "api_version": "v1",
                "base_url": self.config["base_url"],
                "endpoints": list(self.config["endpoints"].keys()),
                "features": {
                    "monitoring": True,
                    "incident_management": True,
                    "alerting": True,
                    "webhooks": bool(self.config.get("webhook_url"))
                }
            }
        except Exception as e:
            print(f"[PORTIA] Failed to get API info: {e}")
            return None

# Convenience functions for easy access
def get_portia_client() -> PortiaSDK:
    """Get a configured Portia SDK client"""
    return PortiaSDK()

def test_portia_connection() -> bool:
    """Test Portia API connection"""
    client = get_portia_client()
    if not client.enabled:
        return False
    
    return client.health_check()

if __name__ == "__main__":
    # Test the SDK
    print("🔌 Portia SDK Test")
    print("=" * 50)
    
    client = get_portia_client()
    if client.enabled:
        print("✅ SDK initialized successfully")
        
        # Test connection
        if client.health_check():
            print("✅ API connection successful")
            
            # Get API info
            info = client.get_api_info()
            if info:
                print(f"✅ API Version: {info['api_version']}")
                print(f"✅ Endpoints: {len(info['endpoints'])} available")
        else:
            print("❌ API connection failed")
    else:
        print("❌ SDK disabled - check configuration")
