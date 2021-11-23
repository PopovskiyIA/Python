earnings = int(input("Введите сумму выручки Вашей фирмы: "))
costs = int(input("Введите сумму издержек Вашей фирмы: "))

income = earnings - costs
if income > 0:
    print("Финансовый результат Вашей фирмы — прибыль")
    profit = income / earnings
    print(f"Рентабельность выручки равна {profit:.0%}")
    employees = int(input("Введите количество сотрудников работающих в Вашей фирме: "))
    income_per_epmloyee = income / employees
    print(f"Прибыль фирмы в расчете на одного сотрудника равна {income_per_epmloyee}")
elif income == 0:
    print("Финансовый результат Вашей фирмы — издержки равны выручке")
else:
    print("Финансовый результат Вашей фирмы — убыток")
