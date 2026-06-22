# === Stage 14: Добавь генерацию краткой сводки по текущим данным ===
# Project: RecipeShelf
def generate_summary():
    if not recipes:
        print("Нет данных для сводки.")
        return
    
    total_recipes = len(recipes)
    all_ingredients = set()
    
    for recipe in recipes:
        for ingredient, amount in recipe.get('ingredients', {}).items():
            all_ingredients.add(ingredient)
            
    print(f"Сводка по каталогу рецептов:\n")
    print(f"Всего рецептов: {total_recipes}")
    
    if all_ingredients:
        sorted_ingredients = sorted(all_ingredients, key=str.lower)
        print(f"\nУникальные ингредиенты ({len(sorted_ingredients)}):")
        for ing in sorted_ingredients[:10]:  # Отображаем топ-10 для краткости
            print(f" - {ing}")
        
        if len(all_ingredients) > 10:
            print(f"... и еще {len(all_ingredients) - 10} ингредиентов")
            
    search_history = getattr(app_state, 'search_history', [])
    if search_history:
        print(f"\nИстория поиска ({len(search_history)} запросов):")
        for i, query in enumerate(search_history[-5:], 1):
            print(f" {i}. '{query}'")
            
    shopping_list = getattr(app_state, 'shopping_list', [])
    if shopping_list:
        print(f"\nТекущий список покупок ({len(shopping_list)} позиций):")
        for item in sorted(shopping_list, key=str.lower)[:10]:
            print(f" - {item}")
            
    if len(app_state.get('shopping_list', [])) > 10:
        print(f"... и еще {len(app_state['shopping_list']) - 10} позиций")
