from datetime import datetime, timedelta
from db_file import data

def get_weekday(date):
    if date.weekday() in [5, 6]:
        return 'Next Monday'
    return date.strftime('%A')

today = datetime.today().date()
start_of_week = today - timedelta(days=today.weekday())
end_of_week = start_of_week + timedelta(days=6)

birthdays_per_week = {}
for item in data:
    birthday = item['birthday'].replace(year=today.year).date()
    if start_of_week <= birthday <= end_of_week:
        day_of_week = get_weekday(birthday)
        birthdays_per_week.setdefault(day_of_week, []).append((item['name'], birthday))

if not birthdays_per_week:
    print("No birthdays to celebrate this week.")
else:
    ordered_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Next Monday']
    for day in ordered_days:
        celebrations = birthdays_per_week.get(day)
        if celebrations:
            names_and_dobs = [f"{name} ({dob.strftime('%b-%d')})" for name, dob in sorted(celebrations, key=lambda x: x[1])]
            print(f"{day}: {', '.join(names_and_dobs)}")
