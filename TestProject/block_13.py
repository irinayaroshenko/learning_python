# def print_message():
#     print('Я - Артур,')
#     print('король британцев. ')
#
#
# print_message()

'''
Звездный прямоугольник 1
Напишите функцию draw_box(), которая выводит звездный прямоугольник с размерами 14×10 в соответствии с образцом:

**********
*        *
*        *
*        *
*        *
*        *
*        *
*        *
*        *
*        *
*        *
*        *
*        *
**********
Примечание. Для вывода прямоугольника используйте цикл for.
'''


# def draw_box():
#     print("*" * 10)
#     for _ in range(12):
#         print("*" + " " * 8 + "*")
#     print("*" * 10)
#
#
# draw_box()
from operator import and_

'''
Звездный треугольник 1
Напишите функцию draw_triangle(), которая выводит звездный прямоугольный треугольник с катетами, равными 10 в соответствии с образцом:
*
**
***
****
*****
******
*******
********
*********
**********
Примечание. Для вывода треугольника используйте цикл for. 
'''
# def draw_triangle():
    # for i in range(1, 11):
    #     print("*" * i)
    # or
    # print(*("*" * i for i in range(1, 11)), sep='\n')


# draw_triangle()

'''Factorial and recursion
Функция факториала наглядно отражает принцип рекурсии, когда для вычисления следующего значения нужен результат предыдущего.
'''
# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n - 1)
#
#
# print(factorial(7))

# n = 5
# print(id(n))  # shows id (address) in memory
# n += 4
# print(id(n))
#
# lst = [1,2,3]
# print(id(lst))
# lst.append(44)
# print(id(lst))

'''
Difference in links to memory!!!
https://stackoverflow.com/questions/2347265/why-does-behave-unexpectedly-on-lists
https://habr.com/ru/company/mailru/blog/454324/
'''
# lst = [1, 2, 3]
# lst_copy = lst
#
# print('Адрес в памяти переменной (имени) lst:', id(lst))
# print('Адрес в памяти переменной (имени) lst_copy:', id(lst_copy))
# if lst is lst_copy:
#     print('Адреса памяти lst и lst_copy совпадают')
# else:
#     print('Адреса памяти lst и lst_copy НЕ совпадают')
#
# '''
# А все потому, что здесь на самом деле создается новая переменная (имя) и
# для нее создается новый объект в памяти
# '''
# lst = lst + [8, 9]   # Здесь создается новый список !!!
#
# print('Адрес в памяти переменной (имени) lst:', id(lst))
# print('Адрес в памяти переменной (имени) lst_copy:', id(lst_copy))
# if lst is lst_copy:
#     print('Адреса памяти lst и lst_copy совпадают')
# else:
#     print('Адреса памяти lst и lst_copy НЕ совпадают')
#
# print(lst)  # [1, 2, 3, 8, 9]
# print(lst_copy)  # [1, 2, 3]
#
#
# lst = [1, 2, 3]
# lst_copy = lst
#
# print('Адрес в памяти переменной (имени) lst:', id(lst))
# print('Адрес в памяти переменной (имени) lst_copy:', id(lst_copy))
# if lst is lst_copy:
#     print('Адреса памяти lst и lst_copy совпадают')
# else:
#     print('Адреса памяти lst и lst_copy НЕ совпадают')
#
# '''
# А здесь НЕ создается новая переменная (имя), потому и lst, и lst_copy
# продолжают ссылаться на один и тот же объект в памяти
# '''
# lst += [8, 9]  # Здесь (операцией +=) изменяется текущий список !!!
#
# print('Адрес в памяти переменной (имени) lst:', id(lst))
# print('Адрес в памяти переменной (имени) lst_copy:', id(lst_copy))
# if lst is lst_copy:
#     print('Адреса памяти lst и lst_copy совпадают')
# else:
#     print('Адреса памяти lst и lst_copy НЕ совпадают')
#
# print(lst)  # [1, 2, 3, 8, 9]
# print(lst_copy)  # [1, 2, 3, 8, 9]

'''
Звездный треугольник
Напишите функцию draw_triangle(fill, base), которая принимает два параметра:
fill – символ заполнитель;
base – величина основания равнобедренного треугольника;
а затем выводит его.
Примечание. Гарантируется, что основание треугольника – нечетное число.
'''
# def draw_triangle(fill, base):
    # for i in range(1, (base // 2 + 1) + 1):
    #     print(fill * i)
    # for j in range(base // 2 + 1, base + 1):
    #     print(fill * (base - j))

    # Other solution
    # for i in range(1, base + 1):
    #     print(fill * min(i, base - i + 1))


