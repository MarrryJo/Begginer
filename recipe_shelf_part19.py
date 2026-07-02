# === Stage 19: Добавь функцию архивации завершённых или старых записей ===
# Project: RecipeShelf
def archive_recipes(archive_threshold_days=365):
    import datetime
    cutoff_date = datetime.date.today() - datetime.timedelta(days=archive_threshold_days)
    archived_count = 0
    for recipe_id, data in list(recipe_database.items()):
        if 'archived' not in data or not data['archived']:
            last_used = data.get('last_used', None)
            if last_used and datetime.date.fromtimestamp(last_used.timestamp()) < cutoff_date:
                data['archived'] = True
                archived_count += 1
    return archived_count
