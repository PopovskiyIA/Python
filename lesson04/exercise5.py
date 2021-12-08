# Реализовать формирование списка, используя функцию range() и возможности генератора. В список должны войти четные
# числа от 100 до 1000 (включая границы). Необходимо получить результат вычисления произведения всех элементов списка.

from functools import reduce

even_numbers = [number for number in range(100, 1001) if number % 2 == 0]


def multiplication(previous_element, current_element):
    """
    Функция перемножает аргументы

    :param previous_element: предыдущий элеменит
    :param current_element: текущий элемент
    :return: произведение двух аргументов
    """
    return int(previous_element) * int(current_element)


print(reduce(multiplication, even_numbers))
