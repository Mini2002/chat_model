from langchain_community.document_loaders import TextLoader
from langchain_huggingface import HuggingFaceEndpoint,ChatHuggingFace
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="mistralai/Mixtral-8x7B-Instruct-v0.1",
    task='text-generation'
)

model = ChatHuggingFace(llm=llm)

prompt = PromptTemplate(template='''write a summary on {topic}''',input_variables=['topic'])

loader = TextLoader('poem.txt',encoding='utf-8')

docs = loader.load()

parser = StrOutputParser()

chain = prompt | model | parser

poem = docs[0].page_content

res = chain.invoke({'topic':poem})

print(res)