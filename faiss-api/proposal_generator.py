from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
from langchain.llms import Ollama
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate

def generate_proposal(input_text):
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    vectordb = FAISS.load_local("vector_store", embeddings)
    retriever = vectordb.as_retriever(search_kwargs={"k": 5})

    llm = Ollama(model="mistral")

    prompt_template = '''
You are a professional business assistant.
Given the following client request: {query}
And based on relevant past proposal context: {context}
Generate a highly relevant, professional proposal.
'''

    PROMPT = PromptTemplate(template=prompt_template, input_variables=["context", "query"])

    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        chain_type="stuff",
        chain_type_kwargs={"prompt": PROMPT},
        return_source_documents=False
    )

    return qa_chain.run(input_text)