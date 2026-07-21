# === Stage 30: Добавь поддержку нескольких пользовательских профилей внутри приложения ===
# Project: RecipeShelf
class Profile:
    def __init__(self, name, preferences=None):
        self.name = name
        self.preferences = preferences or {}

    @classmethod
    def from_input(cls):
        print("Введите имя профиля:")
        name = input("> ").strip() or "Default"
        prefs = {}
        while True:
            print("Добавьте предпочтение (например, 'аллергия: глютен'), или введите 'готово':")
            line = input("> ").strip()
            if line == "готово":
                break
            key, val = line.split(":")
            prefs[key.strip()] = val.strip()
        return cls(name, prefs)

    def save(self, path="profiles.json"):
        import json
        data = [{"name": self.name, "preferences": self.preferences}]
        existing = []
        if os.path.exists(path):
            with open(path) as f:
                existing = json.load(f)
            for e in existing:
                if e["name"] == self.name and e.get("preferences") == self.preferences:
                    return
            data.extend(existing)
        with open(path, "w") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

    @classmethod
    def load(cls, path="profiles.json"):
        import json, os
        if not os.path.exists(path):
            return [cls("Default", {})]
        with open(path) as f:
            data = json.load(f)
        return [cls(d["name"], d.get("preferences", {})) for d in data]

    def find(self, ingredient):
        import re
        pattern = re.compile(ingredient, re.IGNORECASE)
        return any(pattern.search(p.lower()) for p in self.preferences.values())


profiles = Profile.load() if __import__("os").path.exists("profiles.json") else [Profile("Default", {})]

def show_profiles():
    print("\n=== Профили ===")
    for i, p in enumerate(profiles):
        print(f"  [{i}] {p.name} — предпочтения: {', '.join(p.preferences.keys()) if p.preferences else 'нет'}")


def get_profile(index=None):
    if not profiles:
        return None
    if index is None and len(profiles) == 1:
        return profiles[0]
    if index < 0 or index >= len(profiles):
        print("Неверный индекс профиля.")
        return None
    show_profiles()
    try:
        idx = int(input(f"Выберите профиль (0-{len(profiles)-1}): "))
        return profiles[idx]
    except ValueError:
        return None


def apply_profile_filter(ingredient, profile):
    if not profile or ingredient in ("", "_"):
        return True
    return profile.find(ingredient)
