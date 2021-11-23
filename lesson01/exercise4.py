input_value = int(input("Введите целое положительное число: "))

current_value = input_value
max_digit = 0
while current_value > 0:
    digit = current_value % 10
    if digit > max_digit:
        max_digit = digit
    current_value //= 10

print(f"Самая большая цифра в числе {input_value} это {max_digit}")
