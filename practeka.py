# # 1.6.3 ЗАДАНИЯ
#                     # *1*
# surname = input("Введите вашу фамилию: ")
# name = input("Введите ваше имя: ")
# patronymic = input("Введите ваше отчество: ")


# print(f"ФИО в формате фамилия → имя → отчество: {surname} {name} {patronymic}")

# print(f"ФИО в формате имя → отчество → фамилия: {name} {patronymic} {surname}")
#                     #*2*
# surname = input("Введите вашу фамилию: ")

# if surname[-2:] == "ов" or surname[-2:] == "ин":
#     female_surname = surname[:-1] + "а"
#     print(f"Ваша женская фамилия: {female_surname}")
# else:
#     print("Для данной фамилии нельзя преобразовать в женский род")

#                     #*3*
# day = input("Введите день рождения: ")
# month = input("Введите месяц рождения: ")
# year = input("Введите год рождения: ")

# print(f"Дата рождения с точками: {day}.{month}.{year}")
# print(f"Дата рождения с косой чертой: {day}/{month}/{year}")
# print(f"Дата рождения с пробелами: {day} {month} {year}")
# print(f"Дата рождения с тире: {day}-{month}-{year}")


# # 2.8 Задания на работу с основными типами данных

# n = int(input("Введите порядковый номер студента в списке группы по алфавиту: "))
# m = (n - 1) % 5 + 1

# task1 = m
# task2 = m + 5
# task3 = m + 10

# print(f"Студент с порядковым номером {n} должен выполнить задания №{task1}, №{task2}, №{task3}.")

# # 2.8. Задания на работу с основными типами данных

#                 # *1*
# for X in range(1, 100):
#     if X % 13 == 0:
#          print(X)

#                 # *2*
# for X in range(11, 20):
#     print(X)

#                 # *3*
# for X in range(26, 100):
#     for Y in range(26, 100):
#         print(X, Y)

#                 # *4*
# for X in range(1, 100, 2):
#     for Y in range(1, 100, 2):
#         print(X, Y)

#                 # *5*
# for X in range(1, 100):
#     for Y in range(1, 100):
#         if (X % 2 == 0 and Y % 2 != 0) or (X % 2 != 0 and Y % 2 == 0):
#             print(X, Y)

#                 # *6*
# for X in range(-100, 100):
#     for Y in range(-100, 100):
#         if X > 0 or Y > 0:
#             print(X, Y)

#                 # *7*
# for X in range(0, 101, 5):
#     for Y in range(0, 101, 5):
#         for Z in range(0, 101, 5):
#             print(X, Y, Z)

#                 # *8*
# for X in range(0, 101, 3):
#     for Y in range(0, 101, 3):
#         for Z in range(0, 101, 3):
#             if (X % 3 == 0 and Y % 3 != 0 and Z % 3 != 0) or (X % 3 != 0 and Y % 3 == 0 and Z % 3 != 0) or (X % 3 != 0 and Y % 3 != 0 and Z % 3 == 0):
#                 print(X, Y, Z)

#                 # *9*
# for X in range(0, 100):
#     for Y in range(0, 100):
#         for Z in range(0, 100):
#             if (X < 10 and Y >= 10 and Z >= 10) or (X >= 10 and Y < 10 and Z >= 10) or (X >= 10 and Y >= 10 and Z < 10):
#                 print(X, Y, Z)

#                 # *10*
# for X in range(-100, 100):
#     for Y in range(-100, 100):
#         for Z in range(-100, 100):
#             if X < 0 or Y < 0 or Z < 0:
#                 print(X, Y, Z)

# # Задание 5 (Условный оператор)

#                 # *1*
# x = float(input("Введите значение x: "))
# if x > 0:
#     print(1)
# elif x == 0:
#     print(0)
# else:
#     print(-1)

#                 # *2*
# import math

# x = float(input("Введите значение x: "))
# if x > 0:
#     print(math.sin(x) ** 2)
# elif x == 0:
#     print(0)
# else:
#     print(1 + 2 * math.sin(x ** 2))

#                 # *3*
# import math

# x = float(input("Введите значение x: "))
# if x > 0:
#     print(math.cos(x) ** 2)
# elif x == 0:
#     print(0)
# else:
#     print(1 - 2 * math.sin(x ** 2))

#                 # *4*
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

#                 # *5*
# m = int(input("Введите первое целое число m: "))
# n = int(input("Введите второе целое число n: "))

# if m % n == 0:
#     print(f"Частное от деления {m} на {n}: {m // n}")
# else:
#     print(f"{m} на {n} нацело не делится")

#                 # *6*
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

#                 # *7*
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

