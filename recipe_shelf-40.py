# === Stage 40: Добавь CLI-параметры через argparse для основных операций ===
# Project: RecipeShelf
def main():
    import argparse
    parser = argparse.ArgumentParser(description="RecipeShelf CLI")
    parser.add_argument("action", choices=["add", "search", "list"], help="Операция")
    args = parser.parse_args()
    if args.action == "add":
        print("Добавление рецепта")
    elif args.action == "search":
        print("Поиск рецептов")
    elif args.action == "list":
        print("Список рецептов")

if __name__ == "__main__":
    main()
