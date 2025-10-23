from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

st.header("Research paper")

llm = HuggingFaceEndpoint(
    repo_id="HuggingFaceTB/SmolLM3-3B",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)

user_input = st.text_input("Enter your query here")

if st.button("Click here"):
    result = model.invoke(user_input)
    st.write(result.content)
    