#                 # *8*
# distance = float(input("Сколько километров хотите проехать на автомобиле? "))
# consumption = float(input("Сколько литров топлива расходует автомобиль на 100 километров? "))
# fuel_tank = float(input("Сколько литров топлива в вашем баке? "))

# required_fuel = consumption / 100 * distance

# if required_fuel > fuel_tank:
#     print("Недостаточно топлива для поездки указанного расстояния.")
# else:
#     print(f"Достаточно топлива для поездки указанного расстояния. Остаток в баке: {fuel_tank - required_fuel} литров.")

#                 # *9*
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

#                 # *10*
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

#                 # *11*
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

#                 # *12*
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

#                 # *13*
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

#                 # *14*
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



# # Задание 6 (Списки. Кортежи. Словари) 
#                                         # 1. Списки

# # a) Создайте два списка в диапазоне (0, 100) с шагом 10.

# list1 = list(range(0, 100, 10))
# list2 = list(range(0, 100, 10))

# # b) Извлеките из первого списка второй элемент.

# second_element = list1[1]
# print(f"Второй элемент первого списка: {second_element}")

# # c) Измените во втором списке последний объект на число «200».

# list2[-1] = 200
# print(f"Измененный второй список: {list2}")

# # d) Соедините оба списка в один.

# combined_list = list1 + list2
# print(f"Объединенный список: {combined_list}")

# # e) Возьмите срез из соединённого списка.

# slice_list = combined_list[3:8]
# print(f"Срез объединенного списка: {slice_list}")

# # f) Добавьте в список-срез два новых элемента.

# slice_list.extend([250, 300])
# print(f"Измененный срез: {slice_list}")

# # g) Найдите элементы с максимальным и минимальным значением.

# min_value = min(combined_list)
# max_value = max(combined_list)
# print(f"Минимальное значение: {min_value}")
# print(f"Максимальное значение: {max_value}")

#                                         # 2. Кортежи
# students = 15
# students_surname = ("Иванов", "Петров", "Сидоров", "Кузнецов", "Смирнов", "Васильев", "Михайлов", "Федоров", "Попов", "Соколов", "Зайцев", "Павлов", "Козлов", "Морозов", "Волков")
 
# students_number = tuple(range(1, students + 1))
 
# # b) Посмотрите, какая фамилия у студента с номером 5.

# students__surname5 = students_surname[4]
# print(f"Фамилия студента с номером 5: {students__surname5}")

# # c) Посмотрите, что записано во второй кортеж под номером 5.

# print(f"Элемент второго кортежа с номером 5: {students_surname[4]}")

# # d) Объедините два кортежа в один.

# combined_tuple = students_number + students_surname
# print(f"Объединенный кортеж: {combined_tuple}")

# # e) Возьмите срез из соединенного кортежа.

# slice_tuple = combined_tuple[3:10]
# print(f"Срез объединенного кортежа: {slice_tuple}")

#                                         # 3. Словари
# # a) Создайте словарь School и наполните его данными.
# School = {
#     "1a": 25,
#     "1b": 28,
#     "2a": 23,
#     "2b": 26,
#     "3a": 24
# }
# print("Содержимое словаря School:", School)

# # b) Узнайте количество учащихся в классе, который вводит пользователь.

# class_name = input("Введите название класса: ")
# if class_name in School:
#     print(f"В классе {class_name} {School[class_name]} учащихся.")
# else:
#     print("Такого класса не существует.")

# # c) Внесите изменения в словарь.
    
# School["1a"] = 27
# School["2b"] = 25
# School["3a"] = 22
# print("Обновленное содержимое словаря School:", School)

# # d) Добавьте два новых класса.
    
# School["4a"] = 20
# School["4b"] = 21
# print("Содержимое словаря School с новыми классами:", School)

# # e) Удалите один из классов.
    
# del School["2a"]
# print("Содержимое словаря School после удаления класса:", School)

#                                                                         # Глава 3 "ЦИКЛЫ"
# # Задание 7 (Задания на рекуррентные сотношения)
# # Функция для вычисления n-го члена последовательности 1, 2, 3, 4, ...
# def recursive_sequence(n):

#   if n == 1:
#     return 1
#   else:
#     return recursive_sequence(n - 1) + 1

# for i in range(1, 6):
#   print(f"a{i} = {recursive_sequence(i)}")

# # Функция для вычисления n-го члена последовательности 0, 5, 10, 15, ...
# def recursive_sequence(n):

#   if n == 1:
#     return 0 
#   else:
#     return recursive_sequence(n - 1) + 5

# for i in range(1, 6):
#   print(f"a{i} = {recursive_sequence(i)}")

# # Функция для вычисления n-го члена последовательности 1, 1, 1, 1, ...
# def recursive_sequence(n):

