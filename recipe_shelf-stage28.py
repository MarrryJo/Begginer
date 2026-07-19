# === Stage 28: Добавь подсчёт ключевых метрик проекта ===
# Project: RecipeShelf
def print_metrics():
    recipes = list(recipe_data.values()) if isinstance(recipe_data, dict) else []
    total_ingredients = sum(len(r.get("ingredients", {}).get("items", [])) for r in recipes)
    avg_ingredients = (total_ingredients / len(recipes)).__round__(1) if recipes else 0.0
    print(f"Количество рецептов: {len(recipes)}")
    print(f"Общее количество ингредиентов: {total_ingredients}")
    print(f"Среднее количество ингредиентов на рецепт: {avg_ingredients}")
    total_time = sum(r.get("time", {}).get("minutes", 0) for r in recipes) if any(r.get("time")) else 0
    avg_time = (total_time / len(recipes)).__round__(1) if recipes and total_time else 0.0
    print(f"Общее время приготовления: {total_time} минут")
    print(f"Среднее время приготовления: {avg_time} минут")
    total_calories = sum(r.get("nutrition", {}).get("calories", 0) for r in recipes) if any(r.get("nutrition")) else 0
    avg_calories = (total_calories / len(recipes)).__round__(1) if recipes and total_calories else 0.0
    print(f"Общие калории: {total_calories}")
    print(f"Средние калории на рецепт: {avg_calories}")
