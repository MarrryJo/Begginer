# === Stage 7: Добавь сортировку записей по дате, приоритету и названию ===
# Project: RecipeShelf
def sort_recipes(recipes, key='date'):
    if key == 'date':
        return sorted(recipes, key=lambda r: (r.get('created_at') or 0) * -1)
    elif key == 'priority':
        return sorted(recipes, key=lambda r: -(r.get('priority', 5)))
    else:
        return sorted(recipes, key=lambda r: r.get('name', '').lower())