#   if n == 1:
#     return 1
#   else:
#     return recursive_sequence(n - 1)

# for i in range(1, 6):
#   print(f"a{i} = {recursive_sequence(i)}")

# # Функция для вычисления n-го члена последовательности 1, -1, 1, -1, ...
  
# def recursive_sequence(n):

#   if n == 1:
#     return 1
#   else:
#     return -recursive_sequence(n - 1)

# for i in range(1, 6):
#   print(f"a{i} = {recursive_sequence(i)}")

# # Функция для вычисления n-го члена последовательности 1, -2, 3, -4, 5, -6, ...
  
# def recursive_sequence(n):

#   if n == 1:
#     return 1
#   else:
#     return -recursive_sequence(n - 1) + 2 * n - 1

# for i in range(1, 7):
#   print(f"a{i} = {recursive_sequence(i)}")

# #  Пример для последовательности (f) 2, 4, 8, 16, ...
  
# N = 5
# a = [0] * N
# a[0] = 2
# for i in range(1, N):
#     a[i] = 2 * a[i-1]

# print(a) 

# # Функция для вычисления n-го члена последовательности 2, 4, 16, 256, ...

# def recursive_sequence(n):

#   if n == 1:
#     return 2
#   else:
#     return recursive_sequence(n - 1) ** 2

# for i in range(1, 5):
#   print(f"a{i} = {recursive_sequence(i)}")

# # Функция для вычисления n-го члена последовательности 0, 1, 2, 3, 0, 1, 2, 3, ...
  
# def recursive_sequence(n):

#   if n == 1:
#     return 0
#   else:
#     return (recursive_sequence(n - 1) + 1) % 4

# for i in range(1, 11):
#   print(f"a{i} = {recursive_sequence(i)}")

# # Функция для вычисления n-го члена последовательности 1!, 3!, 5!, 7!, ...
  
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

# # Задание 8 (Задания на цикл с условием)

#                 # *1*
# number = 0
# total = 0

# while True:
#     number = int(input("Введите число: "))
#     if number > 0:
#         total += number
#     else:
#         break

# print("Сумма введенных положительных чисел: ", total)

#                 # *2*
# number = 0
# total = 0

# while True:
#     number = int(input("Введите число: "))
#     if number < 0:
#         total += number
#     else:
#         break

# print("Сумма введенных отрицательных чисел: ", total)

#                 # *3*
# number = 0
# total = 0

# while True:
#     number = int(input("Введите число: "))
#     if number != 0:
#         total += number
#     else:
#         break

# print("Сумма введенных чисел: ", total)

#                 # *4*
# number = 0
# total = 0

# while True:
#     number = int(input("Введите число: "))
#     if number % 2 == 0:
#         total += number
#     else:
#         break

# print("Сумма введенных чисел: ", total)

#                 # *5*
# n = int(input("Введите число n: "))

# i = 1

# while i**2 <= n:
#     print(i**2)
#     i += 1

#                 # *6*
# def find_first_square_greater_than(n):

#   i = 1
#   while i * i <= n:
#     i += 1
#   return i

# n = int(input("Введите число: "))
# result = find_first_square_greater_than(n)
# print(f"Первое натуральное число, квадрат которого больше {n}: {result}")

#                 # *7*
# def find_first_greater_than(n):

#   i = 1
#   sum = 1
#   while sum <= n:
#     i += 1
#     sum += 1 / i
#   return sum

# n = int(input("Введите число: "))
# result = find_first_greater_than(n)
# print(f"Первое число в последовательности, которое больше {n}: {result}")

#                 # *8*
# def find_first_smaller_than(a):

#   i = 2
#   sum = 1 + 1 / 2
#   while sum >= a:
#     i += 1
#     sum = 1 + 1 / i
#   return sum

# a = float(input("Введите число: "))
# result = find_first_smaller_than(a)
# print(f"Первое число в последовательности, которое меньше {a}: {result}")

#                 # *9*
# def check_increasing_sequence():

#   count = 0 
#   previous_number = None

#   while True:
#     try:
#       number = float(input("Введите число: "))
#       if previous_number is None:
#         previous_number = number
#         count += 1
#       elif number > previous_number:
#         previous_number = number
#         count += 1
#       else:
#         break
#     except ValueError:
#       print("Некорректный ввод. Введите число.")

#   print(f"Введено {count} чисел.")

# check_increasing_sequence()

#                 # *10*
# def check_decreasing_sequence():

#   count = 0
#   previous_number = None

#   while True:
#     try:
#       number = float(input("Введите число: "))
#       if previous_number is None:
#         previous_number = number
#         count += 1
#       elif number < previous_number:
#         previous_number = number
#         count += 1
#       else:
#         break 
#     except ValueError:
#       print("Некорректный ввод. Введите число.")

