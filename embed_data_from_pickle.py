import pickle
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

def embed_and_store_pickle(file_path):
    """Reads a .pkl file, embeds each customer entry, and stores it in Pinecone."""
    # Initialize Pinecone
    index = initialize_pinecone()

    # Load data from .pkl file
    with open(file_path, 'rb') as file:
        data = pickle.load(file)
        print(data)
        
    # Process each entry in the dataset
    for i, entry in enumerate(data):
        # Assuming each entry has relevant fields like 'customer_data' and 'completion'
        doc_id = f"churn_doc_{i}"
        customer_data = entry.get("customer_data", "")
        completion = entry.get("completion", "")

        # Generate embedding for the customer data
        embedding = get_azure_embedding(customer_data)
        if embedding is not None:
            # Store the embedding in Pinecone with metadata
            metadata = {
                "customer_data": customer_data,
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
embed_and_store_pickle("churn_model.pkl")
