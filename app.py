import os
from pinecone import Pinecone, ServerlessSpec
from flask import Flask, request, jsonify
from sentence_transformers import SentenceTransformer
import cohere

app = Flask(__name__)


pc = Pinecone(api_key="7ea2842e-0423-4c36-a409-79889f26a01d")
index_name = "qa-bot-index"
host = "qa-bot-index-xdapdhq.svc.aped-4627-b74a.pinecone.io"

if index_name not in pc.list_indexes().names():
    pc.create_index(
        name=index_name,
        dimension=768, 
        metric='cosine',  
        spec=ServerlessSpec(
            cloud='aws',
            region='us-east-1'
        )
    )

index = pc.Index(index_name, host=host)

cohere_client = cohere.Client("Ga9HyHd21Nd5XoiXxdSiPzsmtGZJhULrfuS8gfct")

embedding_model = SentenceTransformer('all-MiniLM-L6-v2')

@app.route('/query', methods=['POST'])
def query():
    try:
        query_text = request.json.get('query')
        
        query_embedding = embedding_model.encode([query_text]).tolist()  
        
        query_response = index.query(queries=query_embedding, top_k=5)

        retrieved_docs = [match['id'] for match in query_response['matches']]

        
        cohere_response = cohere_client.generate(
            model='command-xlarge-nightly',
            prompt=f"Context: {retrieved_docs}\nQuestion: {query_text}",
            max_tokens=100
        )

        answer = cohere_response.generations[0].text

        return jsonify({'answer': answer})

    except Exception as e:
        print(f"An error occurred: {e}")
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
