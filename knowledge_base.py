import os
from langchain_community.document_loaders import PyPDFLoader, Docx2txtLoader, TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import OllamaEmbeddings

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
        
        print(f"浠?{directory_path} 鍔犺浇浜?{len(documents)} 涓枃妗?)
        return documents

    def split_documents(self, documents, chunk_size=1000, chunk_overlap=200):
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
            length_function=len,
            separators=["\n\n", "\n", " ", ""]
        )
        split_docs = text_splitter.split_documents(documents)
        print(f"鍒囧垎涓?{len(split_docs)} 涓枃鏈潡")
        return split_docs

    def build_vector_db(self, documents):
        split_docs = self.split_documents(documents)
        self.vector_store = Chroma.from_documents(
            documents=split_docs,
            embedding=self.embeddings,
            persist_directory=self.persist_directory
        )
        self.vector_store.persist()
        print(f"鍚戦噺鏁版嵁搴撴瀯寤哄畬鎴愬苟淇濆瓨鍒?{self.persist_directory}")

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
    
    print("\n姝ｅ湪娴嬭瘯鎼滅储鍔熻兘...")
    query = "浠€涔堟槸 Transformer?"
    results = kb.search(query)
    
    print(f"\n鏌ヨ: {query}")
    print(f"鎵惧埌 {len(results)} 涓浉鍏虫枃鏈潡:")
    for i, result in enumerate(results, 1):
        print(f"\n--- 缁撴灉 {i} ---")
        print(f"鏉ユ簮: {result.metadata.get('source', '鏈煡')}")
        print(f"鍐呭:\n{result.page_content[:200]}...")

if __name__ == "__main__":
    main()