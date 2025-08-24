import os
import requests
from dotenv import load_dotenv

def test_telegram_connection():
    """Test Telegram bot connectivity and send a test message"""
    print("[TEST] Testing Telegram Bot Connection...")
    print("-" * 50)
    
    # Load environment variables
    load_dotenv()
    
    TELEGRAM_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
    TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")
    
    # Check if credentials are set
    if not TELEGRAM_TOKEN:
        print("[ERROR] TELEGRAM_BOT_TOKEN not found in .env file")
        print("   Please set it in your .env file")
        return False
        
    if not TELEGRAM_CHAT_ID:
        print("[ERROR] TELEGRAM_CHAT_ID not found in .env file")
        print("   Please set it in your .env file")
        return False
    
    print(f"[SUCCESS] Bot Token: {TELEGRAM_TOKEN[:10]}...{TELEGRAM_TOKEN[-4:]}")
    print(f"[SUCCESS] Chat ID: {TELEGRAM_CHAT_ID}")
    
    # Test the connection
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    test_message = "🧪 Test message from Portia Uptime Agent\n\nIf you see this, your Telegram bot is working correctly!"
    
    try:
        print("\n[SEND] Sending test message...")
        resp = requests.post(
            url, 
            data={
                "chat_id": TELEGRAM_CHAT_ID, 
                "text": test_message
            }, 
            timeout=10
        )
        
        if resp.status_code == 200:
            print("[SUCCESS] Test message sent successfully!")
            print("[SUCCESS] Telegram bot is working correctly")
            return True
        else:
            print(f"[ERROR] Failed to send message: {resp.status_code}")
            print(f"   Response: {resp.text}")
            return False
            
    except requests.exceptions.Timeout:
        print("[ERROR] Request timed out - check your internet connection")
        return False
    except requests.exceptions.RequestException as e:
        print(f"[ERROR] Request failed: {e}")
        return False
    except Exception as e:
        print(f"[ERROR] Unexpected error: {e}")
        return False

def get_bot_info():
    """Get information about the bot"""
    load_dotenv()
    TELEGRAM_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
    
    if not TELEGRAM_TOKEN:
        print("[ERROR] TELEGRAM_BOT_TOKEN not set")
        return
    
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/getMe"
    
    try:
        resp = requests.get(url, timeout=10)
        if resp.status_code == 200:
            bot_info = resp.json()
            if bot_info.get('ok'):
                bot_data = bot_info['result']
                print(f"\n[BOT] Bot Information:")
                print(f"   Name: {bot_data.get('first_name', 'N/A')}")
                print(f"   Username: @{bot_data.get('username', 'N/A')}")
                print(f"   ID: {bot_data.get('id', 'N/A')}")
                print(f"   Can Join Groups: {bot_data.get('can_join_groups', 'N/A')}")
                print(f"   Can Read Messages: {bot_data.get('can_read_all_group_messages', 'N/A')}")
            else:
                print("[ERROR] Failed to get bot info")
        else:
            print(f"[ERROR] Failed to get bot info: {resp.status_code}")
    except Exception as e:
        print(f"[ERROR] Error getting bot info: {e}")

if __name__ == "__main__":
    print("[START] Portia Uptime Agent - Telegram Test")
    print("=" * 50)
    
    # Test connection
    success = test_telegram_connection()
    
    if success:
        print("\n" + "=" * 50)
        get_bot_info()
        print("\n[SUCCESS] All tests passed! Your Telegram bot is ready to use.")
    else:
        print("\n[ERROR] Telegram test failed. Please check your configuration.")
        print("\n[SETUP] Setup Instructions:")
        print("1. Create a bot with @BotFather on Telegram")
        print("2. Get your bot token and chat ID")
        print("3. Copy env_template.txt to .env")
        print("4. Fill in your credentials in .env")
        print("5. Run this test again")
