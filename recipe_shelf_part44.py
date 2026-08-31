# === Stage 44: Добавь функцию резервного копирования файла данных ===
# Project: RecipeShelf
import shutil, os, datetime

def backup_data_file(filepath: str, backup_dir: str = "backups") -> str:
    """Сохраняет текущую версию файла данных в архив с временной меткой.
    Возвращает путь к созданному файлу. Если файл не существует — создаёт пустой.
    """
    os.makedirs(backup_dir, exist_ok=True)
    if not os.path.exists(filepath):
        src = os.path.join(backup_dir, "empty.dat")
        shutil.copy(src, filepath)
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_path = os.path.join(backup_dir, f"{os.path.basename(filepath)}.{timestamp}.bak")
    shutil.copy2(filepath, backup_path)
    return backup_path

if __name__ == "__main__":
    print(backup_data_file(__file__))
