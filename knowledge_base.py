import os
from langchain.document_loaders import PyPDFLoader, Docx2txtLoader, TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Chroma
from langchain.embeddings import OllamaEmbeddings

class KnowledgeBase:
    def __init__(self, persist_directory="./chroma_db"):
        self.persist_directory = persist_directory
        self.embeddings = OllamaEmbeddings(model="nomic-embed-text")
        self.vector_store = None

    def load_documents(self, directory_path):
        documents = []
        
        for filename in os.listdir(directory_path):
            file_path = os.path.join(directory_path, filename)
            
            if filename.endswith('.pdf'):
                loader = PyPDFLoader(file_path)
                docs = loader.load()
                documents.extend(docs)
            elif filename.endswith('.docx'):
                loader = Docx2txtLoader(file_path)
                docs = loader.load()
                documents.extend(docs)
            elif filename.endswith('.txt'):
                loader = TextLoader(file_path, encoding='utf-8')
                docs = loader.load()
                documents.extend(docs)
        
        print(f"Loaded {len(documents)} documents from {directory_path}")
        return documents

    def split_documents(self, documents, chunk_size=1000, chunk_overlap=200):
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
            length_function=len,
            separators=["\n\n", "\n", " ", ""]
        )
        split_docs = text_splitter.split_documents(documents)
        print(f"Split into {len(split_docs)} chunks")
        return split_docs

    def build_vector_db(self, documents):
        split_docs = self.split_documents(documents)
        self.vector_store = Chroma.from_documents(
            documents=split_docs,
            embedding=self.embeddings,
            persist_directory=self.persist_directory
        )
        self.vector_store.persist()
        print(f"Vector database built and saved to {self.persist_directory}")

    def search(self, query, k=3):
        if self.vector_store is None:
            self.vector_store = Chroma(
                persist_directory=self.persist_directory,
                embedding_function=self.embeddings
            )
        
        results = self.vector_store.similarity_search(query, k=k)
        return results

    def get_retriever(self):
        if self.vector_store is None:
            self.vector_store = Chroma(
                persist_directory=self.persist_directory,
                embedding_function=self.embeddings
            )
        return self.vector_store.as_retriever()

def main():
    kb = KnowledgeBase()
    documents = kb.load_documents("./data")
    kb.build_vector_db(documents)
    
    print("\nTesting search function...")
    query = "What is Transformer?"
    results = kb.search(query)
    
    print(f"\nQuery: {query}")
    print(f"Found {len(results)} relevant chunks:")
    for i, result in enumerate(results, 1):
        print(f"\n--- Result {i} ---")
        print(f"Source: {result.metadata.get('source', 'Unknown')}")
        print(f"Content:\n{result.page_content[:200]}...")

if __name__ == "__main__":
    main()