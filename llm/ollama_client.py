import requests

def ollama_answer(context,query):
    response = requests.post(
        "http://localhost:11434/api/chat",
        json = {
                "model" : "llama3",
                "messages": [
                 {"role":"system", "content":"Answer only from the context"},
                 {"role":"user", "content": f"context:\n{context}\n\nQuestion:\n{query}"} 
                ]
        }
    )

    data = response.json()
    data = response.json()

    if "message" in data:
        return data["message"]["content"]
    elif "response" in data:
        return data["response"]
    else:
        return str(data)