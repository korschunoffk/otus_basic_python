"""
Домашнее задание №1
Функции и структуры данных
"""


def power_numbers(*args):
    return [item * item for item in args]
    """
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    >>> power_numbers(1, 2, 5, 7)
    <<< [1, 4, 25, 49]
    """

def is_number_odd(num):
    if (num % 2) != 0:
        return True
    else:
        return False

def is_number_even(num):
    if (num % 2) == 0:
        return True
    else:
        return False

def is_number_prime(num):
    count = 0
    current_val = 1
    while num >= current_val:
        if (num % current_val == 0):
            count = count + 1
        current_val = current_val + 1
    if count == 2:
        return True
    else:
        return False

# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"

def filter_numbers(numbers, filter_arg = ODD):
    if filter_arg == ODD:
        return list(filter(is_number_odd, numbers))
    elif filter_arg == EVEN:
        return list(filter(is_number_even, numbers))
    elif filter_arg == PRIME:
        return list(filter(is_number_prime, numbers))
    else:
        return
    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)

    >>> filter_numbers([1, 2, 3], ODD)
    <<< [1, 3]
    >>> filter_numbers([2, 3, 4, 5], EVEN)
    <<< [2, 4]
    """

