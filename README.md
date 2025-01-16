# RAG using OpenAI, Pinecone and Langchain - PDF Embedding and Querying - 2025

This project demonstrates how to embed PDF documents using OpenAI embeddings, store the embeddings in Pinecone, and query the documents to extract relevant information. It uses LangChain, Pinecone, and OpenAI's GPT models.

---

## Features
- Load PDF documents and process them into smaller chunks.
- Embed the chunks using OpenAI's `text-embedding-ada-002` model.
- Store embeddings in Pinecone for efficient similarity search.
- Query the stored embeddings to retrieve relevant information.

---

## Prerequisites
Before running this project, ensure you have the following:
- Python 3.11 or later.
- An OpenAI API key.
- A Pinecone API key and an active Pinecone account.
- The required Python packages installed (see below).

---

## Installation
1. Clone this repository:
   ```bash
   git clone <repository_url>
   cd <repository_name>
   ```

2. Install the required Python packages:
   ```bash
   pip install langchain openai pinecone-client
   ```

3. Set up environment variables:
   - `OPENAI_API_KEY`: Your OpenAI API key.
   - `PINECONE_API_KEY`: Your Pinecone API key.

   You can create a `.env` file in the project directory:
   ```env
   OPENAI_API_KEY=your_openai_api_key
   PINECONE_API_KEY=your_pinecone_api_key
   ```

---

## Usage

### Step 1: Embed PDF and Store in Pinecone
See code in LoadPDF.py
```

### Step 2: Query the Stored Embeddings
See code in talktopdf.py

---

## Notes
- Use `text-embedding-ada-002` for cost-effective embeddings.
- Ensure the Pinecone index (`langchain1`) exists before querying.
- Check your Pinecone dashboard to monitor index usage.

---

## License
This project is licensed under the MIT License.

--

## Acknowledgments
- [LangChain Documentation](https://docs.langchain.com/)
- [OpenAI API Documentation](https://platform.openai.com/docs/)
- [Pinecone Documentation](https://www.pinecone.io/docs/)

