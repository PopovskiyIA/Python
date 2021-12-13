# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные. При этом английские
# числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.

translations = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}
with open(r"exercise4_output_numbers.txt", mode="w", encoding="utf-8") as output_file:
    with open(r"exercise4_input_numbers.txt", mode="r", encoding="utf-8") as input_file:
        for line in input_file.readlines():
            separated_line = line.split()
            print(f"{translations.get(separated_line[0])} {separated_line[1]} {separated_line[2]}", file=output_file)
