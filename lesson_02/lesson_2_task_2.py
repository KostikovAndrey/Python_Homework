def is_year_leap(year):
    """
    Проверяет, является ли год високосным.

    Args:
        year (int): Год для проверки

    Returns:
        bool: True если год високосный, False если нет
    """
    return year % 4 == 0


# Выберите год для проверки
year_to_check = 2024

# Вызываем функцию и сохраняем результат в переменную
result = is_year_leap(year_to_check)

# Выводим результат в нужном формате
print(f"год {year_to_check}: {result}")

# Дополнительные примеры для демонстрации
print(f"год 2023: {is_year_leap(2023)}")
print(f"год 2008: {is_year_leap(2008)}")
print(f"год 2009: {is_year_leap(2009)}")
print(f"год 2020: {is_year_leap(2020)}")
