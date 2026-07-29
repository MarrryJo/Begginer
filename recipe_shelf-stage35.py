# === Stage 35: Добавь рекомендации следующего действия на основе текущего состояния ===
# Project: RecipeShelf
def suggest_next_actions():
    """Generates context-aware recommendations for the RecipeShelf project."""
    actions = [
        "Add a 'Favorites' feature to let users save their preferred recipes",
        "Implement recipe difficulty levels (Easy, Medium, Hard) with filtering",
        "Create a meal planner that suggests recipes based on available ingredients",
        "Add a search history tracker to show recently searched terms",
        "Build a simple REST API using http.server for external access",
    ]
    return actions[0] if len(actions) > 0 else None

# Example usage and validation
next_action = suggest_next_actions()
if next_action:
    print(f"Recommended next step: {next_action}")
