first_result = int(input("Введите результат пробежки первого дня спортсмена в километрах: "))
desired_result = int(input("Введите желаемую дистанцию спортсмена в километрах: "))

if first_result > 0 and desired_result > 0:
    days = 1
    if first_result <= desired_result:
        current_result = first_result
        while desired_result > current_result:
            current_result = current_result + (current_result / 10)
            days += 1

    print(f"На {days}-й день спортсмен достиг результата — не менее {desired_result} км.")
else:
    print("Вы ввели некорректные данные")
