# Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому времени года относится месяц (зима,
# весна, лето, осень). Напишите решения через list и через dict.

season_list = ["весна", "лето", "осень", "зима"]

seasons_dictionary = {
    1: season_list[3],
    2: season_list[3],
    3: season_list[0],
    4: season_list[0],
    5: season_list[0],
    6: season_list[1],
    7: season_list[1],
    8: season_list[1],
    9: season_list[2],
    10: season_list[2],
    11: season_list[2],
    12: season_list[3],
}

month = int(input("Введите месяц в виде целого числа от 1 до 12: "))
if 1 <= month <= 12:
    print(f"Время года — {seasons_dictionary[month]}")
else:
    print("Вы ввели некорректное значение")
