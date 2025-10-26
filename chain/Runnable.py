from langchain_huggingface import HuggingFaceEndpoint,ChatHuggingFace
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id='mistralai/Mixtral-8x7B-Instruct-v0.1',
    task='text-generation'
)

model = ChatHuggingFace(llm = llm)

prompt = PromptTemplate(template='''Give me a joke on {topic}''',
                        input_variables=['topic'])

# prompt2 = PromptTemplate(template='''''',input_variables=)

parser = StrOutputParser()

chain = prompt | model | parser

res = chain.invoke({'topic':'cricket'})

print(res)