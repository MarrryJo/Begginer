# === Stage 16: Добавь расчёт месячной статистики по датам ===
# Project: RecipeShelf
def calculate_monthly_stats(recipes, ingredients):
    from collections import defaultdict
    stats = defaultdict(lambda: {'recipes': 0, 'ingredients': set()})
    for recipe in recipes:
        date_str = recipe.get('date', '')
        if not date_str or len(date_str) < 7: continue
        month_key = f"{date_str[:4]}-{date_str[5:7]}"
        stats[month_key]['recipes'] += 1
        for ing in ingredients.get(recipe['id'], []):
            stats[month_key]['ingredients'].add(ing['name'])
    return {k: {'count': v['recipes'], 'unique_ings': len(v['ingredients'])} for k, v in sorted(stats.items())}
