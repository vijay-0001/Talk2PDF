from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_pinecone import PineconeVectorStore
from pinecone import Pinecone
import os

OPENAI_KEY = os.getenv('OPENAI_API_KEY')
PINECONE_API_KEY = os.getenv('PINECONE_API_KEY')

# Initialize OpenAI Embeddings
embeddings = OpenAIEmbeddings(openai_api_key=OPENAI_KEY, model = "text-embedding-ada-002")

# Initialize Pinecone
Pinecone = Pinecone(api_key=PINECONE_API_KEY)
index_name = 'langchain1'

# Load and split the PDF document
loader = PyPDFLoader("IOCResultsQ22024-25.pdf")
data = loader.load()

full_text = " ".join([doc.page_content for doc in data])
text_splitter = RecursiveCharacterTextSplitter(chunk_size=4000, chunk_overlap=800)

texts = text_splitter.split_text(full_text)
#documents = text_splitter.split_documents(data)

# Create and persist the vector store
#vectorstore = PineconeVectorStore.from_documents(documents, embeddings, index_name=index_name)
vectorstore = PineconeVectorStore.from_texts(texts, embeddings, index_name=index_name)
print("Embeddings created and stored.")