# fill, base = input(), int(input())
#
# draw_triangle(fill, base)

'''
Звонок на перемену 😍
(10 баллов) from here https://stepik.org/lesson/494508/step/3?unit=485909
Продолжительность каждого урока в онлайн-школе BEEGEEK 45 минут, а перемены между уроками – 5 минут.
Первый урок начинается ровно в 88 часов утра. Напишите программу, определяющую во сколько заканчивается n-ый урок?
Формат входных данных
На вход программе подается натуральное число n(n≤15) – номер урока.
Формат выходных данных
Программа должна вывести два числа разделенные один пробелом – время в которое заканчивается n-ый урок.
'''
# n = int(input())
# lesson, break_time = 45, 5
# total_time = lesson * n + break_time * (n - 1)
# lesson_time = total_time // 60 + 8
# break_time = total_time % 60
#
# print(lesson_time, break_time)


'''
ФИО
Напишите функцию print_fio(name, surname, patronymic), которая принимает три параметра:
name – имя человека;
surname – фамилия человека;
patronymic – отчество человека;
а затем выводит на печать ФИО человека.
Примечание. Предусмотрите тот факт, что все три буквы в ФИО должны иметь верхний регистр.
'''
# def print_fio(name, surname, patronymic):
    # fio = list()
    # fio.append(surname[0].upper())
    # fio.append(name[0].upper())
    # fio.append(patronymic[0].upper())
    # print(*fio, sep="")

    # or just like this:
    # print(surname[0].upper(), name[0].upper(), patronymic[0].upper(), sep="")

    # Other solution
    # [print(m[0].upper(),end='') for m in [surname,name,patronymic]]
    # Other solution
    # print((surname[0]+name[0]+patronymic[0]).upper())
    # Other solution
    # print(*[i[0].upper() for i in [surname, name, patronymic]], sep='')
    # Other solution
    # print(f"{surname[0]}{name[0]}{patronymic[0]}".upper())


# name, surname, patronymic = input(), input(), input()
#
# print_fio(name, surname, patronymic)


'''
Сумма цифр
Напишите функцию print_digit_sum(), которая принимает одно целое число num и выводит на печать сумму его цифр.
'''
# def print_digit_sum(num):
#     digits = list(str(num))
#     for i in range(len(digits)):  # or print(sum([int(i) for i in str(num)])) or print(sum(map(int, str(n))))
#         digits[i] = int(digits[i])
#     print(sum(digits))
#
# n = int(input())

# В теле функции идет обработка переменной num. А в теле программы может быть любая другая переменная, в данном случае это n.
# print_digit_sum(n)

# def func():
#     global str_global  # Сообщение о том что мы будем работать
#     global num_global  # с глобальными переменными str_global и num_global.
#
#     str_global = str_global + ' добавка из локал'  # Теперь можно даже использовать
#     num_global = 123456789  # присваивание.
#
#
# str_global = 'Строка глобал'  # Глобальная переменная типа строка (string).
# num_global = 2002  # Глобальная переменная целого типа ( int  ).
#
# print(f'Строка "{str_global}"; Число "{num_global}"')  # До изменения.
#
# func()  # Вызов функции изменит значения в переменных.
#
# print(f'Строка "{str_global}"; Число "{num_global}"')  # После изменения.


# функция перевода градусов Фаренгейта в градусы Цельсия
# def convert_to_celsius(temp):
#     result = (5 / 9) * (temp - 32)
#     return result
#
# # основная программа
# temp = float(input('Bвeдитe количество градусов по Фаренгейту: '))
# celsius = convert_to_celsius(temp)
# print(round(celsius))  # градусы Цельсия


'''
Напишите функцию, которая возвращает длину гипотенузы прямоугольного треугольника по известным значениям его катетов.
Для нахождения длины гипотенузы, нам нужно применить теорему Пифагора: квадрат гипотенузы равен сумме квадратов катетов.
Другими словами, если a, b – длины катетов, а c – длина гипотенузы, то имеет место равенство:
c**2 = a**2 + b**2 => c = sqrt(a**2+b**2)
Note: В модуле math имеется встроенная функция hypot(x, у) которая возвращает длину гипотенузы
прямоугольного треугольника с катетами x и y.
'''
# def hypotenuse_length(a, b):
#     c = (a ** 2 + b ** 2) ** 0.5
#     return c

