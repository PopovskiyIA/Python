# Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов (не менее 10
# строк). Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников. Выполнить
# подсчет средней величины дохода сотрудников.

with open(r"exercise3_employee_salary.txt", mode="r", encoding="utf-8") as employee_salary:
    total_salary = 0
    num_of_employee = 0
    for line in employee_salary.readlines():
        num_of_employee += 1
        separated_line = line.split()
        surname = separated_line[0]
        salary = float(separated_line[1])
        if salary < 20000:
            print(f"Сотрудник {surname} имеет оклад менее 20 тысяч")
        total_salary += salary
    print()
    average_salary = round(total_salary / num_of_employee, 2)
    print(f"Средняя величина дохода сотрудников: {average_salary}")
