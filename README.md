QA Bot with Retrieval-Augmented Generation (RAG) Model

This repository contains a QA bot that uses a Retrieval-Augmented Generation (RAG) model for answering questions based on uploaded documents. The bot is designed to retrieve relevant information from a document and generate contextually accurate responses. It uses Pinecone DB to store and retrieve document embeddings and Cohere API for generating coherent answers.



Table of Contents
Overview
Features
Tech Stack
Installation
Usage
Examples
Docker Setup
Deployment
Challenges
Future Improvements
Contributors

Overview
This project is divided into two parts:

Part 1: Development of a Retrieval-Augmented Generation (RAG) model to handle questions related to a provided document or dataset.
Part 2: Creation of an interactive frontend using Streamlit, where users can upload PDFs, ask questions, and retrieve answers in real-time. The backend uses the RAG model built in Part 1.


Memory updated
Here’s a detailed README file for your project that combines both Part 1 and Part 2:

QA Bot with Retrieval-Augmented Generation (RAG) Model
This repository contains a QA bot that uses a Retrieval-Augmented Generation (RAG) model for answering questions based on uploaded documents. The bot is designed to retrieve relevant information from a document and generate contextually accurate responses. It uses Pinecone DB to store and retrieve document embeddings and Cohere API for generating coherent answers.

Table of Contents
Overview
Features
Tech Stack
Installation
Usage
Examples
Docker Setup
Deployment
Challenges
Future Improvements
Contributors
Overview
This project is divided into two parts:

Part 1: Development of a Retrieval-Augmented Generation (RAG) model to handle questions related to a provided document or dataset.
Part 2: Creation of an interactive frontend using Streamlit, where users can upload PDFs, ask questions, and retrieve answers in real-time. The backend uses the RAG model built in Part 1.
Features
Upload PDF documents for text extraction and embedding.
Store document embeddings in Pinecone DB.
Answer user queries based on the uploaded document using Cohere's NLP model.
Display relevant document sections alongside generated answers.
Efficient handling of multiple queries.
Modular code structure and scalable architecture.

Tech Stack
Backend:
Python (Flask, Pinecone DB, Cohere API)
Sentence Transformer (all-mpnet-base-v2)
Frontend:
Streamlit
Containerization:
Docker

Installation
1. Clone the Repository
2. Install Dependencies
3. Set Up Pinecone and Cohere API Keys
Create a .env file in the root of the project and add your Pinecone and Cohere API keys:
4. Run the Application Locally

To run the Streamlit frontend locally:
streamlit run streamlit.py

To run the Flask backend:
python app.py

Usage
Upload PDF File: Use the Streamlit interface to upload a PDF document. The system extracts text from the file, generates embeddings, and stores them in Pinecone DB.

Ask a Question: Enter a question related to the uploaded document in the provided text box. The system retrieves the most relevant sections from the document using the vector embeddings and generates an answer via Cohere's API.

View Results: The relevant document sections and the generated answer are displayed on the interface.

Examples
Example Interaction:
PDF Upload: uploaded_doc.pdf
Question: What is HTML?
Generated Answer: "HTML is the standard language for creating web pages and web applications. It describes the structure of a web page using markup."
The bot retrieves the most relevant parts of the document and generates a concise answer based on the content.

Docker Setup
The project is containerized using Docker to ensure easy deployment.

1. Build the Docker Image
docker build -t qa-bot .
2. Run the Docker Container
docker run -p 8501:8501 qa-bot
3. Access the Application
After running the container, you can access the Streamlit app at:
http://localhost:8501

Deployment
To deploy the project:

Ensure the environment has Docker installed.
Follow the Docker Setup instructions.
Push the container to any cloud platform supporting Docker (e.g., AWS, GCP, Azure).
Challenges
Cohere API Limitations: The number of tokens returned by the Cohere API could be limited depending on your plan.
Future Improvements
Enhanced Scalability: Introduce batching for processing large documents.
Multi-document Support: Allow users to upload and query across multiple documents.
Performance Optimization: Optimize embedding generation for large documents.
Contributors
Hursh Karnik - BTech CSE (AI/ML)
