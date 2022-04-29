import os
import sys
import time
import zipfile

#
#
# print("Command line arguments: ")
# for i in sys.argv:
#     print(i)
#
# print('\nPYTHONPATH contains:', sys.path)
# source = ['"C:\\Users\\i_yaroshenko\\Pictures\\Saved Pictures"', 'C:\\Users\\i_yaroshenko\\vbrvenv\\Scripts']
# print(os.getcwd())
#
# source = ['"C:\\Users\\i_yaroshenko\\Pictures\\Saved Pictures"', 'C:\\Users\\i_yaroshenko\\vbrvenv\\Scripts']
# target_dir = 'D:\\Backup'
# target = target_dir + os.sep + time.strftime('%Y%m%d%H%M%S') + '.zip'
# # zip_command = f'zip -qr {target} {" ".join(source)}'
# zip_command = f'7z a -tzip {target} {" ".join(source)}'
# print(zip_command)
# # print(os.environ.get('Path'))
# if os.system(zip_command) == 0:
#     print(f'Reserve copy is created in {target}')
# else:
#     print('Not created')

# f = open('D:\PyCharm Projects\TestProject\poem.txt')
# poem = '''\
# or what erases it, past the bakery,
# when you tire. We ride the blades again
# beside the crooked bay. You smile.
# I hold you like a hole holds light.
# '''

# while True:
#     line = f.readline()
#     if not len(line):
#         break
#     print(line, end=' ')
# f.close()

# with open('D:\PyCharm Projects\TestProject\poem.txt', 'a') as file:
#     file.write(poem)
#
# with open('D:\PyCharm Projects\TestProject\poem.txt') as file:
#     print(file.read())

# print(eval('2 * 3'))


# Bool data type
'''
операторы and и or возвращают не булевы значения, а сами значения. 
Например,
AND возвращает последний истинный операнд, если оба операнда True, в противном случае первый ложный
1 and 2 -> 2    1 and 0 -> 0    0 and 1 -> 0

OR возвращает первый истинный, если он есть, в противном случае последний ложный
1 or 0 -> 1    0 or 1 -> 1    1 or  2 -> 1    False or 0 -> 0
'''

'''
Предикат делимости
Напишите функцию func(num1, num2), принимающую в качестве аргументов два натуральных числа num1 и num2 и возвращающую
значение True если число num1 делится без остатка на число num2 и False в противном случае.
Результатом вывода программы должно быть "делится" (если функция func() вернула True) и "не делится"
(если функция func() вернула False).
'''
# def func(num1, num2):
#     return num1 % num2 == 0
#
#
# n1, n2 = int(input()), int(input())
# if func(n1, n2):
#     print('делится')
# else:
#     print('не делится')

# list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
# list1[2][2].append(7000)
# print(list1)

# list1 = ['a', 'b', ['c', ['d', 'e', ['f', 'g'], 'k'], 'l'], 'm', 'n']
# sub_list = ['h', 'i', 'j']
# list1[2][1][2].extend(sub_list)
# print(list1)

'''
Когда много вложений, можно вывести их индексы с помощю  enumerate
for i in enumerate(list1):
    print(i)
'''

'''
Дополните приведенный код, используя цикл for и встроенную функцию max(), чтобы он выводил один общий
максимальный элемент среди всех элементов вложенных списков list1.
list1 = [[1, 7, 8], [9, 7, 102], [6, 106, 105], [100, 99, 98, 103], [1, 2, 3]]
maximum = -1

print(maximum)
'''
# list1 = [[1, 7, 8], [9, 7, 102], [6, 106, 105], [100, 99, 98, 103], [1, 2, 3]]
# maximum = -1
# for li in list1:
#     if max(li) > maximum:
#         maximum = max((li))
# print(maximum)

# Other solution
# print((max([max(i) for i in list1])))

# Other solution
# max_string = max(max(list1, key=max))
# print(max_string)

'''
Дополните приведенный код так, чтобы list1 = [[1, 7, 8], [9, 7, 102], [102, 106, 105], [100, 99, 98, 103], [1, 2, 3]]
 имел вид: list1 = [[8, 7, 1], [102, 7, 9], [105, 106, 102], [103, 98, 99, 100], [3, 2, 1]]
'''
# list1 = [[1, 7, 8], [9, 7, 102], [102, 106, 105], [100, 99, 98, 103], [1, 2, 3]]
# for li in list1:
#     li.reverse()
# print(list1)

