import os
import io

from langchain_community.document_loaders import PDFPlumberLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.vectorstores import InMemoryVectorStore
from langchain_ollama import OllamaEmbeddings
from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama.llms import OllamaLLM

template = """
You are an assistant for question-answering tasks. Use the following pieces of retrieved context to answer the question. If you don't know the answer, just say that you don't know. Use three sentences maximum and keep the answer concise.
Question: {question}
Context: {context}
Answer:
"""

embeddings = OllamaEmbeddings(model="deepseek-r1:7b")
vector_store = InMemoryVectorStore(embeddings)

model = OllamaLLM(model="deepseek-r1:7b")

def load_pdf(file_path):
    loader = PDFPlumberLoader(file_path=file_path)
    documents = loader.load()
    return documents

def split_text(documents):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
        add_start_index=True
    )
    return text_splitter.split_documents(documents)

def index_docs(documents):
    vector_store.add_documents(documents)

def retrieve_docs(query):
    return vector_store.similarity_search(query)

def answer_question(question, documents):
    context = "\n\n".join([doc.page_content for doc in documents])
    prompt = ChatPromptTemplate.from_template(template)
    chain = prompt | model
    return chain.invoke({"question": question, "context": context})

if __name__ == "__main__":
    # --- Configuration ---
    file_path = "C:\\Users\\sinjav\\OneDrive - SAS\\GitHub Projects\\ollama-playground-test\\chat-with-pdf\\pdfs\\test.pdf"  # <---  YOUR FILE PATH HERE
    question_to_ask = "What is the main topic of this document?"  # <--- YOUR QUESTION HERE
    output_file_path = r"C:\Users\sinjav\OneDrive - SAS\GitHub Projects\ollama-playground-test\chat-with-pdf\answer.txt" # Path to save the answer

    # --- Load, Process, and Index PDF ---
    documents = load_pdf(file_path)
    chunked_documents = split_text(documents)
    index_docs(chunked_documents)

    # --- Answer the Question ---
    related_documents = retrieve_docs(question_to_ask)
    answer = answer_question(question_to_ask, related_documents)

    # --- Save Answer to Text File ---
    with open(output_file_path, "w") as f:
         f.write(answer) # Access content attribute to get the string answer

    print(f"Answer saved to: {output_file_path}")