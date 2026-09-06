# === Stage 48: Проведи рефакторинг: разнеси крупные функции, сохрани совместимость публичных команд ===
# Project: RecipeShelf
def _split_ingredients(text):
    """Разбивает строку ингредиентов на список, разделяя по запятой,
    отбрасывая лишние пробелы и пустые элементы."""
    return [item.strip() for item in text.split(',') if item.strip()]

def _parse_ingredients(text):
    """Парсит строку ингредиентов, возвращая список уникальных
    строк, отсортированных в исходном порядке появления."""
    seen = set()
    result = []
    for item in _split_ingredients(text):
        if item and item not in seen:
            seen.add(item)
            result.append(item)
    return result

def _format_ingredients(items):
    """Формирует строку ингредиентов из списка, разделяя запятой."""
    return ', '.join(items)

def _normalize_ingredients(items):
    """Нормализует список ингредиентов: убирает лишние пробелы
    и приводит к нижнему регистру."""
    return [item.strip().lower() for item in items]

def _deduplicate_ingredients(items):
    """Удаляет дубликаты из списка ингредиентов, сохраняя порядок."""
    seen = set()
    result = []
    for item in items:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

def _sort_ingredients(items):
    """Сортирует список ингредиентов по алфавиту."""
    return sorted(items)

def _find_ingredient(items, query):
    """Ищет ингредиент в списке, используя нормализованное сравнение."""
    normalized = _normalize_ingredients(items)
    normalized_query = query.strip().lower()
    for item in normalized:
        if normalized_query in item or item in normalized_query:
            return item
    return None

def _build_shopping_list(items):
    """Создаёт список покупок из ингредиентов, отфильтрованных по наличию."""
    return [item for item in items if item is not None]

def _print_ingredients(items):
    """Выводит список ингредиентов в отформатированном виде."""
    print(_format_ingredients(items))

def _print_shopping_list(items):
    """Выводит список покупок в отформатированном виде."""
    print(_format_ingredients(items))

def _print_search_results(items):
    """Выводит результаты поиска ингредиентов."""
    print(_format_ingredients(items))

def _print_sorted_ingredients(items):
    """Выводит отсортированный список ингредиентов."""
    print(_format_ingredients(items))

def _print_deduplicated_ingredients(items):
    """Выводит список ингредиентов без дубликатов."""
    print(_format_ingredients(items))

def _print_normalized_ingredients(items):
    """Выводит нормализованный список ингредиентов."""
    print(_format_ingredients(items))

def _print_unique_ingredients(items):
    """Выводит список уникальных ингредиентов."""
    print(_format_ingredients(items))

def _print_single_ingredient(item):
    """Выводит одиночный ингредиент."""
    print(item)

def _print_all_ingredients(items):
    """Выводит все ингредиенты, разделённые запятой."""
    print(_format_ingredients(items))
