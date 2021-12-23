# Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод init()), который должен
# принимать данные (список списков) для формирования матрицы. Подсказка: матрица — система некоторых математических
# величин, расположенных в виде прямоугольной схемы. Примеры матриц: см. в методичке.
# Следующий шаг — реализовать перегрузку метода str() для вывода матрицы в привычном виде. Далее реализовать
# перегрузку метода add() для реализации операции сложения двух объектов класса Matrix (двух матриц). Результатом
# сложения должна быть новая матрица.

class Matrix:
    rows: list

    def __init__(self, rows):
        if not isinstance(rows, list):
            raise ValueError("Matrix.init - в конструктор переданы некорректные данные")
        for row in rows:
            if not isinstance(row, list):
                raise ValueError("Matrix.init - входной список должен содержать строки матрицы")
            for value in row:
                if not(isinstance(value, int) or isinstance(value, float)):
                    raise ValueError("Matrix.init - значения в матрице должны быть числами")
        self.rows = rows

    def __str__(self):
        output = ''
        for i in range(len(self.rows)):
            output += '\t'.join(map(str, self.rows[i])) + '\n'
        return output

    def __add__(self, other):
        if len(self.rows) != len(other.rows):
            raise ValueError("Matrix.add - матрицы должны быть одинакового размера")
        result = []
        for i in range(len(self.rows)):
            row = []
            if len(self.rows[i]) != len(other.rows[i]):
                raise ValueError(f"Matrix.add - у матриц разное количество элементов в строке {i + 1}")
            for j in range(len(self.rows[i])):
                row.append(int(self.rows[i][j]) + int(other.rows[i][j]))
            result.append(row)
        return Matrix(result)


# Тест
first_matrix = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(f"Первая матрица: \n{first_matrix}")

second_matrix = Matrix([[9, 8, 7], [6, 5, 4], [3, 2, 1]])
print(f"Вторая матрица: \n{second_matrix}")

print(f"Результат суммы матриц: \n{first_matrix + second_matrix}")
