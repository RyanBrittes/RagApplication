#Exemplo de uso do nomic com processamento local de embeddings
from nomic import embed
from chunks import Chunks

#Classe que irá criar os embeddings dos textos e consultas
class Embed:
    def __init__(self):
        self.chunks = Chunks()

    #Criador de embeddings, cria um dicionário com 4 chaves
    def embed_text(self):
        output = embed.text(
            texts=self.chunks.split_data(),
            model='nomic-embed-text-v1.5',
            task_type='search_document'
            #inference_mode='local',
            #device='cpu'
        )['embeddings']
        return output
    
    #Este código está implementado utilizando a API do Nomic, caso deseje processar localmente,
    #Apague os hastags de inference_mode e device
    def embed_query(self, query: str):
        output = embed.text(
            texts=[query],
            model='nomic-embed-text-v1.5',
            task_type='search_document'
            #inference_mode='local',
            #device='cpu'
        )['embeddings']
        return output