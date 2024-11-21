import random


def get_numbers_ticket(min, max, quantity):
    # Перевірка на некоректні вхідні дані
    if min >= max or quantity > (max - min + 1) or min < 0 or quantity <= 0:
        return []

    numbers = []
    while len(numbers) < quantity:
        random_number = random.randint(min, max)
        if random_number not in numbers:
            numbers.append(random_number)
    return numbers


# Тестування функції
lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)
