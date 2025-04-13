import numpy as np
import faiss
from sentence_transformers import SentenceTransformer
from langchain.text_splitter import RecursiveCharacterTextSplitter
from transformers import AutoTokenizer, pipeline

# Choose the model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Load the tokenizer for the "all-MiniLM-L6-v2" model
tokenizer = AutoTokenizer.from_pretrained("sentence-transformers/all-MiniLM-L6-v2")

# Normalize each row of the vector array so that each vector has a unit L2 norm
def normalize(vectors: np.ndarray) -> np.ndarray:
    norms = np.linalg.norm(vectors, axis=1, keepdims=True)
    return vectors / np.maximum(norms, np.finfo(np.float32).eps)

# Length function
def token_length(text: str) -> int:
    # Tokenize with special tokens if needed (for models that require them)
    tokens = tokenizer.encode(text, add_special_tokens=False)
    return len(tokens)

# Text chunker
def text_split(large_text: str):
    splitter = RecursiveCharacterTextSplitter(
    chunk_size=75,
    chunk_overlap=10,
    length_function=token_length  
    )
    
    text_chunks = splitter.split_text(large_text)
    #print("Total number of chunks:", len(text_chunks))
    #for i, chunk in enumerate(text_chunks):
        #print(f"\nChunk {i+1} (Token count: {token_length(chunk)}):\n{chunk}")
    return text_chunks

def embedding(df):
    '''# Text arrays
    info_summaries = df.loc[:,"nl_summary_info"]
    article_summaries = df.loc[:,"Article Summary"]
    deal_summaries = df.loc[:,"nl_summary_deals"]
    
    # Embed summaries
    embed_info = model.encode(info_summaries, show_progress_bar=True)
    embed_nor_info = normalize(embed_info)
    
    # Embed deals
    embed_deals = model.encode(deal_summaries, show_progress_bar=True)
    embed_nor_deals = normalize(embed_deals)
    
    # Embed articles
    embed_nor_articles = []
    for article in article_summaries:
        chunks = text_split(article)
        if not chunks:
            continue
        chunk_embed = model.encode(chunks, show_progress_bar=False)
        chunk_embed = np.array(chunk_embed, dtype=np.float32)
        chunk_nor_embed = normalize(chunk_embed)
        embed_nor_articles.append(chunk_nor_embed)'''
        
    # Save data
    '''np.save('embed_nor_info.npy', embed_nor_info)
    np.save('embed_nor_deals.npy', embed_nor_deals)'''
    #np.save('embed_nor_articles.npy', embed_nor_articles)

    '''embed_nor_articles = np.array(embed_nor_articles, dtype=object)
    np.save('embed_nor_articles.npy', embed_nor_articles, allow_pickle=True)'''

    embed_nor_info = np.load("embed_nor_info.npy")
    embed_nor_deals = np.load("embed_nor_deals.npy")
    embed_nor_articles = np.load("embed_nor_articles.npy")

    embed_nor_data = [embed_nor_info, embed_nor_deals, embed_nor_articles]

    
    return embed_nor_data
