# === Stage 10: Добавь экспорт текущего состояния в JSON-строку ===
# Project: RecipeShelf
def export_to_json():
    import json
    data = {
        "recipes": recipes,
        "ingredients": ingredients,
        "shopping_list": shopping_list
    }
    return json.dumps(data, ensure_ascii=False, indent=2)
