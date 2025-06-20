from langchain.text_splitter import RecursiveCharacterTextSplitter
from extractor import Extractor

#Classe que divide o texto em blocos menores (chunks)
class Chunks:
    def __init__(self):
        #Texto de exemplo que será dividido em blocos menores (chunks)
        self.extractor = Extractor()
        self.text = self.extractor.extract_text()
        self.splitter = RecursiveCharacterTextSplitter(
            chunk_size=100,
            chunk_overlap=30
        )

    #Função que irá realizar o processo de dividir o texto
    def split_data(self):
        #Variável que armazena os blocos de texto divididos
        chunks = self.splitter.split_text(self.text)
        return chunks
