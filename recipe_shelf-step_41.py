# === Stage 41: Добавь режим dry-run для операций изменения данных ===
# Project: RecipeShelf
import copy

def dry_run(operation, recipe, ingredient, amount, unit):
    """Execute operation in dry-run mode: log the intended change without persisting."""
    changes = {
        "operation": operation,
        "recipe": recipe,
        "ingredient": ingredient,
        "amount": amount,
        "unit": unit,
    }
    print(f"[DRY-RUN] {operation}: {recipe} - {amount} {unit} {ingredient}")
    return changes

def dry_run_add_recipe(recipe, ingredients):
    """Simulate adding a recipe and its ingredients."""
    changes = dry_run("add_recipe", recipe, None, None, None)
    changes["ingredients"] = ingredients
    print(f"[DRY-RUN] Added recipe: {recipe} with {len(ingredients)} ingredients")
    return changes

def dry_run_add_ingredient(recipe, ingredient, amount, unit):
    """Simulate adding an ingredient to a recipe."""
    changes = dry_run("add_ingredient", recipe, ingredient, amount, unit)
    print(f"[DRY-RUN] Added {amount} {unit} {ingredient} to {recipe}")
    return changes

def dry_run_remove_ingredient(recipe, ingredient):
    """Simulate removing an ingredient from a recipe."""
    changes = dry_run("remove_ingredient", recipe, ingredient, 0, "")
    print(f"[DRY-RUN] Removed {ingredient} from {recipe}")
    return changes

def dry_run_update_ingredient(recipe, ingredient, amount, unit):
    """Simulate updating an ingredient's amount in a recipe."""
    changes = dry_run("update_ingredient", recipe, ingredient, amount, unit)
    print(f"[DRY-RUN] Updated {ingredient} to {amount} {unit} in {recipe}")
    return changes

def dry_run_add_shopping_list(recipe, ingredient, amount, unit):
    """Simulate adding an item to the shopping list."""
    changes = dry_run("add_shopping_list", recipe, ingredient, amount, unit)
    print(f"[DRY-RUN] Added {amount} {unit} {ingredient} to shopping list")
    return changes

def dry_run_remove_shopping_list(ingredient):
    """Simulate removing an item from the shopping list."""
    changes = dry_run("remove_shopping_list", None, ingredient, 0, "")
    print(f"[DRY-RUN] Removed {ingredient} from shopping list")
    return changes
