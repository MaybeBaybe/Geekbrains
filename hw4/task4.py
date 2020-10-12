"""
Представлен список чисел. Определить элементы списка, не имеющие повторений.
Сформировать итоговый массив чисел, соответствующих требованию. Элементы вывести в порядке их следования в исходном списке.
Для выполнения задания обязательно использовать генератор.
Пример исходного списка: [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11].
Результат: [23, 1, 3, 10, 4, 11]
"""

import random

num_list = []
res_list = []

num_length = random.randint(0, 15)
index = 0

while index < num_length:
    num_list.append(random.randint(0, 1000))
    index += 1

res_list = ([el for el in num_list if num_list.count(el) == 1])
res_list.sort()
print("List is: ", res_list, "\n Base list: ", num_list)
