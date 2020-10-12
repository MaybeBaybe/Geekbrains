"""
Реализовать два небольших скрипта:
а) итератор, генерирующий целые числа, начиная с указанного,
б) итератор, повторяющий элементы некоторого списка, определенного заранее.

Подсказка: использовать функцию count() и cycle() модуля itertools.
Обратите внимание, что создаваемый цикл не должен быть бесконечным.
Необходимо предусмотреть условие его завершения.
Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10 завершаем цикл.
Во втором также необходимо предусмотреть условие, при котором повторение элементов списка будет прекращено.
"""
import random
import itertools


# Часть а
def gen(n):
    new_list = []
    index = 0
    for el in itertools.count(n):
        if index > 21:
            break
        new_list.append(el)
        index = index + 1
    return new_list


gen_list = gen(random.randint(0, 1000))
print("Сгенерированный список: ", gen_list)


# Часть б
def regen_list(user_list):
    new_list = []
    index = 0
    for el in itertools.cycle(user_list):
        if index > 30:
            break
        new_list.append(el)
        index = index + 1
    return new_list


re_list = regen_list(gen_list)
print("Список с повторениями: ", re_list)
