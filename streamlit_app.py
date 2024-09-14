import streamlit as st
from PyPDF2 import PdfReader
from sentence_transformers import SentenceTransformer
from pinecone import Pinecone, ServerlessSpec
import cohere
import tempfile
import os

pc = Pinecone(api_key="7ea2842e-0423-4c36-a409-79889f26a01d")

index_name = "qa-bot-index"
if index_name not in pc.list_indexes().names():
    pc.create_index(
        name=index_name,
        dimension=768,  
        metric='cosine',
        spec=ServerlessSpec(cloud='aws', region='us-west-2')
    )
index = pc.Index(index_name)

cohere_client = cohere.Client("Ga9HyHd21Nd5XoiXxdSiPzsmtGZJhULrfuS8gfct")

model = SentenceTransformer('sentence-transformers/all-mpnet-base-v2')

st.title("Interactive QA Bot")

uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

if uploaded_file is not None:
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_file.write(uploaded_file.read())
        temp_file_path = temp_file.name

    pdf_reader = PdfReader(temp_file_path)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()

    os.remove(temp_file_path)

    doc_embedding = model.encode([text])[0]
    doc_id = "uploaded_doc"
    index.upsert(vectors=[(doc_id, doc_embedding, {'text': text})])

    user_query = st.text_input("Ask a question based on the uploaded document")

    if user_query:
        query_embedding = model.encode(user_query)

        result = index.query(vector=query_embedding.tolist(), top_k=1)

        if 'matches' in result and len(result['matches']) > 0:
            match = result['matches'][0]
            if 'values' in match and len(match['values']) > 0:
                retrieved_text = match['values'][0].get('text', "No relevant metadata found for this match.")
            else:
                retrieved_text = "No relevant metadata found for this match."
        else:
            retrieved_text = "No relevant documents found."

        
        prompt = f"""
        The following is the document content:

        {retrieved_text}

        Based on the provided content, answer the following question:
        {user_query}
        """
        response = cohere_client.generate(
            model='command-xlarge-nightly',
            prompt=prompt,
            max_tokens=150
        )

  
        st.write("Answer:")
        st.write(response.generations[0].text.strip())