# print(hypotenuse_length(4, 5))
#
# x, y = int(input()), int(input())
# hypotenuse = hypotenuse_length(x, y)
# print(hypotenuse)


'''
Напишите функцию get_distance(x1, y1, x2, y2), вычисляющую расстояние между точками (x1; y1) и (x2; y2)
Решение. Расстояние между двумя точками (x1; y1) и (x2; y2) определяется по формуле:
ρ = sqrt{(x_1-x_2)^2 + (y_1-y_2)^2}
Несложно заметить, что искомое расстояние – это длина гипотенузы прямоугольного треугольника с катетами равными
 |x1 - x2| и |y1-y2|
'''
# def get_distance(x1, y1, x2, y2):
#     return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5


# def get_distance(x1, y1, x2, y2):
#     return hypotenuse_length(x1 - x2, y1 - y2)


# x1, y1 = float(input()), float(input())  # считываем координаты первой точки
# x2, y2 = float(input()), float(input())  # считываем координаты второй точки
#
# print(get_distance(x1, y1, x2, y2))      # вычисляем и выводим расстояние между точками


'''
Напишите функцию sum_digits(n), принимающую в качестве аргумента натуральное число и возвращающую сумму его цифр.
'''
# def sum_digits(n):
#     result = 0
#     while n != 0:
#         result += n % 10
#         n //= 10
#     return result
#
#
# n = int(input())
# print(sum_digits(n))


'''
Напишите функцию compute_average(numbers), принимающую в качестве аргумента список чисел и
возвращающую среднее значение элементов списка.
'''
# def compute_average(numbers):
#     return sum(numbers) / len(numbers)
#
#
# numbers = [1, 3, 5, 1, 6, 8, 10, 2]
# print(compute_average(numbers))

'''
Конвертер километров
Напишите функцию convert_to_miles(km), которая принимает в качестве аргумента расстояние в километрах и возвращает
расстояние в милях. Формула для преобразования: мили = километры * 0.6214.
'''
# def convert_to_miles(km):
#     return km * 0.6214
#
#
# num = int(input())
#
# print(convert_to_miles(num))

'''
Количество дней
Напишите функцию get_days(month), которая принимает в качестве аргумента номер месяца и возвращает количество дней
в данном месяце.
Примечание 1. Гарантируется, что передаваемый аргумент находится в диапазоне от 1 до 12.
Примечание 2. Считайте, что год является невисокосным.
'''
# def get_days(month):
#     if month == 2:
#         return 28
#     if month in (4, 6, 9, 11):
#         return 30
#     return 31

# or
#     m = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#     return m[month - 1]

# or
#     return [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31][month - 1]


# num = int(input())
# print(get_days(num))

'''
Делители 1
Напишите функцию get_factors(num), принимающую в качестве аргумента натуральное число и возвращающую список всех
делителей данного числа.
'''
# def get_factors(num):
#     factors = list()
#     for i in range(1, num + 1):
#         if num % i == 0:
#             factors.append(i)
#     return factors

# or
# return [i for i in range(1, num + 1) if num % i == 0]

# n = int(input())
# print(get_factors(n))


'''
Делители 2
Напишите функцию number_of_factors(num), принимающую в качестве аргумента число и возвращающую количество
делителей данного числа.
Примечание 1. Используйте уже реализованную функцию get_factors(num) из предыдущей задачи
'''
# def get_factors(num):
#     return [i for i in range(1, num + 1) if num % i == 0]
#
#
# def number_of_factors(num):
#     return len(get_factors(num))
#
#
# n = int(input())
# print(number_of_factors(n))

'''
Найти всех
Напомним, что строковый метод find('a') возвращает местоположение первого вхождения символа a в строке.
Проблема заключается в том, что данный метод не находит местоположение всех символов а.

Напишите функцию с именем find_all(target, symbol), которая принимает два аргумента: строку target и символ symbol
и возвращает список, содержащий все местоположения этого символа в строке.
Примечание 1. Если указанный символ не встречается в строке, то следует вернуть пустой список.
'''
# def find_all(target, symbol):
    # all_symbols = list()
    # while symbol in target:
    #     all_symbols.append(target.find(symbol))
    #     target = target.replace(symbol, "*", 1)  # better: target.replace(symbol,chr(ord(symbol)-1),1)
    # return all_symbols

    # or
    # all_symbols = list()
    # for i in range(len(target)):
    #     if target[i] == symbol:
    #         all_symbols.append(i)
    # return all_symbols

    # or
    # return [i for i in range(len(target)) if target[i] == symbol]


