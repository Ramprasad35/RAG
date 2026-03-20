from openai import OpenAI
client = OpenAI()

def get_answer(context,query):
    response = client.chat.completions.create(
        model = "gpt-4o-mini",
        messages =[
            {"role":"system","content":"answer only from the context"},
            {"role":"user","content":f"context:\n{context}\n\nQuestion:{query}"}
        ]     
    )
    print("response.choices.[0].messages.content")




    