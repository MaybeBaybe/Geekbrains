"""
Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших двух аргументов.
"""


def my_func(digit1, digit2, digit3):
    min1 = min(digit1, digit2, digit3)
    sum_list = [
        digit1,
        digit2,
        digit3
    ]
    sum_all = sum(sum_list) - min1
    return sum_all


digit1 = float(input("Enter digit1: "))
digit2 = float(input("Enter digit2: "))
digit3 = float(input("Enter digit3: "))
print(my_func(digit1, digit2, digit3))
