def fizz_buzz(n):
    """
    Печатает числа от 1 до n с заменой:
    - чисел, кратных 3, на "Fizz"
    - чисел, кратных 5, на "Buzz"
    - чисел, кратных 3 и 5, на "FizzBuzz"

    Args:
        n (int): Верхняя граница диапазона
    """
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)


# Вызов функции с примером
fizz_buzz(17)
