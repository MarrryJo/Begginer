# === Stage 42: Добавь цветной вывод через ANSI-коды с возможностью отключения ===
# Project: RecipeShelf
import os

def color(text, color):
    """Print colored text with optional ANSI disable."""
    if os.environ.get("DISABLE_ANSI"):
        return text
    codes = {
        "red": "\033[31m", "green": "\033[32m", "yellow": "\033[33m",
        "blue": "\033[34m", "magenta": "\033[35m", "cyan": "\033[36m",
        "white": "\033[37m", "bold": "\033[1m", "reset": "\033[0m",
    }
    code = codes.get(color, codes["reset"])
    print(f"{code}{text}{codes['reset']}")
