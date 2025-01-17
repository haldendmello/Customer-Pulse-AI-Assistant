# embed_jsonl_data.py
import json
import requests
from pinecone_setup import initialize_pinecone

# Azure OpenAI API setup
AZURE_API_KEY = ""  # Replace with your actual API key
AZURE_API_VERSION = "2023-05-15"
AZURE_ENDPOINT = "" # Replace with the actual endpoint

def get_azure_embedding(text):
    """Generate embeddings using Azure OpenAI API."""
    headers = {
        "Content-Type": "application/json",
        "api-key": AZURE_API_KEY,
    }
    payload = {
        "input": text,
        "model": "text-embedding-3-large",
    }
    
    response = requests.post(f"{AZURE_ENDPOINT}?api-version={AZURE_API_VERSION}", headers=headers, json=payload)
    
    if response.status_code == 200:
        embedding = response.json()["data"][0]["embedding"]
        return embedding
    else:
        print(f"Error generating embedding: {response.status_code} - {response.text}")
        return None

def embed_and_store_jsonl(file_path):
    """Reads a .jsonl file, embeds each line's prompt, and stores it in Pinecone."""
    # Initialize Pinecone
    index = initialize_pinecone()

    # Open the .jsonl file and process each line
    with open(file_path, 'r') as file:
        for i, line in enumerate(file):
            # Parse the JSON object from the line
            document = json.loads(line.strip())
            # Generate a unique ID for each document
            doc_id = f"doc_{i}"
            prompt = document.get("prompt", "")
            completion = document.get("completion", "")

            # Generate embedding for the prompt content
            embedding = get_azure_embedding(prompt)
            if embedding is not None:
                # Store the embedding in Pinecone with metadata
                metadata = {
                    "prompt": prompt,
                    "completion": completion
                }
                try:
                    index.upsert([(doc_id, embedding, metadata)])
                    print(f"Document {doc_id} embedded and stored.")
                except Exception as e:
                    print(f"Error storing embedding for document {doc_id}: {e}")
            else:
                print(f"Failed to generate embedding for document {doc_id}")

# Usage
embed_and_store_jsonl("training_data.jsonl")
