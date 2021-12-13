# Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие
# лекционных, практических и лабораторных занятий по этому предмету и их количество. Важно, чтобы для каждого
# предмета не обязательно были все типы занятий. Сформировать словарь, содержащий название предмета и общее
# количество занятий по нему. Вывести словарь на экран.

with open(r"exercise6_academic_subjects.txt", mode="r", encoding="utf-8") as subjects_file:
    subject_map = {}
    for line in subjects_file.readlines():
        separated_line = line.split(":")
        subject_name = separated_line[0]
        total_subject_hours = 0
        lesson_types = separated_line[1].strip().split(" ")
        for hours_with_type in lesson_types:
            first_parenthesis_index = hours_with_type.index("(")
            total_subject_hours += int(hours_with_type[:first_parenthesis_index])
        subject_map[subject_name] = total_subject_hours
    print(subject_map)

