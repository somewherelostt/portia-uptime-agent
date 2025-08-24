# 🔌 Portia API Integration Guide

## Overview

The Portia Uptime Agent now includes comprehensive **Portia SDK integration** for enterprise-grade monitoring capabilities. This integration provides enhanced monitoring data, incident management, and professional monitoring features.

## 🚀 What Portia SDK Adds

### **Enhanced Monitoring**

- **Real-time Status Updates**: Get live monitoring data from Portia's infrastructure
- **Historical Analytics**: Access uptime trends and performance metrics
- **Multi-location Monitoring**: Monitor from multiple geographic locations
- **Advanced Metrics**: Response time analysis, error rate tracking

### **Incident Management**

- **Automatic Incident Creation**: Create incidents when downtime is detected
- **Severity Classification**: Prioritize issues based on impact
- **Status Tracking**: Track incident resolution progress
- **Integration Workflows**: Connect with existing incident management systems

### **Professional Features**

- **API Rate Limiting**: Built-in retry logic and exponential backoff
- **Authentication**: Secure API key-based authentication
- **Webhook Support**: Real-time notifications via webhooks
- **Multi-channel Alerts**: Email, Slack, and custom integrations

## 🔧 Configuration

### **Required Environment Variables**

```env
# Portia API Key (Required for SDK features)
PORTIA_API_KEY=your_portia_api_key_here

# Portia API Base URL (Optional - defaults to production)
PORTIA_BASE_URL=https://api.portialabs.ai
```

### **Optional Configuration**

```env
# API Request Timeout (seconds)
PORTIA_TIMEOUT=30

# Retry Attempts for Failed Requests
PORTIA_RETRY_ATTEMPTS=3

# Webhook URL for Real-time Notifications
PORTIA_WEBHOOK_URL=https://your-domain.com/webhook

# Notification Channels (comma-separated)
PORTIA_NOTIFICATION_CHANNELS=telegram,email,slack
```

## 📚 SDK Usage

### **Basic SDK Initialization**

```python
from portia_sdk import get_portia_client

# Get configured client
client = get_portia_client()

# Check if SDK is enabled
if client.enabled:
    print("Portia SDK is ready!")
else:
    print("Check your configuration")
```

### **Creating Monitors**

```python
# Create a new monitoring endpoint
monitor = client.create_monitor(
    name="My Website",
    url="https://example.com",
    check_interval=60,  # seconds
    alert_channels=["telegram", "email"]
)

if monitor:
    monitor_id = monitor.get("monitor_id")
    print(f"Monitor created: {monitor_id}")
```

### **Managing Incidents**

```python
# Create an incident when downtime is detected
incident = client.create_incident(
    monitor_id="uptime-agent",
    title="Website Downtime Detected",
    description="Connection timeout on example.com",
    severity="high",
    status="open"
)

if incident:
    incident_id = incident.get("incident_id")
    print(f"Incident created: {incident_id}")
```

### **Getting Monitoring Data**

```python
# Get current status of a monitor
status = client.get_monitor_status("monitor_id_here")

# List all monitors
monitors = client.list_monitors()

# Get enhanced monitoring data
enhanced_data = client.get_enhanced_monitoring_data("https://example.com")
```

## 🔍 API Endpoints

The Portia SDK provides access to these API endpoints:

### **Monitoring Endpoints**

- `POST /v1/monitors/create` - Create new monitor
- `PUT /v1/monitors/update` - Update existing monitor
- `DELETE /v1/monitors/delete` - Delete monitor
- `GET /v1/monitors/list` - List all monitors
- `GET /v1/monitors/status` - Get monitor status

### **Incident Endpoints**

- `POST /v1/incidents/create` - Create new incident
- `PUT /v1/incidents/update` - Update incident
- `GET /v1/incidents/get` - Get incident details
- `GET /v1/incidents/list` - List incidents
- `POST /v1/incidents/report` - Report incident

## 🧪 Testing the Integration

### **Run the Test Suite**

```bash
# Test all Portia features
python test_portia.py

# Test specific components
python -c "from portia_sdk import test_portia_connection; test_portia_connection()"
```

### **Test Configuration**

