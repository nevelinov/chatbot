"""Claude LLM implementation."""

import anthropic
from interfaces.llm import LLM
import config

class Claude(LLM):
    """Implementation of the LLM interface for Anthropic's Claude."""
    
    def __init__(self, api_key=None, model=None, system_prompt=None):
        """Initialize the Claude client."""
        self.api_key = api_key or config.ANTHROPIC_API_KEY
        self.model = model or config.CLAUDE_MODEL
        self.system_prompt = system_prompt or "You are a helpful AI assistant that always uses tools when possible. Never rely on your general knowledge when a tool can be used instead."
        self.client = anthropic.Anthropic(api_key=self.api_key)
    
    def generate_response(self, prompt, conversation_history=None):
        """Generate a text response from Claude."""
        messages = self._format_conversation_history(conversation_history)
        messages.append({"role": "user", "content": prompt})
        
        response = self.client.messages.create(
            model=self.model,
            messages=messages,
            max_tokens=1000,
            system=self.system_prompt
        )
        
        return response.content[0].text
    
    def generate_response_with_tools(self, prompt, tools, conversation_history=None):
        """Generate a response that may include tool use."""
        messages = self._format_conversation_history(conversation_history)
        messages.append({"role": "user", "content": prompt})
        
        response = self.client.messages.create(
            model=self.model,
            messages=messages,
            max_tokens=1000,
            tools=tools,
            system=self.system_prompt
        )
        
        # Check if the response indicates tool use
        if response.stop_reason == 'tool_use' and hasattr(response, 'content'):
            # Find the tool_use block in the content
            for block in response.content:
                if block.type == 'tool_use':
                    return {
                        "type": "tool_call",
                        "tool_name": block.name,
                        "arguments": block.input,
                        "text_response": next((b.text for b in response.content if b.type == 'text'), "")
                    }
        
        # Otherwise, return the text response
        return {
            "type": "text",
            "content": response.content[0].text if response.content else ""
        }
    
    def _format_conversation_history(self, conversation_history=None):
        """Format the conversation history for Claude API."""
        if not conversation_history:
            return []
        
        formatted_messages = []
        for message in conversation_history:
            # Handle tool results from previous interactions
            if message.get("type") == "tool_result":
                formatted_messages.append({
                    "role": "user",
                    "content": [
                        {
                            "type": "tool_result",
                            "tool_name": message.get("tool_name"),
                            "content": message.get("content")
                        }
                    ]
                })
            else:
                formatted_messages.append({
                    "role": message["role"],
                    "content": message["content"]
                })
        
        return formatted_messages