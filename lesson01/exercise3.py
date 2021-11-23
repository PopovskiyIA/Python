input_value = input("Введите число n от 0 до 9: ")

if 0 <= int(input_value) < 10:
    first_operand = input_value
    second_operand = input_value + input_value
    third_operand = input_value + input_value + input_value
    result = int(first_operand) + int(second_operand) + int(third_operand)
    print("Считаю результат по формуле n + nn + nnn")
    print(f"{first_operand} + {second_operand} + {third_operand} = {result}")
else:
    print("Вы ввели неправильное число")
