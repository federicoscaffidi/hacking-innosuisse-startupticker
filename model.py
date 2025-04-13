import numpy as np
import json
import spacy
from transformers import pipeline
from sentence_transformers import SentenceTransformer
from embedding import normalize

# Choose the model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Create an embedding for the query and normalize it
def query_embedding(user_query):
    
    # Embed with model
    query_embed = model.encode(user_query, show_progress_bar=False)
    
    # Convert to np array
    query_embed = np.array(query_embed, dtype="float32")
    
    # Normalize
    norm = np.linalg.norm(query_embed)
    epsilon = np.finfo(np.float32).eps
    norm = max(norm, epsilon)
    query_embed_nor = query_embed / norm
    
    # Convert to a 2d array for FAISS 
    query_embed_nor = query_embed_nor[None, :]    
    
    print("\nQuery:", user_query)
    return query_embed_nor

# Search through FAISS similarity
def faiss_search(f_index, dataset, user_query, k=20):
    
    # Embed query
    query_embed_nor = query_embedding(user_query)
    
    # Perform search
    distances, indices = f_index.search(query_embed_nor, k)
    
    output = dataset[indices[0]]
    
    return output

