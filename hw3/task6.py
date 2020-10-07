"""
Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом.
Каждое слово состоит из латинских букв в нижнем регистре. Сделать вывод исходной строки,
но каждое слово должно начинаться с заглавной буквы.
Необходимо использовать написанную ранее функцию int_func().
"""


def int_func(word):
    """
    lower case to lower with first-upper
    example: print(int_func(‘text’)) -> Text
    """
    return word[0].upper() + word[1:]


any_string = input("Enter the word: ").split(" ")
for el in range(0, len(any_string)):
    any_string[el] = int_func(any_string[el])
print(*any_string, sep=" ")
