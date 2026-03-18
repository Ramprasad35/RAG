from sentence_transformers import Sentence_Transformer
model = Sentence_Transformer("all-MiniLM-L6-v2")
def get_embedding(chunks):
    return model.encode("chunks")