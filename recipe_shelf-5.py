# === Stage 5: Добавь удаление записей и аккуратную обработку отсутствующих идентификаторов ===
# Project: RecipeShelf
def delete_recipe(recipe_id):
    if recipe_id not in recipes:
        print(f"Рецепт с ID {recipe_id} не найден.")
        return False
    
    del recipes[recipe_id]
    print(f"Рецепт с ID {recipe_id} успешно удалён.")
    return True

def delete_ingredient(recipe_id, ingredient_name):
    if recipe_id not in recipes:
        print(f"Рецепт с ID {recipe_id} не найден.")
        return False
    
    if ingredient_name not in recipes[recipe_id]['ingredients']:
        print(f"Ингредиент '{ingredient_name}' не найден в рецепте {recipe_id}.")
        return False
    
    del recipes[recipe_id]['ingredients'][ingredient_name]
    print(f"Ингредиент '{ingredient_name}' удалён из рецепта {recipe_id}.")
    return True

def delete_shopping_item(item_name):
    if item_name not in shopping_list:
        print(f"Товар '{item_name}' не найден в списке покупок.")
        return False
    
    del shopping_list[item_name]
    print(f"Товар '{item_name}' удалён из списка покупок.")
    return True
