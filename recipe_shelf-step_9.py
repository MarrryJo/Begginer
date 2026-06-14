# === Stage 9: Добавь импорт начальных данных из JSON-строки ===
# Project: RecipeShelf
import json, sys

DATA_URL = "https://raw.githubusercontent.com/example/recipes/main/data.json"  # Замените на реальный URL или используйте локальный файл

def load_initial_data():
    try:
        response = requests.get(DATA_URL)
        response.raise_for_status()
        data = response.json()
    except Exception as e:
        print(f"[WARN] Не удалось загрузить данные из {DATA_URL}: {e}. Используем встроенные демо-данные.")
        return get_demo_data()

def get_demo_data():
    # Встроенный JSON для работы без сети при первом запуске или отсутствии доступа к URL
    demo_json = '''{
      "recipes": [
        {"id": 1, "title": "Омлет", "ingredients": [{"name": "Яйца", "amount": 3}, {"name": "Молоко", "amount": 50}], "tags": ["завтрак"]},
        {"id": 2, "title": "Паста Карбонара", "ingredients": [{"name": "Спагетти", "amount": 400}, {"name": "Бекон", "amount": 150}], "tags": ["ужин"]}
      ]
    }'''
    return json.loads(demo_json)

def init_database():
    data = load_initial_data()
    recipes_db = {r["id"]: r for r in data.get("recipes", [])}
    
    # Сохраняем в файл для последующего использования без сети
    with open("data.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    return recipes_db

if __name__ == "__main__":
    db = init_database()
    print(f"Загружено {len(db)} рецептов.")
