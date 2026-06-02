import streamlit as st
from langchain.document_loaders import PyPDFLoader, Docx2txtLoader, TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Chroma
from langchain.embeddings import OllamaEmbeddings
from langchain.chains import ConversationalRetrievalChain
from langchain.llms import Ollama
from langchain.memory import ConversationBufferMemory
from langchain.prompts import PromptTemplate
import tempfile
import os

st.set_page_config(page_title="RAG QA System", page_icon="馃", layout="wide")

st.title("馃摎 RAG 鏅鸿兘闂瓟绯荤粺")

if 'vector_store' not in st.session_state:
    st.session_state.vector_store = None
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []
if 'doc_count' not in st.session_state:
    st.session_state.doc_count = 0
if 'chunk_count' not in st.session_state:
    st.session_state.chunk_count = 0
if 'memory' not in st.session_state:
    st.session_state.memory = ConversationBufferMemory(
        memory_key="chat_history",
        return_messages=True
    )
if 'qa_chain' not in st.session_state:
    st.session_state.qa_chain = None

with st.sidebar:
    st.header("鈿欙笍 璁剧疆")
    model_name = st.selectbox("閫夋嫨璇█妯″瀷", ["deepseek-r1:7b", "qwen2:7b"])
    embedding_model = st.selectbox("閫夋嫨宓屽叆妯″瀷", ["nomic-embed-text", "all-minilm"])
    
    st.divider()
    
    st.subheader("馃搳 鐭ヨ瘑搴撶姸鎬?)
    st.info(f"宸插姞杞芥枃妗? {st.session_state.doc_count} 涓?)
    st.info(f"鏂囨湰鍧楁暟閲? {st.session_state.chunk_count} 涓?)
    
    if st.button("馃Ч 娓呴櫎瀵硅瘽鍘嗗彶"):
        st.session_state.chat_history = []
        st.session_state.memory = ConversationBufferMemory(
            memory_key="chat_history",
            return_messages=True
        )
        st.session_state.qa_chain = None
        st.success("瀵硅瘽鍘嗗彶宸叉竻闄?)
    
    if st.button("馃棏锔?娓呯┖鐭ヨ瘑搴?):
        st.session_state.vector_store = None
        st.session_state.doc_count = 0
        st.session_state.chunk_count = 0
        st.session_state.chat_history = []
        st.session_state.memory = ConversationBufferMemory(
            memory_key="chat_history",
            return_messages=True
        )
        st.session_state.qa_chain = None
        if os.path.exists("./chroma_db"):
            import shutil
            shutil.rmtree("./chroma_db")
        st.success("鐭ヨ瘑搴撳凡娓呯┖")

uploaded_files = st.file_uploader(
    "馃搧 涓婁紶鏂囨。",
    type=["pdf", "docx", "txt"],
    accept_multiple_files=True,
    help="鏀寔 PDF銆丏OCX銆乀XT 鏍煎紡鐨勬枃妗?
)

if uploaded_files:
    if st.button("馃殌 鏋勫缓鐭ヨ瘑搴?, type="primary"):
        with st.spinner("姝ｅ湪澶勭悊鏂囨。..."):
            docs = []
            for file in uploaded_files:
                with tempfile.NamedTemporaryFile(delete=False, suffix=os.path.splitext(file.name)[1]) as tmp:
                    tmp.write(file.getvalue())
                    tmp_path = tmp.name
                
                try:
                    if file.name.endswith('.pdf'):
                        loader = PyPDFLoader(tmp_path)
                    elif file.name.endswith('.docx'):
                        loader = Docx2txtLoader(tmp_path)
                    elif file.name.endswith('.txt'):
                        loader = TextLoader(tmp_path, encoding='utf-8')
                    
                    docs.extend(loader.load())
                    st.success(f"鉁?宸插姞杞? {file.name}")
                finally:
                    os.unlink(tmp_path)
            
            st.session_state.doc_count += len(uploaded_files)
            
            text_splitter = RecursiveCharacterTextSplitter(
                chunk_size=1000,
                chunk_overlap=200,
                length_function=len
            )
            split_docs = text_splitter.split_documents(docs)
            st.session_state.chunk_count += len(split_docs)
            
            embeddings = OllamaEmbeddings(model=embedding_model)
            
            if st.session_state.vector_store is None:
                st.session_state.vector_store = Chroma.from_documents(
                    split_docs,
                    embeddings,
                    persist_directory="./chroma_db"
                )
            else:
                st.session_state.vector_store.add_documents(split_docs)
            
            st.session_state.vector_store.persist()
            st.success(f"馃帀 鐭ヨ瘑搴撴瀯寤哄畬鎴愶紒鍏?{len(split_docs)} 涓枃鏈潡")

st.divider()

st.subheader("馃挰 闂瓟浜や簰")

for msg in st.session_state.chat_history:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

def build_qa_chain():
    if st.session_state.vector_store is None:
        return None
    
    llm = Ollama(model=model_name)
    embeddings = OllamaEmbeddings(model=embedding_model)
    
    retriever = st.session_state.vector_store.as_retriever()
    
    system_prompt = """
鍩轰簬鎻愪緵鐨勫弬鑰冩枃妗ｅ洖绛旈棶棰樸€?濡傛灉鏂囨。涓病鏈夌浉鍏充俊鎭紝璇锋槑纭"鏂囨。涓湭鎵惧埌鐩稿叧绛旀"銆?璇风洿鎺ョ粰鍑虹瓟妗堬紝涓嶉渶瑕侀澶栬鏄庛€?    """.strip()
    
    prompt = PromptTemplate(
        template=system_prompt + "\n\n涓婁笅鏂?\n{context}\n\n闂:\n{question}",
        input_variables=["context", "question"]
    )
    
    qa_chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=retriever,
        memory=st.session_state.memory,
        combine_docs_chain_kwargs={"prompt": prompt},
        verbose=False
    )
    
    return qa_chain

if query := st.chat_input("璇疯緭鍏ユ偍鐨勯棶棰?.."):
    if st.session_state.vector_store is None:
        st.warning("鈿狅笍 璇峰厛涓婁紶鏂囨。骞舵瀯寤虹煡璇嗗簱")
    else:
        with st.chat_message("user"):
            st.write(query)
        st.session_state.chat_history.append({"role": "user", "content": query})
        
        with st.chat_message("assistant"):
            with st.spinner("姝ｅ湪鎬濊€?.."):
                if st.session_state.qa_chain is None:
                    st.session_state.qa_chain = build_qa_chain()
                
                result = st.session_state.qa_chain({"question": query})
                answer = result["answer"]
                st.write(answer)
        
        st.session_state.chat_history.append({"role": "assistant", "content": answer})

st.divider()

st.subheader("馃摉 浣跨敤璇存槑")
st.markdown("""
1. **涓婁紶鏂囨。**: 鐐瑰嚮涓婃柟鏂囦欢涓婁紶鍖哄煙锛岄€夋嫨 PDF銆丏OCX 鎴?TXT 鏍煎紡鐨勬枃妗?2. **鏋勫缓鐭ヨ瘑搴?*: 鐐瑰嚮"鏋勫缓鐭ヨ瘑搴?鎸夐挳锛岀郴缁熶細鑷姩瑙ｆ瀽鏂囨。骞跺垱寤哄悜閲忔暟鎹簱
3. **鎻愰棶**: 鍦ㄤ笅鏂硅緭鍏ユ涓緭鍏ラ棶棰橈紝鐐瑰嚮鍙戦€佸嵆鍙幏寰楀洖绛?4. **瀵硅瘽鍘嗗彶**: 绯荤粺浼氳嚜鍔ㄤ繚瀛樺璇濆巻鍙诧紝鏀寔澶氳疆瀵硅瘽

**娉ㄦ剰**: 浣跨敤鍓嶈纭繚宸插畨瑁?Ollama 骞朵笅杞界浉鍏虫ā鍨嬶細
- `ollama pull deepseek-r1:7b`
- `ollama pull nomic-embed-text`
""")