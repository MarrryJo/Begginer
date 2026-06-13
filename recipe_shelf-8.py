# === Stage 8: Реализуй текстовый интерфейс команд с меню действий ===
# Project: RecipeShelf
def print_menu():
    print("\n=== RecipeShelf Menu ===")
    print("1. Show recipes list")
    print("2. Search recipes by name")
    print("3. View ingredients for a recipe")
    print("4. Generate shopping list from selected recipes")
    print("5. Exit")

def run_cli():
    while True:
        try:
            print_menu()
            choice = input("\nEnter command number (1-5): ").strip()
            if choice == "1":
                for r in RECIPES:
                    print(f"\n--- {r['name']} ---")
                    print(r.get('description', 'No description'))
            elif choice == "2":
                query = input("Enter search keyword: ")
                results = [r for r in RECIPES if query.lower() in r['name'].lower()]
                if results:
                    for r in results:
                        print(f"Found: {r['name']}")
                else:
                    print("No recipes found.")
            elif choice == "3":
                name = input("Enter recipe name to view ingredients: ")
                target = next((r for r in RECIPES if r['name'].lower() == name.lower()), None)
                if target:
                    print(f"Ingredients for {target['name']}:")
                    for ing in target.get('ingredients', []):
                        print(f"- {ing}")
                else:
                    print("Recipe not found.")
            elif choice == "4":
                selected = input("Enter recipe name to add to shopping list (or 'all'): ").strip().lower()
                items = set()
                if selected != "all":
                    target = next((r for r in RECIPES if r['name'].lower() == selected), None)
                    if not target:
                        print("Recipe not found.")
                        continue
                    for ing in target.get('ingredients', []):
                        items.add(ing.lower())
                else:
                    for r in RECIPES:
                        for ing in r.get('ingredients', []):
                            items.add(ing.lower())
                if items:
                    print("\nShopping List:")
                    for item in sorted(items):
                        print(f"- {item.capitalize()}")
            elif choice == "5":
                print("Goodbye!")
                break
            else:
                print("Invalid command. Please try again.")
        except KeyboardInterrupt:
            print("\nExiting...")
            break