# s = input()
# char = input()
#
# print(find_all(s, char))


'''
Merge lists 1
Напишите функцию merge(list1, list2), которая принимает в качестве аргументов два отсортированных по возрастанию списка,
состоящих из целых чисел, и объединяет их в один отсортированный список.
Примечание 1. Списки list1 и list2 могут иметь разную длину.
Примечание 2. Можно использовать списочный метод sort(), а можно обойтись и без него
'''
# list.sort() сортирует список и сохраняет отсортированный исходный список, а sorted(list) создаёт и возвращает
# отсортированный новый список без изменения исходного списка.
# метод .sort() применяется только к спискам, функция sorted() отсортирует всё, что угодно
# Для списков list.sort() быстрее, чем sorted() потому что ему не нужно создавать копию.
# Для любого другого итеративного выбора - sorted()
# https://www.rupython.com/sorted-list-vs-list-sort-2667.html

# def merge(list1, list2):
    # list1 += list2
    # list1.sort()
    # return list1

# or
#     list1 += list2
#     return sorted(list1)

# or
#     return sorted(list1 + list2)
#
# numbers1 = [int(c) for c in input().split()]
# numbers2 = [int(c) for c in input().split()]
# print(merge(numbers1, numbers2))

# Other solution. Without .sort() method
# def merge(list1, list2):
#     first, second = list1[:], list2[:]
#     result = []
#
#     while first and second:
#         if first[0] <= second[0]:
#             item = first.pop(0)
#         else:
#             item = second.pop(0)
#         result.append(item)
#
#     result.extend(first if first else second)
#     return result
#
#
# numbers1 = [int(c) for c in input().split()]
# numbers2 = [int(c) for c in input().split()]
#
# print(merge(numbers1, numbers2))


'''
При работе со списками, знайте что .append() работает быстрее чем +=, а += быстрее чем .extend() из одного элемента.
'''

'''For time counting'''
# from datetime import datetime
#
# start_time = datetime.now()
#
# # вставьте свой код сюда
#
#
# end_time = datetime.now()
#
# print('Duration: {}'.format(end_time - start_time))


'''
Merge sort for one list
'''
# def merge_sort(A):
#     if len(A) == 1 or len(A) == 0:
#         return A
#     L, R = A[:len(A) // 2], A[len(A) // 2:]
#     merge_sort(L)
#     merge_sort(R)
#     n = m = k = 0
#     C = [0] * (len(L) + len(R))
#     while n < len(L) and m < len(R):
#         if L[n] <= R[m]:
#             C[k] = L[n]
#             n += 1
#         else:
#             C[k] = R[m]
#             m += 1
#         k += 1
#     while n < len(L):
#         C[k] = L[n]
#         n += 1
#         k += 1
#     while m < len(R):
#         C[k] = R[m]
#         m += 1
#         k += 1
#     for i in range(len(A)):
#         A[i] = C[i]
#     return A
#
#
# A = [6, 5, 3, 1, 8, 4, 7, 2]
# print(merge_sort(A))

'''
Merge sort for 2 already sorted lists
'''
# def quick_merge(list1, list2):
#     result = []
#
#     p1 = 0  # указатель на первый элемент списка list1
#     p2 = 0  # указатель на первый элемент списка list2
#
#     while p1 < len(list1) and p2 < len(list2):  # пока не закончился хотя бы один список
#         if list1[p1] <= list2[p2]:
#             result.append(list1[p1])
#             p1 += 1
#         else:
#             result.append(list2[p2])
#             p2 += 1
#
#     if p1 < len(list1):  # прицепление остатка
#         result += list1[p1:]
#     if p2 < len(list2):
#         result += list2[p2:]
#
#     return result
#
#
# list1 = [3, 10, 11, 12, 47, 57, 58, 63, 77, 79, 80, 95]
# list2 = [0, 11, 12, 20, 24, 26, 47, 48, 53, 65, 70, 81, 84, 84, 90]
# list3 = quick_merge(list1, list2)
# print(list3)

