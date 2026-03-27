import pickle
import faiss
import numpy as np 


def create_index(embeddings):
    dimensions = embeddings.shape[1]
    index = faiss.IndexFlatL2(dimensions)
    index.add(np.array(embeddings))
    return index

def search(index,query_embedding,chunks,k=3):
    D,I = index.search(query_embedding,k)
    if D[0][0] > 1.0:
      return []  
    return [chunks[i] for i in I[0]]

def save_index(index,path="faiss_index.bin"):
    faiss.write_index(index,path)

def load_index(path="faiss_index.bin"):
    return faiss.read_index(path) 

def save_chunks(chunks,path="chunks.pkl"):
    with open(path,"wb") as f:
        pickle.dump(chunks,f)

def load_chunks(path="chunks.pkl"):
    with open(path,"rb") as f:
        return pickle.load(f)
    
