# === Stage 24: Добавь компактный вывод одной записи с деталями ===
# Project: RecipeShelf
def print_recipe_card(recipe):
    """Компактный вывод одной карточки рецепта."""
    title = recipe.get("title", "Без названия")
    print(f"{'='*50}")
    print(f"  📖 {title}")
    print(f"{'='*50}")

    prep_time = recipe.get("prep_time", "?")
    cook_time = recipe.get("cook_time", "?")
    servings = recipe.get("servings", "?")
    difficulty = recipe.get("difficulty", "легкий")
    print(f"  ⏱ Готовность: {prep_time} (подготовка) + {cook_time} (приготовление)")
    print(f"  👥 Порций: {servings} | Трудность: {difficulty}")

    ingredients = recipe.get("ingredients", [])
    if ingredients:
        print(f"\n  🛒 Ингредиенты:")
        for ing in ingredients[:8]:
            print(f"    • {ing}")
        if len(ingredients) > 8:
            print(f"    ... и ещё {len(ingredients) - 8} ингредиентов")

    steps = recipe.get("steps", [])
    if steps:
        print(f"\n  👨‍🍳 Приготовление:")
        for i, step in enumerate(steps[:4], 1):
            print(f"    {i}. {step}")
        if len(steps) > 4:
            print(f"    ... и ещё {len(steps) - 4} шагов")

    tags = recipe.get("tags", [])
    if tags:
        tag_str = ", ".join(tags[:3])
        if len(tags) > 3:
            tag_str += f", ..."
        print(f"\n  🏷️ Теги: {tag_str}")

    print(f"{'='*50}\n")
