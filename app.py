import streamlit as st
from langchain.document_loaders import PyPDFLoader, Docx2txtLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import Chroma
from langchain.embeddings import OllamaEmbeddings
from langchain.chains import RetrievalQA
from langchain.llms import Ollama
import tempfile
import os

st.set_page_config(page_title="RAG QA System", page_icon="馃")

st.title("RAG QA System")
st.sidebar.title("Settings")

model_name = st.sidebar.selectbox("Select Model", ["deepseek-r1:7b", "qwen2:7b"])

@st.cache_resource
def init_chain():
    try:
        embeddings = OllamaEmbeddings(model=model_name)
        llm = Ollama(model=model_name)
        return embeddings, llm
    except Exception as e:
        st.error(f"Failed to initialize Ollama: {e}")
        return None, None

embeddings, llm = init_chain()

if 'vector_store' not in st.session_state:
    st.session_state.vector_store = None

uploaded_files = st.file_uploader("Upload documents", type=["pdf", "docx"], accept_multiple_files=True)

if uploaded_files and embeddings:
    with st.spinner("Processing documents..."):
        docs = []
        for file in uploaded_files:
            with tempfile.NamedTemporaryFile(delete=False, suffix=os.path.splitext(file.name)[1]) as tmp:
                tmp.write(file.getvalue())
                tmp_path = tmp.name
            
            if file.name.endswith('.pdf'):
                loader = PyPDFLoader(tmp_path)
            elif file.name.endswith('.docx'):
                loader = Docx2txtLoader(tmp_path)
            
            docs.extend(loader.load())
            os.unlink(tmp_path)
        
        text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
        split_docs = text_splitter.split_documents(docs)
        
        st.session_state.vector_store = Chroma.from_documents(split_docs, embeddings)
        st.success(f"Processed {len(split_docs)} document chunks")

query = st.text_input("Ask a question about your documents:")

if query and st.session_state.vector_store and llm:
    with st.spinner("Generating answer..."):
        qa_chain = RetrievalQA.from_chain_type(
            llm=llm,
            chain_type="stuff",
            retriever=st.session_state.vector_store.as_retriever()
        )
        result = qa_chain.run(query)
        st.write("### Answer:")
        st.write(result)
elif query and not st.session_state.vector_store:
    st.warning("Please upload documents first")