@echo off
chcp 65001 >nul
echo ========================================
echo   RAG 闂瓟绯荤粺 - 鍚姩鍣?
echo ========================================
echo.
echo [1/4] 妫€鏌?Ollama...
ollama --version >nul 2>&1
if %errorlevel% neq 0 (
    echo 鉂?閿欒锛氭湭妫€娴嬪埌 Ollama锛?
    echo.
    echo 璇锋寜浠ヤ笅姝ラ瀹夎锛?
    echo 1. 璁块棶 https://ollama.com/download/windows
    echo 2. 涓嬭浇骞跺畨瑁?Ollama
    echo 3. 瀹夎瀹屾垚鍚庨噸鍚鑴氭湰
    echo.
    pause
    exit /b 1
)
echo 鉁?Ollama 宸插畨瑁?
echo.

echo [2/4] 妫€鏌ユā鍨?..
ollama list | findstr "deepseek-r1" >nul
if %errorlevel% neq 0 (
    echo 鈿狅笍  鏈壘鍒?deepseek-r1:7b 妯″瀷
    echo 姝ｅ湪涓嬭浇妯″瀷锛堢害7GB锛岄渶瑕佷竴浜涙椂闂?..锛?
    ollama pull deepseek-r1:7b
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
