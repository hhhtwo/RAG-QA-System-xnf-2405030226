from langchain.chains import ConversationalRetrievalChain
from langchain.llms import Ollama
from langchain.embeddings import OllamaEmbeddings
from langchain.vectorstores import Chroma
from langchain.memory import ConversationBufferMemory
from langchain.prompts import PromptTemplate
from knowledge_base import KnowledgeBase

class RAGQASystem:
    def __init__(self, model_name="deepseek-r1:7b", embedding_model="nomic-embed-text"):
        self.model_name = model_name
        self.embedding_model = embedding_model
        self.kb = KnowledgeBase()
        self.llm = Ollama(model=model_name)
        self.embeddings = OllamaEmbeddings(model=embedding_model)
        self.memory = ConversationBufferMemory(
            memory_key="chat_history",
            return_messages=True
        )
        self.qa_chain = None
        
        self.system_prompt = """
Answer the question based on the provided reference documents.
If no relevant information is found in the documents, clearly say "No relevant answer found in the documents".
Please provide the answer directly without additional explanation.
        """.strip()

    def load_knowledge_base(self, data_dir="./data"):
        try:
            documents = self.kb.load_documents(data_dir)
            if documents:
                self.kb.build_vector_db(documents)
                print(f"Knowledge base loaded with {len(documents)} documents")
            else:
                print("No documents found, attempting to load from existing vector database...")
                self.kb.vector_store = Chroma(
                    persist_directory=self.kb.persist_directory,
                    embedding_function=self.embeddings
                )
        except Exception as e:
            print(f"Failed to load knowledge base: {e}")
            print("Attempting to load from existing vector database...")
            self.kb.vector_store = Chroma(
                persist_directory=self.kb.persist_directory,
                embedding_function=self.embeddings
            )

    def build_qa_chain(self):
        retriever = self.kb.get_retriever()
        
        prompt = PromptTemplate(
            template=self.system_prompt + "\n\nContext:\n{context}\n\nQuestion:\n{question}",
            input_variables=["context", "question"]
        )
        
        self.qa_chain = ConversationalRetrievalChain.from_llm(
            llm=self.llm,
            retriever=retriever,
            memory=self.memory,
            combine_docs_chain_kwargs={"prompt": prompt},
            verbose=False
        )

    def ask(self, question):
        if self.qa_chain is None:
            self.build_qa_chain()
        
        result = self.qa_chain({"question": question})
        return result["answer"]

    def clear_history(self):
        self.memory.clear()

def test_rag_system():
    print("=== RAG Question Answering System Test ===")
    
    rag = RAGQASystem()
    rag.load_knowledge_base()
    rag.build_qa_chain()
    
    test_questions = [
        ("What is Natural Language Processing?", "Relevant Question"),
        ("What are the two main parts of the Transformer architecture?", "Relevant Question"),
        ("What are the pre-training tasks of BERT?", "Relevant Question"),
        ("What are common text classification algorithms?", "Relevant Question"),
        ("What are the application scenarios of sentiment analysis?", "Relevant Question"),
        ("What is machine learning?", "Irrelevant Question"),
        ("What is the weather today?", "Irrelevant Question")
    ]
    
    print("\n--- Starting Tests ---")
    for question, category in test_questions:
        print(f"\n銆恵category}銆?)
        print(f"Question: {question}")
        try:
            answer = rag.ask(question)
            print(f"Answer: {answer}")
        except Exception as e:
            print(f"Answer Failed: {e}")
    
    print("\n--- Tests Completed ---")

if __name__ == "__main__":
    test_rag_system()