'''
Merge lists 2
На вход программе подается число n, а затем n строк, содержащих целые числа в порядке возрастания, разделенные символом
пробела. Из данных строк формируются списки чисел.
Напишите программу, которая объединяет указанные списки в один отсортированный список с помощью функции quick_merge(),
а затем выводит его.
'''
# def quick_merge():
#     result = []
#     for i in range(int(input())):
#         result.extend(int(c) for c in input().split())
#     result.sort()
#     return result
#
# print(*quick_merge())


# Other solution with reuse quick_merge() function
# def quick_merge(list1, list2):
#     result = []
#
#     p1 = 0  # указатель на первый элемент списка list1
#     p2 = 0  # указатель на первый элемент списка list2
#
#     while p1 < len(list1) and p2 < len(list2):  # пока не закончился хотя бы один список
#         if list1[p1] <= list2[p2]:
#             result.append(list1[p1])
#             p1 += 1
#         else:
#             result.append(list2[p2])
#             p2 += 1
#
#     if p1 < len(list1):  # прицепление остатка
#         result += list1[p1:]
#     elif p2 < len(list2):
#         result += list2[p2:]
#
#     return result
#
#
# lst = list()
# for _ in range(int(input())):
#     lst = quick_merge(lst, [int(i) for i in input().split()])
# print(*lst)

# or
# total_list = []
# for i in range(int(input())):
#     num = [int(q) for q in input().split()]
#     total_list = quick_merge(total_list, num)
# print(*total_list)

# or
# a_list = []
# lists = [[int(i) for i in input().split()] for _ in range(int(input()))]
#
# for i in range(len(lists)):
#     a_list = quick_merge(a_list, lists[i])
# print(*a_list)


# List slices
# s = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(s[:0:-3])  # [9, 6, 3]
# print(s[-1:0:-3])  # [9, 6, 3]
# print(s[::-3])  # [9, 6, 3, 0]


# Bool function
# def is_even(num):
#     return num % 2 == 0
#
# for i in range(10):
#     print(is_even(i))


'''
Is Valid Triangle?
Напишите функцию is_valid_triangle(side1, side2, side3), которая принимает в качестве аргументов три натуральных числа,
и возвращает значение True если существует невырожденный треугольник со сторонами side1, side2, side3 и False в противном случае.
'''
# def is_valid_triangle(side1, side2, side3):
#     return side1 + side2 > side3 and side1 + side3 > side2 and side2 + side3 > side1
#
#
# # or
# def is_valid_triangle(*sides):  # в данном случае звездочка запаковывает все переданные функции аргументы в один кортеж
#     return sum(sides) - max(sides) > max(sides)
#
# a, b, c = int(input()), int(input()), int(input())
# print(is_valid_triangle(a, b, c))


'''
Is a Number Prime? 🌶️
Напишите функцию is_prime(num), которая принимает в качестве аргумента натуральное число и возвращает значение True,
если число является простым и False в противном случае.
'''
# def is_prime(num):
#     if num == 1:
#         return False
#     for i in range(2, num // 2 + 1):  # or (2, int(n**0.5)+1)
#         if num % i == 0:
#             return False
#     return True

# other solution
# def is_prime(num):
#     return len([i for i in range(1, num+1) if num % i == 0]) == 2


# n = int(input())
# print(is_prime(n))

# a, b = int(input()), int(input())
# for i in range(a, b + 1):
#     count = 0
#     if i == 1:
#         continue
#     for j in range(2, i // 2 + 1):
#         if i % j == 0:
#             count += 1
#     if count == 0:
#         print(i)


'''
Next Prime 🌶️🌶️
Напишите функцию get_next_prime(num), которая принимает в качестве аргумента натуральное число num и возвращает первое
простое число большее числа num.
Примечание 1. Используйте функцию is_prime() из предыдущей задачи.
'''
# def is_prime(num):
#     if num == 1:
#         return False
#     for i in range(2, num // 2 + 1):  # or (2, int(n**0.5)+1)
#         if num % i == 0:
#             return False
#     return True
#
#
# def get_next_prime(num):
#     num += 1
#     while not is_prime(num):
#         num += 1
#     return num
#
#
# n = int(input())
# print(get_next_prime(n))


