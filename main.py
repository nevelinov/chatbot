"""Main module for the LLM Chatbot application."""

import sys

import config

from cli import run_cli

from llms.claude import Claude

from tools.documentation_search import DocumentationSearchTool
from tools.forum_search import ForumSearchTool

def init_llm():
    """Initialize the LLM client."""
    return Claude(
        api_key=config.ANTHROPIC_API_KEY, 
        model=config.CLAUDE_MODEL,
        system_prompt=config.SYSTEM_PROMPT
    )

def init_tools():
    """Initialize all available tools."""
    tool_instances = []
    
    if "documentation_search" in config.TOOLS:
        tool_instances.append(DocumentationSearchTool())
    
    if "forum_search" in config.TOOLS:
        tool_instances.append(ForumSearchTool())
    
    return tool_instances

def get_tool_definitions(tools):
    """Get tool definitions for the LLM API."""
    return [tool.definition for tool in tools]

def get_tool_by_name(tools, name):
    """Get a tool instance by name."""
    for tool in tools:
        if tool.definition["name"] == name:
            return tool
    return None

def process_query(llm, tools, query, history):
    """Process a user query using the LLM and tools."""
    tool_definitions = get_tool_definitions(tools)
    
    # Get initial response from LLM
    response = llm.generate_response_with_tools(query, tool_definitions, history)
    
    # If the LLM wants to use a tool
    if response["type"] == "tool_call":
        tool_name = response["tool_name"]
        tool_args = response["arguments"]
        
        # Print tool invocation message
        print(config.TOOL_INVOCATION_MSG.format(tool_name))
        
        # Find and execute the tool
        tool = get_tool_by_name(tools, tool_name)
        if tool:
            tool_result = tool.execute(tool_args)
            
            # Update history with the tool call and result
            history.append({"role": "user", "content": query})
            history.append({"role": "assistant", "content": f"I'll use the {tool_name} tool to answer."})
            history.append({"role": "user", "content": f"Tool result: {tool_result}"})
            
            # Get final response from LLM with the tool result
            final_response = llm.generate_response(
                f"Based on the result from the {tool_name} tool ({tool_result}), "
                f"provide a helpful response to the original query: {query}", 
                history
            )
            return final_response
        else:
            return f"Error: Tool '{tool_name}' not found."
    else:
        print(response)
        # LLM didn't use a tool, return its response
        return "I don't have the knowledge to answer this question."

def main():
    """Main entry point for the application."""
    try:
        # Initialize LLM and tools
        llm = init_llm()
        tools = init_tools()
        
        # Start the CLI
        run_cli(process_query, llm, tools)
        
    except Exception as e:
        print(config.ERROR_GENERAL.format(str(e)))
        sys.exit(1)

if __name__ == "__main__":
    main()