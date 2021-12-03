# Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших двух
# аргументов.

def my_func(num1, num2, num3):
    """
    Функция принимает три аргумента и возвращает сумму наибольших двух аргументов

    :param num1: первое число
    :param num2: второе число
    :param num3: тертье число
    :return: сумма наибольших двух аргументов
    """
    try:
        first = int(num1)
        second = int(num2)
        third = int(num3)
        first_pair_sum = first + second
        second_pair_sum = second + third
        third_pair_sum = first + third
        return max(first_pair_sum, second_pair_sum, third_pair_sum)
    except ValueError:
        print("Не могу вычислить наибольшую сумму двух аргументов, так как были переданы некорректные данные")


# тест
input_values = input("Введите три числа через пробел: ").split(" ")
if len(input_values) == 3:
    result = my_func(input_values[0], input_values[1], input_values[2])
    print(f"Наибольшая сумма двух аргументов равна {result}")
else:
    print("Вы ввели неправильное количество чисел")
