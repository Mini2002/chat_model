from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="HuggingFaceTB/SmolLM3-3B",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)

user_input = input()

result = model.invoke(user_input)

print(result.content)
