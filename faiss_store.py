import numpy as np
import faiss

def faiss_saver(embed_data):
    
    # FAISS for info data
    embed_nor_info = np.array(embed_data[0])
    info_dim = embed_nor_info.shape[1]
    info_index = faiss.IndexFlatIP(info_dim)
    info_index.add(embed_nor_info)
    print("Number of vectors in FAISS info_index:", info_index.ntotal)
    
    # FAISS for deals data
    embed_nor_deals = np.array(embed_data[1])
    deals_dim = embed_nor_deals.shape[1]
    deals_index = faiss.IndexFlatIP(deals_dim)
    deals_index.add(embed_nor_deals)
    print("Number of vectors in FAISS deals_index:", deals_index.ntotal)
    
    # FAISS for articles data
    embed_nor_articles = embed_data[2]
    
    if embed_nor_articles.any():
        # Flatten the list-of-arrays into a single 2D NumPy array;
        # each row is a chunk embedding
        embed_nor_articles = np.vstack(embed_nor_articles)
    else:
        embed_nor_articles = np.array([])  # In case no embeddings were generated
        print("No embeddings were generated.")

    dimension = embed_nor_articles.shape[1]
    articles_index = faiss.IndexFlatIP(dimension)
    articles_index.add(embed_nor_articles)
    print("Number of vectors in FAISS articles index:", articles_index.ntotal)
    
    indices = [info_index, deals_index, articles_index]
    return indices

