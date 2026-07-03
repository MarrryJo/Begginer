# === Stage 20: Добавь восстановление записей из архива ===
# Project: RecipeShelf
import json, os, sys

ARCHIVE_FILE = "recipes_archive.json"

def restore_from_archive():
    if not os.path.exists(ARCHIVE_FILE):
        return 0
    
    try:
        with open(ARCHIVE_FILE, 'r', encoding='utf-8') as f:
            archived_data = json.load(f)
        
        for item in archived_data.get('recipes', []):
            if not any(r['id'] == item['id'] and r['version'] < item.get('version', 0) 
                       for r in recipes_db.values()):
                recipes_db[item['id']] = item
        
        os.remove(ARCHIVE_FILE)
        return len(archived_data.get('recipes', []))
    except Exception:
        pass

restore_from_archive()
