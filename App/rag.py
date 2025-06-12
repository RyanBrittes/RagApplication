from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.llms import Ollama
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains import RetrievalQA


# 1. Carregar PDF
pdf_path = "/home/ryan/Documents/AI/RagApp/Files/rag_file01.pdf"
loader = PyPDFLoader(pdf_path)
documents = loader.load()

# 2. Dividir em chunks
splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)
texts = splitter.split_documents(documents)

# 3. Carregar embedding Nomic
embeddings = HuggingFaceEmbeddings(
    model_name="nomic-ai/nomic-embed-text-v1",
    model_kwargs={
        "device": "cpu",  # ou "cpu" se não tiver GPU
        "trust_remote_code": True
    }
)

# 4. Criar vetor store com Chroma
db = Chroma.from_documents(
    documents=texts,
    embedding=embeddings,
    persist_directory="./ChromaDB"
)

retriever = db.as_retriever()

# 5. LLM via Ollama
llm = Ollama(model="gemma3:1b")

# 6. Criar cadeia RAG
qa = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=retriever,
    return_source_documents=True
)

# 7. Fazer pergunta
pergunta = "Qual o principal conteúdo deste documento PDF?"
resposta = qa(pergunta)

# 8. Mostrar resposta
print("\n🔍 Resposta:\n", resposta["result"])
print("\n📁 Fontes:")
for doc in resposta["source_documents"]:
    print("-", doc.metadata.get("source", "Desconhecido"))
