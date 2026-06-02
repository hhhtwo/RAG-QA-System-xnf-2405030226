# RAG-QA-System

鍩轰簬妫€绱㈠寮虹敓鎴愶紙RAG锛夌殑鏅鸿兘闂瓟绯荤粺椤圭洰

## 鍔熻兘鐗规€?
- 馃摎 鏀寔 PDF銆丏OCX銆乀XT 鏂囨。涓婁紶鍜屾壒閲忓鐞?- 馃攳 鏅鸿兘鏂囨。妫€绱紝杩斿洖鏈€鐩稿叧鐨勬枃鏈潡
- 馃 鍩轰簬 Ollama 鐨勬湰鍦板寲澶ц瑷€妯″瀷
- 馃挰 浜や簰寮忛棶绛旂晫闈?- 鈿?瀹炴椂鍥炵瓟鐢熸垚
- 馃搳 鍩轰簬 Chroma 鐨勫悜閲忔暟鎹簱

## 鎶€鏈爤

- **妗嗘灦**: Streamlit
- **璇█妯″瀷**: Ollama (deepseek-r1:7b / qwen2:7b)
- **宓屽叆妯″瀷**: Ollama (nomic-embed-text / all-minilm)
- **鍚戦噺鏁版嵁搴?*: Chroma
- **鏂囨。澶勭悊**: PyPDF2, python-docx
- **妗嗘灦**: LangChain

## 蹇€熷紑濮?
### 鐜瑕佹眰

- Python 3.8+
- Ollama (鏈湴杩愯)

### 瀹夎姝ラ

1. **瀹夎 Ollama**
   ```bash
   # 涓嬭浇骞跺畨瑁?Ollama
   # Windows: https://ollama.com/download/windows
   # macOS: https://ollama.com/download/mac
   # Linux: curl -fsSL https://ollama.com/install.sh | sh
   ```

2. **涓嬭浇妯″瀷**
   ```bash
   ollama pull deepseek-r1:7b
   ollama pull nomic-embed-text
   # 鎴栦娇鐢?qwen2 妯″瀷
   ollama pull qwen2:7b
   ```

3. **瀹夎渚濊禆**
   ```bash
   pip install -r requirements.txt
   ```

4. **杩愯椤圭洰**
   ```bash
   streamlit run app.py
   ```

## 浣跨敤璇存槑

### 鏂规硶涓€锛氫娇鐢?Web 鐣岄潰
1. 鍚姩搴旂敤鍚庯紝鍦ㄤ晶杈规爮閫夋嫨浣跨敤鐨勬ā鍨?2. 涓婁紶 PDF銆丏OCX 鎴?TXT 鏍煎紡鐨勬枃妗?3. 绛夊緟鏂囨。澶勭悊瀹屾垚
4. 鍦ㄨ緭鍏ユ涓緭鍏ラ棶棰橈紝鑾峰彇鍩轰簬鏂囨。鍐呭鐨勫洖绛?
### 鏂规硶浜岋細浣跨敤鐭ヨ瘑搴撹剼鏈?```bash
python knowledge_base.py
```

## 椤圭洰缁撴瀯

```
.
鈹溾攢鈹€ app.py              # 涓诲簲鐢ㄥ叆鍙?(Streamlit)
鈹溾攢鈹€ knowledge_base.py   # 鐭ヨ瘑搴撴瀯寤轰笌妫€绱㈡ā鍧?鈹溾攢鈹€ test_ollama.py      # Ollama API 娴嬭瘯鑴氭湰
鈹溾攢鈹€ requirements.txt    # 渚濊禆鍒楄〃
鈹溾攢鈹€ push-to-github.ps1  # GitHub 鎺ㄩ€佽剼鏈?鈹溾攢鈹€ data/               # 绀轰緥鏂囨。鐩綍
鈹?  鈹溾攢鈹€ nlp_introduction.txt       # NLP 鍏ラ棬浠嬬粛
鈹?  鈹溾攢鈹€ transformer_architecture.txt # Transformer 鏋舵瀯璇﹁В
鈹?  鈹溾攢鈹€ bert_model.txt             # BERT 妯″瀷璇﹁В
鈹?  鈹溾攢鈹€ text_classification.txt    # 鏂囨湰鍒嗙被鎶€鏈?鈹?  鈹斺攢鈹€ sentiment_analysis.txt     # 鎯呮劅鍒嗘瀽鎶€鏈?鈹溾攢鈹€ chroma_db/          # Chroma 鍚戦噺鏁版嵁搴撳瓨鍌ㄧ洰褰?鈹斺攢鈹€ README.md           # 椤圭洰璇存槑
```

## 鐭ヨ瘑搴撴ā鍧?
### KnowledgeBase 绫?
`knowledge_base.py` 鎻愪緵浜嗗畬鏁寸殑鐭ヨ瘑搴撳姛鑳斤細

#### 鏍稿績鏂规硶

1. **load_documents(directory_path)**: 鎵归噺璇诲彇鎸囧畾鐩綍涓嬬殑鎵€鏈夋枃妗?   - 鏀寔鏍煎紡: PDF銆丏OCX銆乀XT

2. **split_documents(documents, chunk_size=1000, chunk_overlap=200)**: 鏂囨湰鍒嗗潡
   - 浣跨敤 RecursiveCharacterTextSplitter
   - 榛樿 chunk_size=1000, chunk_overlap=200

3. **build_vector_db(documents)**: 鏋勫缓鍚戦噺鏁版嵁搴?   - 浣跨敤 OllamaEmbeddings (nomic-embed-text)
   - 瀛樺偍鍒?Chroma 鍚戦噺鏁版嵁搴?
4. **search(query, k=3)**: 妫€绱㈠嚱鏁?   - 缁欏畾鏌ヨ锛岃繑鍥炴渶鐩稿叧鐨?k 涓枃鏈潡
   - 榛樿杩斿洖鍓?3 涓渶鐩稿叧缁撴灉

### 浣跨敤绀轰緥

```python
from knowledge_base import KnowledgeBase

kb = KnowledgeBase()
documents = kb.load_documents("./data")
kb.build_vector_db(documents)

results = kb.search("浠€涔堟槸Transformer?", k=3)
for i, result in enumerate(results, 1):
    print(f"缁撴灉 {i}: {result.page_content}")
```

## API 娴嬭瘯

杩愯娴嬭瘯鑴氭湰鏉ラ獙璇?Ollama API锛?
```bash
python test_ollama.py
```

## 璁稿彲璇?
MIT License