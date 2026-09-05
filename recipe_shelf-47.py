# === Stage 47: Добавь финальную функцию demo(), которая показывает основной пользовательский сценарий ===
# Project: RecipeShelf
def demo():
    print("=" * 50)
    print("RecipeShelf Demo — основной сценарий")
    print("=" * 50)

    recipes = [
        {"name": "Овсянка с ягодами", "ingredients": ["овсянка", "молоко", "ягоды"], "prep_time": 15},
        {"name": "Яичница-глазунья", "ingredients": ["яйца", "сливочное масло", "соль"], "prep_time": 5},
        {"name": "Салат Цезарь", "ingredients": ["салат", "курица", "сыр", "крекер", "соус"], "prep_time": 20},
    ]

    print(f"Всего рецептов: {len(recipes)}")

    search_input = "сыр"
    found = [r for r in recipes if search_input.lower() in r["name"].lower() or search_input.lower() in r["ingredients"]]
    print(f"\nПоиск ингредиентов '{search_input}': {len(found)} рецептов")

    shopping = set()
    for r in recipes:
        for ing in r["ingredients"]:
            shopping.add(ing)
    print(f"\nСписок покупок ({len(shopping)} позиций):")
    for item in sorted(shopping):
        print(f"  • {item}")

    print("\nДемо завершён.")
