# === Stage 45: Добавь восстановление из резервной копии ===
# Project: RecipeShelf
def load_recipe_from_backup():
    """Восстанавливает рецепт из резервной копии .bak файла."""
    backup_file = "recipes_backup.bak"
    if not os.path.exists(backup_file):
        print("Резервная копия не найдена.")
        return None
    with open(backup_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    recipes = data.get("recipes", {})
    for r in recipes:
        r["id"] = r.get("id", random.randint(1000, 9999))
        r["date_added"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"Восстановлено {len(recipes)} рецептов из резервной копии.")
    return recipes