#   print(f"Введено {count} чисел.")
 
# check_decreasing_sequence()

#                 # *11*
# def check_integer_sequence():

#   count = 0  # Счетчик введенных чисел

#   while True:
#     try:
#       number = float(input("Введите число: "))
#       if number.is_integer():
#         count += 1
#       else:
#         break
#     except ValueError:
#       print("Некорректный ввод. Введите число.")

#   print(f"Введено {count} целых чисел.")

# check_integer_sequence()

#                 # *12*
# def check_numbers_less_than_10():

#   count = 0

#   while True:
#     try:
#       number = float(input("Введите число: "))
#       if number < 10:
#         count += 1
#       else:
#         break
#     except ValueError:
#       print("Некорректный ввод. Введите число.")

#   print(f"Введено {count} чисел, меньших 10.")

# check_numbers_less_than_10()

#                 # *13*
# def find_max_digit_index(number):

#   max_digit = 0
#   index_from_end = 0
#   index_from_start = 0

#   digit_index = 0
#   for digit in str(number)[::-1]:
#     digit = int(digit)
#     if digit > max_digit:
#       max_digit = digit
#       index_from_end = digit_index
#       index_from_start = len(str(number)) - digit_index - 1
#     digit_index += 1

#   return index_from_end, index_from_start

# number = int(input("Введите число: "))
# index_from_end, index_from_start = find_max_digit_index(number)
# print(f"Максимальная цифра в числе {number} имеет индекс:")
# print(f"  от конца числа: {index_from_end}")
# print(f"  от начала числа: {index_from_start}")

#                 # *14*
# def find_min_digit_index(number):

#   min_digit = 9
#   index_from_end = 0
#   index_from_start = 0

#   digit_index = 0
#   for digit in str(number)[::-1]:
#     digit = int(digit)
#     if digit < min_digit:
#       min_digit = digit
#       index_from_end = digit_index
#       index_from_start = len(str(number)) - digit_index - 1
#     digit_index += 1

#   return index_from_end, index_from_start

# number = int(input("Введите число: "))
# index_from_end, index_from_start = find_min_digit_index(number)
# print(f"Минимальная цифра в числе {number} имеет индекс:")
# print(f"  от конца числа: {index_from_end}")
# print(f"  от начала числа: {index_from_start}")

#                 # *15*
# def find_min_digit_index(number):

#   min_digit = 9
#   index_from_end = 0
#   index_from_start = 0

#   digit_index = 0
#   for digit in str(number)[::-1]:
#     digit = int(digit)
#     if digit < min_digit:
#       min_digit = digit
#       index_from_end = digit_index
#       index_from_start = len(str(number)) - digit_index - 1
#     digit_index += 1

#   return index_from_end, index_from_start

# number = int(input("Введите число: "))
# index_from_end, index_from_start = find_min_digit_index(number)
# print(f"Минимальная цифра в числе {number} имеет индекс:")
# print(f"  от конца числа: {index_from_end}")
# print(f"  от начала числа: {index_from_start}")

# # Задание 9 (Задания на цикл со счётчиком)

#                 # *1*
# sum_even_numbers = 0

# for i in range(2, 91, 2):
#   sum_even_numbers += i

# print(f"Сумма всех четных чисел от 1 до 90: {sum_even_numbers}")

#                 # *2*
# def sum_even_numbers_in_range(a, b):

#   sum_even = 0
#   for i in range(a, b + 1):
#     if i % 2 == 0:
#       sum_even += i
#   return sum_even

# a = int(input("Введите начало диапазона: "))
# b = int(input("Введите конец диапазона: "))

# sum_even = sum_even_numbers_in_range(a, b)
# print(f"Сумма всех четных чисел в диапазоне от {a} до {b}: {sum_even}")

#                 # *3*
# sum_odd_numbers = 0

# for i in range(1, 91, 2):
#   sum_odd_numbers += i

# print(f"Сумма всех нечетных чисел от 1 до 90: {sum_odd_numbers}")

#                 # *4*
# def sum_odd_numbers_in_range(a, b):

#   sum_odd = 0
#   for i in range(a, b + 1):
#     if i % 2 != 0:
#       sum_odd += i
#   return sum_odd

# a = int(input("Введите начало диапазона: "))
# b = int(input("Введите конец диапазона: "))

# sum_odd = sum_odd_numbers_in_range(a, b)
# print(f"Сумма всех нечетных чисел в диапазоне от {a} до {b}: {sum_odd}")

#                 # *5*
# for i in range(1, 10):
#   print(f"{i} x 5 = {i * 5}")

#                 # *6*
# for i in range(1, 10):
#   print(f"{i} x 9 = {i * 9}")

