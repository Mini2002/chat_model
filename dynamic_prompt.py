from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from dotenv import load_dotenv
import streamlit as st
from langchain_core.prompts import PromptTemplate

load_dotenv()


st.header("this is new ")

llm = HuggingFaceEndpoint(
    repo_id="mistralai/Mixtral-8x7B-Instruct-v0.1",
    task="text-generation"
)


model = ChatHuggingFace(llm = llm)

paper_input = st.selectbox("select reserch paper name",["gpt","bert"])

input_style = st.selectbox("select explation style", ["business","formal","witty"])

template = PromptTemplate(template="""
you need to give me a detailed summary in 10 lines on {paper_input} and the tone of the langauge should be {input_style}
                        """,
                            input_variables=["paper_input", "input_style"],
                            validate_template=True)

prompt = template.invoke({
    'paper_input':paper_input,
    'input_style':input_style
})

if st.button("summary"):
    res = model.invoke(prompt)
    st.write(res.content)