# Other solution with generator
# [x.reverse() for x in list1]
# # or
# list1 = [lst[::-1] for lst in list1]
# print(list1)


# Other solution with map
# print(list(map(list, map(reversed, list1))))

# lst = [1, 2, 3, 4, 5]
# lst1 = list(map(lambda el: [el], lst))
# print(lst1)  # [[1], [2], [3], [4], [5]]

'''
Дополните приведенный код так, чтобы он выводил единственное число: сумму всех чисел списка list1 разделённую на
общее количество всех чисел.
list1 = [[1, 7, 8], [9, 7, 102], [102, 106, 105], [100, 99, 98, 103], [1, 2, 3]]
'''
list1 = [[1, 7, 8], [9, 7, 102], [102, 106, 105], [100, 99, 98, 103], [1, 2, 3]]
# summ, count = 0, 0
# for li in list1:
#     count += len(li)
#     summ += sum(li)
# print(summ / count)

# My other solution
# list1 = [[1, 7, 8], [9, 7, 102], [102, 106, 105], [100, 99, 98, 103], [1, 2, 3]]
# summ = sum(sum(li) for li in list1)
# count = sum([len(i) for i in list1])
# print(summ / count)

# My other solution
# print(sum(map(sum, list1)) / sum(map(len, list1)))

# Other options
'''
Зачем в функции SUM второй аргумент? Он указывает значение, к которому следует суммировать все элементы из iterable.
Например, если мы укажем
sum([1, 2, 3], 1)
то этот код вернет сумму элементов списка + 1, то есть, 7.
Если второй аргумент не указывать, то, логично, что, по умолчанию, он равен нулю.
Теперь возвращаемся к нашему списку.
Если не указывать второй аргумент, то ф-я SUM попробует к нашему итоговому списку прибавить 0, что, очевидно, приведет
к ошибке. Чтобы такого не было, нам нужно задать второй аргумент пустым списком, тогда ф-я SUM прибавит к итоговому
списку пустой список, что не приведет к ошибке и не исказит результат.
sum(list1, []) - приводим двумерный список к одномерному

Данный трюк работает только с двумерными списками, и он сильно неэффективный по скорости при увеличении кол-ва списков.
'''
# list1 = sum([i for j in list1 for i in j])
# or
# list2 = sum(sum(list1, []))
# print(list2)

# n, m = int(input()), int(input())    # считываем значения n и m
# my_list = [0] * n
#
# for i in range(n):
#     my_list[i] = [0] * m
# my_list[0][0] = 17
# print(my_list)


# Examples of nested lists
# n, m = int(input()), int(input())    # считываем значения n и m
# my_list = [[0] * m ] * n
# my_list[0][0] = 17
# print(my_list)

# my_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# for i in my_list:
#     for j in i:
#         print(j, end=' ')   # используем необязательный параметр end
#     print()

# my_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#
# for i in range(len(my_list)):
#     for j in range(len(my_list[i])):
#         print(my_list[j][i], end=' ')    # выводим my_list[j][i] вместо my_list[i][j]
#     print()

# Make list. Option 1
# n, m = int(input()), int(input())
# my_list = []
# for _ in range(n):
#     my_list.append([0] * m)
# print(my_list)

# Make list. Option 2
# n, m = int(input()), int(input())
# my_list = [0] * n
# for i in my_list:
#     print(id(i))
# print(my_list)
# print('my_list id =', id(my_list))
# for li in range(n):
#     my_list[li] = [1] * m
#     print(id(my_list[li]))
# print(my_list)
# print('my_list id =', id(my_list))
# my_list[0][0] = 2
# print(my_list, id(my_list[0]))

# Make list. Option 3. List comprehension (generator)
# my_list = [[0] * m for _ in range(n)]
# print(my_list)

