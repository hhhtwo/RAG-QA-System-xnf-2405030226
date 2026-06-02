# RAG-QA-System

鍩轰簬妫€绱㈠寮虹敓鎴愶紙RAG锛夌殑鏅鸿兘闂瓟绯荤粺椤圭洰

## 鍔熻兘鐗规€?
- 馃摎 鏀寔 PDF 鍜?DOCX 鏂囨。涓婁紶
- 馃攳 鏅鸿兘鏂囨。妫€绱?- 馃 鍩轰簬 Ollama 鐨勬湰鍦板寲澶ц瑷€妯″瀷
- 馃挰 浜や簰寮忛棶绛旂晫闈?- 鈿?瀹炴椂鍥炵瓟鐢熸垚

## 鎶€鏈爤

- **妗嗘灦**: Streamlit
- **璇█妯″瀷**: Ollama (deepseek-r1:7b / qwen2:7b)
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
   # 鎴?   ollama pull qwen2:7b
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

1. 鍚姩搴旂敤鍚庯紝鍦ㄤ晶杈规爮閫夋嫨浣跨敤鐨勬ā鍨?2. 涓婁紶 PDF 鎴?DOCX 鏍煎紡鐨勬枃妗?3. 绛夊緟鏂囨。澶勭悊瀹屾垚
4. 鍦ㄨ緭鍏ユ涓緭鍏ラ棶棰橈紝鑾峰彇鍩轰簬鏂囨。鍐呭鐨勫洖绛?
## 椤圭洰缁撴瀯

```
.
鈹溾攢鈹€ app.py              # 涓诲簲鐢ㄥ叆鍙?鈹溾攢鈹€ requirements.txt    # 渚濊禆鍒楄〃
鈹溾攢鈹€ test_ollama.py      # Ollama 娴嬭瘯鑴氭湰
鈹溾攢鈹€ push-to-github.ps1  # GitHub 鎺ㄩ€佽剼鏈?鈹斺攢鈹€ README.md           # 椤圭洰璇存槑
```

## API 娴嬭瘯

杩愯娴嬭瘯鑴氭湰鏉ラ獙璇?Ollama API锛?
```bash
python test_ollama.py
```

## 璁稿彲璇?
MIT License