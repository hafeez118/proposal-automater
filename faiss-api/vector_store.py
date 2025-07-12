from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.docstore.document import Document
import os

def build_vectorstore(doc_texts):
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    docs = [Document(page_content=txt) for txt in doc_texts]
    db = FAISS.from_documents(docs, embeddings)
    db.save_local("vector_store")