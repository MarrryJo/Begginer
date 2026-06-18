# === Stage 12: Добавь загрузку данных из локального JSON-файла с обработкой ошибок ===
# Project: RecipeShelf
def load_recipes_from_json(filepath):
    try:
        import json
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
        if not isinstance(data, list):
            raise ValueError("JSON должен содержать массив рецептов")
        recipes = []
        for i, item in enumerate(data):
            try:
                recipe_id = item.get('id', i + 1)
                title = item.get('title')
                ingredients = item.get('ingredients', [])
                if not all([recipe_id, title]):
                    print(f"Пропуск рецепта {i+1}: отсутствуют обязательные поля")
                    continue
                recipes.append({'id': recipe_id, 'title': title, 'ingredients': ingredients})
            except Exception as e:
                print(f"Ошибка парсинга рецепта {i+1}: {e}")
        return recipes
    except FileNotFoundError:
        print(f"Файл не найден: {filepath}")
        return []
    except json.JSONDecodeError as e:
        print(f"Ошибка чтения JSON: {e}")
        return []
