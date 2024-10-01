import random

def get_numbers_ticket(min, max, quantity):
    # Перевірка на діапазон по обмеженням
    if min < 1 or max > 1000 or quantity < 1 or quantity > (max - min + 1):
        return [] # Повертаємо пустий список
    
    #Генерація унікальних випадкових чисел
    unique_nums = set()

    while len(unique_nums) < quantity:
        numbers = random.randint(min, max)
        unique_nums.add(numbers) # Формуємо унікальність

    return sorted(unique_nums) #Повертаємо відсортований список

#Приклад

lottery_nums = get_numbers_ticket(1,49,6)
print("Ваші номери:", lottery_nums)
lottery_nums_var = get_numbers_ticket(1,36,5)
print("Ваші номери:", lottery_nums_var)
    