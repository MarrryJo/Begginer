# === Stage 32: Добавь журнал действий пользователя ===
# Project: RecipeShelf
class ActionLog:
    def __init__(self, max_size=100):
        self._log = []
        self.max_size = max_size

    def log(self, action_type, recipe_id=None, ingredient_ids=None):
        entry = {"type": action_type}
        if recipe_id is not None:
            entry["recipe"] = recipe_id
        if ingredient_ids is not None:
            entry["ingredients"] = list(ingredient_ids)
        self._log.append(entry)
        if len(self._log) > self.max_size:
            del self._log[:self.max_size - len(self._log)]

    def get_log(self):
        return list(reversed(self._log))

    def summary(self):
        counts = {}
        for entry in self._log:
            t = entry.get("type", "unknown")
            counts[t] = counts.get(t, 0) + 1
        return counts


class RecipeShelfWithLog(RecipeShelf):
    def __init__(self):
        super().__init__()
        self.action_log = ActionLog()

    def search(self, query):
        results = [r for r in self.recipes if any(query.lower() in name.lower() for name in r["names"])]
        self.action_log.log("search", ingredient_ids=[i.id for i in results[0]["ingredients"] if results])
        return results

    def get_shopping_list(self, recipe_id):
        recipe = next((r for r in self.recipes if r["id"] == recipe_id), None)
        if not recipe:
            raise ValueError(f"Recipe {recipe_id} not found")
        list_ = [ing.to_dict() for ing in recipe["ingredients"]]
        self.action_log.log("shopping_list", ingredient_ids=[i.id for i in list_])
        return list_

    def add_recipe(self, recipe_data):
        r = super().add_recipe(recipe_data)
        self.action_log.log("add_recipe")
        return r

    def remove_recipe(self, recipe_id):
        removed = super().remove_recipe(recipe_id)
        if removed:
            self.action_log.log("remove_recipe", recipe_id=recipe_id)
        return removed