'''
Good password 🌶️
Напишите функцию is_password_good(password), которая принимает в качестве аргумента строковое значение пароля password
и возвращает значение True если пароль является надежным и False в противном случае.

Пароль является надежным если:
его длина не менее 8 символов; 
он содержит как минимум одну заглавную букву (верхний регистр); 
он содержит как минимум одну строчную букву (нижний регистр);
он содержит хотя бы одну цифру.
'''
# def is_password_good(password):
#     digit, small, big = 0, 0, 0
#     if len(password) < 8:
#         return False
#     for i in password:
#         if i.isdigit():
#             digit += 1
#         elif i.isalpha() and i.islower():
#             small += 1
#         elif i.isalpha() and i.isupper():
#             big += 1
#     if digit > 0 and small > 0 and big > 0:
#         return True
#     return False

# Other solution
# def is_password_good(password):
#     if len(password) < 8:
#         return False
#     flag1 = False
#     flag2 = False
#     flag3 = False
#     for c in password:
#         if c.isupper():
#             flag1 = True
#         elif c.islower():
#             flag2 = True
#         elif c.isdigit():
#             flag3 = True
#     return flag1 and flag2 and flag3
#
# Other solution
# def is_password_good(password):
#     return len(password) > 7 and password != password.lower() and password != password.upper() and not password.isalpha()

# Other solution
# def is_password_good(password):
#     upp = [i for i in password if i.isupper()]
#     low = [i for i in password if i.islower()]
#     dig = [i for i in password if i.isdigit()]
#     return all([len(password) >= 8, upp, low, dig])

'''Explanation:
встроенная функция all(последовательность) возвращает True, только если все элементы последовательности истинные
(или, если последовательность пуста). Если хотя бы один элемент последовательности ложный функция вернёт False.

all([]) # True
all([True, True, True])  # True
all([True, True, False])  # False

all([[1, 2], [], [5, 2]]) # False
all([['a', 'b'], [4, 5], ['3', 8]]) # True

all([1, 2, 0])  # False
all([1, 2, 3])  # True

all([1 == 1, 2 < 3, 5 >= 4]) # True
all([2 == 3, 0 < 5, 9 > 4]) # False
Если в password нет больших букв, то список upp будет пустой, если нет маленьких то low, а если нет цифр, то пустой
будет список dig. Пустой список = False, не пустой список = True. Поэтому, если хотя бы один из списков пуст или
длина пароля < 8, то функция all() вернёт False  А если все элементы последовательности в all() истинны - вернёт True

Говоря, про all()  нельзя не сказать про any()
Есть в python   аналогичная all() встроенная функция, называется any(iterable), которая возвращает True,
если хотя бы какой-нибудь элемент iterable возвращает истину. Если итерируемый объект пуст, возвращается False.

any([])  # False

any([False, False, False])  # False
any([False, True, False])  # True

any([0, 0, 0, 0])  # False
any([0, 1, 0, 0])  # True
'''

# txt = input()
# print(is_password_good(txt))

'''
Ровно в одном
Напишите функцию is_one_away(word1, word2), которая принимает в качестве аргументов два слова word1 и word2
и возвращает значение True если слова имеют одинаковую длину и отличаются ровно в 1 символе и False в противном случае.
'''
# def is_one_away(word1, word2):
#     if len(word1) != len(word2):
#         return False
#     count = 0
#     for i in range(len(word1)):
#         if word1[i] != word2[i]:
#             count += 1
#     return count == 1
#
# # Other solution
# def is_one_away(word1, word2):
#     return len(word1) == len(word2) and len([i for i in range(len(word1)) if word1[i] != word2[i]]) == 1
#
# txt1 = input()
# txt2 = input()
# print(is_one_away(txt1, txt2))

'''
Палиндром 🌶️
Напишите функцию is_palindrome(text), которая принимает в качестве аргумента строку text и возвращает значение True,
если указанный текст является палиндромом и False в противном случае.

Примечание 1. Палиндром – это строка, которая читается одинаково в обоих направлениях

Примечание 2. При проверке считайте большие и маленькие буквы одинаковыми, а также игнорируйте пробелы,
а также символы , . ! ? -.

Примечание 3. Следующий программный код:
print(is_palindrome('А роза упала на лапу Азора.'))  - True
print(is_palindrome('Gabler Ruby - burrel bag!'))  - True
print(is_palindrome('BEEGEEK'))  - False
'''
# def is_palindrome(text):
#     lst_palindr = [i.lower() for i in text if i.isalpha()]
#     return lst_palindr == lst_palindr[::-1]
#
# # Other solution
# def is_palindrome(text):
#     phrase = ''.join([a for a in text if a.isalpha()]).lower()
#     return phrase == phrase[::-1]
#
# Other solution
# def is_palindrome(text):
#     t = [c.lower() for c in text if c not in ', .!?-']
#     return t == list(reversed(t))
#
# txt = input()
# print(is_palindrome(txt))


