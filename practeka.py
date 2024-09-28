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

                # *5*
# m = int(input("Введите первое целое число m: "))
# n = int(input("Введите второе целое число n: "))

# if m % n == 0:
#     print(f"Частное от деления {m} на {n}: {m // n}")
# else:
#     print(f"{m} на {n} нацело не делится")

                # *6*
# import math

# a = float(input("Введите коэффициент a: "))
# b = float(input("Введите коэффициент b: "))
# c = float(input("Введите коэффициент c: "))

# discriminant = b**2 - 4*a*c

# if discriminant < 0:
#     print("Уравнение не имеет корней")
# elif discriminant == 0:
#     x = -b / (2*a)
#     print("Уравнение имеет единственный корень: x =", x)
# else:
#     x1 = (-b + math.sqrt(discriminant)) / (2*a)
#     x2 = (-b - math.sqrt(discriminant)) / (2*a)
#     print("Уравнение имеет два корня:")
#     print("x1 =", x1)
#     print("x2 =", x2)

                # *7*
# age = int(input("Введите ваш возраст: "))

# if age >= 0 and age <= 7:
#     print("Вам в детский сад")
# elif age > 7 and age <= 18:
#     print("Вам в школу")
# elif age > 18 and age <= 25:
#     print("Вам в профессиональное учебное заведение")
# elif age > 25 and age <= 60:
#     print("Вам на работу")
# elif age > 60 and age <= 120:
#     print("Вам предоставляется выбор")
# else:
#     for i in range(5):
#         print("Ошибка! Это программа для людей!")

                # *8*
# distance = float(input("Сколько километров хотите проехать на автомобиле? "))
# consumption = float(input("Сколько литров топлива расходует автомобиль на 100 километров? "))
# fuel_tank = float(input("Сколько литров топлива в вашем баке? "))

# required_fuel = consumption / 100 * distance

# if required_fuel > fuel_tank:
#     print("Недостаточно топлива для поездки указанного расстояния.")
# else:
#     print(f"Достаточно топлива для поездки указанного расстояния. Остаток в баке: {fuel_tank - required_fuel} литров.")

                # *9*
# a = float(input("Введите длину первой стороны треугольника: "))
# b = float(input("Введите длину второй стороны треугольника: "))
# c = float(input("Введите длину третьей стороны треугольника: "))

# if a + b <= c or a + c <= b or b + c <= a:
#     print("Такого треугольника не существует.")
# else:
#     if a == b == c:
#         print("Треугольник является равносторонним.")
#     elif a == b or a == c or b == c:
#         print("Треугольник является равнобедренным.")
#     else:
#         print("Треугольник является разносторонним.")

#     sides = [a, b, c]
#     hypotenuse = max(sides)
#     sides.remove(hypotenuse)
#     if hypotenuse**2 == sides[0]**2 + sides[1]**2:
#         print("Треугольник является прямоугольным.")

                # *10*
# def get_weight_category(weight):

#   if weight <= 60:
#     return "Легкий вес"
#   elif weight <= 64:
#     return "Первый полусредний вес"
#   elif weight <= 69:
#     return "Полусредний вес"
#   else:
#     return "Неизвестная категория"

# # Пример использования
# weight = int(input("введите вес: ")) 
# category = get_weight_category(weight)
# print(f"Боксер с весом {weight} кг относится к категории: {category}")

                # *11*
# def get_game_result(points):

#     if points ==3:
#         return "Пабеда"
#     elif points == 1:
#         return "Ничья"
#     elif points == 0:
#         return "Не пабеда"
#     else:
#         return "Некорректное количество очков"
    
# points = int(input("Введите количество очков, полученных командой: "))
# result = get_game_result(points)
# print(f"Результат матча: {result}")

                # *12*
# def get_day_name(day_number):
  
#   days = {
#     1: "Понедельник",
#     2: "Вторник",
#     3: "Среда",
#     4: "Четверг",
#     5: "Пятница",
#     6: "Суббота",
#     7: "Воскресенье",
#   }

#   if day_number in days:
#     return days[day_number]
#   else:
#     return "Некорректный номер дня"

# day_number = int(input("Введите номер дня недели"))
# day_name = get_day_name(day_number)
# print(f"День недели {day_number}: {day_name}")

                # *13*
# def get_month_name(month_number):

#   months = {
#     1: "Январь",
#     2: "Февраль",
#     3: "Март",
#     4: "Апрель",
#     5: "Май",
#     6: "Июнь",
#     7: "Июль",
#     8: "Август",
#     9: "Сентябрь",
#     10: "Октябрь",
#     11: "Ноябрь",
#     12: "Декабрь",
#   }

#   if month_number in months:
#     return months[month_number]
#   else:
#     return "Некорректный номер месяца"


# month_number = int(input("Введите номер месяца: "))  
# month_name = get_month_name(month_number)
# print(f"Месяц {month_number}: {month_name}")

                # *14*
# def get_season_by_month(month_number):

#   if month_number in range(1, 4):
#     return "Зима"
#   elif month_number in range(4, 7):
#     return "Весна"
#   elif month_number in range(7, 10):
#     return "Лето"
#   elif month_number in range(10, 13):
#     return "Осень"
#   else:
#     return "Некорректный номер месяца"


# month_number = int(input("Введите номер месяца: "))
# season = get_season_by_month(month_number)
# print(f"Месяц {month_number}: {season}")



# Задание 6 (Списки. Кортежи. Словари) 
                                        # 1. Списки

# a) Создайте два списка в диапазоне (0, 100) с шагом 10.

# list1 = list(range(0, 100, 10))
# list2 = list(range(0, 100, 10))

# b) Извлеките из первого списка второй элемент.

# second_element = list1[1]
# print(f"Второй элемент первого списка: {second_element}")

