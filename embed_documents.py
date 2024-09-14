import pinecone
from sentence_transformers import SentenceTransformer

embedding_model = SentenceTransformer('all-MiniLM-L6-v2')

documents = ["Document 1 text", "Document 2 text", "Document 3 text"]

pinecone.init(api_key="7ea2842e-0423-4c36-a409-79889f26a01d", environment="us-east-1")

index_name = "qa-bot-index"

if index_name not in pinecone.list_indexes():
    pinecone.create_index(index_name, dimension=768) 

index = pinecone.Index(index_name)

embeddings = embedding_model.encode(documents)

ids = [f"doc-{i}" for i in range(len(documents))]

index.upsert(vectors=zip(ids, embeddings))
