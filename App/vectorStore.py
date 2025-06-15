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

    def collection_verify_create(self):
        verify_collections = self.client.list_collections()
        collection_names = [col.name for col in verify_collections]
        if "ragApplication" in collection_names:
            print("Coleção já existente")
        else:
            self.client.create_collection(name="ragApplication")
            print("Nova coleção criada")
    
    #Método que adiciona os embeddings e documentos na coleção do ChromaDB
    def collection_add(self):
        self.collection_verify_create()

        collection = self.client.get_collection(name="ragApplication")
        ids = [f"id{i}" for i in range(len(self.documents.split_data()))]
        
        if collection.count() == 0:
            collection.add(
                embeddings=self.embedding.embed_text(),
                documents=self.documents.split_data(),
                ids=ids
            )
            print("Dados adicionados ao BD")
        else:
            
            print("Dados já existentes no BD")
    
    #Método que realiza a consulta na coleção do ChromaDB, trazendo os 3 resultados mais relevantes
    def collection_query(self, query):
         self.collection_add()

         collection = self.client.get_collection(name="ragApplication")

         return collection.query(
            query_embeddings=query,
            n_results=3
        )
    