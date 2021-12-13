# Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами. Программа
# должна подсчитывать сумму чисел в файле и выводить ее на экран.
import random

with open(r"exercise5_numbers.txt", mode="w+") as numbers_file:
    numbers_list = [random.randint(0, 100) for x in range(20)]
    print(*numbers_list, sep=' ', file=numbers_file)
    numbers_file.seek(0)
    numbers = [int(x) for x in numbers_file.readline().split()]
    print(f"Итоговая сумма чисел в файле exercise5_numbers.txt: {sum(numbers)}")
