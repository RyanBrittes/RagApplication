import chromadb
from chromadb.config import Settings
from embed import Embed
from chunks import Chunks

#Classe que utiliza o ChromaDB como armazenamento vetorial
class VectorStore:
    def __init__(self):
        self.embedding = Embed()
        self.documents = Chunks()
        self.client = chromadb.PersistentClient(
            path="/home/ryan/Documents/AI/RagApp/ChromaDB",
            settings=Settings(allow_reset=True)
            )   
        self.collection = self.client.get_or_create_collection(
            name="ragApplication", 
            )

    #Método que adiciona os embeddings e documentos na coleção do ChromaDB
    def collection_add(self):
        self.collection.add(
            embeddings= self.embedding.embed_text(),
            documents= self.documents.split_data(),
            ids=[f"id{i}" for i in range(len(self.documents.split_data()))]
        )
    
    #Método que realiza a consulta na coleção do ChromaDB, trazendo os 3 resultados mais relevantes
    def collection_query(self, query):
         return self.collection.query(
            query_embeddings=query,
            n_results=3
        )
    