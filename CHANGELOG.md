# Changelog - Portia Uptime Agent

## [2.0.0] - 2024-12-19

### 🚀 Major Changes

- **Removed Groq API integration** - No longer supported
- **Removed Ollama integration** - No longer supported  
- **Removed Hugging Face integration** - No longer supported
- **Removed Portia AI integration** - No longer supported
- **Simplified to Google AI Studio only** - Now the sole AI provider

### ✨ New Features

- **Google AI Studio (Gemini) integration** - Primary AI provider for uptime analysis
- **Simplified configuration** - Only requires Google AI API key
- **Streamlined codebase** - Removed unnecessary complexity

### 🔧 Code Changes

- **main.py**: Completely rewritten to only use Google AI Studio
- **env_template.txt**: Simplified to only include Google AI configuration
- **requirements.txt**: Removed unnecessary dependencies (groq, schedule)
- **install_googleai.py**: New installation script for Google AI dependencies
- **test_googleai.py**: New test script for Google AI integration
- **monitor_continuous.py**: New simple continuous monitoring script

### 🗑️ Removed Files

- `install_groq.py` - Groq installation script
- `monitor.py` - Complex monitoring script
- `test_all.py` - Comprehensive test suite
- `test_groq.py` - Groq test script

### 📚 Documentation Updates

- **README.md**: Updated to reflect Google AI-only approach
- Removed all references to multiple AI providers
- Simplified setup instructions
- Updated project structure
- Updated dependencies list

### 🎯 Benefits

- **Simpler setup** - Only one AI provider to configure
- **Cleaner code** - Removed unused AI provider code
- **Better maintainability** - Single AI integration to maintain
- **Focused functionality** - Google AI Studio is powerful and reliable

### 📋 Migration Guide

1. **Update environment variables**:
   - Remove: `AI_PROVIDER`, `GROQ_API_KEY`, `OLLAMA_BASE_URL`, `HUGGINGFACE_API_KEY`
   - Keep: `GOOGLE_AI_API_KEY`, `MONITORED_URL`, `TELEGRAM_BOT_TOKEN`, `TELEGRAM_CHAT_ID`

2. **Install new dependencies**:

   ```bash
   python install_googleai.py
   ```

3. **Test the new setup**:

   ```bash
   python test_googleai.py
   python main.py
   ```

4. **For continuous monitoring**:

   ```bash
   python monitor_continuous.py
   ```

### 🔑 Required Configuration

- `GOOGLE_AI_API_KEY`: Your Google AI Studio API key from <https://aistudio.google.com/app/u/0/apikey>
- `MONITORED_URL`: The website you want to monitor
- `TELEGRAM_BOT_TOKEN`: Your Telegram bot token
- `TELEGRAM_CHAT_ID`: Your Telegram chat ID

### 📝 Notes

- The system still includes fallback to direct HTTP monitoring if Google AI fails
- All existing Telegram functionality remains unchanged
- Monitoring intervals can still be configured via `MONITORING_INTERVAL` environment variable
