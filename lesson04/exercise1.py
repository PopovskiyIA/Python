# Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника. В расчете
# необходимо использовать формулу: (выработка в часах*ставка в час) + премия. Для выполнения расчета для конкретных
# значений необходимо запускать скрипт с параметрами.

import sys

try:
    script_name, worked_hours, hourly_salary, bonus = sys.argv
    salary = (int(worked_hours) * int(hourly_salary)) + int(bonus)
    print(f"Заработная плата сотрудника состовляет {salary} рублей")
except ValueError:
    print("Ошибка типа при расчёте заработной платы сотрудника. Были переданы некорретные аргументы")
