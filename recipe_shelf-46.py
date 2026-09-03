# === Stage 46: Добавь миграцию версии структуры данных ===
# Project: RecipeShelf
import json, pathlib

DATA_FILE = pathlib.Path("data.json")

def migrate_data():
    if not DATA_FILE.exists():
        return
    with open(DATA_FILE) as f:
        data = json.load(f)
    if data.get("__version__") is None:
        data["__version__"] = 46
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
