# === Stage 29: Добавь конфигурацию приложения через словарь настроек ===
# Project: RecipeShelf
APP_SETTINGS = {
    "app_name": "RecipeShelf",
    "version": "0.1.0",
    "language": "ru",
    "default_encoding": "utf-8",
    "max_recipe_title_length": 255,
    "search_max_results": 20,
    "shopping_list_default_days_validity": 7,
    "log_level": "INFO",
}

def get_setting(key: str):
    """Возвращает значение настройки по ключу или None."""
    return APP_SETTINGS.get(key)


def set_app_config(**kwargs):
    """Обновляет настройки приложения из словаря. Возвращает обновлённый словарь."""
    global APP_SETTINGS
    APP_SETTINGS.update(kwargs)
    return dict(APP_SETTINGS)
