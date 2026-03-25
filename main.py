from src.pdf_loader import pdf_reader
from src.text_processing import chunk_text
from src.VectorDB import search , create_index,save_index,load_index,load_chunks,save_chunks
from src.embedding import query_embedding , get_embedding
import os
from src.llm import get_answer 
import numpy as np

def main():
    text = pdf_reader("C:\\Users\\RamprasadSK\\OneDrive - ConceptVines\\Documents\\RAG\\DATA\\sample.pdf")
    
    chunks = chunk_text(text=text, chunk_size=500)

    embeddings= [get_embedding(chunks)for chunk in chunks]
    embeddings = np.array(embeddings)

    if os.path.exists("faiss_index_bin"):
         index = load_index()
         chunks = load_chunks()
    else:
         index = create_index(embeddings)
         save_index(index)
         save_chunks(chunks)

    query = input("Answer a question:")
    query_vec = query_embedding(query)

    results = search(index,query_vec,chunks)

    context = "\n".join(results)

    answer = get_answer(context,query)
    
    
    print("\n".join(results))

if __name__ == "__main__":
     main()

    