# === Stage 2: Добавь модели данных и функции валидации пользовательского ввода ===
# Project: RecipeShelf
class Recipe:
    def __init__(self, title, ingredients):
        self.title = title
        self.ingredients = ingredients

class Ingredient:
    def __init__(self, name, quantity=None):
        self.name = name
        self.quantity = quantity

def validate_input(user_input):
    if not user_input.strip():
        return None
    parts = user_input.split(maxsplit=1)
    if len(parts) == 1:
        return Ingredient(name=parts[0].strip())
    elif len(parts) == 2:
        name, qty = parts
        try:
            quantity = float(qty) if qty.replace('.', '').isdigit() else None
        except ValueError:
            quantity = None
        return Ingredient(name=name.strip(), quantity=quantity)
    return None

def parse_recipe_line(line):
    parts = line.split(':')
    if len(parts) != 2:
        return None
    title, ingredients_str = parts
    ingredients = []
    for ing in ingredients_str.split(';'):
        ing = ing.strip()
        if not ing:
            continue
        ing_parts = ing.split(maxsplit=1)
        if len(ing_parts) == 1:
            ingredients.append(Ingredient(name=ing_parts[0]))
        else:
            try:
                quantity = float(ing_parts[1])
            except ValueError:
                quantity = None
            ingredients.append(Ingredient(name=ing_parts[0], quantity=quantity))
    return Recipe(title=title.strip(), ingredients=ingredients)