#                 # *7*
# n = int(input("Введите целое число (2 ≤ n ≤ 9): "))

# if 2 <= n <= 9:
#   for i in range(1, 10):
#     print(f"{i} x {n} = {i * n}")
# else:
#   print("Число n должно быть в диапазоне от 2 до 9.")

#                 # *8*
# price_per_kg = float(input("Введите стоимость 1 кг сыра: "))

# for weight in range(50, 1001, 50):
#   price = weight / 1000 * price_per_kg
#   print(f"{weight} г сыра: {price:.2f} руб.")

#                 # *9*
# price_per_kg = float(input("Введите стоимость 1 кг конфет: "))

# for weight in range(100, 2001, 100):
#   price = weight / 1000 * price_per_kg
#   print(f"{weight} г конфет: {price:.2f} руб.")

#                 # *10*
# sum = 0
# for i in range(10, 101):
#     sum += i

# print(f"Сумма всех целых чисел от 10 до 100: {sum}")

#                 #*11*
# a = int(input("Введите значение a: "))

# sum = 0
# for i in range(a, 101):
#     sum += i

# print(f"Сумма всех целых чисел от {a} до 100: {sum}")

#                 # *12*
# b = int(input("Введите значение b: "))

# sum = 0
# for i in range(10, b + 1):
#     sum += i

# print(f"Сумма всех целых чисел от 10 до {b}: {sum}")

#                 # *13*
# a = int(input("Введите значение a: "))
# b = int(input("Введите значение b: "))

# sum = 0
# for i in range(a, b + 1):
#     sum += i

# print(f"Сумма всех целых чисел от {a} до {b}: {sum}")

#                 # *14*
# product = 1
# for i in range(10, 101):
#   product *= i

# print(f"Произведение всех целых чисел от 10 до 100: {product}")

#                 # *15*
# a = int(input("Введите значение a: "))
# b = int(input("Введите значение b: "))

# product = 1
# for i in range(a, b + 1):
#   product *= i

# print(f"Произведение всех целых чисел от {a} до {b}: {product}")

# # Задание 10 (Задания на комбинацию циклов со счётчиком и условием)

                # *1*
# n = int(input("Введите количество гостей: "))

# # 1. Каждому гостю достался хотя бы 1 кусок
# cuts_for_one_piece = 0
# while 2**cuts_for_one_piece < n:
#   cuts_for_one_piece += 1

# # 2. Как минимум половине гостей досталось по 2 куска
# cuts_for_half_with_two_pieces = 0
# while 2**cuts_for_half_with_two_pieces < n // 2:
#   cuts_for_half_with_two_pieces += 1

# # 3. Каждому гостю досталось по 1 куску и еще 10 кусков в запасе
# cuts_for_one_piece_and_ten_left = 0
# while 2**cuts_for_one_piece_and_ten_left < n + 10:
#   cuts_for_one_piece_and_ten_left += 1

# print(f"Чтобы каждому гостю достался хотя бы 1 кусок, нужно сделать {cuts_for_one_piece} разрезов.")
# print(f"Чтобы как минимум половине гостей досталось по 2 куска, нужно сделать {cuts_for_half_with_two_pieces} разрезов.")
# print(f"Чтобы каждому гостю досталось по 1 куску и еще 10 кусков в запасе, нужно сделать {cuts_for_one_piece_and_ten_left} разрезов.")

                # *2*
# total_twos = 0
# days_skipped = 0
# months_skipped = 0


# for month in range(1, 10):

#     days_skipped_this_month = month + 1  
#     total_twos += days_skipped_this_month * 2  
#     days_skipped += days_skipped_this_month
#     months_skipped += 1
#     total_twos += 3 

#     if total_twos >= 70:
#         break

# print(f"Василий может прогуливать школу {months_skipped} раз.")
# print(f"Всего Василий прогуляет {days_skipped} дней.")

                # *3*
# n = int(input("Введите количество детей: "))
# m = int(input("Введите количество кубиков: "))

# child_number = 1
# cubes_taken = 1
# while cubes_taken <= m:
#   print(f"Ребенок {child_number} берет {cubes_taken} кубиков.")
#   m -= cubes_taken

#   if cubes_taken > 25:
#     cubes_taken -= 25

#   child_number = (child_number % n) + 1
#   cubes_taken *= 2

# print(f"Проиграл ребенок {child_number}.")

                # *4*
# x0 = 1
# x1 = 1
# n = 1 

# while x1 <= 1000:
#   x0, x1 = x1, x0 + x1
#   n += 1

# print(f"Первое число в последовательности Фибоначчи, которое больше 1000: {x1}")
# print(f"Номер этого числа: {n}")

                # *5*
# import math

# def fibonacci(n):

