# Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата
# «день-месяц-год». В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать
# число, месяц, год и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить
# валидацию числа, месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных
# данных.

class Date:
    date_string: str

    def __init__(self, date_string: str):
        self.date_string = date_string

    @classmethod
    def extract(cls, date_string):
        values = date_string.split("-")
        return [int(values[0]), int(values[1]), int(values[2])]

    @staticmethod
    def valid(day, month, year):
        if 1 > day or day > 31:
            print(f"Неправильное значение дня: {day}")
            return False

        if 1 > month or month > 12:
            print(f"Неправильное значение месяца: {month}")
            return False

        if 0 > year:
            print(f"Неправильное значение года: {year}")
            return False

        return True

    def __str__(self):
        return f"Текущая дата: {self.date_string}"


# Тест
correct_date = Date("29-12-2021")
print(correct_date)
date_values = Date.extract(correct_date.date_string)
if Date.valid(date_values[0], date_values[1], date_values[2]):
    print("Корректная дата")
else:
    print("Некорректная дата")
