# Ollama 瀹夎鎸囧崡

## 馃摜 鎵嬪姩瀹夎姝ラ

### 姝ラ1锛氫笅杞?Ollama 瀹夎绋嬪簭

**鏂规硶1锛氬畼缃戜笅杞斤紙鎺ㄨ崘锛?*
1. 鎵撳紑娴忚鍣ㄨ闂細https://ollama.com/download/windows
2. 鐐瑰嚮 "Download for Windows" 鎸夐挳
3. 绛夊緟涓嬭浇瀹屾垚锛堢害 50MB锛?
**鏂规硶2锛氱洿鎺ヤ笅杞介摼鎺?*
1. 澶嶅埗浠ヤ笅閾炬帴鍒版祻瑙堝櫒鍦板潃鏍忥細
   ```
   https://github.com/ollama/ollama/releases/download/v0.1.48/ollama-windows-amd64.exe
   ```
2. 绛夊緟涓嬭浇瀹屾垚

### 姝ラ2锛氬畨瑁?Ollama

1. 鍙屽嚮涓嬭浇鐨?`ollama-windows-amd64.exe` 鏂囦欢
2. 鎸夌収瀹夎鍚戝瀹屾垚瀹夎
3. **瀹夎瀹屾垚鍚庡繀椤婚噸鍚數鑴?*

### 姝ラ3锛氶獙璇佸畨瑁?
1. 鎵撳紑 **鍛戒护鎻愮ず绗?*锛圕MD锛夋垨 **PowerShell**
2. 鎵ц浠ヤ笅鍛戒护楠岃瘉瀹夎锛?   ```bash
   ollama --version
   ```
3. 濡傛灉鏄剧ず鐗堟湰鍙凤紝璇存槑瀹夎鎴愬姛锛?
### 姝ラ4锛氫笅杞芥ā鍨?
鎵撳紑鍛戒护鎻愮ず绗︼紝鎵ц浠ヤ笅鍛戒护锛?
```bash
# 涓嬭浇澶ц瑷€妯″瀷锛堢害7GB锛?ollama pull deepseek-r1:7b

# 涓嬭浇宓屽叆妯″瀷锛堢害200MB锛?ollama pull nomic-embed-text
```

### 姝ラ5锛氬惎鍔ㄥ簲鐢?
```bash
# 杩涘叆椤圭洰鐩綍
cd C:\Users\Administrator\Desktop\浜哄伐鏅鸿兘

# 鍚姩 Streamlit 搴旂敤
streamlit run app.py
```

## 馃殌 蹇€熷惎鍔ㄨ剼鏈?
鍒涘缓涓€涓?`start_app.bat` 鏂囦欢锛?
```batch
@echo off
chcp 65001 >nul
echo ========================================
echo   RAG 鏅鸿兘闂瓟绯荤粺 - 鍚姩鍣?echo ========================================
echo.

echo [1/4] 妫€鏌?Ollama...
ollama --version >nul 2>&1
if %errorlevel% neq 0 (
    echo 鉂?閿欒锛氭湭妫€娴嬪埌 Ollama锛?    echo.
    echo 璇峰厛瀹夎 Ollama锛?    echo 1. 璁块棶 https://ollama.com/download/windows
    echo 2. 涓嬭浇骞跺畨瑁?    echo 3. 瀹夎瀹屾垚鍚庨噸鍚數鑴?    echo 4. 閲嶆柊杩愯姝よ剼鏈?    echo.
    pause
    exit /b 1
)
echo 鉁?Ollama 宸插畨瑁?
echo.
echo [2/4] 妫€鏌ユā鍨?..
ollama list | findstr "deepseek-r1" >nul
if %errorlevel% neq 0 (
    echo 鈿狅笍  鏈壘鍒?deepseek-r1:7b 妯″瀷
    echo 姝ｅ湪涓嬭浇妯″瀷锛堢害7GB锛岄渶瑕佷竴浜涙椂闂?..锛?    ollama pull deepseek-r1:7b
)
ollama list | findstr "nomic-embed" >nul
if %errorlevel% neq 0 (
    echo 姝ｅ湪涓嬭浇宓屽叆妯″瀷...
    ollama pull nomic-embed-text
)
echo 鉁?妯″瀷宸插氨缁?
echo.
echo [3/4] 妫€鏌ヤ緷璧?..
python -c "import streamlit" >nul 2>&1
if %errorlevel% neq 0 (
    echo 鈿狅笍  姝ｅ湪瀹夎渚濊禆...
    pip install streamlit langchain chromadb PyPDF2 python-docx tiktoken ollama langchain-community
)
echo 鉁?渚濊禆宸插氨缁?
echo.
echo [4/4] 鍚姩搴旂敤...
echo.
echo ========================================
echo   搴旂敤鍚姩涓?..
echo   娴忚鍣ㄥ皢鑷姩鎵撳紑 http://localhost:8501
echo ========================================
echo.
streamlit run app.py
pause
```

## 鈿狅笍 甯歌闂

### 闂1锛?ollama' 涓嶆槸鍐呴儴鎴栧閮ㄥ懡浠?**瑙ｅ喅鏂规硶锛?*
- 纭繚 Ollama 宸叉纭畨瑁?- 閲嶅惎鐢佃剳浣跨幆澧冨彉閲忕敓鏁?- 鎵嬪姩娣诲姞 Ollama 瀹夎璺緞鍒扮郴缁熺幆澧冨彉閲?
### 闂2锛氭ā鍨嬩笅杞芥參
**瑙ｅ喅鏂规硶锛?*
- 纭繚缃戠粶杩炴帴绋冲畾
- 鍙互灏濊瘯鏇存崲缃戠粶
- 绛夊緟涓嬭浇瀹屾垚锛堥娆′笅杞界害7GB锛?
### 闂3锛氬唴瀛樹笉瓒?**瑙ｅ喅鏂规硶锛?*
- 鍏抽棴鍏朵粬鍗犵敤鍐呭瓨鐨勭▼搴?- 纭繚鐢佃剳鑷冲皯鏈?16GB 鍐呭瓨
- 鍙互灏濊瘯浣跨敤杈冨皬鐨勬ā鍨嬶細`ollama pull qwen2:1.5b`

### 闂4锛氱鍙ｈ鍗犵敤
**瑙ｅ喅鏂规硶锛?*
- 妫€鏌?8501 绔彛鏄惁琚叾浠栫▼搴忓崰鐢?- 浣跨敤鍏朵粬绔彛鍚姩锛歚streamlit run app.py --server.port 8502`

## 馃搵 瀹屾暣鍛戒护鍒楄〃

```bash
# 瀹夎妫€鏌?ollama --version

# 鏌ョ湅宸插畨瑁呮ā鍨?ollama list

# 涓嬭浇妯″瀷
ollama pull deepseek-r1:7b
ollama pull nomic-embed-text

# 鍚姩搴旂敤
streamlit run app.py

# 鍋滄搴旂敤锛堟寜 Ctrl+C锛?```

## 馃摓 鎶€鏈敮鎸?
濡傛灉閬囧埌闂锛岃鎸変互涓嬮『搴忔鏌ワ細

1. 鉁?Ollama 鏄惁宸插畨瑁咃細`ollama --version`
2. 鉁?妯″瀷鏄惁宸蹭笅杞斤細`ollama list`
3. 鉁?Python 渚濊禆鏄惁瀹夎锛歚pip list | findstr "streamlit"`
4. 鉁?绔彛 8501 鏄惁鍙敤

---

*鏂囨。鏇存柊鏃ユ湡锛?026骞?鏈?鏃?
