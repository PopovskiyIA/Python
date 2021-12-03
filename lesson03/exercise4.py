# Программа принимает действительное положительное число x и целое отрицательное число y. Необходимо выполнить
# возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y). При решении задания
# необходимо обойтись без встроенной функции возведения числа в степень.

def my_func(base, negative_power):
    """
    Функция возводит число в отрицательную степень

    :param base: основание
    :param negative_power: показатель степени
    :return: base в степени negative_power
    """
    try:
        base_value = float(base)
        power_value = int(negative_power)
        if base_value > 0 > power_value:
            result = 1
            for i in range(abs(power_value)):
                result *= 1.0/base_value
            return result
        elif base_value < 0:
            print("Основние степени ниже нуля")
        else:
            print("Показатель степени больше нуля")
    except ValueError:
        print("Были переданы некорректные данные в функцию возведения в степень")


# тест
first_value = input("Введите действительное положительное число: ")
second_value = input("Введите целое отрицательное число: ")
result_value = my_func(first_value, second_value)
print(f"Результат возведения в степень = {result_value}")
