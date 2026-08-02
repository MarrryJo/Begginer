# === Stage 38: Добавь расширенный набор тестов для ошибок и пограничных случаев ===
# Project: RecipeShelf
def test_error_handling():
    assert is_valid_recipe_name("") == False
    assert is_valid_recipe_name("   ") == False
    assert is_valid_recipe_name(None) == False
    assert get_ingredient(1, {}) == None
    assert get_ingredient(0, {"a": 1}) == 1
    assert get_ingredient(-1, {"a": 1}) == None
    assert search_recipes("nonexistent", []) == []
    assert search_recipes("", [{}]) == [{}]
    assert calculate_shopping_list({}) == set()
    assert calculate_shopping_list({"a": "b"}) == {"b"}
