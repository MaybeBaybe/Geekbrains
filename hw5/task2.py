"""
Создать текстовый файл (не программно),
сохранить в нем несколько строк, выполнить подсчет количества строк, количества слов в каждой строке.
"""

file = open("user_data_2.txt", 'r')
str_count = 0
words_count = []

for string in file.readlines():
    str_count = str_count + 1
    words_count.append(string.count(' ') + 1)

file.close()

print(f"В файле user_data_2.txt {str_count} строк")

index = 0
while index < len(words_count):
    print(f"В строке №{index + 1} кол-во слов: {words_count[index]}")
    index += 1
