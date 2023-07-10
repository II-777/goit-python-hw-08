from datetime import datetime, timedelta

def get_birthdays_per_week(users):
    today = datetime.now().date()
    next_monday = today + timedelta(days=(7 - today.weekday()) % 7)
    birthdays_per_week = []

    for i in range(7):
        current_day = next_monday + timedelta(days=i)
        birthday_users = [user['name'] for user in users if user['birthday'].date() == current_day]
        if birthday_users:
            celebration_day = "This" if i == 0 else "Next"
            if current_day.weekday() in [5, 6]:  # Saturday or Sunday
                celebration_day += " Monday"
            else:
                celebration_day += f" {current_day.strftime('%A')}"
            birthdays_per_week.append(f"{celebration_day}: {', '.join(birthday_users)}")

    return birthdays_per_week

users = [
    {'name': 'Bill', 'birthday': datetime(2023, 7, 10)},
    {'name': 'Jill', 'birthday': datetime(2023, 7, 10)},
    {'name': 'Kim', 'birthday': datetime(2023, 7, 16)},
    {'name': 'Jan', 'birthday': datetime(2023, 7, 16)},
]

birthdays = get_birthdays_per_week(users)

if birthdays:
    for birthday in birthdays:
        print(birthday)
else:
    print("No birthdays to celebrate this week.")
