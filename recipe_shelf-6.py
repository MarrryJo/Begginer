# === Stage 6: Добавь фильтрацию записей по статусу, категории или тегам ===
# Project: RecipeShelf
def filter_recipes(recipes, status=None, category=None, tags=None):
    filtered = []
    for r in recipes:
        if status is not None and r.get('status') != status:
            continue
        if category is not None and r.get('category') != category:
            continue
        if tags is not None:
            recipe_tags = r.get('tags', [])
            if not any(tags in recipe_tags for tags in [tags]):
                continue
        filtered.append(r)
    return filtered

def get_shopping_list(recipes):
    items = {}
    for r in recipes:
        for ing in r.get('ingredients', []):
            name = ing.get('name')
            amount = ing.get('amount', 0)
            if name in items:
                items[name] += amount
            else:
                items[name] = amount
    return list(items.items())

def search_recipes(recipes, query):
    query = query.lower()
    results = []
    for r in recipes:
        title = r.get('title', '').lower()
        desc = r.get('description', '').lower()
        tags = ' '.join(r.get('tags', [])).lower()
        if query in title or query in desc or query in tags:
            results.append(r)
    return results
