# === Stage 15: Добавь расчёт недельной статистики по датам ===
# Project: RecipeShelf
def calculate_weekly_stats(recipes, start_date):
    from datetime import timedelta, date
    week_start = start_date - timedelta(days=start_date.weekday())
    week_end = week_start + timedelta(weeks=1)
    daily_totals = {d: 0 for d in range(date.fromtimestamp(start_date.timestamp()), date.fromtimestamp(week_end.timestamp()))}
    for r in recipes:
        if r.get('date') and start_date <= r['date'] < week_end:
            day_key = r['date'].strftime('%Y-%m-%d')
            try:
                daily_totals[date.strptime(day_key, '%Y-%m-%d')] += 1
            except ValueError:
                pass
    return {k.strftime('%Y-%m-%d'): v for k, v in sorted(daily_totals.items()) if v > 0}
