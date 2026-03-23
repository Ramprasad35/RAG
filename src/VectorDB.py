import pickle
import faiss
import numpy as np 


def create_index(embeddings):
    dimensions = embeddings.shape[1]
    index = faiss.indexFlatL2(dimensions)
    index.add(np.array(embeddings))
    return index

def search(index,query_embedding,chunks,k=3):
    D,I = index.search(query_embedding,k)
    return [chunks[i] for i in I[0]]

def save_index(index,path="faiss_index_bin"):
    faiss.write_index(index,path)

def load_index(index,path="faiss_index_bin"):
    return faiss.read_index(index,path)

def save_chunks(chunks,path="chunks.pkl"):
    with open(path,"wb") as f:
        pickle.dump(chunks,f)

def load_chunks(path="chunk.pkl"):
    with open(path,"rb") as f:
        return pickle.laod(f)
    