# Generator. Difference.
# list_a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# list_b = [[x ** 2 for x in row] for row in list_a]  # [[1, 4, 9], [16, 25, 36], [49, 64, 81]]
# list_c = [x ** 2 for row in list_a for x in row]    # [1, 4, 9, 16, 25, 36, 49, 64, 81]
# print(list_b)
# print(list_c)

# Транспонирование матрицы (процесс замены строк матрицы на ее столбцы, а столбцов соответственно на строки)
# matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
# matrix_1 = [[row[i] for row in matrix] for i in range(len(matrix))]  # [[1, 5, 9], [2, 6, 10], [3, 7, 11]]
# print(matrix_1)
# # For better understanding how this generator works:
# for i in range(len(matrix)):     # 1 5 9
#     for row in matrix:           # 2 6 10
#         print(row[i], end=' ')   # 3 7 11
#     print()

# Сгенерировать одномерный список через вложенные генераторы
# list_1 = [j ** 2 for j in [i + 1 for i in range(5)]]  # [1, 4, 9, 16, 25]
# print(list_1)

# ОБХОД МАТРИЦЫ В РАЗНЫХ НАПРАВЛЕНИЯХ  https://www.youtube.com/watch?v=0qtLrRm36J0&list=PLQAt0m1f9OHvv2wxPGSCWjgy1qER_FvB6&index=32
# a = [[0, 2, 4, 6],
#      [1, 5, 9, 13],
#      [3, 10, 17, 19]
#      ]                # Output
# print('From left to right + From top to bottom')
# for i in range(len(a)):             # for i in range(3):           0 2 4 6
#     for j in range(len(a[i])):         # for i in range(4):        1 5 9 13
#         print(a[i][j], end=' ')                                  # 3 10 17 19
#     print()
#
# print('From top to bottom + From left to right')
# for j in range(len(a[i])):          # for i in range(4):
#     for i in range(len(a)):             # for i in range(3):
#         print(a[i][j], end=' ')
#     print()

# !! Способ переставления просто индексов без переставления циклов возможен только при размере матрицы n*n, напр., 3*3
# Если матрица не квадратная, напр., 3*4, то будет IndexError: list index out of range
# a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# for i in range(len(a)):                                          # 1 4 7
#     for j in range(len(a[i])):                                   # 2 5 8
#         print(a[j][i], end=' ')  # переставлене индексов         # 3 6 9
#     print()

# print('From right to left + From bottom to top')
# for i in range(len(a)-1, -1, -1):           # for i in range(2, -1, -1):     19 17 10 3
#     for j in range(len(a[i])-1, -1, -1):      # for i in range(3, -1, -1):   13 9 5 1
#         print(a[i][j], end=' ')                                             # 6 4 2 0
#     print()
#
# print('From bottom to top + From right to left')
# for j in range(len(a[i])-1, -1, -1):                                       # 19 13 6
#     for i in range(len(a)-1, -1, -1):                                      # 17 9 4
#         print(a[i][j], end=' ')                                            # 10 5 2
#     print()                                                                # 3 1 0

'''
Список по образцу 1
На вход программе подается число n. Напишите программу, кот. создает и выводит построчно список, состоящий
из n списков [[1, 2, ..., n], [1, 2, ..., n], ..., [1, 2, ..., n]].
'''
# n = int(input())
# lst = []
# for i in range(n):
#     elem = [j for j in range(1, n + 1)]
#     lst.append(elem)
#     print(elem, end='\n')

# My other solution
# n = int(input())
# lst1 = [[j for j in range(1, n + 1)] for i in range(n)]
# for i in lst1:
#     print(i)

# Other solution
# n = int(input())
# result = []
# for _ in range(n):
#     result.append(list(range(1, n + 1)))
# print(*result, sep='\n')

# Other solution
# n = int(input())
# for _ in range(n):
#     my_list = []
#     for i in range(1, n+1):
#         my_list.append(i)
#     print(my_list)

'''
How to use \n in list comprehension: print(*[[i for i in range(1, n + 1)]] * n, sep='\n')
'''

'''
Список по образцу 2
На вход программе подается число n. Напишите программу, кот. создает и выводит построчно вложенный список, состоящий
из n списков [[1], [1, 2], [1, 2, 3], ..., [1, 2, ..., n]].
Input: 3
Output:
[1]
[1, 2]
[1, 2, 3]
'''
# n = int(input())
# lst = []
# for i in range(1, n + 1):
#     elem = [j for j in range(1, i + 1)]
#     lst.append(elem)
#     print(elem)

