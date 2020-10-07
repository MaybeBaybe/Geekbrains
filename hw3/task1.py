"""
Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
"""


def division(digit1, digit2):
    try:
        return digit1 / digit2
    except ZeroDivisionError:
        print("You're trying divide by zero.")


digit1 = float(input("Enter the first digit: "))
digit2 = float(input("Enter the second digit: "))
print(division(digit1, digit2))
