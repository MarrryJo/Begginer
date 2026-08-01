# === Stage 37: Добавь мини-набор unit-тестов без внешних зависимостей ===
# Project: RecipeShelf
import unittest


class TestRecipeShelf(unittest.TestCase):
    def setUp(self):
        from recipe_shelf import RecipeShelf
        self.app = RecipeShelf()

    def test_add_recipe(self):
        self.app.add_recipe("Омлет", ["яйца"], "5 мин")
        recipes = list(self.app.get_all_recipes())
        self.assertEqual(len(recipes), 1)
        self.assertEqual(recipes[0].name, "Омлет")

    def test_search_by_name(self):
        self.app.add_recipe("Борщ", ["свекла", "картофель"], "1 ч")
        results = list(self.app.search_recipes("б"))
        names = [r.name for r in results]
        self.assertIn("Борщ", names)

    def test_search_by_ingredient(self):
        self.app.add_recipe("Салат", ["огурец", "помидор"], "5 мин")
        results = list(self.app.search_recipes(ingredient="огурец"))
        self.assertEqual(len(results), 1)

    def test_add_to_shopping_list(self):
        self.app.add_to_shopping_list("яйца", 2)
        self.app.add_to_shopping_list("молоко", 1)
        items = list(self.app.get_shopping_items())
        self.assertEqual(len(items), 2)

    def test_shopping_item_count(self):
        self.app.add_to_shopping_list("яйца", 3)
        item = next(i for i in self.app.get_shopping_items() if i.name == "яйца")
        self.assertEqual(item.quantity, 3)


if __name__ == "__main__":
    unittest.main()
