# === Stage 13: Добавь поиск по нескольким полям без учёта регистра ===
# Project: RecipeShelf
def search_recipes(query, recipes):
    if not query:
        return recipes
    q = query.lower()
    results = []
    for r in recipes:
        text = (r.get('title', '') + ' ' + r.get('description', '')).lower()
        ingredients_str = ' '.join(r.get('ingredients', [])).lower()
        if q in text or q in ingredients_str:
            results.append(r)
    return results
