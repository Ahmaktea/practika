# 1.6.3 ЗАДАНИЯ
                    # *1*
# surname = input("Введите вашу фамилию: ")
# name = input("Введите ваше имя: ")
# patronymic = input("Введите ваше отчество: ")


# print(f"ФИО в формате фамилия → имя → отчество: {surname} {name} {patronymic}")

# print(f"ФИО в формате имя → отчество → фамилия: {name} {patronymic} {surname}")
                    #*2*
# surname = input("Введите вашу фамилию: ")

# if surname[-2:] == "ов" or surname[-2:] == "ин":
#     female_surname = surname[:-1] + "а"
#     print(f"Ваша женская фамилия: {female_surname}")
# else:
#     print("Для данной фамилии нельзя преобразовать в женский род")

                    #*3*
# day = input("Введите день рождения: ")
# month = input("Введите месяц рождения: ")
# year = input("Введите год рождения: ")

# print(f"Дата рождения с точками: {day}.{month}.{year}")
# print(f"Дата рождения с косой чертой: {day}/{month}/{year}")
# print(f"Дата рождения с пробелами: {day} {month} {year}")
# print(f"Дата рождения с тире: {day}-{month}-{year}")





# 2.8 Задания на работу с основными типами данных

# n = int(input("Введите порядковый номер студента в списке группы по алфавиту: "))
# m = (n - 1) % 5 + 1

# task1 = m
# task2 = m + 5
# task3 = m + 10

# print(f"Студент с порядковым номером {n} должен выполнить задания №{task1}, №{task2}, №{task3}.")


# 2.8. Задания на работу с основными типами данных

                # *1*
# for X in range(1, 100):
#     if X % 13 == 0:
#          print(X)

                # *2*
# for X in range(11, 20):
#     print(X)

                # *3*
# for X in range(26, 100):
#     for Y in range(26, 100):
#         print(X, Y)

                # *4*
# for X in range(1, 100, 2):
#     for Y in range(1, 100, 2):
#         print(X, Y)

                # *5*
# for X in range(1, 100):
#     for Y in range(1, 100):
#         if (X % 2 == 0 and Y % 2 != 0) or (X % 2 != 0 and Y % 2 == 0):
#             print(X, Y)

                # *6*
# for X in range(-100, 100):
#     for Y in range(-100, 100):
#         if X > 0 or Y > 0:
#             print(X, Y)

                # *7*
# for X in range(0, 101, 5):
#     for Y in range(0, 101, 5):
#         for Z in range(0, 101, 5):
#             print(X, Y, Z)

                # *8*
# for X in range(0, 101, 3):
#     for Y in range(0, 101, 3):
#         for Z in range(0, 101, 3):
#             if (X % 3 == 0 and Y % 3 != 0 and Z % 3 != 0) or (X % 3 != 0 and Y % 3 == 0 and Z % 3 != 0) or (X % 3 != 0 and Y % 3 != 0 and Z % 3 == 0):
#                 print(X, Y, Z)

                # *9*
# for X in range(0, 100):
#     for Y in range(0, 100):
#         for Z in range(0, 100):
#             if (X < 10 and Y >= 10 and Z >= 10) or (X >= 10 and Y < 10 and Z >= 10) or (X >= 10 and Y >= 10 and Z < 10):
#                 print(X, Y, Z)

                # *10*
# for X in range(-100, 100):
#     for Y in range(-100, 100):
#         for Z in range(-100, 100):
#             if X < 0 or Y < 0 or Z < 0:
#                 print(X, Y, Z)

# Задание 5 (Условный оператор)

                # *1*
# x = float(input("Введите значение x: "))
# if x > 0:
#     print(1)
# elif x == 0:
#     print(0)
# else:
#     print(-1)

                # *2*
# import math

# x = float(input("Введите значение x: "))
# if x > 0:
#     print(math.sin(x) ** 2)
# elif x == 0:
#     print(0)
# else:
#     print(1 + 2 * math.sin(x ** 2))

                # *3*
# import math

# x = float(input("Введите значение x: "))
# if x > 0:
#     print(math.cos(x) ** 2)
# elif x == 0:
#     print(0)
# else:
#     print(1 - 2 * math.sin(x ** 2))

                # *4*
# num1 = float(input("Введите первое число: "))
# num2 = float(input("Введите второе число: "))

# sum_result = num1 + num2
# sub_result = num1 - num2
# mul_result = num1 * num2

# if num2 != 0:
#     div_result = num1 / num2
# else:
#     div_result = "Деление на ноль недопустимо"

# print(f"Сумма: {sum_result}")
# print(f"Разность: {sub_result}")
# print(f"Произведение: {mul_result}")
# print(f"Частное: {div_result}")