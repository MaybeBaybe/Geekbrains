"""
Пользователь вводит строку из нескольких слов, разделённых пробелами.
Вывести каждое слово с новой строки.
Строки необходимо пронумеровать. Если в слово длинное, выводить только первые 10 букв в слове.
"""
str_with_some_words = input("Enter your words  in the format like word, space,word,space and etc: ")
list_of_words = str_with_some_words.split(" ")
for index, word in enumerate(list_of_words):
    if len(word) <= 10:
        print("The word N{} is {}".format(index, word))
    else:
        print("The word N{} is {}".format(index, word[0:10]))
