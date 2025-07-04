# TradingAgents Configuration Guide

This document provides a comprehensive guide to configuring TradingAgents for different use cases and providers.

## 📋 Configuration Overview

TradingAgents supports flexible configuration through the `DEFAULT_CONFIG` dictionary. You can customize:

- **LLM Providers**: OpenAI, Google, Anthropic, OpenRouter, Ollama
- **Embedding Providers**: OpenAI, Google, Ollama (can be different from LLM provider)
- **Model Selection**: Choose specific models for different tasks
- **Trading Parameters**: Debate rounds, risk management settings
- **Data Sources**: Online tools vs cached data

## 🔧 Core Configuration Options

### Directory Settings
```python
config = {
    "project_dir": "/path/to/project",           # Project root directory
    "results_dir": "./results",                  # Output directory for results
    "data_dir": "/path/to/data",                # Financial data directory
    "data_cache_dir": "./dataflows/data_cache", # Cache directory
}
```

### LLM Configuration
```python
config = {
    "llm_provider": "openai",                    # openai, google, anthropic, openrouter, ollama
    "backend_url": "https://api.openai.com/v1", # API endpoint
    "deep_think_llm": "o4-mini",                # Model for complex reasoning
    "quick_think_llm": "gpt-4o-mini",           # Model for quick tasks
}
```

### Embedding Configuration (New!)
```python
config = {
    "embedding_provider": "openai",              # openai, google, ollama
    "embedding_model": "text-embedding-3-small", # Specific embedding model
    "embedding_backend_url": None,               # Custom endpoint (optional)
}
```

### Trading Strategy Settings
```python
config = {
    "max_debate_rounds": 1,                      # Agent debate iterations
    "max_risk_discuss_rounds": 1,                # Risk management discussions
    "max_recur_limit": 100,                      # Maximum recursion depth
    "online_tools": True,                        # Use real-time data vs cached
}
```

## 🚀 Configuration Examples

### Example 1: OpenAI Everything (Default)
```python
from tradingagents.default_config import DEFAULT_CONFIG

config = DEFAULT_CONFIG.copy()
# Uses OpenAI for both LLM and embeddings
```

### Example 2: Google Everything
```python
config = DEFAULT_CONFIG.copy()
config["llm_provider"] = "google"
config["backend_url"] = "https://generativelanguage.googleapis.com/v1beta/openai/"
config["deep_think_llm"] = "gemini-2.5-pro"
config["quick_think_llm"] = "gemini-2.5-flash-lite-preview-06-17"
config["embedding_provider"] = "google"
config["embedding_model"] = "text-embedding-004"
```

### Example 3: Mixed Providers (Cost Optimization)
```python
config = DEFAULT_CONFIG.copy()
# Use Google for LLM (cost-effective)
config["llm_provider"] = "google"
config["backend_url"] = "https://generativelanguage.googleapis.com/v1beta/openai/"
config["deep_think_llm"] = "gemini-2.5-flash-lite-preview-06-17"
config["quick_think_llm"] = "gemini-2.5-flash-lite-preview-06-17"
# Use OpenAI for embeddings (higher quality)
config["embedding_provider"] = "openai"
config["embedding_model"] = "text-embedding-3-large"
config["embedding_backend_url"] = "https://api.openai.com/v1"
```

### Example 4: Local Development with Ollama
```python
config = DEFAULT_CONFIG.copy()
config["llm_provider"] = "ollama"
config["backend_url"] = "http://localhost:11434/v1"
config["deep_think_llm"] = "llama3.1"
config["quick_think_llm"] = "llama3.2"
config["embedding_provider"] = "ollama"
config["embedding_model"] = "nomic-embed-text"
```

### Example 5: Hybrid Setup (Local LLM + Cloud Embeddings)
```python
config = DEFAULT_CONFIG.copy()
# Local LLM for cost savings
config["llm_provider"] = "ollama"
config["backend_url"] = "http://localhost:11434/v1"
config["deep_think_llm"] = "llama3.1"
config["quick_think_llm"] = "llama3.2"
# Cloud embeddings for quality
config["embedding_provider"] = "openai"
config["embedding_model"] = "text-embedding-3-small"
config["embedding_backend_url"] = "https://api.openai.com/v1"
```

## 🔑 Environment Variables

Create a `.env` file with your API keys:

```bash
# Required for OpenAI models
OPENAI_API_KEY=your_openai_api_key_here

# Required for Google models
GOOGLE_API_KEY=your_google_api_key_here

# Required for financial data
FINNHUB_API_KEY=your_finnhub_api_key_here

# Optional: Custom results directory
TRADINGAGENTS_RESULTS_DIR=./custom_results
```

## 📊 Model Recommendations

### For Production (High Quality)
```python
config["deep_think_llm"] = "o3-mini"           # OpenAI reasoning model
config["quick_think_llm"] = "gpt-4o"           # OpenAI standard model
config["embedding_model"] = "text-embedding-3-large"  # High-quality embeddings
```

### For Development (Cost Effective)
```python
config["deep_think_llm"] = "gpt-4o-mini"       # Cheaper OpenAI model
config["quick_think_llm"] = "gpt-4o-mini"      # Same for consistency
config["embedding_model"] = "text-embedding-3-small"  # Cost-effective embeddings
```

### For Local Development
```python
config["deep_think_llm"] = "llama3.1"          # Local Ollama model
config["quick_think_llm"] = "llama3.2"         # Faster local model
config["embedding_model"] = "nomic-embed-text" # Local embeddings
```

## 🎯 Performance Tuning

### High-Quality Analysis
```python
config["max_debate_rounds"] = 3                 # More thorough analysis
config["max_risk_discuss_rounds"] = 2           # Enhanced risk assessment
config["online_tools"] = True                   # Real-time data
```

### Fast Analysis
```python
config["max_debate_rounds"] = 1                 # Quick decisions
config["max_risk_discuss_rounds"] = 1           # Basic risk check
config["online_tools"] = False                  # Use cached data
```

## 🐳 Docker Configuration

When using Docker, pass environment variables:

```bash
# Build image
docker build -t trading-app .

# Run with environment file
docker run --rm -it --env-file ./.env \
  -v "$(pwd)/results_dir:/app/results_dir" \
  trading-app python -m cli.main
```

## 🔧 CLI Configuration

The CLI now supports embedding configuration through interactive prompts:

1. **Step 5**: Select LLM Provider
2. **Step 7**: Configure Embedding Provider (New!)
   - Choose same as LLM or different provider
   - Select specific embedding model
   - Configure custom endpoints

## 💡 Best Practices

1. **Cost Optimization**: Use local models for development, cloud for production
2. **Quality vs Speed**: Balance model quality with response time needs
3. **Mixed Providers**: Combine cost-effective LLMs with high-quality embeddings
4. **Environment Security**: Never commit API keys to version control
5. **Resource Management**: Monitor API usage and costs

## 🚨 Troubleshooting

### Common Issues

1. **API Key Errors**: Ensure all required API keys are set in `.env`
2. **Model Not Found**: Verify model names match provider specifications
3. **Connection Errors**: Check backend URLs and network connectivity
4. **Local Ollama**: Ensure Ollama server is running for local models

### Debug Mode

Enable debug mode for detailed logging:
```python
ta = TradingAgentsGraph(debug=True, config=config)
```

## 📚 Additional Resources

- [OpenAI Models](https://platform.openai.com/docs/models)
- [Google AI Models](https://ai.google.dev/models)
- [Ollama Models](https://ollama.ai/library)
- [FinnHub API](https://finnhub.io/docs/api)
