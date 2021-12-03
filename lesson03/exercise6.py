# Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же, но с прописной
# первой буквой. Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом.
# Каждое слово состоит из латинских букв в нижнем регистре. Сделать вывод исходной строки, но каждое слово должно
# начинаться с заглавной буквы. Необходимо использовать написанную ранее функцию int_func().

def int_func(word):
    """
    Функция принимающую слово из маленьких латинских букв и возвращающую его же, но с прописной первой буквой
    :param word: слово в нижнем регистре
    :return: word с большой зашлавной первой буквой или None если word в
    """

    if word.islower():
        return word.capitalize()
    else:
        return


# Тест

input_values = input("Введите слова в нижем регистре через пробел: ").split(" ")
all_word_in_lower_case = True
for value in input_values:
    if not value.islower():
        all_word_in_lower_case = False
        print(f"Вы ввели слово {value} не в нижнем регистре")
        break

new_string = ""
if all_word_in_lower_case:
    for value in input_values:
        new_string += int_func(value) + " "
    print(new_string.strip())
else:
    print("Не буду обрабатывать строку. Мы договаривались на нижний регистр")
