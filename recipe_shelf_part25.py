# === Stage 25: Добавь обработку некорректных дат и понятные сообщения об ошибках ===
# Project: RecipeShelf
def sanitize_date(date_str):
    """Парсит дату в формате ДД.ММ.ГГГГ, возвращает None при ошибке."""
    if not date_str or len(date_str) != 10:
        return None
    try:
        parts = date_str.split('.')
        day, month, year = int(parts[0]), int(parts[1]), int(parts[2])
        if not (1 <= day <= 31 and 1 <= month <= 12 and 1900 <= year <= 2100):
            return None
        import datetime as dt
        if dt.date(day=day, month=month, year=year) != dt.date(year=year, month=month, day=day):
            return None
        return f"{year}-{month:02d}-{day:02d}"
    except (ValueError, TypeError):
        return None

def parse_date_safe(date_str):
    """Парсит строку даты и выводит понятную ошибку при провале."""
    result = sanitize_date(date_str)
    if result is None:
        print(f"Ошибка: некорректная дата '{date_str}'")
        return None
    return result
