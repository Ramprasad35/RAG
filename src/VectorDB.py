from embedding import get_embedding
import faiss
import numpy as np 
from text_processing import chunk_text 
from pdf_loader import pdf_reader

text = pdf_reader("filename.pdf")
chunks = chunk_text(text)

embeddings = get_embedding(chunks) 
dimensions = embeddings.shape[1]
index = faiss.indexFlatL2(dimensions)
index.add(np.array(embeddings))