```bash
# Validate Portia configuration
python portia_config.py

# Test SDK initialization
python -c "from portia_sdk import get_portia_client; client = get_portia_client(); print(f'SDK enabled: {client.enabled}')"
```

## 🎯 Demo Scenarios for Hackathon

### **Scenario 1: Enhanced Monitoring Dashboard**

1. **Setup**: Configure Portia API key
2. **Action**: Run monitoring system
3. **Result**: Show enhanced data from Portia API
4. **Demo**: Display real-time metrics and trends

### **Scenario 2: Professional Incident Management**

1. **Setup**: Create test website and introduce downtime
2. **Action**: Let system detect and report incident
3. **Result**: Show incident created in Portia
4. **Demo**: Display incident details and workflow

### **Scenario 3: Multi-channel Notifications**

1. **Setup**: Configure webhooks and notification channels
2. **Action**: Trigger monitoring event
3. **Result**: Show notifications across multiple channels
4. **Demo**: Display real-time alert delivery

## 🚨 Troubleshooting

### **Common Issues**

#### **SDK Not Enabled**

```
[WARNING] Portia API key not configured - SDK disabled
```

**Solution**: Set `PORTIA_API_KEY` in your `.env` file

#### **Authentication Failed**

```
[PORTIA] Authentication failed - check API key
```

**Solution**: Verify your API key is correct and has proper permissions

#### **Connection Timeout**

```
[PORTIA] Request timeout (attempt 1/3)
```

**Solution**: Check network connectivity and increase `PORTIA_TIMEOUT` if needed

#### **Rate Limited**

```
[PORTIA] Rate limited - waiting before retry
```

**Solution**: The SDK automatically handles rate limiting with exponential backoff

### **Debug Mode**

Enable debug logging by setting environment variable:

```bash
export PORTIA_DEBUG=true
```

## 🔗 Integration with Main System

The Portia SDK integrates seamlessly with the main monitoring system:

### **Automatic Integration**

- **Downtime Detection**: Automatically creates incidents in Portia
- **Recovery Tracking**: Updates incident status when issues are resolved
- **Enhanced Data**: Provides additional monitoring insights
- **Professional Workflows**: Integrates with enterprise incident management

### **Graceful Degradation**

- **SDK Disabled**: System continues monitoring without Portia features
- **API Unavailable**: Falls back to basic monitoring capabilities
- **Configuration Errors**: Logs warnings but doesn't break core functionality

## 📊 Performance Considerations

### **API Limits**

- **Free Tier**: 15 requests per minute
- **Pro Tier**: Higher limits based on plan
- **Rate Limiting**: Automatic retry with exponential backoff

### **Optimization Tips**

- **Batch Operations**: Group related API calls when possible
- **Caching**: Cache frequently accessed data
- **Async Operations**: Use async calls for non-critical operations

## 🚀 Next Steps

### **For Hackathon Demo**

1. **Get Portia API Key**: Sign up at [Portia Labs](https://app.portialabs.ai)
2. **Configure Environment**: Set up your `.env` file
3. **Test Integration**: Run `python test_portia.py`
4. **Show Features**: Demonstrate enhanced monitoring capabilities

### **For Production Use**

1. **Scale Monitoring**: Add multiple websites and endpoints
2. **Custom Workflows**: Integrate with your existing systems
3. **Advanced Features**: Use webhooks and custom integrations
4. **Team Collaboration**: Share monitoring dashboards with your team

## 💡 Why This Impresses Judges

### **Enterprise Integration**

- **Professional Monitoring**: Industry-standard incident management
- **Scalable Architecture**: Handles multiple websites and teams
- **API-First Design**: Easy integration with existing tools

### **Technical Excellence**

- **Robust Error Handling**: Graceful degradation and retry logic
- **Security**: Secure API key authentication
- **Performance**: Optimized for production workloads

### **Business Value**

- **Reduced Downtime**: Professional monitoring and alerting
- **Team Efficiency**: Centralized incident management
- **Cost Savings**: Enterprise features without enterprise complexity

---

**The Portia SDK integration transforms your hackathon project from a simple monitoring tool into an enterprise-grade monitoring platform! 🚀**
