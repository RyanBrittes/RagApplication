import fitz

#Parte do processo responsável por extrair o texto do PDF
class Extractor:
    def __init__(self):
        self.pdf_path = "/home/ryan/Documents/AI/RagApp/Files/rag_file01.pdf"
        self.pdf_file = fitz.open(self.pdf_path)
        self.string_pdf = ""

    #Extrai o texto do PDF, armazena em uma string e retorna o valor
    def extract_text(self):
        for page in self.pdf_file:
            self.string_pdf += page.get_text()
        self.pdf_file.close()
        return self.string_pdf
    