#   golden_ratio = (1 + math.sqrt(5)) / 2
#   return int((1 / math.sqrt(5)) * (golden_ratio**n - ((1 - golden_ratio)**n)))

# def fibonacci_iterative(n):

#   if n <= 1:
#     return n
#   else:
#     x0 = 1
#     x1 = 1
#     for i in range(2, n + 1):
#       x0, x1 = x1, x0 + x1
#     return x1

# # Находим n, начиная с которого ошибка больше 0.001
# n = 1
# while abs(fibonacci(n) - fibonacci_iterative(n)) <= 0.001:
#   n += 1

# print(f"Начиная с {n}-го члена последовательности Фибоначчи, ошибка вычисления по формуле Бине превышает 0.001.")

                # *6*
# import random

# balance = 3  # Начальный баланс

# while balance > 0:
#   choice = int(input("Орёл (0) или решка (1)? Введите любое другое число для выхода: "))

#   if choice == 0:
#     user_choice = "Орёл"
#   elif choice == 1:
#     user_choice = "Решка"
#   else:
#     print("Игра окончена.")
#     break

#   coin_side = random.choice(["Орёл", "Решка"])
#   print(f"Выпал {coin_side}")

#   if coin_side == user_choice:
#     print("Вы выиграли!")
#     balance += 1
#   else:
#     print("Вы проиграли.")
#     balance -= 1

#   print(f"Ваш баланс: {balance} руб.")

# print("Игра окончена. У вас больше нет денег.")

                # *7*
# deposit = 1000
# month = 1

# # 1. Определение месяца, когда увеличение превысит 30 рублей
# while True:
#   increase = deposit * 0.02
#   if increase > 30:
#     break
#   deposit += increase
#   month += 1

# print(f"Увеличение вклада превысит 30 рублей в {month}-м месяце.")

# # 2. Определение месяца, когда вклад превысит 1200 рублей
# month = 1
# while deposit <= 1200:
#   deposit += deposit * 0.02
#   month += 1

# print(f"Вклад превысит 1200 рублей через {month} месяцев.")

                # *8*
# distance = 10
# day = 1

# # 1. День, когда пробег больше 20 км
# while distance <= 20:
#   distance *= 1.1
#   day += 1

# print(f"Лыжник пробежит больше 20 км в {day}-й день.")

# # 2. День, когда суммарный пробег больше 100 км
# distance = 10
# day = 1
# total_distance = 0
# while total_distance <= 100:
#   total_distance += distance
#   distance *= 1.1
#   day += 1

# print(f"Суммарный пробег лыжника превысит 100 км в {day}-й день.")

                                        # Глава 4
                                    # Массивы. Модуль numpy
                                        # Задание 11
                # *1*
# import numpy as np

# array_10 = np.zeros(10)

# array_55 = np.zeros(55)

# matrix_3x4 = np.zeros((3, 4))

# array_3d = np.zeros((2, 4, 5))

# print("Одномерный массив длины 10:", array_10)
# print("Одномерный массив длины 55:", array_55)
# print("Матрица 3×4:\n", matrix_3x4)
# print("Трёхмерный массив формы 2 × 4 × 5:\n", array_3d)

                # *2*
# import numpy as np

# array_10 = np.ones(10)

# array_55 = np.ones(55)

# matrix_3x4 = np.ones((3, 4))

# array_3d = np.ones((2, 4, 5))

# print("Одномерный массив длины 10:", array_10)
# print("Одномерный массив длины 55:", array_55)
# print("Матрица 3×4:\n", matrix_3x4)
# print("Трёхмерный массив формы 2 × 4 × 5:\n", array_3d)

                # *4*
# import numpy as np

# array_10 = np.full(10, 9)

# array_55 = np.full(55, 9)

# matrix_3x4 = np.full((3, 4), 9)

# array_3d = np.full((2, 4, 5), 9)

# print("Одномерный массив длины 10:", array_10)
# print("Одномерный массив длины 55:", array_55)
# print("Матрица 3×4:\n", matrix_3x4)
# print("Трёхмерный массив формы 2 × 4 × 5:\n", array_3d)

                # *5*
# import numpy as np

# array = np.arange(-10, 10, 0.1)

# print(array)

                # *6*
# import numpy as np
# import math

# e = math.e
# array = np.arange(-e, e, e/50)

# print(array)

                # *7*
# import numpy as np
# import math

# pi = math.pi
# array = np.arange(-15 * pi, 15 * pi, pi / 12)

# print(array)

                # *8*
# import numpy as np

# identity_matrix = np.identity(5)

# print(identity_matrix)

                # *9*
# import numpy as np

# diagonal_matrix = np.diag([0.5] * 5)

# print(diagonal_matrix)

                # *10*
