import streamlit as st  # Import the Streamlit library for creating web applications

from langchain_community.document_loaders import SeleniumURLLoader  # Import SeleniumURLLoader to load web pages with JavaScript rendering
from langchain_text_splitters import RecursiveCharacterTextSplitter  # Import RecursiveCharacterTextSplitter to split text into chunks
from langchain_core.vectorstores import InMemoryVectorStore  # Import InMemoryVectorStore to store text embeddings in memory
from langchain_ollama import OllamaEmbeddings  # Import OllamaEmbeddings to create text embeddings using Ollama models
from langchain_core.prompts import ChatPromptTemplate  # Import ChatPromptTemplate to create prompt templates for language models
from langchain_ollama.llms import OllamaLLM  # Import OllamaLLM to use Ollama language models

# Define a template for the prompt that will be sent to the language model
template = """
You are an assistant for question-answering tasks. Use the following pieces of retrieved context to answer the question. If you don't know the answer, just say that you don't know. Use three sentences maximum and keep the answer concise.
Question: {question} 
Context: {context} 
Answer:
"""

# Initialize Ollama embeddings with the "llama3.2" model
embeddings = OllamaEmbeddings(model="llama3.2")
# Create an in-memory vector store to store the embeddings
vector_store = InMemoryVectorStore(embeddings)

# Initialize Ollama language model with the "llama3.2" model
model = OllamaLLM(model="llama3.2")

# Function to load a web page using Selenium
def load_page(url):
    loader = SeleniumURLLoader(
        urls=[url]
    )
    documents = loader.load()

    return documents

# Function to split text into smaller chunks
def split_text(documents):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
        add_start_index=True
    )
    data = text_splitter.split_documents(documents)

    return data

# Function to index documents in the vector store
def index_docs(documents):
    vector_store.add_documents(documents)

# Function to retrieve documents from the vector store based on a query
def retrieve_docs(query):
    return vector_store.similarity_search(query)

# Function to answer a question based on a given context
def answer_question(question, context):
    prompt = ChatPromptTemplate.from_template(template)
    chain = prompt | model
    return chain.invoke({"question": question, "context": context})

# Set the title of the Streamlit application
st.title("AI Crawler")
# Create a text input field for the user to enter a URL
url = st.text_input("Enter URL:")

# Load the web page content
documents = load_page(url)
# Split the loaded content into smaller chunks
chunked_documents = split_text(documents)

# Index the chunked documents in the vector store
index_docs(chunked_documents)

# Create a chat input field for the user to enter a question
question = st.chat_input()

# If a question is entered
if question:
    # Display the user's question in the chat interface
    st.chat_message("user").write(question)
    # Retrieve relevant documents from the vector store
    retrieve_documents = retrieve_docs(question)
    # Combine the content of the retrieved documents into a single context string
    context = "\n\n".join([doc.page_content for doc in retrieve_documents])
    # Generate an answer to the question
    answer = answer_question(question, context)
    # Display the assistant's answer in the chat interface
    st.chat_message("assistant").write(answer)
