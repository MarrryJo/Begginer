# === Stage 17: Добавь группировку записей по категориям ===
# Project: RecipeShelf
def group_by_category(recipes):
    groups = {}
    for r in recipes:
        cat = r.get('category', 'Other')
        if cat not in groups:
            groups[cat] = []
        groups[cat].append(r)
    return groups
