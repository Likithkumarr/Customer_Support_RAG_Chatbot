import streamlit as st
import os

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_ollama import OllamaLLM, OllamaEmbeddings
from langchain_chroma import Chroma
from langchain_core.documents import Document
from langchain_classic.chains import RetrievalQA
from langchain_core.prompts import PromptTemplate

st.title("🤖 Customer Support Knowledge Bot")

# Load documents
docs = []

for file in os.listdir("support_docs"):

    file_path = f"support_docs/{file}"

    try:
        if file.endswith(".pdf"):
            loader = PyPDFLoader(file_path)
            docs.extend(loader.load())

        elif file.endswith(".txt"):
            with open(file_path, "r", encoding="utf-8") as f:
                text = f.read()

            docs.append(
                Document(
                    page_content=text,
                    metadata={"source": file}
                )
            )

    except Exception as e:
        st.warning(f"Skipping file {file} due to error: {e}")

# Split documents
splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)

documents = splitter.split_documents(docs)

st.write(f"Loaded documents: {len(documents)}")

# Embeddings
embeddings = OllamaEmbeddings(
    model="nomic-embed-text"
)

# Vector DB
vectordb = Chroma.from_documents(
    documents=documents,
    embedding=embeddings,
    persist_directory="chroma_db"
)

retriever = vectordb.as_retriever()

# LLM
llm = OllamaLLM(
    model="phi3",
    temperature=0
)

# Prompt
prompt_template = """
You are a customer support assistant.

Use ONLY the provided context to answer the question.
Do NOT add extra information.

If the answer is not present in the context, say:
"I could not find the answer in the documents."

Context:
{context}

Question:
{question}

Answer:
"""

PROMPT = PromptTemplate(
    template=prompt_template,
    input_variables=["context", "question"]
)

# RAG chain
qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=retriever,
    chain_type="stuff",
    chain_type_kwargs={
        "prompt": PROMPT
    }
)

# User input
question = st.text_input("Ask a support question")

if st.button("Get Answer"):

    result = qa_chain.invoke({
        "query": question
    })

    st.subheader("Answer")
    st.write(result["result"])
# import streamlit as st
# import os

# from langchain_community.document_loaders import PyPDFLoader
# from langchain_text_splitters import RecursiveCharacterTextSplitter
# from langchain_ollama import OllamaLLM, OllamaEmbeddings
# from langchain_chroma import Chroma
# from langchain_core.documents import Document
# from langchain_classic.chains import RetrievalQA

# st.title("🤖 Customer Support Knowledge Bot")

# # Load documents
# docs = []

# for file in os.listdir("support_docs"):

#     file_path = f"support_docs/{file}"

#     try:
#         if file.endswith(".pdf"):
#             loader = PyPDFLoader(file_path)
#             docs.extend(loader.load())

#         elif file.endswith(".txt"):
#             with open(file_path, "r", encoding="utf-8") as f:
#                 text = f.read()

#             docs.append(
#                 Document(
#                     page_content=text,
#                     metadata={"source": file}
#                 )
#             )
#     except Exception as e:
#         st.warning(f"Skipping file {file} due to error")

# # Split documents
# splitter = RecursiveCharacterTextSplitter(
#     chunk_size=500,
#     chunk_overlap=50
# )

# documents = splitter.split_documents(docs)

# # Embeddings
# embeddings = OllamaEmbeddings(model="nomic-embed-text")

# # Vector DB
# vectordb = Chroma.from_documents(
#     documents,
#     embedding=embeddings,
#     persist_directory="chroma_db"
# )

# retriever = vectordb.as_retriever()

# # LLM
# llm = OllamaLLM(model="mistral")
# llm = OllamaLLM(model="phi3")

# # RAG chain
# qa_chain = RetrievalQA.from_chain_type(
#     llm=llm,
#     retriever=retriever
# )

# # User input
# question = st.text_input("Ask a support question")

# if st.button("Get Answer"):

#     result = qa_chain.invoke({"query": question})

#     st.subheader("Answer")
#     st.write(result["result"])