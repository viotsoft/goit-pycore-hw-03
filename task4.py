from datetime import datetime, timedelta

def get_upcoming_birthdays(users):
    today = datetime.today().date() # Поточна дата
    upcoming_birthdays = []

    for user in users:
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date().replace(year=today.year) 
        # Конвертуємо дату народження з рядка в об'єкт datetime

        if birthday < today:
            birthday = birthday.replace(year=today.year + 1)
            # Якщо день народження вже був цього року, то беремо його на наступний рік


        days_until_birthday = (birthday - today).days #різницю між днем народження та поточним днем

        if 0 <= days_until_birthday <= 7:
            if birthday.weekday() in [5, 6]:  # Якщо день народження на вихідні дні
                # переносимо на робочі дні привітання
                monday = today + timedelta(days=(7 - today.weekday()) + 1)
                congratulation_date = monday.strftime("%Y.%m.%d")
            else:
                congratulation_date = birthday.strftime("%Y.%m.%d")

            # Додаємо користувача та дату привітання в результат
            upcoming_birthdays.append({
                "name": user["name"],
                "congratulation_date": congratulation_date
            })

    return upcoming_birthdays

# Приклад використання функції

users = [
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.27"}
]
upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)


# Для тестування з конкретною датою
# Змінюємо дату на 2024.01.22 для отримання заданого результату
today_fixed = datetime(2024, 1, 22).date()

# Зміна значення today в функції для тестування
def get_upcoming_birthdays_fixed(users, today_fixed):
    end_date = today_fixed + timedelta(days=7)  # Дата через 7 днів
    upcoming_birthdays = []

    for user in users:
        name = user['name']
        # Конвертуємо дату народження з рядка в об'єкт datetime
        birthday = datetime.strptime(user['birthday'], "%Y.%m.%d").date()

        # Створюємо дату дня народження на поточний рік
        birthday_this_year = birthday.replace(year=today_fixed.year)

        # Якщо день народження вже був цього року, то беремо його на наступний рік
        if birthday_this_year < today_fixed:
            birthday_this_year = birthday_this_year.replace(year=today_fixed.year + 1)

        # Якщо день народження випадає в межах наступних 7 днів
        if today_fixed <= birthday_this_year <= end_date:
            # Перевіряємо, чи день народження припадає на вихідний
            if birthday_this_year.weekday() == 5:  # Субота
                congratulation_date = birthday_this_year + timedelta(days=2)  # Переносимо на понеділок
            elif birthday_this_year.weekday() == 6:  # Неділя
                congratulation_date = birthday_this_year + timedelta(days=1)  # Переносимо на понеділок
            else:
                congratulation_date = birthday_this_year  # Якщо будній день, залишаємо дату
            
            # Додаємо користувача та дату привітання в результат
            upcoming_birthdays.append({
                'name': name,
                'congratulation_date': congratulation_date.strftime('%Y.%m.%d')
            })
    
    return upcoming_birthdays

# Викликаємо функцію та виводимо результат
upcoming_birthdays = get_upcoming_birthdays_fixed(users, today_fixed)
print("Список привітань на цьому тижні:", upcoming_birthdays)