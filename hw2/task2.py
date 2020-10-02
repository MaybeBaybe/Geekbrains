"""
Для списка реализовать обмен значений соседних элементов, т.е.
Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
При нечетном количестве элементов последний сохранить на своем месте.
Для заполнения списка элементов необходимо использовать функцию input().
"""
# for index, element in list
list_base = []
i = 0
while True:
    i += 1
    element = input("Enter the element: ")
    if element == "":
        break
    list_base.append(element)
print(list_base)
final_list = list_base[:]
if len(list_base) % 2 == 0:
    for i in range(0, len(final_list) - 1):
        final_list[::2], final_list[1::2] = final_list[1::2], final_list[::2]
    print(final_list)
else:
    final_list_for_change = final_list[:-1]
    for i in range(0, len(final_list_for_change) - 1):
        final_list_for_change[::2], final_list_for_change[1::2] = final_list_for_change[1::2], final_list_for_change[::2]
    final_list_for_change.append(final_list[-1])
    print(final_list_for_change)
