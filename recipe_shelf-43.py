# === Stage 43: Добавь пагинацию длинных списков ===
# Project: RecipeShelf
class Pagination:
    def __init__(self, items, page_size=10):
        self.items = items
        self.page_size = page_size
        self.total_pages = (len(items) + page_size - 1) // page_size if items else 0

    def page(self, page_num):
        start = (page_num - 1) * self.page_size
        end = start + self.page_size
        return self.items[start:end], page_num < self.total_pages, page_num > 1

    def pages(self):
        return list(range(1, self.total_pages + 1))
Pagination
