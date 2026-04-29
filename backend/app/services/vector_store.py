from sentence_transformers import SentenceTransformer
import chromadb

model = SentenceTransformer("all-MiniLM-L6-v2")
client = chromadb.Client()
collection = client.get_or_create_collection(name="docs")

def store_docs(docs):
    for i, doc in enumerate(docs):
        embedding = model.encode(doc["doc"]).tolist()

        collection.add(
            ids=[str(i)],
            documents=[doc["doc"]],
            embeddings=[embedding]
        )

def query_docs(query):
    embedding = model.encode(query).tolist()

    results = collection.query(
        query_embeddings=[embedding],
        n_results=2
    )

    return results["documents"][0]