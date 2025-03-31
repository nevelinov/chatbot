"""Forum search tool."""

from interfaces.tool import Tool
import random

class ForumSearchTool(Tool):
    """Tool for searching forum posts and discussions."""
    
    @property
    def definition(self):
        """Get the tool definition for Claude API."""
        return {
            "name": "forum_search",
            "description": "Search for similar issues, discussions and posts in Telerik UI for Blazor forum. Should be used for troubleshooting issues related to Telerik Blazor UI components for Blazor. Should not be used for general documentation of Telerik UI components for Blazor.",
            "input_schema": {
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                        "description": "The search query to find relevant forum discussions"
                    }
                },
                "required": ["query"]
            }
        }
    
    def execute(self, arguments):
        """
        Execute the forum search with the provided query.
        Due to scraping restrictions in the forum
        the tool is hardcoded to work just for a few queries.
        """
        query = arguments.get("query", "").strip()

        if self.contains_all_words(query, "ai prompt"):
            with open("./resources/ai_prompt.md", 'r', encoding='utf-8') as file:
                file_content = file.read()
                return file_content
            
        if self.contains_all_words(query, "notifications"):
            with open("./resources/notifications.md", 'r', encoding='utf-8') as file:
                file_content = file.read()
                return file_content
        
        if self.contains_all_words(query, "custom maps"):
            with open("./resources/custom_maps.md", 'r', encoding='utf-8') as file:
                file_content = file.read()
                return file_content
        
        return "There are no relevant threads in the forum."

    def contains_all_words(self, llm_query, hardcoded_query):
        # Convert both strings to lowercase for case-insensitive comparison
        llm_query_words = llm_query.lower().split()
        hardcoded_query_words = hardcoded_query.lower().split()
        
        # Check if each word in the hardcoded query is in the llm query
        for word in hardcoded_query_words:
            if word not in llm_query_words:
                return False
        
        return True