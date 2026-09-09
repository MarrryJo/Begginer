# === Stage 50: Сделай аккуратную финальную полировку сообщений, названий функций и комментариев ===
# Project: RecipeShelf
def polish_recipe_display(recipe):
    """Returns a nicely formatted display string for a recipe."""
    lines = [f"📖 {recipe['name']}"]
    lines.append(f"⏱  Время: {recipe.get('time', '—')} мин")
    if recipe.get('difficulty'):
        icons = {'Easy': '😊', 'Medium': '😐', 'Hard': '🤯'}
        lines.append(f"💪 Сложность: {icons.get(recipe['difficulty'], recipe['difficulty'])}")
    lines.append(f"👥 Порций: {recipe.get('servings', '—')}")
    lines.append(f"🔥 Калории: {recipe.get('calories', '—')} ккал")
    lines.append(f"📝 Ингредиенты:")
    for ing in recipe.get('ingredients', []):
        lines.append(f"  • {ing['name']} — {ing.get('amount', '')}")
    lines.append(f"🔍 Ингредиенты, которые нужно купить:")
    for ing in recipe.get('shopping', []):
        lines.append(f"  • {ing['name']} — {ing.get('amount', '')}")
    lines.append(f"👨‍🍳 Шаги приготовления:")
    for i, step in enumerate(recipe.get('steps', []), 1):
        lines.append(f"  {i}. {step}")
    lines.append(f"🏷️  Метки: {', '.join(recipe.get('tags', [])) or '—'}")
    return "\n".join(lines)
