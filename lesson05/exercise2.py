# Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
# количества слов в каждой строке.

with open(r"exercise2_line_calc.txt", "r") as line_calc_file:
    lines_amount = 0
    for line in line_calc_file.readlines():
        lines_amount += 1
        words_amount = len(line.split())
        print(f"В строке {lines_amount} количество слов: {words_amount}")
    print(f"Количество строк в файле: {lines_amount}")
