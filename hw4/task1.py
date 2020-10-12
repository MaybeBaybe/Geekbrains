"""
Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
В расчете необходимо использовать формулу: (выработка в часах*ставка в час) + премия.
Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.
"""
import sys
from hw4 import funcFor1

try:
    file, emp_hours, emp_rate, emp_bonus = sys.argv
except ValueError:
    print("Invalid args")
    exit()
try:
    print(hw4.funcFor1(float(emp_hours), float(emp_rate), float(emp_bonus)))
except ValueError:
    print("Smth wrong")
