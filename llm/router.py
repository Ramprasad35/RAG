PROVIDER = "ollama"

#from llm.openai_client import openai_answer
from llm.ollama_client import ollama_answer

def get_answer(context,query):
    if PROVIDER == "openai":
        return openai_answer(context,query)
    elif PROVIDER == "ollama":
        return ollama_answer(context,query)