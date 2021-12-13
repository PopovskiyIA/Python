# Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем. Об окончании
# ввода данных свидетельствует пустая строка.

with open(r"exercise1_user_input.txt", mode="w", encoding="utf-8") as user_input_file:
    while True:
        input_value = input("Введите любой текст: ")
        if input_value:
            print(input_value, file=user_input_file)
        else:
            break

