from langchain_pinecone import PineconeVectorStore
from langchain_openai import ChatOpenAI
from langchain_openai import OpenAIEmbeddings
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains.combine_documents import create_stuff_documents_chain
from pinecone import Pinecone
import os

OPENAI_KEY = os.getenv('OPENAI_API_KEY')
PINECONE_API_KEY = os.getenv('PINECONE_API_KEY')

# Initialize OpenAI Embeddings
# embeddings = OpenAIEmbeddings(openai_api_key=OPENAI_KEY, model = "text-embedding-ada-002")
embeddings = OpenAIEmbeddings(openai_api_key=OPENAI_KEY, model = "text-embedding-3-small")

# Initialize OpenAI Chat Model
llm = ChatOpenAI(temperature=0.6, openai_api_key=OPENAI_KEY, model="gpt-4o-mini")

# Reinitialize Pinecone and load the vector store
Pinecone = Pinecone(api_key=PINECONE_API_KEY)
index_name = 'langchain2'
vectorstore = PineconeVectorStore(index_name=index_name, embedding=embeddings)

# Query the vector store
#query = "What was the revenue from operations for quarter ending 30.09.2024?"
query = "What dividends per unitholder have been distributed for the last few quarters? "
results = vectorstore.similarity_search(query, k=20)
#print(results)

# Use the retrieved context to generate an answer
prompt = ChatPromptTemplate.from_template("Based on this {context}, provide the answer to {question}")
chain = create_stuff_documents_chain(llm, prompt)

result = chain.invoke({"context": results, "question": query})
print(result)
