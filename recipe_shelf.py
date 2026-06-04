# === Stage 1: Создай базовую структуру файла приложения, точку входа и демонстрационные данные ===
# Project: RecipeShelf
import json

# Демонстрационные данные: рецепты, ингредиенты и список покупок
RECIPE_DATA = {
    "recipes": [
        {"id": 1, "name": "Омлет", "ingredients": ["яйца", "молоко", "соль"]},
        {"id": 2, "name": "Паста Карбонара", "ingredients": ["спагетти", "бекон", "сыр", "яйца"]}
    ],
    "shopping_list": []
}

def save_data(data):
    with open("recipe_shelf.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def load_data():
    try:
        with open("recipe_shelf.json", "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        save_data(RECIPE_DATA)
        return RECIPE_DATA

if __name__ == "__main__":
    data = load_data()
    print(f"Загружено {len(data['recipes'])} рецептов.")
    print("Список покупок пуст, добавьте ингредиенты при создании рецепта.")
