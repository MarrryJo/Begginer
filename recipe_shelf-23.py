# === Stage 23: Добавь форматированный вывод таблицей в консоль ===
# Project: RecipeShelf
import sys


def format_table(headers, rows):
    """Compact console table: aligns columns by width and prints them."""
    if not headers or not rows:
        return ""
    ncols = len(headers)
    widths = [len(str(h)) for h in headers]
    for row in rows:
        if row is None:
            continue
        cells = list(row)
        if len(cells) != ncols:
            while len(cells) < ncols:
                cells.append("")
            cells = cells[:ncols]
        for i, cell in enumerate(cells):
            w = widths[i]
            s = str(cell)
            if len(s) > w:
                s = s[:w - 1] + "\n" + s[w - 1:]
                widths[i] += 1
        for i, cell in enumerate(cells):
            s = str(cell).replace("\n", " ")
            cells[i] = s
    lines = [f"{'|'.join(str(h).ljust(widths[i]) for i, h in enumerate(headers))}"]
    sep = f"{'—' * widths[0]}|"
    for w in widths[1:]:
        sep += f"{'—' * w}|"
    lines.append(sep)
    for row in rows:
        line = " | ".join(str(c).ljust(widths[i]) for i, c in enumerate(cells))
        lines.append(line)
    return "\n".join(lines)


if __name__ == "__main__":
    print(format_table(
        ["ID", "Название", "Категория"],
        [
            (1, "Борщ", "Суп"),
            (2, "Оладьи", "Десерт"),
            (3, "Пельмени", "Горячее"),
        ],
    ))
