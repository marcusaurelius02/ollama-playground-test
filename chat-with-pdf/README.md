# DeepSeek RAG System with Ollama

This Streamlit application builds a Retrieval-Augmented Generation (RAG) system using DeepSeek R1 and Ollama. It allows users to upload a PDF document and ask questions related to its content. The system retrieves relevant chunks from the document and uses the DeepSeek R1 language model to generate a concise answer.

## Features

*   Upload and process PDF documents.
*   Split documents into semantic chunks using HuggingFace embeddings.
*   Create a vector store for efficient retrieval of relevant content.
*   Utilize the DeepSeek R1 language model (via Ollama) for question answering.
*   User-friendly Streamlit interface.

## Dependencies

*   streamlit
*   langchain\_community
*   langchain\_experimental
*   HuggingFaceEmbeddings
*   FAISS
*   Ollama

To install the dependencies, run:

```bash
pip install -r requirements.txt
```

## Usage

1.  Upload a PDF file using the file uploader in the application.
2.  Type your question related to the document in the text input field.
3.  The system will process your query and display the answer.

## Settings

The application uses the following settings:

*   **Embedding Model**: HuggingFace
*   **Retriever Type**: Similarity Search
*   **LLM**: DeepSeek R1 (Ollama)

These settings are hardcoded in the script.

## Notes

*   Make sure you have Ollama installed and the DeepSeek R1 model available.
*   The application uses a temporary file named `temp.pdf` to store the uploaded PDF.
