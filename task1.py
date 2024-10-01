from datetime import datetime

# Створіть функцію get_days_from_today(date)


def get_days_from_today(date):
    # Функція приймає один параметр:дату у форматі 'РРРР-ММ-ДД' (наприклад, '2020-10-09').
    given_date = datetime.strptime(date, "%Y-%m-%d")
# Отримайте поточну дату, використовуючи
    today = datetime.now()
# Розрахуйте різницю між поточною датою та заданою датою.
    difference = (today - given_date).days
# Поверніть різницю у днях як ціле число.
    return difference


date_input = "2025-10-30"

days_difference = get_days_from_today(date_input)
print(f"Скільки днів з {date_input} до сьогодні: {days_difference}")
