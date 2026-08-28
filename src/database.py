from src.config import DB_PATH

DB_PATH.parent.mkdir(parents=True, exist_ok=True)

from pathlib import Path

print(Path.cwd(), "\n")
print(DB_PATH, "\n")
print(DB_PATH.resolve())
