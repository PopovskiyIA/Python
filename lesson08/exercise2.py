# Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу на данных,
# вводимых пользователем. При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту
# ситуацию и не завершиться с ошибкой.

class SafeDivision(Exception):

    def __init__(self, text):
        self.text = text

    @staticmethod
    def div(first_value, second_value):
        try:
            if second_value == 0:
                raise SafeDivision("Делитель не должен быть равным нулю")
            result = first_value / second_value
        except ValueError:
            print("Вы ввели не число")
        except SafeDivision as err:
            print(err)
        else:
            print(f"Результат деления {result}")


# Тест
first = float(input("Введите делимое число: "))
second = float(input("Введите делитель: "))

SafeDivision.div(first, second)
