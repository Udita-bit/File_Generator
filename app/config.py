import os
from dotenv import load_dotenv

load_dotenv()

# ─────────────────────────────
# API KEYS
# ─────────────────────────────
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
if not GROQ_API_KEY:
    raise RuntimeError("GROQ_API_KEY not found in .env")

# ─────────────────────────────
# BASE PATH
# ─────────────────────────────
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# ─────────────────────────────
# DATABASE
# ─────────────────────────────
DB_PATH = os.path.join(BASE_DIR, "ai_files.db")

# ─────────────────────────────
# FILE STORAGE
# ─────────────────────────────
FILES_DIR = os.path.join(BASE_DIR, "app", "files")
os.makedirs(FILES_DIR, exist_ok=True)

# ─────────────────────────────
# RAG DATA
# ─────────────────────────────
DATA_DIR = os.path.join(BASE_DIR, "app", "data")
os.makedirs(DATA_DIR, exist_ok=True)