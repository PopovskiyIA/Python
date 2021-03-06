# Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение. При вызове функции
# должен создаваться объект-генератор. Функция должна вызываться следующим образом: for el in fact(n). Функция
# отвечает за получение факториала числа, а в цикле необходимо выводить только первые n чисел, начиная с 1! и до n!

from math import factorial


def fact(n):
    for value in range(1, n + 1):
        yield factorial(value)


iteration = 0
for el in fact(4):
    iteration += 1
    print(f"{iteration}! = {el}")
