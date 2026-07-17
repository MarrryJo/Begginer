# === Stage 27: Добавь функции сброса демо-данных и очистки состояния ===
# Project: RecipeShelf
def reset_demo_data():
    """Сбросить все демо-данные в исходное состояние."""
    global recipes, ingredients, shopping_list, search_query
    recipes = [
        {
            "id": 1,
            "title": "Омлет с сыром",
            "ingredients": ["яйца", "сыр", "сливочное масло"],
            "time_minutes": 10,
            "difficulty": "easy"
        },
        {
            "id": 2,
            "title": "Паста Карбонара",
            "ingredients": ["спагетти", "бекон", "яйца", "сыр пармезан", "сметана"],
            "time_minutes": 25,
            "difficulty": "medium"
        },
        {
            "id": 3,
            "title": "Салат Цезарь",
            "ingredients": ["латук", "куриная грудка", "сыр пармезан", "кунжут"],
            "time_minutes": 15,
            "difficulty": "easy"
        },
    ]
    ingredients = [
        {"name": "яйца", "quantity": 0},
        {"name": "сыр", "quantity": 0},
        {"name": "бекон", "quantity": 0},
        {"name": "спагетти", "quantity": 0},
        {"name": "куриная грудка", "quantity": 0},
    ]
    shopping_list = []
    search_query = ""


def clear_state():
    """Очистить все данные и вернуть начальные значения."""
    global recipes, ingredients, shopping_list, search_query
    reset_demo_data()
    print("Все данные сброшены к начальным значениям.")
