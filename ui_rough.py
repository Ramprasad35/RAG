@app.get("/")
def home():
    return{"rag is running"}

@app.post("/ask")
def ask(q:Query):
    



