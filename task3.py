import re


def normalize_phone(phone_number):
    """
    Функція нормалізує телефонні номери, видаляючи зайві символи 
    і додаючи код країни '+38' для українських номерів, якщо код не вказаний.
    """
    # Видалення всіх символів, окрім цифр та '+'
    phone_number = re.sub(r'[^\d+]', '', phone_number)

    # Якщо номер починається з '+'
    if phone_number.startswith('+'):
        # Якщо номер не починається з '+380', залишаємо код країни як є
        if not phone_number.startswith('+380'):
            return phone_number
    else:
        # Якщо номер починається з '380', додаємо '+'
        if phone_number.startswith('380'):
            phone_number = '+' + phone_number
        else:
            # Якщо немає міжнародного коду, додаємо код '+38'
            phone_number = '+38' + phone_number

    return phone_number


# Тестування функції з різними форматами номерів
raw_numbers = [
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

# Перевірка результатів
normalized_phones = [normalize_phone(phone) for phone in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", normalized_phones)