# My other solution
# print(*[[j for j in range(1, i + 1)] for i in range(1, n + 1)], sep='\n')
# lst1 = [[j for j in range(1, i + 1)] for i in range(1, n + 1)]
# print(lst1)

# My other solution
# result = []
# for i in range(1, n + 1):
#     result.append(list(range(1, i + 1)))
# print(*result, sep='\n')

'''
Треугольник Паскаля 1 🌶️
Треугольник Паскаля — бесконечная таблица биномиальных коэффициентов, имеющая треугольную форму.
В этом треугольнике на вершине и по бокам стоят единицы. Каждое число равно сумме двух расположенных над ним чисел.
0:      1
1:     1 1
2:    1 2 1
3:   1 3 3 1
4:  1 4 6 4 1
      .....

На вход программе подается число n. Напишите программу, кот. возвращает указанную строку треугольника Паскаля в виде
списка (нумерация строк начинается с нуля).
Примечание 1. Решение удобно оформить в виде функции pascal(), которая принимает номер строки и возвращает
соответствующую строку треугольника Паскаля. Formula: n! / (m! * (n - m)!)
Input: 3
Output: [1, 3, 3, 1]
'''
# from math import factorial
#
# def pascal(n):
#     lst = []
#     for i in range(n + 1):
#         elem = [int(factorial(i) / (factorial(j) * (factorial(i - j)))) for j in range(i + 1)]
#         lst.append(elem)
#     return lst[n]
#
#
# print(pascal(int(input())))

# Other solution
# def pascal(line):
#     lst_gen = [[1], [1, 1]]
#     if line <= 1:
#         return lst_gen[line]
#     else:
#         for i in range(line - 1):
#             lst_row = [1]
#             k = len(lst_gen[-1])
#             for j in range(k - 1):
#                 elem = lst_gen[-1][j] + lst_gen[-1][j + 1]
#                 lst_row.append(elem)
#             lst_row.append(1)
#             lst_gen.append(lst_row)
#     return lst_gen[line]
#
#
# print(pascal(int(input())))

'''
Треугольник Паскаля 2
На вход программе подается натур. число n (n≥1). Напишите программу, кот. выводит первые n строк треугольника Паскаля.
Input: 5
Output:
1
1 1
1 2 1
1 3 3 1
1 4 6 4 1
'''
# n = int(input())
# triangle = [[1], [1, 1]]
# for i in range(1, n - 1):
#     row = [1]
#     for j in range(len(triangle[i]) - 1):
#         el = triangle[i][j] + triangle[i][j + 1]
#         row.append(el)
#     row.append(1)
#     triangle.append(row)
#
# for i in range(n):
#     print(*triangle[i])


# !!! вывод двумерного массива одной строчкой !!!
# [print(*lst) for lst in triangle]


'''
Упаковка дубликатов 🌶️
На вход программе подается строка текста, содержащая символы, отделенные символом пробела.
Напишите программу, кот. упаковывает последовательности одинаковых символов заданной строки в подсписки.
Input: g i v e t h h i i s m a a a n a g u u n
Output: [['g'], ['i'], ['v'], ['e'], ['t'], ['h', 'h'], ['i', 'i'], ['s'], ['m'], ['a', 'a', 'a'], ['n'], ['a'], ['g'], ['u', 'u'], ['n']]
'''
# s = input().split()
# elem = [s[0]]
# duplicates = []
# for i in range(1, len(s)):
#     if s[i] == s[i - 1]:
#         elem += s[i]
#     else:
#         duplicates.append(elem)
#         elem = [s[i]]
# duplicates.append(elem)
# print(duplicates)

# or with function
# def duplicates(text):
#     text = text.split()
#     elem = [text[0]]
#     duplicate = []
#     for i in range(1, len(text)):
#         if text[i] == text[i - 1]:
#             elem += text[i]
#         else:
#             duplicate.append(elem)
#             elem = [text[i]]
#     duplicate.append(elem)
#     return duplicate
#
#
# s = input()
# print(duplicates(s))

