"""
Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов (не менее 10 строк).
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.

Пример файла:
Иванов 23543.12
Петров 13749.32

Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4

Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
"""
import codecs

salary_sum = 0
salaries = []
rus_list = ["Один", "Два", "Три", "Четыре"]
eng_list = []
try:
    with codecs.open("data_for_task3.1.txt", "r+", "utf-8") as first_task:
        for string in first_task.readlines():
            surname = string[0:(string.index(" "))]
            salary = string[(string.index(" ") + 1):]
            salaries.append(float(salary))
            if float(salary) < 20000:
                print("Оклад сотрудник {} меньше 20000 и равен: {}".format(surname, salary))
        print("Средняя зп сотрудников равна: ", sum(salaries) / len(salaries))
    with codecs.open("data3_2.txt", "w+", "utf-8") as second_task:

        for string in second_task:
            eng_list.append(string)
        print(eng_list)
        index = 0
        while index < len(eng_list):
            string_list = eng_list[index]
            list_with_text = string_list[(string.index(" ") + 1):]
            second_task.write(rus_list[index] + " " + list_with_text[index])
            index += 1
except IOError:
    print("Something was wrong")
