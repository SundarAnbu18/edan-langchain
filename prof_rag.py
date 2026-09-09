from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS

load_dotenv()

texts = [
    "Sundar full name is sundar anbu",
    "Sundar is a good person",
    "sun is heat place",
]

embeddings = OpenAIEmbeddings(model="text-embedding-3-small")

index = FAISS.from_texts(texts, embeddings)
index.save_local("index.faiss")

results = index.similarity_search("what is sun?", k=2)
for doc in results:
    print(doc.page_content)