# My other solution
# s = input().split()
# result = [[]]
# for i in s:
#     if i in result[-1] or len(result[-1]) < 1:
#         result[-1].append(i)
#     else:
#         result.append([i])
# print(result)

# Other solution
# a = input().split()
# l = [[a[0]]]
# for i in a[1:]:
#     if i == l[-1][-1]:
#         l[-1].append(i)
#     else:
#         l.append([i])
# print(l)

'''
Разбиение на чанки 🌶️
На вход программе подаются две строки, на одной символы, отделенные символом пробела, на другой число n.
Из первой строки формируется список.
Реализуйте функцию chunked(), которая принимает на вход список и число, задающее размер чанка (куска),
а возвращает список из чанков указанной длины.
Input:
a b c d e f r g b
2
Output:
[['a', 'b'], ['c', 'd'], ['e', 'f'], ['r', 'g'], ['b']]
'''
# def chunked(string, n):
#     res = []
#     for i in string:
#         if res and len(res[-1]) != n:
#             res[-1].append(i)
#         else:
#             res.append([i])
#     return res
#
#
# string_to_chunk, chunk_size = input().split(), int(input())
# print(chunked(string_to_chunk, chunk_size))

# My other solution
# def chunked(data, size):
#     chunk_list = [[data[0]]]
#     for i in data[1:]:
#         if len(chunk_list[-1]) != size:
#             chunk_list[-1].append(i)
#         else:
#             chunk_list.append([i])
#     return chunk_list
#
#
# s = input().split()
# n = int(input())
# print(chunked(s, n))

# Other solution
# def chunked(symbols, n):
#     result = []
#     for i in range(0, len(symbols), n):
#         result.append(symbols[i:i + n])
#     return result
#
# symbols = input().split()
# n = int(input())
#
# print(chunked(symbols, n))

# Other solution
# во время использования срезов не возникает ошибок, если один из индексов выходит за границы
# def chunked(sp, n):
#     return [sp[x:x + n] for x in range(0, len(sp), n)]
#
#
# s = input().split()
# n = int(input())
# print(chunked(s, n))


'''
Подсписки списка 🌶️🌶️
Подсписок — часть другого списка. Подсписок может содержать один элемент, несколько, и даже ни одного.
Например, [1], [2], [3] и [4] — подсписки списка [1, 2, 3, 4]. Список [2, 3] — подсписок списка [1, 2, 3, 4],
но список [2, 4] не подсписок списка [1, 2, 3, 4], так как элементы 2 и 4 во втором списке не смежные.
Пустой список — подсписок любого списка. Сам список — подсписок самого себя, то есть
список [1, 2, 3, 4] подсписок списка [1, 2, 3, 4].

На вход программе подается строка текста, содержащая символы, отделенные символом пробела. Из данной строки
формируется список. Напишите программу, кот. выводит список, содержащий все возможные подсписки списка, включая пустой список.
Примечание. Порядок списков одинаковой длины должен соответствовать порядку их вхождения в основной список.
Input: a b c d e f
Output: [[], ['a'], ['b'], ['c'], ['d'], ['e'], ['f'], ['a', 'b'], ['b', 'c'], ['c', 'd'], ['d', 'e'], ['e', 'f'], 
['a', 'b', 'c'], ['b', 'c', 'd'], ['c', 'd', 'e'], ['d', 'e', 'f'], ['a', 'b', 'c', 'd'], ['b', 'c', 'd', 'e'], 
['c', 'd', 'e', 'f'], ['a', 'b', 'c', 'd', 'e'], ['b', 'c', 'd', 'e', 'f'], ['a', 'b', 'c', 'd', 'e', 'f']]

Input: a b v
Output: [[], ['a'], ['b'], ['v'], ['a', 'b'], ['b', 'v'], ['a', 'b', 'v']]

Input: 1 2 3 0
Output: 
[[], 
['1'], ['2'], ['3'], ['0'], 
['1', '2'], ['2', '3'], ['3', '0'], 
['1', '2', '3'], ['2', '3', '0'], 
['1', '2', '3', '0']]
'''
# s = input().split()
# len_s = len(s)
# sub_lists = [[]]
#
# for i in range(1, len_s + 1):
#     for j in range(len_s - i):
#         sub_lists.append(s[j:j+i])
#     len_s -= 1
# print(sub_lists)

