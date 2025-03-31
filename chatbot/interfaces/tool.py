"""Interface definition for tools."""

from abc import ABC, abstractmethod

class Tool(ABC):
    """Abstract base class for tools that can be used by an LLM."""
    
    @property
    @abstractmethod
    def definition(self):
        """Get the tool definition in the format required by the LLM API."""
        pass
    
    @abstractmethod
    def execute(self, arguments):
        """Execute the tool with the provided arguments."""
        pass