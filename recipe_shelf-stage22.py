# === Stage 22: Добавь проверку просроченных напоминаний ===
# Project: RecipeShelf
def check_expired_reminders(self):
            now = datetime.now()
            for reminder in self.reminders:
                if reminder['date'] < now and not reminder.get('done', False):
                    print(f"⚠️  Напоминание просрочено: {reminder['message']}")