# c) Измените во втором списке последний объект на число «200».

# list2[-1] = 200
# print(f"Измененный второй список: {list2}")

# d) Соедините оба списка в один.

# combined_list = list1 + list2
# print(f"Объединенный список: {combined_list}")

# e) Возьмите срез из соединённого списка.

# slice_list = combined_list[3:8]
# print(f"Срез объединенного списка: {slice_list}")

# f) Добавьте в список-срез два новых элемента.

# slice_list.extend([250, 300])
# print(f"Измененный срез: {slice_list}")

# g) Найдите элементы с максимальным и минимальным значением.

# min_value = min(combined_list)
# max_value = max(combined_list)
# print(f"Минимальное значение: {min_value}")
# print(f"Максимальное значение: {max_value}")

                                        # 2. Кортежи
# students = 15
# students_surname = ("Иванов", "Петров", "Сидоров", "Кузнецов", "Смирнов", "Васильев", "Михайлов", "Федоров", "Попов", "Соколов", "Зайцев", "Павлов", "Козлов", "Морозов", "Волков")
 
# students_number = tuple(range(1, students + 1))
 
# b) Посмотрите, какая фамилия у студента с номером 5.

# students__surname5 = students_surname[4]
# print(f"Фамилия студента с номером 5: {students__surname5}")

# c) Посмотрите, что записано во второй кортеж под номером 5.

# print(f"Элемент второго кортежа с номером 5: {students_surname[4]}")

# d) Объедините два кортежа в один.

# combined_tuple = students_number + students_surname
# print(f"Объединенный кортеж: {combined_tuple}")

# e) Возьмите срез из соединенного кортежа.

# slice_tuple = combined_tuple[3:10]
# print(f"Срез объединенного кортежа: {slice_tuple}")

                                        # 3. Словари
# a) Создайте словарь School и наполните его данными.
# School = {
#     "1a": 25,
#     "1b": 28,
#     "2a": 23,
#     "2b": 26,
#     "3a": 24
# }
# print("Содержимое словаря School:", School)

# b) Узнайте количество учащихся в классе, который вводит пользователь.
# class_name = input("Введите название класса: ")
# if class_name in School:
#     print(f"В классе {class_name} {School[class_name]} учащихся.")
# else:
#     print("Такого класса не существует.")

# c) Внесите изменения в словарь.
# School["1a"] = 27
# School["2b"] = 25
# School["3a"] = 22
# print("Обновленное содержимое словаря School:", School)

# d) Добавьте два новых класса.
# School["4a"] = 20
# School["4b"] = 21
# print("Содержимое словаря School с новыми классами:", School)

# e) Удалите один из классов.
# del School["2a"]
# print("Содержимое словаря School после удаления класса:", School)

                                                                        # Глава 3 "ЦИКЛЫ"
# Задание 7 (Задания на рекуррентные сотношения)
# Функция для вычисления n-го члена последовательности 1, 2, 3, 4, ...
# def recursive_sequence(n):

#   if n == 1:
#     return 1
#   else:
#     return recursive_sequence(n - 1) + 1

# for i in range(1, 6):
#   print(f"a{i} = {recursive_sequence(i)}")

# Функция для вычисления n-го члена последовательности 0, 5, 10, 15, ...
# def recursive_sequence(n):

#   if n == 1:
#     return 0 
#   else:
#     return recursive_sequence(n - 1) + 5

# for i in range(1, 6):
#   print(f"a{i} = {recursive_sequence(i)}")

# Функция для вычисления n-го члена последовательности 1, 1, 1, 1, ...
# def recursive_sequence(n):

#   if n == 1:
#     return 1
#   else:
#     return recursive_sequence(n - 1)

# for i in range(1, 6):
#   print(f"a{i} = {recursive_sequence(i)}")

# Функция для вычисления n-го члена последовательности 1, -1, 1, -1, ...
  
# def recursive_sequence(n):

#   if n == 1:
#     return 1
#   else:
#     return -recursive_sequence(n - 1)

# for i in range(1, 6):
#   print(f"a{i} = {recursive_sequence(i)}")

# Функция для вычисления n-го члена последовательности 1, -2, 3, -4, 5, -6, ...
  
# def recursive_sequence(n):

#   if n == 1:
#     return 1
#   else:
#     return -recursive_sequence(n - 1) + 2 * n - 1

# for i in range(1, 7):
#   print(f"a{i} = {recursive_sequence(i)}")

#  Пример для последовательности (f) 2, 4, 8, 16, ...
  
# N = 5
# a = [0] * N
# a[0] = 2
# for i in range(1, N):
#     a[i] = 2 * a[i-1]

# print(a) 

# Функция для вычисления n-го члена последовательности 2, 4, 16, 256, ...
# def recursive_sequence(n):

#   if n == 1:
#     return 2
#   else:
#     return recursive_sequence(n - 1) ** 2

# for i in range(1, 5):
#   print(f"a{i} = {recursive_sequence(i)}")

# Функция для вычисления n-го члена последовательности 0, 1, 2, 3, 0, 1, 2, 3, ...
# def recursive_sequence(n):

#   if n == 1:
#     return 0
#   else:
#     return (recursive_sequence(n - 1) + 1) % 4

# for i in range(1, 11):
#   print(f"a{i} = {recursive_sequence(i)}")

# Функция для вычисления n-го члена последовательности 1!, 3!, 5!, 7!, ...
# def factorial(n):

#   if n == 0:
#     return 1
#   else:
#     return n * factorial(n - 1)

# def recursive_sequence(n):

#   if n == 1:
#     return factorial(1)
#   else:
#     return factorial(2 * n - 1)

# for i in range(1, 5):
#   print(f"a{i} = {recursive_sequence(i)}")