'''
BEEGEEK
BEEGEEK наконец открыл свой банк в котором используются специальные банкоматы с необычным паролем.
Действительный пароль BEEGEEK банка имеет вид a:b:c, где a, b и c – натуральные числа.
Поскольку основатель BEEGEEK фанатеет от математики, то он решил:

число a – должно быть палиндромом;
число b – должно быть простым;
число c – должно быть четным.
Напишите функцию is_valid_password(password), которая принимает в качестве аргумента строковое значение пароля password
и возвращает значение True если пароль является действительным паролем BEEGEEK банка и False в противном случае.

Примечание. Следующий программный код:
print(is_valid_password('1221:101:22'))  - True
print(is_valid_password('565:30:50'))    - False
print(is_valid_password('112:7:9'))      - False
print(is_valid_password('1221:101:22:22'))  - False
'''
# def is_palindrome(text):
#     lst_palindr = [i for i in text if i.isdigit()]
#     return lst_palindr == lst_palindr[::-1]
#
# def is_prime(num):
#     if num == 1:
#         return False
#     for i in range(2, num // 2 + 1):
#         if num % i == 0:
#             return False
#     return True
#
# def is_valid_password(password):
#     pass_lst = [int(i) for i in password.split(':')]
#     return len(pass_lst) == 3 and is_palindrome(str(pass_lst[0])) and is_prime(pass_lst[1]) and pass_lst[2] % 2 == 0
#
# # Other solution
# # def is_valid_password(password):
# #     password = password.split(':')
# #     a, b, c = password[0], int(password[1]), int(password[2])
# #     if len(password) != 3 or a != a[::-1] or c % 2 != 0:
# #         return False
# #     for i in range(2, b):
# #         if b % i == 0:
# #             return False
# #     return True
#
#
# psw = input()
# print(is_valid_password(psw))

'''
Правильная скобочная последовательность 🌶️
Напишите функцию is_correct_bracket(text), которая принимает в качестве аргумента непустую строку text, состоящую из
символов ( и ) и возвращает значение True, если поступившая на вход строка является правильной скобочной
последовательностью и False в противном случае.

Примечание 1. Правильной скобочной последовательностью называется строка, состоящая только из символов ( и ),
где каждой открывающей скобке найдется парная закрывающая скобка.

Примечание 2. Следующий программный код:
print(is_correct_bracket('()(()())'))  - True
print(is_correct_bracket(')(())('))    - False
())(()  - False
'''
# def is_correct_bracket(text):
#     if text.startswith(')') or text.endswith('(') or text.count('(') != text.count(')'):
#         return False
#
#     text_list = list(text)
#     length = len(text_list)
#     while length > 1:
#         text_list.remove('(')
#         text_list.remove(')')
#         if not len(text_list):  # use 'not' instead of len(text_list) == 0   For sequences, (strings, lists, tuples),
#             return True                                      # use the fact that empty sequences are false
#         if text_list[0] == ')':
#             return False
#         length = len(text_list)
#     return True
#
#
# txt = input()
# print(is_correct_bracket(txt))
# Explanation: https://stackoverflow.com/questions/43121340/why-is-the-use-of-lensequence-in-condition-values-considered-incorrect-by-pyli

# Other solution
# def is_correct_bracket(text):
#     count = 0
#     for i in text:
#         if i == '(':
#             count += 1
#         elif i == ')':
#             count -= 1
#         if count < 0:
#             return False
#     return count == 0

# Other solution
# def is_correct_bracket(text):
#     while '()' in text:
#         text = text.replace('()', '')
#     return not text
# При возврате строки text мы интерпретируем её как логическую переменную (пустая строка - False, непустая - True)
# Оператор not инвертирует значение логической переменной и функция возвратит True если строка пустая, а пустая она
# только в случае, если последовательность скобок правильная.


'''
A list of the fruit contains fruit_name and property saying its fruit. Another list consume has two items juice and eat.
With the help of pop() and append() we can do something interesting. 
'''
# fruit = [['Orange', 'Fruit'], ['Banana', 'Fruit'], ['Mango', 'Fruit']]
# consume = ['Juice', 'Eat']
# possible = []
#
# for item in fruit:
#     for use in consume:
#         item.append(use)
#         possible.append(item[:])
#         item.pop(-1)
# print(possible)

