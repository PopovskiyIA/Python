# Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая строка должна содержать данные о
# фирме: название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать. Далее реализовать список.
# Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.

import json

with open(r"exercise7_companies_info.txt", mode="r", encoding="utf-8") as companies_file:
    companies_proceeds = {}
    total_profit = 0
    profit_companies_amount = 0

    for line in companies_file.readlines():
        separated_line = line.split(" ")
        company_name = separated_line[0]
        proceeds = int(separated_line[2])
        costs = int(separated_line[3])
        profit = proceeds - costs
        companies_proceeds[company_name] = profit

        if profit > 0:
            profit_companies_amount += 1
            total_profit += profit

    json_data = [companies_proceeds]
    average_profit = round(total_profit / profit_companies_amount, 2)
    json_data.append({"average_profit": average_profit})

    with open(r"exercise7_output.json", mode="w", encoding="utf-8") as json_file:
        json.dump(json_data, json_file)
