"""Documentation search tool."""

import os

import ollama
from pinecone.grpc import PineconeGRPC as Pinecone

import config
from interfaces.tool import Tool

class DocumentationSearchTool(Tool):
    """Tool for performing searches in the Telerik UI for Blazor documentation."""
    
    def __init__(self, api_key=None, index_name=None):
        """Initialize the Pinecone client."""

        self.api_key = api_key or config.PINECONE_API_KEY
        self.index_name = index_name or config.PINECONE_INDEX_NAME
        
        self.pinecone_client = Pinecone(self.api_key)
        self.pinecone_index = self.pinecone_client.Index(self.index_name)

    @property
    def definition(self):
        """Get the tool definition for Claude API."""
        return {
            "name": "documentation_search",
            "description": "Search for text that is semantically similar to the user question in the documentation. Should be used for general documentation of Telerik UI components for Blazor. Should not be used for troubleshooting issues related to Telerik Blazor UI components for Blazor.",
            "input_schema": {
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                        "description": "The text to search for similar content"
                    }
                },
                "required": ["query"]
            }
        }
    
    def execute(self, arguments):
        """Execute the documentation search using the provided query."""
        query = arguments.get("query", "").strip()

        return self.perform_similarity_search(query)
    
    def perform_similarity_search(self, query):
        # Generate embeddings for the input
        embeddings = self.generate_embedding(query)
        
        # Perform similarity search in Pinecone using the generated embedding
        search_results = self.pinecone_index.query(
            namespace=config.PINECONE_NAMESPACE,
            vector=embeddings,
            top_k=config.TOP_RESULTS,
            include_metadata=True,
            include_values=False
        )

        return self.extract_top_result_md(search_results)
    
    def generate_embedding(self, text):
        # Generate the embedding using the Ollama API
        response = ollama.embed(model=config.EMBEDDING_MODEL_NAME, input=text)
        embedding = response['embeddings']  # Assuming the embedding is returned in this field
        
        # Ensure the embedding is a list of floats
        embedding = [float(i) for i in embedding[0]]
        return embedding
    
    def extract_top_result_md(self, search_results):
        top_result = search_results['matches'][0] if search_results['matches'] else None
        if top_result:
            file_path = top_result['metadata']['file_path']  # Get the file path from metadata
            full_path = os.path.join(config.BASE_DIR, file_path)  # Combine with the base directory
            
            # Read the content of the file
            try:
                with open(full_path, 'r', encoding='utf-8') as file:
                    file_content = file.read()
            except FileNotFoundError:
                file_content = "File not found or cannot be read."
        
            return file_content
        
        return "No relevant content found in the documentation."
    
    