# Other solution
# s = input().split()
# a = [[]]
# for i in range(1, len(s)+1):
#     for j in range(len(s)):
#         if i == len(s[j:j+i]):
#             a.append(s[j:j+i])
# print(a)


'''
Вывести матрицу 1
На вход программе подаются два натуральных числа n и m, каждое на отдельной строке — количество строк и столбцов
в матрице. Далее вводятся сами элементы матрицы — слова, каждое на отдельной строке (n×m слов);
подряд идут элементы сначала первой строки, затем второй, и т.д.

Программа должна вывести считанную матрицу, разделяя ее элементы одним пробелом.
'''
# n, m = int(input()), int(input())
# matrix = []
# for _ in range(n):
#     elem = [input().split() for _ in range(m)]
#     matrix.append(elem)
#     print(*elem)

# Other solution
# n = int(input())
# m = int(input())
#
# lst = [[input() for _ in range(m)] for _ in range(n)]
# [print(*i) for i in lst]


'''
Вывести матрицу 2
На вход программе подаются два натуральных числа n и m, каждое на отдельной строке — количество строк и столбцов
в матрице. Далее вводятся сами элементы матрицы — слова, каждое на отдельной строке (n×m слов);
подряд идут элементы сначала первой строки, затем второй, и т.д.

Напишите программу, кот. считывает элементы матрицы один за другим, выводит их в виде матрицы, выводит пустую строку,
и снова ту же матрицу, но уже поменяв местами строки со столбцами: первая строка выводится как первый столбец, и тд.
Input:
3
3
1
2
3
4
5
6
7
8
9
Output:
1 2 3
4 5 6
7 8 9

1 4 7
2 5 8
3 6 9
'''
# n, m = int(input()), int(input())
# matrix = [[input() for _ in range(m)] for _ in range(n)]
# [print(*i) for i in matrix]
# print()
# for i in range(m):
#     for j in range(n):
#         print(matrix[j][i], end=' ')
#     print()
# also for-loop can be written this way:
# [print(*[matrix[j][i] for j in range(n)]) for i in range(m)]

'''
След матрицы
Следом квадратной матрицы называется сумма элементов главной диагонали.
Напишите программу, кот. выводит одно число — след заданной матрицы.

На вход программе подаётся натуральное число n — количество строк и столбцов в матрице, затем элементы матрицы (целые
числа) построчно через пробел.
'''
# n, trace = int(input()), 0
# matrix = [list(map(int, input().split())) for _ in range(n)]  # for loop for this generator is below
# or
# matrix = [[*map(int, input().split())] for _ in range(int(input()))]

# for i in range(len(matrix)):
#     trace += matrix[i][i]
# print(trace)

# my other way for trace counting: better use enumerate instead of range(len(some iterable))
# for i, v in enumerate(matrix):
#     trace += v[i]
# print(trace)

# for loop for generator
# for i in range(n):
#     row = list(map(int, input().split()))
#     matrix.append(row)

# Other solution without creating and saving matrix
# res = 0
# for i in range(int(input())):
#     res += int(input().split()[i])
# print(res)

# with sum()
# n = int(input())
# matrix = [input().split() for i in range(n)]
# print(sum([int(matrix[i][i]) for i in range(n)]))

# Other solution with sum()
# print(sum(int(input().split()[j]) for j in range(int(input()))))

'''
Больше среднего
Напишите программу, кот. выводит количество элементов квадратной матрицы в каждой строке, больших среднего
арифметического элементов данной строки.

На вход программе подаётся натуральное число n — количество строк и столбцов в матрице,
затем элементы матрицы (целые числа) построчно через пробел.
Программа должна вывести n чисел — для каждой строки количество элементов матрицы, больших среднего арифметического
элементов данной строки.
Input:
4
1 2 3 4
5 6 3 15
0 2 3 1
5 2 8 5
Output:
2
1
2
1
'''
# matrix = [[*map(int, input().split())] for i in range(int(input()))]
# matrix=[[int(i) for i in input().split()] for _ in range(n)]  # other way to generate matrix
# n = len(matrix)
#
# for i in range(n):
#     count = 0
#     avg = sum(matrix[i]) / n
#     for j in range(n):
#         if matrix[i][j] > avg:
#             count += 1
#     print(count)

