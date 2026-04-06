from fastapi import FastAPI
from src.VectorDB import search,load_index ,load_chunks
from src.embedding import query_embedding
from llm.router import get_answer
from pydantic import BaseModel

app = FastAPI()

index = load_index()
all_chunks = load_chunks()

@app.get("/")
def home():
    return{"RAG is running "}

class Query(BaseModel):
    query:str
    
@app.post("/ask")
def ask(q: Query):

    query = q.query

    if not query.strip():
        return{"error":"Empty query"}

    query_vec = query_embedding(query)
    results =search(index,query_vec, all_chunks ,k=5)

    if not  results():
        return{"message":"Not inside the document","Source" : []}

    context = "/n".join(c["text"]for c in  results)
        
    if not  context.strip():
        return {"message":"Empty context" , "Source":[]}


    answer = get_answer(context,query)

    from collections import defaultdict
    source_pages = defaultdict(set)

    for c in results:
        sources[c["sources"]].add (c["pages"])

    sources=[
        {"sources": s ,"pages":sorted(list(p))}
            for s,p in source_pages.items()
        ]

    return{"answer":answer , "source":sources}

    

