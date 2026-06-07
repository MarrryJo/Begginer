# === Stage 4: Добавь функцию редактирования существующих записей по идентификатору ===
# Project: RecipeShelf
def edit_recipe(recipe_id, new_data):
    if recipe_id not in recipes:
        print(f"Рецепт с ID {recipe_id} не найден.")
        return False
    
    existing = recipes[recipe_id]
    
    # Обновляем только предоставленные поля, сохраняя остальные
    for key, value in new_data.items():
        if key in existing:
            existing[key] = value
    
    print(f"Рецепт {recipe_id} успешно обновлен.")
    return True

# Пример вызова (раскомментируйте при необходимости):
# edit_recipe(1, {"title": "Новое название", "ingredients": ["Яйцо", "Молоко"]})