# Other solution
# for _ in range(int(input())):
#     lst = list(map(int, input().split()))
#     avg = sum(lst) / len(lst)
#     print(sum(i > avg for i in lst))


# for i, v in enumerate(matrix):
#     count = 0
#     avg = sum(v) / len(v)
#     if v[i] > avg:
#         count += 1
#     print(count)

'''
Максимальный в области 1
На вход программе подаётся натуральное число n — количество строк и столбцов в матрице, затем элементы матрицы (целые
числа) построчно через пробел.
Напишите программу, кот. выводит максимальный элемент в заштрихованной области квадратной матрицы. Элементы главной
диагонали также учитываются. Область, обозначенная х
x----
xx---
xxx--
xxxx-
xxxxx

Input:
3
1 4 5
6 7 8
1 1 6
Output:
7
'''
# n = int(input())
# matrix = [list(map(int, input().split())) for _ in range(n)]
# max_value = matrix[0][0]
#
# for i in range(n):
#     for j in range(n):
#         if i >= j and matrix[i][j] > max_value:
#             max_value = matrix[i][j]
# print(max_value)

# Other solution
# n = int(input())
# matrix = [[int(j) for j in input().split()] for _ in range(n)]
# largest = 0
# for i in range(n):
#     for j in range(i + 1):
#         if matrix[i][j] > largest:
#             largest = matrix[i][j]
# print(largest)

# Other solution
# n = int(input())
# matrix = [list(map(int, input().split())) for i in range(n)]
# a = []
# for i in range(n):
#     a.append(max(matrix[i][:i+1]))
# print(max(a))

# Other solution
# l = []
# for i in range(int(input())):
#     l.extend(list(map(int, input().split()[:i + 1])))
# print(max(l))

'''
Максимальный в области 2 🌶️
Напишите программу, кот. выводит одно число — максимальный элемент в заштрихованной области квадратной матрицы. Элементы
диагоналей также учитываются.
На вход подаётся натуральное число n — количество строк и столбцов в матрице, затем элементы матрицы (целые числа)
построчно через пробел.
x---x
xx-xx
xxxxx
xx-xx
x---x

Input:
3
1 4 5
6 7 8
1 1 6
Output:
8
'''
# n = int(input())
# matrix = [list(map(int, input().split())) for i in range(n)]
# result = []
#
# for i in range(n):
#     for j in range(n):
#         if j <= i <= n - j - 1 or n - j - 1 <= i <= j:
#             result.append(matrix[i][j])
# print(max(result))

'''
Суммы четвертей
Квадратная матрица разбивается на 4 четверти, ограниченные главной и побочной диагоналями: верхнюю, нижнюю, левую и
правую. Напишите программу, кот. вычисляет сумму элементов: верхней четверти; правой; нижней; левой четверти.
Формат входных данных
На вход программе подаётся натуральное число n — количество строк и столбцов в матрице, затем элементы матрицы
(целые числа) построчно через пробел.
Примечание. Элементы диагоналей не учитываются.
Input:
5
1 4 3 4 7
5 6 7 8 4
3 8 5 6 1
1 2 9 4 8
5 6 1 5 8
Output:
Верхняя четверть: 18
Правая четверть: 19
Нижняя четверть: 21
Левая четверть: 17
---
Input
2
99 72
65 11
Output:
Верхняя четверть: 0
Правая четверть: 0
Нижняя четверть: 0
Левая четверть: 0
'''
# n = int(input())
# up, down, left, right = 0, 0, 0, 0
# matrix = [list(map(int, input().split())) for _ in range(n)]
# for i in range(n):
#     for j in range(n):
#         if i < j and i < n - j - 1:
#             up += matrix[i][j]
#         elif i > j and i > n - j - 1:
#             down += matrix[i][j]
#         elif j < i < n - j - 1:
#             left += matrix[i][j]
#         elif n - j - 1 < i < j:
#             right += matrix[i][j]
# print(f'Верхняя четверть: {up}\nПравая четверть: {right}\nНижняя четверть: {down}\nЛевая четверть: {left}')

