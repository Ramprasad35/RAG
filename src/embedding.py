from sentence_transformers import SentenceTransformer
model = SentenceTransformer("all-MiniLM-L6-v2",trust_remote_code = True)
def get_embedding(all_chunks):
    return model.encode(all_chunks)
def query_embedding(query):
    return model.encode([query])    