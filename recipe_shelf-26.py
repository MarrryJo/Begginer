# === Stage 26: Добавь набор демо-команд для быстрого ручного тестирования ===
# Project: RecipeShelf
def demo_quick_test():
    """Быстрый ручной тест: показать 3 случайных рецепта + поиск."""
    import random
    recipes = get_all_recipes()
    if not recipes:
        print("⚠️ Нет рецептов. Загрузите файл с данными или добавьте демо-рецепты.")
        return
    sample = random.sample(recipes, min(3, len(recipes)))
    for r in sample:
        print(f"📖 {r.title} ({len(r.ingredients)} ингредиентов)")
    query = input("Поиск (или Enter для пропуска): ").strip().lower() or ""
    if query:
        found = [r for r in recipes if query.lower() in r.title.lower()]
        if not found and any(query.lower() in ing.lower() for r in recipes for ing in r.ingredients):
            found = [r for r in recipes]
        print(f"\n🔍 Найдено: {len(found)}")
        for r in found[:3]:
            print(f"  - {r.title}")

demo_quick_test()
