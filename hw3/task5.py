"""
Программа запрашивает у пользователя строку чисел, разделенных пробелом. При нажатии Enter должна выводиться сумма чисел.
Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
Но если вместо числа вводится специальный символ, выполнение программы завершается.
Если специальный символ введен после нескольких чисел,
то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.
"""
counter_of_numbers = []


def sum_and_list(list_of_digits):
    while True:
        user_num = input("Enter any digit with space - separator: ").split(" ")
        # you can create list with list(input())
        try:
            for digit in user_num:
                digit = float(digit)
                counter_of_numbers.append(digit)
            if user_num == "exit":
                print(counter_of_numbers)
                print(sum(counter_of_numbers))
                break
            print(counter_of_numbers)
            print(sum(counter_of_numbers))
        except ValueError:
            print(f"You're out, list is {counter_of_numbers} and sum is {sum(counter_of_numbers)}")


print(sum_and_list(counter_of_numbers))
