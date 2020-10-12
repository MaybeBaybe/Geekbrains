"""
Представлен список чисел.
Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для формирования списка использовать генератор.
Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
Результат: [12, 44, 4, 10, 78, 123].
"""
import random

num_list = []
res_list = []

num_length = random.randint(0, 20)
index = 0

while index < num_length:
    num_list.append(random.randint(0, 1000))
    if index != 0 and num_list[index] > num_list[index - 1]:
        res_list.append(num_list[index])
    index = index + 1

print(f"Base list: {num_list}\nGot list: {res_list}")