from src.pdf_loader import pdf_reader
from src.text_processing import chunk_text
from src.VectorDB import search , create_index,save_index,load_index,load_chunks,save_chunks
from src.embedding import query_embedding , get_embedding
import os
from llm.router import get_answer
import numpy as np 

def main():
    all_chunks = []
    for pdf_file in os.listdir("data"):
       if pdf_file.endswith(".pdf"):
          pages = pdf_reader(f"data/{pdf_file}")
          
          for page_num , page_text in enumerate(pages):
               chunks = chunk_text(page_text)
               for chunk in chunks:
                    all_chunks.append({
                         "text": chunk ,
                         "source": pdf_file ,
                         "page":page_num
                    })    

    embeddings = [get_embedding(c["text"]) for c in all_chunks] 
    embeddings = np.array(embeddings)

    if os.path.exists("faiss_index.bin"):
         index = load_index()
         chunks = load_chunks()
    else:
         index = create_index(embeddings)
         save_index(index)
         save_chunks(chunks)

    query = input("Ask  a question:")
    query_vec = query_embedding(query)

    results = search(index,query_vec,chunks,k=5)

    context = "\n".join(results)
    answer = get_answer(context,query)
    print(answer)

if __name__ == "__main__": 
     main() 
 
    