from datetime import datetime


def get_days_from_today(date):
    """
    Функція приймає один параметр: дату у форматі 'YYYY-MM-DD'.
    """
    try:
        given_date = datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        raise ValueError(
            "Неправильний формат дати. Використовуйте формат 'YYYY-MM-DD'.")

    # Отримуємо поточну дату
    today = datetime.now()
    # Розрахунок різниці в днях
    difference = (today - given_date).days
    return difference


# Приклад використання
date_input = "2024-10-30"

try:
    days_difference = get_days_from_today(date_input)
    print(f"Скільки днів з {date_input} до сьогодні: {days_difference}")
except ValueError as e:
    print(e)
