import numpy as np
from dataframe import make_df
from embedding import embedding, text_split
from faiss_store import faiss_saver
from model import faiss_search

def main(user_query):

    # Create the dataframe
    merged_df = make_df()

    # Create a list of chunked articles
    articles_chunks = []
    for article in merged_df.loc[:,"Article Summary"]:
        # Split the article into text chunks using our custom text_split function
        chunks = text_split(article)
        for vez in chunks:
            articles_chunks.append(vez)
    articles_chunks = np.array(articles_chunks)

    # Embed all data in vectors
    embed_data = embedding(merged_df)

    # Create FAISS indices
    f_indices = faiss_saver(embed_data)
    info_index = f_indices[0]
    deals_index = f_indices[1]
    articles_index = f_indices[2]

    

    # Search in the FAISS indices
    info_output = faiss_search(info_index, merged_df.loc[:,"nl_summary_info"], user_query)
    deals_output = faiss_search(deals_index, merged_df.loc[:,"nl_summary_deals"], user_query)
    articles_output = faiss_search(articles_index, articles_chunks, user_query)

    return [info_output, deals_output, articles_output]

