import chromadb
from sentence_transformers import SentenceTransformer

chroma_client = chromadb.PersistentClient(path="models/chroma_db")

collection = chroma_client.get_or_create_collection(name="legal_chunks")
embedding_model = SentenceTransformer("all-MiniLM-L6-v2")

def store_chunks(chunks):
    embeddings = embedding_model.encode(chunks).tolist()
    ids = [f"chunk_{i}" for i in range(len(chunks))]
    collection.add(documents=chunks, embeddings=embeddings, ids=ids)

def retrieve_chunks(query, top_k=4):
    query_embedding = embedding_model.encode([query])[0].tolist()
    results = collection.query(query_embeddings=[query_embedding], n_results=top_k)
    return results['documents'][0]
