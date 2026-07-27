# === Stage 34: Добавь простую систему шаблонов для быстрого создания записей ===
# Project: RecipeShelf
def create_from_template(template_name, **kwargs):
    templates = _get_templates()
    if template_name not in templates:
        raise ValueError(f"Unknown template: {template_name}")
    tmpl = templates[template_name]()
    for field, value in kwargs.items():
        setattr(tmpl, field, value)
    return tmpl

def add_from_template(template_name, **kwargs):
    recipe = create_from_template(template_name, **kwargs)
    recipes.append(recipe)
    return recipe

_register_templates(
    "quick_salad", lambda: Recipe(title="Салат-капуста", ingredients=[{"name": "Капуста", "amount": 1}, {"name": "Уксус", "amount": 2}], servings=4, prep_time=5),
    "quick_soup", lambda: Recipe(title="Куриный суп", ingredients=[{"name": "Курица", "amount": 300}, {"name": "Картофель", "amount": 2}, {"name": "Лук", "amount": 1}], servings=6, prep_time=40),
)

add_from_template("quick_salad", title="Салат-капуста с морковью")
