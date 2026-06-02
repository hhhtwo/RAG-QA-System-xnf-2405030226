# RAG-QA-System

鍩轰簬妫€绱㈠寮虹敓鎴愶紙RAG锛夌殑鏅鸿兘闂瓟绯荤粺椤圭洰

## 椤圭洰绠€浠?
鏈」鐩疄鐜颁簡涓€涓畬鏁寸殑RAG鏅鸿兘闂瓟绯荤粺锛屾敮鎸佹枃妗ｄ笂浼犮€佺煡璇嗗簱鏋勫缓銆佹櫤鑳介棶绛旂瓑鍔熻兘銆傜郴缁熷熀浜嶰llama鏈湴鍖栨ā鍨嬶紝鏃犻渶鑱旂綉鍗冲彲杩愯銆?
## 鍔熻兘鐗规€?
- 馃摎 鏀寔 PDF銆丏OCX銆乀XT 鏂囨。涓婁紶鍜屾壒閲忓鐞?- 馃攳 鏅鸿兘鏂囨。妫€绱紝杩斿洖鏈€鐩稿叧鐨勬枃鏈潡
- 馃 鍩轰簬 Ollama 鐨勬湰鍦板寲澶ц瑷€妯″瀷锛坉eepseek-r1:7b / qwen2:7b锛?- 馃挰 浜や簰寮?Web 闂瓟鐣岄潰锛屾敮鎸佸杞璇?- 鈿?瀹炴椂鍥炵瓟鐢熸垚锛屾敮鎸佷細璇濊蹇?- 馃搳 鍩轰簬 Chroma 鐨勫悜閲忔暟鎹簱
- 馃摝 鏀寔鎵撳寘涓虹嫭绔?exe 鍙墽琛屾枃浠?
## 鎶€鏈爤

- **妗嗘灦**: Streamlit
- **璇█妯″瀷**: Ollama (deepseek-r1:7b / qwen2:7b)
- **宓屽叆妯″瀷**: Ollama (nomic-embed-text / all-minilm)
- **鍚戦噺鏁版嵁搴?*: Chroma
- **鏂囨。澶勭悊**: PyPDF2, python-docx
- **妗嗘灦**: LangChain

## 鐜瑕佹眰

- Python 3.8+
- Ollama (鏈湴杩愯)
- 鑷冲皯 8GB 鍐呭瓨锛堝缓璁?16GB+锛?
## 瀹夎姝ラ

### 1. 瀹夎 Ollama

```bash
# Windows: https://ollama.com/download/windows
# macOS: https://ollama.com/download/mac
# Linux: curl -fsSL https://ollama.com/install.sh | sh
```

### 2. 涓嬭浇妯″瀷

```bash
ollama pull deepseek-r1:7b
ollama pull nomic-embed-text
# 鎴栦娇鐢?qwen2 妯″瀷
ollama pull qwen2:7b
```

### 3. 瀹夎渚濊禆

```bash
pip install -r requirements.txt
```

### 4. 杩愯椤圭洰

**鏂瑰紡涓€锛歐eb 鐣岄潰**
```bash
streamlit run app.py
```

**鏂瑰紡浜岋細鍛戒护琛岀増鏈?*
```bash
python rag_qa_chain.py
```

### 5. 鎵撳寘涓?EXE锛堝彲閫夛級

```bash
pip install pyinstaller
pyinstaller rag_qa.spec
```

## 浣跨敤璇存槑

### Web 鐣岄潰浣跨敤

1. **涓婁紶鏂囨。**: 鐐瑰嚮鏂囦欢涓婁紶鍖哄煙锛岄€夋嫨 PDF銆丏OCX 鎴?TXT 鏍煎紡鐨勬枃妗?2. **鏋勫缓鐭ヨ瘑搴?*: 鐐瑰嚮"鏋勫缓鐭ヨ瘑搴?鎸夐挳锛岀郴缁熶細鑷姩瑙ｆ瀽鏂囨。骞跺垱寤哄悜閲忔暟鎹簱
3. **鎻愰棶**: 鍦ㄨ緭鍏ユ涓緭鍏ラ棶棰橈紝鐐瑰嚮鍙戦€佸嵆鍙幏寰楀洖绛?4. **瀵硅瘽鍘嗗彶**: 绯荤粺浼氳嚜鍔ㄤ繚瀛樺璇濆巻鍙诧紝鏀寔澶氳疆瀵硅瘽

### 鍛戒护琛屼娇鐢?
```python
from rag_qa_chain import RAGQASystem

rag = RAGQASystem()
rag.load_knowledge_base()
rag.build_qa_chain()

answer = rag.ask("浠€涔堟槸Transformer?")
print(answer)
```

## 椤圭洰缁撴瀯

