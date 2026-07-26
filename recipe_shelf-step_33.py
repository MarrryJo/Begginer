# === Stage 33: Добавь откат последнего действия там, где это разумно ===
# Project: RecipeShelf
class ActionHistory:
    def __init__(self):
        self._stack = []

    @property
    def stack(self):
        return self._stack

    def push(self, action):
        self._stack.append(action)

    def pop(self):
        if not self._stack:
            raise IndexError("Action history is empty")
        return self._stack.pop()

    def clear(self):
        self._stack.clear()


def undo_recipe_action(recipe_state, recipe_id):
    actions = {
        "add_ingredient": lambda s, r: (s["ingredients"], s["name"]),
        "remove_ingredient": lambda s, r: (s["ingredients"], s["name"]),
        "update_name": lambda s, r: (s["name"], s["name"]),
    }

    if recipe_id not in actions:
        return recipe_state

    current = actions[recipe_id](recipe_state, recipe_id)
    return current
