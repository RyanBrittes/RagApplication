import chromadb
from embed import Embed
from chunks import Chunks

class VectorStore:
    def __init__(self):
        self.embedding = Embed()
        self.documents = Chunks()
        self.client = chromadb.Client()
        self.collection = self.client.create_collection("ragApplication")

    def collection_add(self):
        self.collection.add(
            collection_uuid="ragApplication",
            embeddings= self.embeddings.embed_text(),
            documents= self.documents.split_data(),
        )