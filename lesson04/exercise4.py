# Представлен список чисел. Определить элементы списка, не имеющие повторений. Сформировать итоговый массив чисел,
# соответствующих требованию. Элементы вывести в порядке их следования в исходном списке. Для выполнения
# задания обязательно использовать генератор.

input_values = input("Введите числа через пробел: ").split(" ")

numbers = []
for value in input_values:
    if value.isnumeric():
        numbers.append(int(value))
    else:
        print(f"Вы обманули программу и ввели значение = {value}. Программа зываершается")
        exit()

non_repeating_numbers = [numbers[index] for index in range(len(numbers)) if numbers.count(numbers[index]) == 1]
print(f"Список неповторяющихся значений: {non_repeating_numbers}")