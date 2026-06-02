# RAG 闂瓟绯荤粺 - 瀹屾暣瀹夎鎸囧崡

## 馃敡 绗竴姝ワ細瀹夎 Ollama锛堝繀椤诲厛瀹夎锛?
### Windows
1. 璁块棶 https://ollama.com/download/windows
2. 涓嬭浇骞跺畨瑁?Ollama
3. 瀹夎瀹屾垚鍚庯紝**閲嶅惎鐢佃剳**鎴栭噸鏂版墦寮€鍛戒护琛岀獥鍙?
### 楠岃瘉瀹夎
鎵撳紑鏂扮殑鍛戒护琛岀獥鍙ｏ紝杈撳叆锛?```bash
ollama --version
```
濡傛灉鏄剧ず鐗堟湰鍙凤紝璇存槑瀹夎鎴愬姛锛?
## 馃摜 绗簩姝ワ細涓嬭浇妯″瀷

鍦ㄥ懡浠よ涓緷娆℃墽琛岋細
```bash
# 涓嬭浇澶ц瑷€妯″瀷锛堢害7GB锛?ollama pull deepseek-r1:7b

# 涓嬭浇宓屽叆妯″瀷锛堢害200MB锛?ollama pull nomic-embed-text
```

## 馃悕 绗笁姝ワ細瀹夎 Python 渚濊禆

鍦ㄩ」鐩洰褰曚笅鎵ц锛?```bash
pip install streamlit langchain chromadb PyPDF2 python-docx tiktoken ollama langchain-community
```

濡傛灉瀹夎瓒呮椂锛屽彲浠ュ皾璇曪細
```bash
pip install --timeout=120 streamlit langchain chromadb PyPDF2 python-docx tiktoken ollama langchain-community
```

## 馃殌 绗洓姝ワ細鍚姩搴旂敤

### 鏂瑰紡涓€锛歐eb 鐣岄潰锛堟帹鑽愶級
```bash
streamlit run app.py
```

### 鏂瑰紡浜岋細鍛戒护琛岀増鏈?```bash
python rag_qa_chain.py
```

## 馃搵 蹇€熷惎鍔ㄨ剼鏈?
鍒涘缓涓€涓?`start.bat` 鏂囦欢锛?```batch
@echo off
echo ========================================
echo   RAG 闂瓟绯荤粺
echo ========================================
echo.
echo 姝ｅ湪妫€鏌?Ollama...
ollama list
if %errorlevel% neq 0 (
    echo.
    echo 閿欒锛氭湭妫€娴嬪埌 Ollama锛?    echo 璇峰厛瀹夎 Ollama锛歨ttps://ollama.com/download/windows
    pause
    exit /b 1
)

echo.
echo 姝ｅ湪鍚姩搴旂敤...
echo.
streamlit run app.py
pause
```

## 馃挕 浣跨敤璇存槑

1. 鍚姩搴旂敤鍚庯紝娴忚鍣ㄤ細鑷姩鎵撳紑锛坔ttp://localhost:8501锛?2. 鍦ㄤ晶杈规爮閫夋嫨妯″瀷
3. 涓婁紶 PDF/DOCX/TXT 鏂囨。
4. 鐐瑰嚮"Build Knowledge Base"鏋勫缓鐭ヨ瘑搴?5. 鍦ㄨ緭鍏ユ涓彁闂?
## 鈿狅笍 甯歌闂

### 闂1锛氭彁绀?'ollama' 涓嶆槸鍐呴儴鎴栧閮ㄥ懡浠?**瑙ｅ喅鏂规硶**锛氶噸鏂板畨瑁?Ollama锛屽畨瑁呭畬鎴愬悗閲嶅惎鐢佃剳

### 闂2锛氭ā鍨嬩笅杞芥參
**瑙ｅ喅鏂规硶**锛氬彲浠ユ洿鎹负 qwen2:7b 妯″瀷锛?```bash
ollama pull qwen2:7b
```

### 闂3锛氫緷璧栧畨瑁呭け璐?**瑙ｅ喅鏂规硶**锛?- 浣跨敤鍥藉唴闀滃儚婧愶細
```bash
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple streamlit langchain chromadb PyPDF2 python-docx tiktoken ollama langchain-community
```

### 闂4锛氬唴瀛樹笉瓒?**瑙ｅ喅鏂规硶**锛氱‘淇濈數鑴戣嚦灏戞湁 16GB 鍐呭瓨锛屽叧闂叾浠栧崰鐢ㄥ唴瀛樼殑绋嬪簭

## 馃摓 鎶€鏈敮鎸?
濡傛灉閬囧埌闂锛岃妫€鏌ワ細
1. Ollama 鏄惁宸叉纭畨瑁呭苟杩愯
2. 妯″瀷鏄惁宸蹭笅杞斤細`ollama list`
3. Python 渚濊禆鏄惁宸插畨瑁咃細`pip list`
4. 绔彛 8501 鏄惁琚崰鐢?
---

**椤圭洰宸插畬鎴愶紒鎵€鏈変唬鐮佸凡涓婁紶鍒?GitHub锛?*
https://github.com/hhhtwo/RAG-QA-System-xnf-2405030226
