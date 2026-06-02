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

st.title("馃摎 RAG Question Answering System")

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
    st.header("鈿欙笍 Settings")
    model_name = st.selectbox("Select Language Model", ["deepseek-r1:7b", "qwen2:7b"])
    embedding_model = st.selectbox("Select Embedding Model", ["nomic-embed-text", "all-minilm"])
    
    st.divider()
    
    st.subheader("馃搳 Knowledge Base Status")
    st.info(f"Documents Loaded: {st.session_state.doc_count}")
    st.info(f"Text Chunks: {st.session_state.chunk_count}")
    
    if st.button("馃Ч Clear Chat History"):
        st.session_state.chat_history = []
        st.session_state.memory = ConversationBufferMemory(
            memory_key="chat_history",
            return_messages=True
        )
        st.session_state.qa_chain = None
        st.success("Chat history cleared")
    
    if st.button("馃棏锔?Clear Knowledge Base"):
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
        st.success("Knowledge base cleared")

uploaded_files = st.file_uploader(
    "馃搧 Upload Documents",
    type=["pdf", "docx", "txt"],
    accept_multiple_files=True,
    help="Supports PDF, DOCX, and TXT formats"
)

if uploaded_files:
    if st.button("馃殌 Build Knowledge Base", type="primary"):
        with st.spinner("Processing documents..."):
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
                    st.success(f"鉁?Loaded: {file.name}")
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
            st.success(f"馃帀 Knowledge Base Built! {len(split_docs)} chunks created")

st.divider()

st.subheader("馃挰 Question & Answer")

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
Answer the question based on the provided reference documents.
If no relevant information is found in the documents, clearly say "No relevant answer found in the documents".
Please provide the answer directly without additional explanation.
    """.strip()
    
    prompt = PromptTemplate(
        template=system_prompt + "\n\nContext:\n{context}\n\nQuestion:\n{question}",
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

if query := st.chat_input("Enter your question..."):
    if st.session_state.vector_store is None:
        st.warning("鈿狅笍 Please upload documents and build knowledge base first")
    else:
        with st.chat_message("user"):
            st.write(query)
        st.session_state.chat_history.append({"role": "user", "content": query})
        
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                if st.session_state.qa_chain is None:
                    st.session_state.qa_chain = build_qa_chain()
                
                result = st.session_state.qa_chain({"question": query})
                answer = result["answer"]
                st.write(answer)
        
        st.session_state.chat_history.append({"role": "assistant", "content": answer})

st.divider()

st.subheader("馃摉 Usage Instructions")
st.markdown("""
1. **Upload Documents**: Click the file upload area above and select PDF, DOCX, or TXT files
2. **Build Knowledge Base**: Click "Build Knowledge Base" button to process documents
3. **Ask Questions**: Type your question in the input box below and press Enter
4. **Chat History**: The system will automatically save conversation history

**Note**: Before using, ensure Ollama is installed and models are downloaded:
- `ollama pull deepseek-r1:7b`
- `ollama pull nomic-embed-text`
""")