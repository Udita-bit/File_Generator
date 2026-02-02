import os
from app.config import FILES_DIR

def save_file(filename: str, content: str):
    path = os.path.join(FILES_DIR, filename)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    return path

def delete_file(filename: str):
    path = os.path.join(FILES_DIR, filename)
    if os.path.exists(path):
        os.remove(path)
        return True
    return False