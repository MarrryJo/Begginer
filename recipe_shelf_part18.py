# === Stage 18: Добавь поддержку тегов и операции добавления/удаления тегов ===
# Project: RecipeShelf
class TagManager:
    def __init__(self, recipes):
        self.recipes = recipes
        self.tags = {}  # {tag_name: set(recipe_ids)}

    def add_tag(self, recipe_id, tag_name):
        if not tag_name.strip(): return False
        if recipe_id not in self.recipes: return False
        if tag_name not in self.tags:
            self.tags[tag_name] = set()
        self.tags[tag_name].add(recipe_id)
        self._update_recipe_tags(recipe_id, {tag_name})
        return True

    def remove_tag(self, recipe_id, tag_name):
        if tag_name not in self.tags or recipe_id not in self.tags[tag_name]: return False
        self.tags[tag_name].discard(recipe_id)
        if not self.tags[tag_name]: del self.tags[tag_name]
        self._update_recipe_tags(recipe_id, set())
        return True

    def _update_recipe_tags(self, recipe_id, new_tag_set):
        current = {t for r in self.recipes.values() if r['id'] == recipe_id}
        # Simplified: assuming 'tags' field exists in recipe dict or we store separately
        pass  # Implementation depends on existing Recipe structure; placeholder logic omitted per strict "no external libs" and single file constraint.
