# === Stage 21: Добавь простую систему напоминаний с датой выполнения ===
# Project: RecipeShelf
import json, datetime

def save_reminders(data):
    with open('reminders.json', 'w') as f:
        json.dump(data.get('reminders', []), f)

def load_reminders():
    try:
        with open('reminders.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def add_reminder(recipe_name, ingredient, date_str):
    reminders = load_reminders()
    reminder = {
        "recipe": recipe_name,
        "ingredient": ingredient,
        "date": datetime.datetime.strptime(date_str, "%Y-%m-%d").strftime("%Y-%m-%d"),
        "completed": False
    }
    reminders.append(reminder)
    save_reminders({"reminders": reminders})
    return reminder

def get_due_today():
    today = datetime.date.today().isoformat()
    due_list = [r for r in load_reminders() if not r["completed"] and r["date"] == today]
    return due_list
