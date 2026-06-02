from langchain.chains import ConversationalRetrievalChain
from langchain_community.llms import Ollama
from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.vectorstores import Chroma
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
鍩轰簬鎻愪緵鐨勫弬鑰冩枃妗ｅ洖绛旈棶棰樸€?
濡傛灉鏂囨。涓病鏈夋壘鍒扮浉鍏充俊鎭紝璇锋槑纭"鏂囨。涓湭鎵惧埌鐩稿叧绛旀"銆?
璇风洿鎺ユ彁渚涚瓟妗堬紝涓嶈棰濆瑙ｉ噴銆?
        """.strip()

    def load_knowledge_base(self, data_dir="./data"):
        try:
            documents = self.kb.load_documents(data_dir)
            if documents:
                self.kb.build_vector_db(documents)
                print(f"鐭ヨ瘑搴撳凡鍔犺浇锛屽叡 {len(documents)} 涓枃妗?)
            else:
                print("鏈壘鍒版枃妗ｏ紝灏濊瘯浠庣幇鏈夊悜閲忔暟鎹簱鍔犺浇...")
                self.kb.vector_store = Chroma(
                    persist_directory=self.kb.persist_directory,
                    embedding_function=self.embeddings
                )
        except Exception as e:
            print(f"鍔犺浇鐭ヨ瘑搴撳け璐? {e}")
            print("灏濊瘯浠庣幇鏈夊悜閲忔暟鎹簱鍔犺浇...")
            self.kb.vector_store = Chroma(
                persist_directory=self.kb.persist_directory,
                embedding_function=self.embeddings
            )

    def build_qa_chain(self):
        retriever = self.kb.get_retriever()
        
        prompt = PromptTemplate(
            template=self.system_prompt + "\n\n涓婁笅鏂?\n{context}\n\n闂:\n{question}",
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
    print("=== RAG 闂瓟绯荤粺娴嬭瘯 ===")
    
    rag = RAGQASystem()
    rag.load_knowledge_base()
    rag.build_qa_chain()
    
    test_questions = [
        ("浠€涔堟槸鑷劧璇█澶勭悊?", "鐩稿叧闂"),
        ("Transformer 鏋舵瀯鐨勪袱涓富瑕侀儴鍒嗘槸浠€涔?", "鐩稿叧闂"),
        ("BERT 鐨勯璁粌浠诲姟鏄粈涔?", "鐩稿叧闂"),
        ("甯歌鐨勬枃鏈垎绫荤畻娉曟湁鍝簺?", "鐩稿叧闂"),
        ("鎯呮劅鍒嗘瀽鐨勫簲鐢ㄥ満鏅湁鍝簺?", "鐩稿叧闂"),
        ("浠€涔堟槸鏈哄櫒瀛︿範?", "鏃犲叧闂"),
        ("浠婂ぉ澶╂皵鎬庝箞鏍?", "鏃犲叧闂")
    ]
    
    print("\n--- 寮€濮嬫祴璇?---")
    for question, category in test_questions:
        print(f"\n銆恵category}銆?)
        print(f"闂: {question}")
        try:
            answer = rag.ask(question)
            print(f"鍥炵瓟: {answer}")
        except Exception as e:
            print(f"鍥炵瓟澶辫触: {e}")
    
    print("\n--- 娴嬭瘯瀹屾垚 ---")

if __name__ == "__main__":
    test_rag_system()