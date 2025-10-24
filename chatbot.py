from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="HuggingFaceTB/SmolLM3-3B",
    task="text-generation"
)

model= ChatHuggingFace(llm =llm)

chat_history = []

while True:
    user = input("You:")
    chat_history.append(user)
    if user == "exit":
        break
    res = model.invoke(user)
    chat_history.append(res.content)
    print(res.content)