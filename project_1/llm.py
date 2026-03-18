from langchain_ollama import ChatOllama
from langchain_cerebras import ChatCerebras
from dotenv import load_dotenv
load_dotenv()

ollama=False
if ollama:
    llm=ChatOllama(model="gemma3:1b")
else:
    llm=ChatCerebras(model="gpt-oss-120b")