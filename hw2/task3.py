"""
 Пользователь вводит месяц в виде целого числа от 1 до 12.
 Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
 Напишите решения через list и через dict.
"""
month = int(input("Enter number of month: "))
dict_of_seasons = {"Winter": [12, 1, 2], "Spring": [3, 4, 5], "Summer": [6, 7, 8], "Autumn": [9, 10, 11]}
for key, value in dict_of_seasons.items():
    for el in value:
        if month == el:
            print(key)
list_of_seasons = [
    [12, 1, 2, "Winter"],
    [3, 4, 5, "Spring"],
    [6, 7, 8, "Summer"],
    [9, 10, 11, "Autumn"]
]
for el in list_of_seasons:
    for i in range(0, len(el) - 1):
        if el[i] == month:
            print(el[-1])
