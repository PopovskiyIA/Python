# Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.

input_values = input("Введите числа через пробел: ").split(" ")

numbers = []
for value in input_values:
    if value.isnumeric():
        numbers.append(int(value))
    else:
        print(f"Вы обманули программу и ввели значение = {value}. Программа завершается")
        exit()

processed_values = [numbers[index + 1] for index in range(0, len(numbers) - 1) if numbers[index + 1] > numbers[index]]
print(f"Элементы значения которых больше предыдущего элемента: {processed_values}")
