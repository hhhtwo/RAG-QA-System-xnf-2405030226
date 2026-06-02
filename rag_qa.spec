import sys
from pathlib import Path
from PyInstaller.utils.hooks import collect_all

block_cipher = None

streamlit_path = Path(__file__).resolve().parent

datas = [
    (str(streamlit_path / "data"), "data"),
    (str(streamlit_path / "app.py"), "."),
    (str(streamlit_path / "knowledge_base.py"), "."),
    (str(streamlit_path / "rag_qa_chain.py"), "."),
    (str(streamlit_path / "test_ollama.py"), "."),
    (str(streamlit_path / "requirements.txt"), "."),
    (str(streamlit_path / "README.md"), "."),
]

hiddenimports = [
    "streamlit",
    "langchain",
    "langchain_community",
    "chromadb",
    "pypdf",
    "docx",
    "tiktoken",
    "ollama",
    "sqlalchemy",
    "numpy",
    "scipy",
    "sklearn",
    "requests",
    "urllib3",
    "certifi",
    "charset_normalizer",
    "idna",
]

excludedimports = []

a = Analysis(
    ['app.py'],
    pathex=[str(streamlit_path)],
    binaries=[],
    datas=datas,
    hiddenimports=hiddenimports,
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=excludedimports,
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='RAG-QA-System',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='RAG-QA-System',
)