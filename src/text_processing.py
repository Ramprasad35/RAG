def chunk_text(text,chunk_size=500,overlap=100):
    chunks = []
    start = 0 
    while start < len(text):
        end = start + chunk_size
        chunks.append(text[start:end])
        start = end - overlap 

    for i in range(0,len(text),chunk_size):
        chunks.append(text[i:i+chunk_size])
        return chunks 
    chunks = chunk_text(text) 
    print(len(chunks))