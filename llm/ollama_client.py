import requests

def ollama_answer(context,query):
    response = requests.post(
        "http://localhost:11434/api/chat",
        json = {
                "model" : "llama3",
                "messages": [
                 {"role":"system", "content":"Answer clearly using the context.Do not copy.explain in your own words"},
                 {"role":"user", "content": f"context:\n{context}\n\nQuestion:\n{query}"} 
                ],
                "stream": False
        }
    )

    data = response.json()                                                                                                                                     

    if "message" in data:
        return data["message"]["content"]
    elif "response" in data:
        return data["response"]
    else:
        return str(data)