'''
Змеиный регистр
Напишите функцию convert_to_python_case(text), которая принимает в качестве аргумента строку в CamelCase и преобразует
его в snake_case.  ThisIsCamelCased -> this_is_camel_cased
'''
# def convert_to_python_case(text):
#     text1 = text[0]
#     for i in range(1, len(text)):
#         if text[i].islower() or text[i].isdigit():
#             text1 += text[i]
#         elif text[i].isupper():
#             text1 += '_' + text[i]
#     return text1.lower()

# Other solution
# def convert_to_python_case(text):
#     s = ''
#     for i in text:
#         if i.isupper():
#             i = '_' + i.lower()
#         s = s + i
#     return s[1:]

# Other solution
# def convert_to_python_case(text):
#     text = text[0].lower() + text[1:]
#     for i in text:
#         if i.isupper():
#             text = text.replace(i, '_'+i.lower(), 1)
#     return text

# Other solution
# def convert_to_python_case(text):
#     for i in text:
#         if i in 'QWERTYUIOPASDFGHJKLZXCVBNM':
#             text = text.replace(i, '_' + i.lower())
#     return text[1:]
#
# txt = input()
# print(convert_to_python_case(txt))

'''
Середина отрезка
Напишите функцию get_middle_point(x1, y1, x2, y2), которая принимает в качестве аргументов координаты концов отрезка
(x_1; y_1) и (x_2; y_2) и возвращает координаты точки, являющейся серединой данного отрезка.
Примечание 1. Координаты середины отрезка вычисляются по формуле: ((x1+x2)/2; (y1+y2)/2)
'''
# def get_middle_point(x1, y1, x2, y2):
#     return (x1 + x2) / 2, (y1 + y2) / 2
#
#
# x_1, y_1 = int(input()), int(input())
# x_2, y_2 = int(input()), int(input())
# x, y = get_middle_point(x_1, y_1, x_2, y_2)
# print(x, y)


'''
Площадь и длина
Напишите функцию get_circle(radius), которая принимает в качестве аргумента радиус окружности и возвращает два значения:
длину окружности и площадь круга, ограниченного данной окружностью.
Примечание 1. Длина окружности и площадь круга радиуса r вычисляются по формулам: С=2πr,S=πr**2
Примечание 2. Для числа π используйте глобальную константу из модуля math.
'''
# from math import pi
# def get_circle(radius):
#     c = 2 * pi * radius
#     s = pi * radius ** 2
#     return c, s
#
#
# r = float(input())
# length, square = get_circle(r)
# print(length, square)  # 9.42477796076938 7.0685834705770345
# print(get_circle(r))  # (9.42477796076938, 7.0685834705770345)


'''
Корни уравнения 🌶️🌶️
Напишите функцию solve(a, b, c), которая принимает в качестве аргументов три целых числа a, b, c – коэффициенты
квадратного уравнения ax^2+bx+c = 0 и возвращает его корни в порядке возрастания.
Примечание. Гарантируется, что квадратное уравнение имеет корни.
It's based on one of the previous task:  Квадратное уравнение 🌶️🌶️
https://stepik.org/lesson/265110/step/7?unit=246058

from math import pow, sqrt

a, b, c = float(input()), float(input()), float(input())
D = pow(b, 2) - 4 * a * c

if D > 0:
    x1 = (-b + sqrt(D)) / (2 * a)
    x2 = (-b - sqrt(D)) / (2 * a)
    if x1 < x2:
        print(x1, x2, sep="\n")
    else:
        print(x2, x1, sep="\n")
elif D == 0:
    x1 = (-b + sqrt(D)) / (2 * a)
    print(x1)
else:
    print("Нет корней")
'''
# from math import pow, sqrt
#
# def solve(a, b, c):
#     d = pow(b, 2) - 4 * a * c
#     x1 = (-b + sqrt(d)) / (2 * a)
#     x2 = (-b - sqrt(d)) / (2 * a)
#     return min(x1, x2), max(x1, x2)
#
# # считываем данные
# a, b, c = int(input()), int(input()), int(input())
#
# # вызываем функцию
# x1, x2 = solve(a, b, c)
# print(x1, x2)
