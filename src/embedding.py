from sentence_transformers import SentenceTransformer
model = SentenceTransformer("all-MiniLM-L6-v2",trust_remote_code = True)
def get_embedding(chunks):
    return model.encode(chunks)
def query_embedding(query):
    return model.encode([query])