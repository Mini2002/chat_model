from langchain_community.document_loaders import WebBaseLoader

url = 'https://amazon.jobs/en/jobs/3082667/data-engineer-i'
loader = WebBaseLoader(url)

docs = loader.load()

print(docs[0])