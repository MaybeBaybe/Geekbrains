"""
Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая строка должна содержать данные о фирме:
название, форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.

Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. Если фирма получила убытки,
в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].

Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:

[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
"""
import codecs

file = codecs.open("task6.txt", "r", "utf-8")
name = []
ownership = []
proceeds = []
costs = []
for string in file.readlines():
    count = 0
    main_count = string.count(" ")
    while count <= main_count and len(string) != 0:
        try:
            space_ind = string.index(" ")
            value = string[0:space_ind]
            if count == 0:
                name.append(value)
            elif count == 1:
                ownership.append(value)
            elif count == 2:
                proceeds.append(float(value))
            string = string[(space_ind + 1):]
        except ValueError:
            value = string[0:]
            costs.append(float(value))
        count = count + 1
file.close()

ind = 0
company_count = 0
profit_sum = 0
profit = []
pair_list = []
while ind < len(name):
    profit.append(proceeds[ind] - costs[ind])
    if profit[ind] > 0:
        company_count = company_count + 1
        profit_sum = profit_sum + profit[ind]
    pair_list.append((name[ind], profit[ind]))
    ind = ind + 1
average_profit = profit_sum / company_count
first_dict = dict(pair_list)
final_list = [first_dict, {"average_profit": average_profit}]
final_string = "[" + str(final_list[0]) + "," + str(final_list[1]) + "]"

with open('task6.json', 'w') as j_file:
    j_file.write(final_string)