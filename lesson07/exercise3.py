# Реализовать программу работы с органическими клетками, состоящими из ячеек. Необходимо создать класс Клетка. В его
# конструкторе инициализировать параметр, соответствующий количеству ячеек клетки (целое число). В классе должны быть
# реализованы методы перегрузки арифметических операторов: сложение (add()), вычитание (sub()), умножение (mul()),
# деление (truediv()). Данные методы должны применяться только к клеткам и выполнять увеличение, уменьшение,
# умножение и целочисленное (с округлением до целого) деление клеток, соответственно.

class Cell:
    size: int

    def __init__(self, size):
        if size <= 0:
            raise ValueError(f"Cell.init - размер клетки должен быть положительным числом больше нуля")
        self.size = size

    def __str__(self):
        return str(f'Размер клетки равен {self.size} ячеек')

    @staticmethod
    def __value_check(other):
        if not isinstance(other, Cell):
            raise ValueError(f"Cell.value_check - в метод передан аргумент некорректного типа {type(other)}")

    def __add__(self, other):
        self.__value_check(other)
        return Cell(self.size + other.size)

    def __sub__(self, other):
        self.__value_check(other)
        difference = self.size - other.size
        if difference > 0:
            return Cell(difference)
        else:
            print("Cell.sub - невозможно выполнить операцию так как разность количества ячеек двух клеток меньше "
                  "либо равна нулю")

    def __mul__(self, other):
        self.__value_check(other)
        return Cell(self.size * other.size)

    def __truediv__(self, other):
        self.__value_check(other)
        return Cell(self.size // other.size)

    def make_order(self, amount_in_row):
        if amount_in_row < 0:
            raise ValueError("Cell.make_order - аргумент метода должен быть больше либо равен нулю")
        elif amount_in_row == 0:
            return "*" * self.size
        else:
            output = ""
            unassigned_symbols = self.size
            while unassigned_symbols > 0:
                unassigned_symbols -= amount_in_row
                if unassigned_symbols >= 0:
                    output += "*" * amount_in_row
                    if unassigned_symbols > 0:
                        output += "\n"
                else:
                    output += "*" * (amount_in_row + unassigned_symbols)
            return output


# Тест

first_cell = Cell(12)
second_cell = Cell(15)
third_cell = Cell(2)

print(f"Сложение: {first_cell + second_cell}")
print(f"Вычитание: {first_cell - third_cell}")
print(f"Умножение: {second_cell * third_cell}")
print(f"Деление: {second_cell / third_cell}")
print(f"make_order:\n{first_cell.make_order(5)}")
print(f"make_order:\n{second_cell.make_order(5)}")
