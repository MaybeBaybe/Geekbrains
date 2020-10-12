"""
Реализовать формирование списка, используя функцию range() и возможности генератора.
В список должны войти четные числа от 100 до 1000 (включая границы).
Необходимо получить результат вычисления произведения всех элементов списка.
Подсказка: использовать функцию reduce().
"""
from functools import reduce


def my_func(el, el_prev):
    return el * el_prev


new_list = ([el for el in range(100, 1001) if el % 2 == 0])
res_list = reduce(my_func, new_list)
print("Base list: ", new_list, "\n Mult-result: ", res_list)