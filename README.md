# RAG-QA-System

A Retrieval-Augmented Generation (RAG) based question answering system.

## Project Overview

This project implements a complete RAG-based intelligent question answering system that supports document upload, knowledge base construction, and intelligent question answering. The system is based on local Ollama models and can run without network connection.

## Features

- 馃摎 Supports PDF, DOCX, and TXT document upload and batch processing
- 馃攳 Intelligent document retrieval, returning the most relevant text chunks
- 馃 Local large language models based on Ollama (deepseek-r1:7b / qwen2:7b)
- 馃挰 Interactive web Q&A interface with multi-turn conversation support
- 鈿?Real-time answer generation with session memory
- 馃搳 Chroma-based vector database
- 馃摝 Supports packaging as standalone EXE executable

## Technology Stack

- **Framework**: Streamlit
- **Language Model**: Ollama (deepseek-r1:7b / qwen2:7b)
- **Embedding Model**: Ollama (nomic-embed-text / all-minilm)
- **Vector Database**: Chroma
- **Document Processing**: PyPDF2, python-docx
- **Framework**: LangChain

## Environment Requirements

- Python 3.8+
- Ollama (running locally)
- At least 8GB RAM (16GB+ recommended)

## Installation Steps

### 1. Install Ollama

```bash
# Windows: https://ollama.com/download/windows
# macOS: https://ollama.com/download/mac
# Linux: curl -fsSL https://ollama.com/install.sh | sh
```

### 2. Download Models

```bash
ollama pull deepseek-r1:7b
ollama pull nomic-embed-text
# Or use qwen2 model
ollama pull qwen2:7b
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Application

**Method 1: Web Interface**
```bash
streamlit run app.py
```

**Method 2: Command Line Version**
```bash
python rag_qa_chain.py
```

### 5. Package as EXE (Optional)

```bash
pip install pyinstaller
pyinstaller rag_qa.spec
```

## Usage Instructions

### Web Interface Usage

1. **Upload Documents**: Click the file upload area and select PDF, DOCX, or TXT files
2. **Build Knowledge Base**: Click "Build Knowledge Base" button to process documents
3. **Ask Questions**: Type your question in the input box and press Enter
4. **Chat History**: The system automatically saves conversation history

### Command Line Usage

```python
from rag_qa_chain import RAGQASystem

rag = RAGQASystem()
rag.load_knowledge_base()
rag.build_qa_chain()

answer = rag.ask("What is Transformer?")
print(answer)
```

## Project Structure

```
.
鈹溾攢鈹€ app.py                # Streamlit web application entry
鈹溾攢鈹€ knowledge_base.py     # Knowledge base construction and retrieval module
鈹溾攢鈹€ rag_qa_chain.py       # RAG QA chain (command line version)
鈹溾攢鈹€ test_ollama.py        # Ollama API test script
鈹溾攢鈹€ rag_qa.spec           # PyInstaller packaging configuration
鈹溾攢鈹€ requirements.txt      # Dependency list
鈹溾攢鈹€ .gitignore            # Git ignore configuration
鈹溾攢鈹€ data/                 # Sample documents directory
鈹?  鈹溾攢鈹€ nlp_introduction.txt       # NLP introduction
鈹?  鈹溾攢鈹€ transformer_architecture.txt # Transformer architecture
鈹?  鈹溾攢鈹€ bert_model.txt             # BERT model explanation
鈹?  鈹溾攢鈹€ text_classification.txt    # Text classification techniques
鈹?  鈹斺攢鈹€ sentiment_analysis.txt     # Sentiment analysis techniques
鈹溾攢鈹€ chroma_db/            # Chroma vector database storage
鈹斺攢鈹€ README.md             # Project documentation
```

## Key Technical Points

### RAG Process

1. **Document Loading**: Supports PDF, DOCX, TXT formats
2. **Text Chunking**: Uses RecursiveCharacterTextSplitter (chunk_size=1000, chunk_overlap=200)
3. **Vectorization**: Uses Ollama embedding model (nomic-embed-text)
4. **Vector Storage**: Uses Chroma vector database
5. **Retrieval**: Similarity-based text retrieval
6. **Generation**: Uses ConversationalRetrievalChain to connect retriever and large model

### System Prompt

```
Answer the question based on the provided reference documents.
If no relevant information is found in the documents, clearly say "No relevant answer found in the documents".
Please provide the answer directly without additional explanation.
```

## Q&A Test Examples

### Relevant Questions

| Question | Expected Answer |
|----------|----------------|
| What is Natural Language Processing? | NLP is a subfield of AI focusing on computer-human language interaction |
| What are the two main parts of Transformer architecture? | Encoder and Decoder |
| What are BERT's pre-training tasks? | Masked Language Modeling and Next Sentence Prediction |
| What are common text classification algorithms? | Naive Bayes, SVM, Logistic Regression, etc. |
| What are sentiment analysis application scenarios? | Social media monitoring, product review analysis, etc. |

### Irrelevant Questions

| Question | Expected Answer |
|----------|----------------|
| What is machine learning? | No relevant answer found in the documents |
| What is the weather today? | No relevant answer found in the documents |

## Known Issues and Improvement Directions

### Known Issues

- First model loading may take a long time
- Large document processing may consume significant memory

### Improvement Directions

- Support more document formats (Markdown, HTML)
- Add document summarization feature
- Support multilingual documents
- Optimize large document processing performance

## License

MIT License

## GitHub Repository

https://github.com/hhhtwo/RAG-QA-System-xnf-2405030226