# N1
# var1,var2 = "Misha",21
# print(var1,var2)
# var1 = input("input your last name")
# var2 = int(input("inpur your phone number"))
# print("Human {} with phone {}".format(var1,var2))
# N2
# time = int(input("Input time, using only seconds >>> "))
# print("{} hours :{} minutes: {} seconds".format((time / 3600), (time / 60), time))
# N3
# digit = int(input("input digit >>> "))
# counter = 1
# sum = digit
# while digit > counter:
#     buff = digit * 10**counter
#     sum += buff
#     counter += 1
# print(sum)
# N4
# digit = int(input("Input positive integer >>> "))
# max = 0
# while digit != 0:
#     last_digit = digit % 10
#     buff = digit // 10
#     if max <= last_digit:
#         max = last_digit
#     digit = buff
# print(max)
# N5
# Запросите у пользователя значения выручки и издержек фирмы. Определите, с каким финансовым результатом
# работает фирма (прибыль — выручка больше издержек, или убыток — издержки больше выручки).
# Выведите соответствующее сообщение. Если фирма отработала с прибылью, вычислите рентабельность выручки
# (соотношение прибыли к выручке).
# Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.
# revenue = int(input("Please, enter your revenue: "))
# costs = int(input("Please, enter your costs: "))
# profit = revenue-costs
# if revenue > costs:
#     print("Company works in plus and its profitability is {}".format(profit/revenue))
# else:
#     print("Company words in minus")
# quantity = int(input("Please, enter the quantity of people in your company"))
# print("Profit per employee is {}".format(profit/quantity))
# N6
# 6. Спортсмен занимается ежедневными пробежками. В первый день его результат составил a километров.
# Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего.
# Требуется определить номер дня, на который результат спортсмена составит не менее b километров.
# Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.
# Например: a = 2, b = 3.
# Результат:
# 1-й день: 2
# 2-й день: 2,2
# 3-й день: 2,42
# 4-й день: 2,66
# 5-й день: 2,93
# 6-й день: 3,22
# Ответ: на 6-й день спортсмен достиг результата — не менее 3 км
# a = int(input("Enter your first result of running: "))
# b = int(input("Enter the border of kilometers: "))
# a_test = a
# counter = 1
# while a_test < b:
#     buff = 0.1 * a_test
#     a_test += buff
#     counter += 1
# print("On {}th day the sportsman reach the result - more than {} km ".format(counter, int(a_test)))
