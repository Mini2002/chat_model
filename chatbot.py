from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from langchain_core.messages import SystemMessage,HumanMessage,AIMessage
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="mistralai/Mixtral-8x7B-Instruct-v0.1",
    task="text-generation"
)

model= ChatHuggingFace(llm =llm)

chat_history = [
    SystemMessage(content="You are a helpful assistant")
]

while True:
    user = input("You:")
    chat_history.append(HumanMessage(content = user))
    if user == "exit":
        break
    res = model.invoke(chat_history)
    chat_history.append(AIMessage(content=res.content))
    print(res.content)