# Other solution
# n = int(input())
# matrix = [[int(i) for i in input().split()] for _ in range(n)]
# upper, lower, left, right = 0, 0, 0, 0
#
# for i in range(n):
#     upper += sum(matrix[i][i+1:n-i-1])
#     left += sum(matrix[i][:min(i, n-i-1)])
#     right += sum(matrix[i][max(n-i, i+1):])
#     lower += sum(matrix[i][n-i:i])
#
# print(f'Верхняя четверть: {upper}')
# print(f'Правая четверть: {right}')
# print(f'Нижняя четверть: {lower}')
# print(f'Левая четверть: {left}')

'''
Таблица умножения
На вход программе подаются два натуральных числа n и m — количество строк и столбцов в матрице.
Создайте матрицу mult размером n×m и заполните её таблицей умножения по формуле mult[i][j] = i * j.
Программа должна вывести таблицу умножения отводя на вывод каждого числа ровно 3 символа
(для этого используйте строковый метод ljust()).
Input:
4
6
Output:
0  0  0  0  0  0
0  1  2  3  4  5
0  2  4  6  8  10
0  3  6  9  12 15
'''
# n, m = int(input()), int(input())
# matrix = [[(i * j) for j in range(m)] for i in range(n)]
#
# for i in range(n):
#     for j in range(m):
#         print(str(matrix[i][j]).ljust(3), end='')
#     print()

# My other solution
# n, m = int(input()), int(input())
# matrix = [[str(i * j) for j in range(m)] for i in range(n)]
# for i in matrix:
#     for j in i:
#         print(j.ljust(3), end='')
#     print()

# Other solution with f-string
# n, m = int(input()), int(input())
# for i in range(n):
#     for j in range(m):
#         print(f'{i * j:<3}', end="")
#     print()

# Other solution
# n, m = int(input()), int(input())
# [print(*[str(i*j).ljust(3) for j in range(m)]) for i in range(n)]

# Other solution
# n = int(input())
# m = int(input())
# mult = [[str(i * j).ljust(3) for i in range(m)] for j in range(n)]
#
# for line in mult:
#     print(' '.join(line))


'''
0 0 0 0 0 0 0 0 0
0 1 2 3 4 5 6 7 8
0 2 4 6 8 10 12 14 16
0 3 6 9 12 15 18 21 24
0 4 8 12 16 20 24 28 32
0 5 10 15 20 25 30 35 40
0 6 12 18 24 30 36 42 48
0 7 14 21 28 35 42 49 56
0 8 16 24 32 40 48 56 64
'''
# matrix = [[1, 9, 5, 8], [6, 7, 8, 6], [1, 1, 6, 2], [2, 7, 4, 6]]
# n = 4
# list1 = [[1, 7, 8], [9, 7, 102], [6, 106, 105], [100, 99, 98, 103], [1, 2, 3]]
# list2 = []
# for li in list1:
#     list2.append(max(li))
# print(max(list2))

# lst = [[j for j in range(1, i + 1)] for i in range(1, n + 1)]
# lst1 = [[j for j in range(1, n + 1)] for i in range(n)]
# for i in range(1, n + 1):
#     # for j in range(1, i + 1):
#     elem = [j for j in range(1, i + 1)]
#     lst.append(elem)
#     print(elem)
# for i in range(n):
#     lst.append(list(range(1, n + 1)))
# print(*lst, sep='\n')

# Так теж можна
# text = ''.join(i for i in text1 if i.isalpha())

# Так теж можна
# out = [['Верхняя четверть:', 0], ['Правая четверть:', 0], ['Нижняя четверть:', 0], ['Левая четверть:', 0]]
# [print(i, j) for i, j in out]

# matrix = [[1, 9, 5, 8],
#           [6, 7, 8, 6],
#           [1, 1, 6, 2],
#           [2, 7, 4, 6],
#           [0, 3, 4, 9]]

a, b, c, d = int(input()), int(input()), int(input()), int(input())

if d > b:
    payment = c * (d - b) + a
else:
    payment = a

print(payment)