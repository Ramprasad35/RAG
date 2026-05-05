import requests
import time

def ollama_answer(context,query):
        url="http://localhost:11434/api/chat"
        payload= {
                "model" : "llama3",
                "messages": [
                 {"role":"system", "content":"Answer clearly using the context.Do not copy.explain in your own words"},
                 {"role":"user", "content": f"context:\n{context}\n\nQuestion:\n{query}"} 
                ],
                "stream": False
        }

        for i in range(3):
                try:
                    response = requests.post(url,json=payload,timeout=30)
                    data = response.json()
                                               
                    if "message" in data:
                        return data["message"]["content"]
                    elif "response" in data:
                        return data["content"]
                    else:
                        return str(data)
                
                except requests.exceptions.RequestException as e:
                     print(f"Attempt{i+1} failed:",e)
                     time.sleep(2)
        return None
   


    