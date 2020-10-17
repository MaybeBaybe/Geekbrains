"""
 Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
 Об окончании ввода данных свидетельствует пустая строка.
"""
while True:
    user_data = input("Enter the information: ")
    try:
        with open("user_reader.txt", "a") as user_reader:
            user_file = user_reader.write("\n" + user_data + "\n")
    except IOError:
        print("Something was wrong")
    if user_data == "":
        print("You decide to finish the input")
        break
