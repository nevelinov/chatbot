"""Interface definition for LLM providers."""

from abc import ABC, abstractmethod

class LLM(ABC):
    """Abstract base class for LLM providers."""
    
    @abstractmethod
    def generate_response(self, prompt, conversation_history=None):
        """Generate a response based on the provided prompt and conversation history."""
        pass
    
    @abstractmethod
    def generate_response_with_tools(self, prompt, tools, conversation_history=None):
        """Generate a response based on the provided prompt, tools and conversation history."""
        pass