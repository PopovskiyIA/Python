# Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число», реализуйте перегрузку
# методов сложения и умножения комплексных чисел. Проверьте работу проекта, создав экземпляры класса (комплексные
# числа) и выполнив сложение и умножение созданных экземпляров. Проверьте корректность полученного результата.

class ComplexNumber:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        return f'z = {self.a + other.a} + {self.b + other.b} * i'

    def __mul__(self, other):
        return f'z = {self.a * other.a - (self.b * other.b)} + {self.b * other.a + self.a * other.b} * i'

    def __str__(self):
        return f'z = {self.a} + {self.b} * i'


# Тест
first = ComplexNumber(3, -4)
second = ComplexNumber(-1, 2)
print(f"Первое число: {first}")
print(f"Второе число: {second}")
print(f"Сумма чисел: {first + second}")
print(f"Результат умножения: {first * second}")
