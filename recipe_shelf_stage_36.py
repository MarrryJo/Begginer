# === Stage 36: Добавь проверку целостности данных и функцию ремонта простых проблем ===
# Project: RecipeShelf
def check_and_repair_data():
    """Проверяет целостность данных и пытается исправить простые проблемы."""
    issues = []
    
    # Проверка 1: Все рецепты имеют уникальный ID
    ids = set(ingredient_recipes.keys()) if ingredient_recipes else set()
    duplicate_ids = [id for id in ids if ids.count(id) > 1]
    if duplicate_ids:
        print(f"Предупреждение: найдены дубликаты IDs рецептов: {duplicate_ids}")
    
    # Проверка 2: Все ингредиенты в рецептах существуют
    all_ingredients = set()
    for recipe_name, ingredients in ingredient_recipes.items():
        if isinstance(ingredients, dict):
            all_ingredients.update(ingredients.keys())
    
    invalid_ingredients = [ing for ing in all_ingredients if ing not in ingredient_list]
    if invalid_ingredients:
        print(f"Предупреждение: найдены невалидные ингредиенты: {invalid_ingredients}")
        
        # Попытка исправить - удалить рецепты с невалидными ингредиентами
        for recipe_name, ingredients in list(ingredient_recipes.items()):
            if isinstance(ingredients, dict):
                invalid_in_recipe = [ing for ing in ingredients.keys() if ing not in ingredient_list]
                if invalid_in_recipe:
                    print(f"Удаляю рецепт '{recipe_name}' с невалидными ингредиентами")
                    del ingredient_recipes[recipe_name]
    
    # Проверка 3: Все названия продуктов содержат хотя бы одну букву
    for product in list(product_list):
        if not any(c.isalpha() for c in str(product)):
            print(f"Предупреждение: продукт '{product}' не содержит букв")
    
    # Проверка 4: Все цены - неотрицательные числа
    for price_str, price in list(price_dict.items()):
        if price < 0 or not isinstance(price, (int, float)):
            print(f"Предупреждение: цена для '{price_str}' некорректна")

# Пример использования
check_and_repair_data()
