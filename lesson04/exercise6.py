# Реализовать два небольших скрипта:
# а) итератор, генерирующий целые числа, начиная с указанного,
# б) итератор, # повторяющий элементы некоторого списка, определенного заранее.
# Например, в первом задании выводим целые числа, # начиная с 3, а при достижении числа 10 завершаем цикл.
# Во втором также необходимо предусмотреть условие, при котором повторение элементов списка будет прекращено.

from itertools import count
from itertools import cycle

for element in count(3):
    if element > 10:
        break
    else:
        print(element)

print()

iteration_num = 10
for character in cycle("GeekBrains"):
    if iteration_num == 0:
        break
    else:
        iteration_num -= 1
        print(character)
