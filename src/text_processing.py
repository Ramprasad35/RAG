def chunk_text(text,chunk_size=300):
    chunks = []
    for i in range(0,len(text),chunk_size):
        chunks.append(text[i:i+chunk_size])
        return chunks
    chunks = chunk_text(text)
    print(len(chunks))