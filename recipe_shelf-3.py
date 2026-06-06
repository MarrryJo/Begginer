# === Stage 3: Реализуй хранение состояния в памяти и функции добавления записей ===
# Project: RecipeShelf
class RecipeShelf:
    def __init__(self):
        self.recipes = {}
        self.shopping_list = []

    def add_recipe(self, name, ingredients, instructions):
        if name in self.recipes:
            print(f"Рецепт '{name}' уже существует.")
            return False
        self.recipes[name] = {
            "ingredients": ingredients,
            "instructions": instructions
        }
        print(f"Рецепт '{name}' добавлен.")
        return True

    def add_to_shopping_list(self, ingredient):
        if ingredient not in self.shopping_list:
            self.shopping_list.append(ingredient)
            return True
        return False

    def get_recipe(self, name):
        return self.recipes.get(name)

    def get_shopping_list(self):
        return self.shopping_list.copy()
