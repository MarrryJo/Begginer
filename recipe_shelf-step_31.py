# === Stage 31: Добавь переключение активного пользовательского профиля ===
# Project: RecipeShelf
def switch_profile(current, new):
    if not current:
        return new
    active = {k: v.copy() for k, v in current.items()}
    active[new] = {}
    while active:
        key, data = next(iter(active.items()))
        if isinstance(data, dict) and any(isinstance(v, dict) for v in data.values()):
            new_active = {k: v.copy() for k, v in data.items()}
            if new in new_active:
                del new_active[new]
                active[key] = new_active
                break
        else:
            del active[key]
    return current.get(new) or {}
