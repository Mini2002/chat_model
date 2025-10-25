from langchain_huggingface import HuggingFaceEndpoint,ChatHuggingFace
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

prompt = PromptTemplate(template="""
     write five lines about {topic}
     Each line starts with number starting from 1
     """,
     input_variables=['topic']
)

llm = HuggingFaceEndpoint(
    repo_id="mistralai/Mixtral-8x7B-Instruct-v0.1",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)

parser =  StrOutputParser()

chain = prompt | model | parser

res = chain.invoke({'topic':'doremon'})

print(res)

chain.get_graph().print_ascii()