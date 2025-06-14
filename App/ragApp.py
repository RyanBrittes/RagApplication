from vectorStore import VectorStore
from embed import Embed

#Classe utilizada para juntar as funcionalidades do RAG e pronta para ser chamada
class RagApp:
    def __init__(self):
        self.vector_store = VectorStore()
        self.embed = Embed()
    
    #Método que mescla o armazenamento vetorial e o embedder
    def compair_vector(self, question: str):
        #Adiciona uma collection no ChromaDB
        self.vector_store.collection_add()
        #Armazena o embedding da pergunta
        query = self.embed.embed_query(question)
        return self.vector_store.collection_query(query)['documents']