# import numpy as np

# matrix = np.full((5, 5), 2)
# np.fill_diagonal(matrix, 1)

# print(matrix)

                # *11*
# import numpy as np

# matrix = np.zeros((5, 5))
# for i in range(5):
#   matrix[:, i] = i + 1

# print(matrix)

                # *12*
# import numpy as np

# matrix = np.zeros((5, 5))

# for i in range(5):
#   matrix[i, :] = i + 1

# print(matrix)

                # *13*
# import numpy as np

# matrix = np.zeros((5, 5))

# for i in range(5):
#   for j in range(i + 1, 5):
#     matrix[i, j] = 1

# for i in range(5):
#   for j in range(i):
#     matrix[i, j] = -1

# print(matrix)

                # *14*
# import numpy as np

# matrix = np.zeros((5, 5))

# np.fill_diagonal(matrix, 1)

# for i in range(5):
#   for j in range(i + 1, 5):
#     matrix[i, j] = -2

# print(matrix)

                # *15*
# import numpy as np

# matrix = np.zeros((5, 5))

# np.fill_diagonal(matrix, 1)

# for i in range(5):
#   for j in range(i):
#     matrix[i, j] = 2

# print(matrix)

# Задание 12

# import numpy as np

# # Загрузка данных из файла
# matrix = np.loadtxt("lower_triangular_matrix.txt")

# # Проверка размерности
# print("Размерность матрицы:", matrix.shape)

# # Создание одномерного массива-диапазона
# vector = np.arange(5)

# # Прибавление вектора к матрице
# result_matrix = matrix + vector

# print("Матрица после сложения с вектором:\n", result_matrix)

# # Поиск максимального и минимального элементов
# max_value = np.max(result_matrix)
# min_value = np.min(result_matrix)
# print("Максимальный элемент:", max_value)
# print("Минимальный элемент:", min_value)

# # Сумма элементов по строкам
# row_sums = np.sum(result_matrix, axis=1)
# print("Сумма элементов по строкам:\n", row_sums)

# # Сохранение в файлы
# np.savetxt("result_matrix.txt", result_matrix)
# np.savetxt("vector.txt", vector)

# print("Матрица сохранена в файл result_matrix.txt")
# print("Вектор сохранен в файл vector.txt")

# Задание 13

# import numpy as np
# import math

# def tabulate_function(function, start, end, step):
  
#   x_values = np.arange(start, end + step, step)
#   y_values = [function(x) for x in x_values]
#   return list(zip(x_values, y_values))

# # 1. x^2 на отрезке x ∈ [-2; 2]
# print("x^2 на отрезке x ∈ [-2; 2]")
# print("Шаг 0.01:", tabulate_function(lambda x: x**2, -2, 2, 0.01))
# print("Шаг 0.1:", tabulate_function(lambda x: x**2, -2, 2, 0.1))
# print("Шаг 0.25:", tabulate_function(lambda x: x**2, -2, 2, 0.25))

# # 2. x^3 на отрезке x ∈ [-2; 2]
# print("\nx^3 на отрезке x ∈ [-2; 2]")
# print("Шаг 0.01:", tabulate_function(lambda x: x**3, -2, 2, 0.01))
# print("Шаг 0.1:", tabulate_function(lambda x: x**3, -2, 2, 0.1))
# print("Шаг 0.25:", tabulate_function(lambda x: x**3, -2, 2, 0.25))

# # 3. x^4 на отрезке x ∈ [-2; 2]
# print("\nx^4 на отрезке x ∈ [-2; 2]")
# print("Шаг 0.01:", tabulate_function(lambda x: x**4, -2, 2, 0.01))
# print("Шаг 0.1:", tabulate_function(lambda x: x**4, -2, 2, 0.1))
# print("Шаг 0.25:", tabulate_function(lambda x: x**4, -2, 2, 0.25))

# # 4. cos(2πt) на отрезке t ∈ [-10; 10]
# print("\ncos(2πt) на отрезке t ∈ [-10; 10]")
# print("Шаг 1:", tabulate_function(lambda t: math.cos(2 * math.pi * t), -10, 10, 1))
# print("Шаг 0.25:", tabulate_function(lambda t: math.cos(2 * math.pi * t), -10, 10, 0.25))

# # 5. (1/t)cos(2πt) на отрезке t ∈ [1; 10]
# print("\n(1/t)cos(2πt) на отрезке t ∈ [1; 10]")
# print("Шаг 1:", tabulate_function(lambda t: (1/t) * math.cos(2 * math.pi * t), 1, 10, 1))
# print("Шаг 0.25:", tabulate_function(lambda t: (1/t) * math.cos(2 * math.pi * t), 1, 10, 0.25))

