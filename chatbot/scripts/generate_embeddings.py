import os
import re
import ollama
from pinecone.grpc import PineconeGRPC as Pinecone
import uuid

# Hardcoded constants
EMBEDDING_MODEL_NAME = "nomic-embed-text"  # Replace with the actual Ollama model name
PINECONE_API_KEY = "pcsk_RpwkS_16esUpqMivoyLMTeBiuDtWt7M99zDGjuESY2iM2MuYGvFdwX51VTGLCe5C6gRmr"  # Replace with your Pinecone API key
PINECONE_INDEX_NAME = "blazor-docs"  # Replace with your Pinecone index name
PINECONE_NAMESPACE = "test1"  # Replace with the namespace you want to use

pc = Pinecone(api_key=PINECONE_API_KEY)
index = pc.Index("blazor-docs")

def find_md_files_with_yaml_front_matter(root_dir):
    yaml_pattern = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)

    matching_files = []
    
    for dirpath, _, filenames in os.walk(root_dir):
        for filename in filenames:
            if not filename.endswith(".md"):
                continue  # Skip non-Markdown files
            
            file_path = os.path.join(dirpath, filename)
            try:
                with open(file_path, 'r', encoding='utf-8') as file:
                    content = file.read(4096)  # Read more to ensure full front matter is captured
                    if yaml_pattern.match(content):
                        matching_files.append(file_path)
            except Exception as e:
                print(f"Skipping {file_path}: {e}")
    
    return matching_files

def extract_yaml_content(file_path):
    yaml_pattern = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)
    
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            match = yaml_pattern.search(content)
            if match:
                return match.group(1)  # Return the YAML content between ---
            else:
                print(f"No YAML front matter found in {file_path}")
                return None
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return None

def generate_embedding(text):
    # Generate the embedding using the Ollama API
    response = ollama.embed(model=EMBEDDING_MODEL_NAME, input=text)
    embedding = response['embeddings']  # Assuming the embedding is returned in this field
    
    # Ensure the embedding is a list of floats
    embedding = [float(i) for i in embedding[0]]
    return embedding

def persist_embedding_to_pinecone(embedding, metadata):
    # Initialize Pinecone client using GRPC API
    pc = Pinecone(api_key=PINECONE_API_KEY)
    index = pc.Index(PINECONE_INDEX_NAME)

    # Generate a unique ID for the embedding
    embedding_id = str(uuid.uuid4())
    
    # Prepare the data for the upsert operation
    vectors = [{
        "id": embedding_id,
        "values": embedding,
        "metadata": metadata
    }]
    
    # Perform the upsert operation
    index.upsert(vectors=vectors, namespace=PINECONE_NAMESPACE)

if __name__ == "__main__":
    # the directory where the blazor-docs repo is, e.g r"C:\Users\{username}\Projects\blazor-docs"
    ROOT_DIRECTORY = ""  # Use raw string for Windows paths
    files = find_md_files_with_yaml_front_matter(ROOT_DIRECTORY)
    
    print("Markdown files with YAML front matter:")
    for file in files:        
        # Extract the YAML front matter content
        yaml_content = extract_yaml_content(file)
        
        if yaml_content:
            # Generate the embedding for the YAML content
            embedding = generate_embedding(yaml_content)
            
            # Prepare metadata for Pinecone
            metadata = {
                "file_path": os.path.relpath(file, ROOT_DIRECTORY),
                "embedded_text": yaml_content
            }
            
            # Persist the embedding and metadata to Pinecone
            persist_embedding_to_pinecone(embedding, metadata)
            print(f"Embedding for {file} has been persisted to Pinecone.")