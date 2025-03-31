"""Configuration settings."""

# API Configuration
ANTHROPIC_API_KEY = "sk-..."
CLAUDE_MODEL = "claude-3-5-haiku-latest"

# System Prompt
SYSTEM_PROMPT = """
You are a helpful AI assistant that answers questions on Telerik UI components for Blazor.
You use tools to help you answer questions easily and when no tools are suitable you shortly explain that the question is beyound your capabilities.
User questions are divided into two main groups:
1. Finding, explaining and demonstrating a suitable component for the user need
2. Troubleshooting user issues
"""

# CLI Configuration
CLI_PROMPT = "You> "
EXIT_COMMANDS = ["exit", "quit", "q", "bye"]
DEBUG_COMMANDS = ["debug", "show messages"]

# Tool Configuration
TOOLS = [
    "documentation_search",
    "forum_search"
]

# Messages
TOOL_INVOCATION_MSG = "Invoking tool: {}"
ERROR_NO_ANTHROPIC_API_KEY = "Error: ANTHROPIC_API_KEY not set."
ERROR_GENERAL = "An error occurred: {}"

# Similarity search
EMBEDDING_MODEL_NAME = "nomic-embed-text"
PINECONE_API_KEY = "pcsk_..."
PINECONE_INDEX_NAME = "blazor-docs"
PINECONE_NAMESPACE = "test"
BASE_DIR = "" # where the bazel-docs repo is, e.g "C:\Users\{username]\Projects\blazor-docs"
TOP_RESULTS = 1 # more are currently non-supported