# # 6. e^(-t)cos(2πt) на отрезке t ∈ [-10; 10]
# print("\ne^(-t)cos(2πt) на отрезке t ∈ [-10; 10]")
# print("Шаг 1:", tabulate_function(lambda t: math.exp(-t) * math.cos(2 * math.pi * t), -10, 10, 1))
# print("Шаг 0.25:", tabulate_function(lambda t: math.exp(-t) * math.cos(2 * math.pi * t), -10, 10, 0.25))

# # 7. 4sin(πt + π/8) - 1 на отрезке t ∈ [-10; 10]
# print("\n4sin(πt + π/8) - 1 на отрезке t ∈ [-10; 10]")
# print("Шаг 1:", tabulate_function(lambda t: 4 * math.sin(math.pi * t + math.pi / 8) - 1, -10, 10, 1))
# print("Шаг 0.25:", tabulate_function(lambda t: 4 * math.sin(math.pi * t + math.pi / 8) - 1, -10, 10, 0.25))

# # 8. 2cos(t-2) + sin(2t-4) на отрезке t ∈ [-20π; 10π]
# print("\n2cos(t-2) + sin(2t-4) на отрезке t ∈ [-20π; 10π]")
# print("Шаг π:", tabulate_function(lambda t: 2 * math.cos(t - 2) + math.sin(2 * t - 4), -20 * math.pi, 10 * math.pi, math.pi))
# print("Шаг π/12:", tabulate_function(lambda t: 2 * math.cos(t - 2) + math.sin(2 * t - 4), -20 * math.pi, 10 * math.pi, math.pi / 12))

# # 9. ln(x + 1) на отрезке x ∈ [0; e - 1]
# print("\nln(x + 1) на отрезке x ∈ [0; e - 1]")
# print("Шаг 0.01:", tabulate_function(lambda x: math.log(x + 1), 0, math.e - 1, 0.01))
# print("Шаг 0.001:", tabulate_function(lambda x: math.log(x + 1), 0, math.e - 1, 0.001))

# # 10. log2(|x|) на отрезке x ∈ [-4; 4]
# print("\nlog2(|x|) на отрезке x ∈ [-4; 4]")
# print("Шаг 0.1:", [(x, math.log2(abs(x))) for x in np.arange(-4, 4, 0.1) if x != 0])
# print("Шаг 0.25:", [(x, math.log2(abs(x))) for x in np.arange(-4, 4, 0.25) if x != 0])

# # 11. 2^x на отрезке x ∈ [-2; 2]
# print("\n2^x на отрезке x ∈ [-2; 2]")
# print("Шаг 0.01:", tabulate_function(lambda x: 2**x, -2, 2, 0.01))
# print("Шаг 0.1:", tabulate_function(lambda x: 2**x, -2, 2, 0.1))
# print("Шаг 0.25:", tabulate_function(lambda x: 2**x, -2, 2, 0.25))

# # 12. e^x на отрезке x ∈ [-2; 2]
# print("\ne^x на отрезке x ∈ [-2; 2]")
# print("Шаг 0.01:", tabulate_function(lambda x: math.exp(x), -2, 2, 0.01))
# print("Шаг 0.1:", tabulate_function(lambda x: math.exp(x), -2, 2, 0.1))
# print("Шаг 0.25:", tabulate_function(lambda x: math.exp(x), -2, 2, 0.25))

# # 13. 2^(-x) на отрезке x ∈ [-2; 2]
# print("\n2^(-x) на отрезке x ∈ [-2; 2]")
# print("Шаг 0.01:", tabulate_function(lambda x: 2**(-x), -2, 2, 0.01))
# print("Шаг 0.1:", tabulate_function(lambda x: 2**(-x), -2, 2, 0.1))
# print("Шаг 0.25:", tabulate_function(lambda x: 2**(-x), -2, 2, 0.25))

# # 14. √3^x на отрезке x ∈ [1; 125]
# print("\n√3^x на отрезке x ∈ [1; 125]")
# print("Шаг 1:", tabulate_function(lambda x: math.sqrt(3)**x, 1, 125, 1))
# print("Шаг 5 (с 1 и 5):", [(1, math.sqrt(3)**1), (5, math.sqrt(3)**5)] + tabulate_function(lambda x: math.sqrt(3)**x, 6, 125, 5))

# # 15. √5^x на отрезке x ∈ [1; 32]
# print("\n√5^x на отрезке x ∈ [1; 32]")
# print("Шаг 1:", tabulate_function(lambda x: math.sqrt(5)**x, 1, 32, 1))
# print("Шаг 0.25:", tabulate_function(lambda x: math.sqrt(5)**x, 1, 32, 0.25))


                                #         Глава 5
                                # Графики. Модуль matplotlib