```
.
鈹溾攢鈹€ app.py                # Streamlit Web 搴旂敤鍏ュ彛
鈹溾攢鈹€ knowledge_base.py     # 鐭ヨ瘑搴撴瀯寤轰笌妫€绱㈡ā鍧?鈹溾攢鈹€ rag_qa_chain.py       # RAG 闂瓟閾撅紙鍛戒护琛岀増鏈級
鈹溾攢鈹€ test_ollama.py        # Ollama API 娴嬭瘯鑴氭湰
鈹溾攢鈹€ rag_qa.spec           # PyInstaller 鎵撳寘閰嶇疆
鈹溾攢鈹€ requirements.txt      # 渚濊禆鍒楄〃
鈹溾攢鈹€ .gitignore            # Git 蹇界暐鏂囦欢閰嶇疆
鈹溾攢鈹€ data/                 # 绀轰緥鏂囨。鐩綍
鈹?  鈹溾攢鈹€ nlp_introduction.txt       # NLP 鍏ラ棬浠嬬粛
鈹?  鈹溾攢鈹€ transformer_architecture.txt # Transformer 鏋舵瀯璇﹁В
鈹?  鈹溾攢鈹€ bert_model.txt             # BERT 妯″瀷璇﹁В
鈹?  鈹溾攢鈹€ text_classification.txt    # 鏂囨湰鍒嗙被鎶€鏈?鈹?  鈹斺攢鈹€ sentiment_analysis.txt     # 鎯呮劅鍒嗘瀽鎶€鏈?鈹溾攢鈹€ chroma_db/            # Chroma 鍚戦噺鏁版嵁搴撳瓨鍌ㄧ洰褰?鈹斺攢鈹€ README.md             # 椤圭洰璇存槑
```

## 鍏抽敭鎶€鏈偣

### RAG 娴佺▼

1. **鏂囨。鍔犺浇**: 鏀寔 PDF銆丏OCX銆乀XT 澶氱鏍煎紡
2. **鏂囨湰鍒嗗潡**: 浣跨敤 RecursiveCharacterTextSplitter锛坈hunk_size=1000, chunk_overlap=200锛?3. **鍚戦噺鍖?*: 浣跨敤 Ollama 宓屽叆妯″瀷锛坣omic-embed-text锛?4. **鍚戦噺瀛樺偍**: 浣跨敤 Chroma 鍚戦噺鏁版嵁搴?5. **妫€绱?*: 鍩轰簬鐩镐技搴︾殑鏂囨湰妫€绱?6. **鐢熸垚**: 浣跨敤 ConversationalRetrievalChain 杩炴帴妫€绱㈠櫒鍜屽ぇ妯″瀷

### 绯荤粺鎻愮ず璇?
```
鍩轰簬鎻愪緵鐨勫弬鑰冩枃妗ｅ洖绛旈棶棰樸€?濡傛灉鏂囨。涓病鏈夌浉鍏充俊鎭紝璇锋槑纭"鏂囨。涓湭鎵惧埌鐩稿叧绛旀"銆?璇风洿鎺ョ粰鍑虹瓟妗堬紝涓嶉渶瑕侀澶栬鏄庛€?```

## 闂瓟娴嬭瘯绀轰緥

### 鐩稿叧闂

| 闂 | 棰勬湡鍥炵瓟 |
|------|----------|
| 浠€涔堟槸鑷劧璇█澶勭悊? | 鑷劧璇█澶勭悊鏄汉宸ユ櫤鑳界殑涓€涓噸瑕佸垎鏀?.. |
| Transformer鏋舵瀯鐢卞摢涓ら儴鍒嗙粍鎴? | 缂栫爜鍣ㄥ拰瑙ｇ爜鍣?|
| BERT鐨勯璁粌浠诲姟鏈夊摢浜? | 鎺╃爜璇█妯″瀷鍜屼笅涓€鍙ラ娴?|
| 鏂囨湰鍒嗙被鐨勫父鐢ㄧ畻娉曟湁鍝簺? | 鏈寸礌璐濆彾鏂€佹敮鎸佸悜閲忔満銆侀€昏緫鍥炲綊绛?|
| 鎯呮劅鍒嗘瀽鏈夊摢浜涘簲鐢ㄥ満鏅? | 绀句氦濯掍綋鐩戞帶銆佷骇鍝佽瘎璁哄垎鏋愮瓑 |

### 鏃犲叧闂

| 闂 | 棰勬湡鍥炵瓟 |
|------|----------|
| 浠€涔堟槸鏈哄櫒瀛︿範? | 鏂囨。涓湭鎵惧埌鐩稿叧绛旀 |
| 浠婂ぉ澶╂皵鎬庝箞鏍? | 鏂囨。涓湭鎵惧埌鐩稿叧绛旀 |

## 宸茬煡闂涓庢敼杩涙柟鍚?
### 宸茬煡闂

- 棣栨鍔犺浇妯″瀷鍙兘闇€瑕佽緝闀挎椂闂?- 澶ф枃妗ｅ鐞嗗彲鑳藉崰鐢ㄨ緝澶氬唴瀛?
### 鏀硅繘鏂瑰悜

- 鏀寔鏇村鏂囨。鏍煎紡锛堝 Markdown銆丠TML锛?- 娣诲姞鏂囨。鎽樿鍔熻兘
- 鏀寔澶氳瑷€鏂囨。
- 浼樺寲澶ф枃妗ｅ鐞嗘€ц兘

## 璁稿彲璇?
MIT License

## GitHub 浠撳簱

https://github.com/hhhtwo/RAG-QA-System-xnf-2405030226