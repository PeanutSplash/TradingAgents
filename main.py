from dotenv import load_dotenv
from tradingagents.graph.trading_graph import TradingAgentsGraph
from tradingagents.default_config import DEFAULT_CONFIG

# Load environment variables at application entrypoint
load_dotenv()

# Create a custom config
config = DEFAULT_CONFIG.copy()
config["llm_provider"] = "google"  # Use Google for LLM
config["backend_url"] = "https://generativelanguage.googleapis.com/v1beta/openai/"  # Google backend
config["deep_think_llm"] = "gemini-2.5-pro"  # Use Google model
config["quick_think_llm"] = "gemini-2.5-flash-lite-preview-06-17"  # Use Google model
# Embedding configuration - can use different provider than LLM
config["embedding_provider"] = "google"  # Use Google for embeddings
config["embedding_model"] = "text-embedding-004"  # Google embedding model
config["embedding_backend_url"] = "https://generativelanguage.googleapis.com/v1beta/openai/"  # Google embedding backend
config["max_debate_rounds"] = 1  # Increase debate rounds
config["online_tools"] = True  # Use online tools

# Initialize with custom config
ta = TradingAgentsGraph(debug=True, config=config)

# forward propagate
_, decision = ta.propagate("NVDA", "2024-05-10")
print(decision)

# Memorize mistakes and reflect
# ta.reflect_and_remember(1000) # parameter is the position returns
