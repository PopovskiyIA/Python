# Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
# Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять список
# только числами. Класс-исключение должен контролировать типы данных элементов списка.

class NumbersKeeper(Exception):
    numbers: list

    def __init__(self):
        self.numbers = []

    def append(self, value: str):
        if value.isnumeric():
            self.numbers.append(int(value))
        else:
            print(f"Вы ввели не число: {value}")


# Тест
number_keeper = NumbersKeeper()
stop_program = False
while not stop_program:
    input_values = input("Введите любые целые числа через пробел. Для выхода ввведите stop: ").split(" ")
    for input_value in input_values:
        if input_value == "stop":
            stop_program = True
            break
        else:
            number_keeper.append(input_value)

print("Вы ввели следующие числа:")
print(*number_keeper.numbers, sep=" ")
