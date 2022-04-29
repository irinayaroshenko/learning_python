'''
На easy
На вход программе подаются два целых числа a и b (b != 0), каждое на отдельной строке. Напишите программу, которая выводит:

сумму чисел a и b;
разность чисел a и b;
произведение чисел a и b;
частное чисел a и b;
целую часть от деления числа a на b;
остаток от деления числа a на b;
корень квадратный из суммы их 10-х степеней: sqrt{a^{10} + b^{10}}
'''
# a, b = int(input()), int(input())
# print(f'{a + b}\n{a - b}\n{a * b}\n{a / b:.3f}\n{a // b}\n{a % b}\n{(a ** 10 + b ** 10) ** 0.5}')


'''
Индекс массы тела (in eng: BMI (body mass index))
Напишите программу для вычисления и оценки индекса массы тела (ИМТ) человека.
ИМТ показывает весит человек больше или меньше нормы для своего роста. ИМТ человека рассчитывают по формуле:

ИМТ = масса (кг) / рост(м) * рост(м), где масса измеряется в кг, а рост — в м.

Масса человека считается оптимальной, если его ИМТ находится между 18.5 и 25.
Если ИМТ меньше 18.5, то считается, что человек весит ниже нормы.
Если ИМТ больше 25, то считается, что человек весит больше нормы.

Программа должна вывести "Оптимальная масса", если ИМТ находится между 18.5 и 25 (включительно).
"Недостаточная масса", если ИМТ меньше 18.5 и "Избыточная масса", если значение ИМТ больше 25.

Формат входных данных
На вход программе подается два числа: масса и рост человека, каждое на отдельной строке.
Все входные числа являются вещественными, используйте для них тип данных float.
'''
# weight, height = float(input()), float(input())
# index = weight / height ** 2
# if index < 18.5:
#     print('Недостаточная масса')
# elif 18.5 <= index <= 25:
#     print('Оптимальная масса')
# else:
#     print('Избыточная масса')

# for i in range(60, 92):
#     height = 1.81
#     index = i / height ** 2
#     if index < 18.5:
#         print(i, 'кг', 'Недостаточная масса')
#     elif 18.5 <= index <= 25:
#         print(i, 'кг', 'Оптимальная масса')
#     else:
#         print(i, 'кг', 'Избыточная масса')

'''
Стоимость строки
Дана строка текста. Напишите программу для подсчета стоимости строки, исходя из того, что один любой символ
(в том числе пробел) стоит 60 копеек. Ответ дайте в рублях и копейках в соответствии с примерами.
'''
# text = input()
# price = 60 * len(text)
# rub = price // 100
# kop = price % 100
# # print(f'{kop:.2f}')
# print(f'{rub} р. {kop} коп.')


'''
Количество слов
Дана строка, состоящая из слов, разделенных пробелами.
Напишите программу, кот. подсчитывает количество слов в этой строке.
Примечание 1. Кроме слов в тексте могут присутствовать только пробелы (один или несколько).
Примечание 2. Решите задачу в одну строчку кода
'''
# print(len(input().split()))


'''
Зодиак
Китайский гороскоп назначает животным годы в 12-летнем цикле.
Один 12-летний цикл показан в таблице ниже. Таким образом, 2012 год будет очередным годом дракона.

Год	Животное
2000	Дракон
2001	Змея
2002	Лошадь
2003	Овца
2004	Обезьяна
2005	Петух
2006	Собака
2007	Свинья
2008	Крыса
2009	Бык
2010	Тигр
2011	Заяц
Напишите программу, которая считывает год и отображает название связанного с ним животного.
Ваша программа должна корректно работать с любым годом, не только теми, что перечислены в таблице.
'''
# zodiak = ['Обезьяна', 'Петух', 'Собака', 'Свинья', 'Крыса', 'Бык', 'Тигр', 'Заяц', 'Дракон', 'Змея', 'Лошадь', 'Овца']
# year = int(input())
# print(zodiak[year % 12])


'''
Переворот числа
Дано пятизначное или шестизначное натуральное число.
Напишите программу, которая изменит порядок его последних пяти цифр на обратный. Число нужно выводить без незначащих нулей.

Exampes:
560000 -> 500006
25000 -> 52
12345 -> 54321
'''
# num = int(input())
# if len(str(num)) == 6:
#     reverse = ''
#     n = str(num // 100000)
# else:
#     reverse = ''
#     n = ''
# for i in range(5):
#     digit = num % 10
#     reverse += str(digit)
#     num //= 10
# print((n + reverse).lstrip('0'))

# My other solution
# num = int(input())
# digit = str(num // 100000)
# num = str(num)
# if len(num) == 5:
#     print(int(num[::-1]))
# else:
#     print(int(digit + num[-1:-6:-1]))

# Other solution
# s = input()
# print(int(s[:-5] + s[:-6:-1]))

# Other solution
# s = input()
# print(int(s[:-5] + s[-5:][::-1])) # запись s[-5::-1] означает: сделай срез, начиная с -5 элемента по последний двигаясь
# в сторону начала строки. Естественно вы никогда не достигните конца строки двигаясь к началу.
# А s[-5:][::-1] сначала берет срез от -5 по конечный элемент, а уже потом переворачивает результат.

# slices with negative indexing. revert last 10 symbols
# str_exmpl = 'believe%in*beauty&of_dreams'
# str_new = str_exmpl[:-10]  # believe%in*beauty
# revert = str_exmpl[:-11:-1]
# print(str_new, revert)
# print(str_new + revert)

'''
Standard American Convention
На вход программе подаётся натуральное число.
Напишите программу, которая вставляет в заданное число запятые в соответствии со стандартным американским соглашением
о запятых в больших числах. 1000000 -> 1,000,000  12345 -> 12,345  100 -> 100
'''
# n = int(input())
# print(f'{n:,}')

# Other solution
# s = input()
# n = []
#
# while len(s) > 0:
#     n.append(s[-3:])
#     s = s[:-3]
#
# new_n = n[:: -1]
# print(*new_n, sep=',')

# Other solution
# num = input()
# print(len(num))
# for idx in range(len(num) - 3, 0, -3):
#     print(len(num) - 3)
#     num = num[:idx] + ',' + num[idx:]
# print(num)

'''
Задача Иосифа Флавия 🌶️🌶️
n человек, пронумерованных числами от 1 до n, стоят в кругу.
Они начинают считаться, каждый k-й по счету человек выбывает из круга, после чего счет продолжается со следующего
за ним человека. Напишите программу, определяющую номер человека, который останется в кругу последним.

Примечание. Визуализацию работы алгоритма . https://www.youtube.com/watch?v=uCsD3ZGzMgE&t=11s
'''
# n, k = int(input()), int(input())

# from math import log2, ceil, floor
# Solution if k = 2
# def greater_number_pow_of_two(x):
#     if x % 2 != 0:
#         x -= 1
#
#     while ceil(log2(x)) != floor(log2(x)):
#         x -= 2
#     return x
#
#
# x = int(input())
# y = greater_number_pow_of_two(x)
#
# # last_one formula: last_alive = 2 * l + 1
# last_one = (x - y) * 2 + 1
# print(last_one)

# Recursion
# def josefus(n, k):
#     if n == 1:
#         return 1
#     else:
#         survivor = (josefus(n - 1, k) + k - 1) % n + 1
#         return survivor
#
#
# num, step = int(input()), int(input())
# print(josefus(num, step))

# ppl = [i for i in range(1, 51)]
# print(ppl)
# # ppl = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
# k = 2
# i = k
# # length = len(ppl)
# while len(ppl) > 1:
#     print(ppl.pop(i))  # kill prisoner at i
#     i = (i + k) % len(ppl)
# print('Survivor: ', ppl[0])

# n, k = int(input()), int(input())
# lst = [i for i in range(1, n + 1)]
# while len(lst) > 1:
#     for i in range(k - 1):
#         lst.append(lst.pop(0))
#     del lst[0]
# print(*lst)

# Other solution (don't understand how it works)
# n = int(input())
# k = int(input())
#
# res = 0
# for i in range(1, n + 1):
#     res = (res + k) % i
# print(res + 1)

# import time
#
# start = time.time()
# for pen in range(0, 91, 10):
#     for pensil in range(0, 101, 5):
#         for eraser in range(0, 101, 2):
#             if pen + pensil + eraser == 100 and pen // 10 + pensil // 5 + eraser // 2 == 30:
#                 print(f'pen - {int(pen / 10)}, pensil - {int(pensil / 5)}, eraser - {int(eraser / 2)}')
#
# print(time.time() - start)
# pen - 2, pensil - 8, eraser - 20 and pen - 5, pensil - 0, eraser - 25


# Parameters and arguments in functions
# def say(message, times = 4):
#     print(message * times)
# say('Hello', 1)
# say('Bye', 7)

# Tuples and dictionaries as parameters in functions
# def total(a, b=4, *numbers, **phonebook):
#     print(f'a = {a}\tb = {b}')
#
#     for i in numbers:
#         print(f'item from numbers: {i}')
#
#     for first_part, second_part in phonebook.items():
#         print(first_part, second_part)
#
#
# total(17, Jack=1123, John=2231, Inge=1560)
# total(17, 3, Jack=1123, John=2231, Inge=1560)
# total(17, 4, 1, 2, 9, Jack=1123, John=2231, Inge=1560)


'''
Если некоторые ключевые параметры должны быть доступны только по ключу, а не как
позиционные аргументы, их можно объявить после параметра со звёздочкой 
'''
# def total1(initial=5, *numbers, extra_number):
#     count = initial
#     for number in numbers:
#         count += number
#     count += extra_number
#     print(count)
#
#
# total(10, 1, 2, 3, extra_number=50)  # 66
# total(10, 1, 2, 3)   # TypeError: total() needs keyword-only argument extra_number

# Если вам нужны аргументы, передаваемые только по ключу, но не нужен параметр со звёздочкой,
# то можно просто указать одну звёздочку без указания имени: def total(initial=5, *, extra_number).

# Docstrings and how to call it to output
# def doc_example(a, b):
#     """
#     To show docstr use print(func_name.__doc__)
#
#     :param a: some text
#     :param b: other text
#     :return: text concatenation
#     """
#     c = a + b
#     return c
#
#
# print(doc_example.__doc__)
# print(doc_example('abc', 'DEF'))

# Modules. Page 77 in book http://svp.pp.ua/AByteOfPython/AByteofPythonRussian-2.02.pdf
# import sys
# import os
# print('Command line arguments:')
# for i in sys.argv:
#     print(i)
#
# print('\nPYTHONPATH variable contains\n', sys.path)
# print('\n', os.getcwd())   # get current working directory

# n = int(input('Give number greater than 10: '))
# simple_numbers = [2, 3]
# count = 2
# a = 5
#
# while count < n:
#     b = 0
#     for i in range(2, a + 1):
#         if i <= a ** 0.5:
#             if a % i == 0:
#                 print(i, 'is not simple number')
#                 b = 1
#             else:
#                 pass
#     if b != 1:
#         print(a, 'is simple')
#         simple_numbers += [a]
#     count += 1
#     a += 2
# print(simple_numbers)

'''
Координатные четверти
Дан набор точек на координатной плоскости. Необходимо подсчитать и вывести количество точек, лежащих в каждой
координатной четверти.
Формат входных данных
В первой строке записано количество точек. Каждая следующая строка состоит из двух целых чисел — координат точки
(сначала абсцисса – x, затем ордината – y), разделенных символом пробела.
Формат выходных данных
Программа должна вывести количество точек, лежащих в каждой координатной четверти, как в примерах.

Примечание. Учтите, что точки, лежащие на осях координат, не принято относить к какой либо координатной четверти.
Пример:
Input:
10
4 8
-3 -1
-4 9
4 0
-4 0
5 -2
0 0
1 1
13 -3
-43 3
Output:
Первая четверть: 2
Вторая четверть: 2
Третья четверть: 1
Четвертая четверть: 2
'''

# l = []
# all_dots = []
# for _ in range(int(input())):
#     l.extend(input().split())
#
# while len(l) > 0:
#     if int(l[0]) > 0 and int(l[1]) > 0:
#         all_dots.append(1)
#     elif int(l[0]) < 0 < int(l[1]):
#         all_dots.append(2)
#     elif int(l[0]) == 0 or int(l[1]) == 0:
#         pass
#     elif int(l[0]) < 0 and int(l[1]) < 0:
#         all_dots.append(3)
#     else:
#         all_dots.append(4)
#     l = l[2:]
# print(f'''Первая четверть: {all_dots.count(1)}
# Вторая четверть: {all_dots.count(2)}
# Третья четверть: {all_dots.count(3)}
# Четвертая четверть: {all_dots.count(4)}''')

# Other solution
# n = int(input())
# count = [0, 0, 0, 0]
# names = ['Первая четверть:', 'Вторая четверть:',
#          'Третья четверть:', 'Четвертая четверть:']
#
# for _ in range(n):
#     # первый элемент списка присваивается x, второй элемент списка - y
#     x, y = [int(num) for num in input().split()]
#     if x > 0 and y > 0:
#         count[0] += 1
#     elif x < 0 and y > 0:
#         count[1] += 1
#     elif x < 0 and y < 0:
#         count[2] += 1
#     elif x > 0 and y < 0:
#         count[3] += 1
#
# for i in range(4):
#     print(names[i], count[i])

'''
Больше предыдущего
На вход программе подается строка текста из натуральных чисел. Из неё формируется список чисел.
Напишите программу подсчета количества чисел, которые больше предшествующего им в этом списке числа, то есть,
стоят вслед за меньшим числом.
Sample
Input: 1 1 3 2 2 1 1 1 Output: 1
'''
# numbers = [int(num) for num in input().split()]  # or nums = list(map(int, input().split()))
# count = 0
#
# for i in range(len(numbers) - 1):
#     if numbers[i] < numbers[i + 1]:
#         count += 1

# or
# for i in range(1, len(numbers)):
#     if numbers[i] > numbers[i - 1]:
#         count += 1
#
# print(count)

'''
Назад, вперёд и наоборот
На вход программе подается строка текста из натуральных чисел. Из элементов строки формируется список чисел.
Напишите программу, которая меняет местами соседние элементы списка (a[0] c a[1], a[2] c a[3] и т.д.).
Если в списке нечетное количество элементов, то последний остается на своем месте.
Программа должна вывести измененный список, разделяя его элементы одним пробелом.
Sample
1 2 3 4 5 -> 2 1 4 3 5 ; 2 3 2 4 -> 3 2 4 2
'''
# nums = list(map(int, input().split()))
# for i in range(1, len(nums), 2):
#     nums[i - 1], nums[i] = nums[i], nums[i - 1]
# print(*nums)


'''
Сдвиг в развитии
На вход программе подается строка текста из натуральных чисел. Из элементов строки формируется список чисел.
Напишите программу циклического сдвига элементов списка направо, когда последний элемент становится первым, а остальные
сдвигаются на одну позицию вперед, в сторону увеличения индексов.
Программа должна вывести элементы измененного списка с циклическим сдвигом, разделяя его элементы одним пробелом.
Sample
1 2 3 4 5 - > 5 1 2 3 4
'''
# My solution #1
# digits = list(map(int, input().split()))
# digits1 = digits[:-1]
# digits1.insert(0, digits[-1])
# print(*digits1)

# My solution #2
# digits = [i for i in input().split()]
# digits2 = list()
# digits2.append(digits[-1])
# digits2.extend(digits[:-1])
# print(*digits2)

# Other solution !!!
# n = input().split()
# print(n.pop(), *n)
# or
# print(*[n[-1]] + n[:-1])


'''
Различные элементы
На вход программе подается строка текста, содержащая натуральные числа, разделенные символом пробела, расположенные по неубыванию.
Из строки формируется список чисел. Напишите программу для подсчета количества разных элементов в списке.
Программа должна вывести одно число – количество различных элементов списка.
Примечание. Задачу можно решить без множеств.
Sample
2 2 5 5 5 5 8 10 10 -> 4 ; 5 5 5 5 5 555 -> 2
'''
# new_s = list(map(int, input().split()))
# count = 0
# for i in range(len(new_s) - 1):
#     if new_s[i + 1] > new_s[i]:
#         count += 1
# print(count + 1)

# Or with counter = 1
# numbers = input().split()
# counter = 1
#
# for i in range(len(numbers) - 1):
#     if numbers[i] != numbers[i + 1]:
#         counter += 1
#
# print(counter)

# With set (my solution)
# new_s = list(map(int, input().split()))
# list_to_set = set(new_s)
# print(len(list_to_set))

# One line with set (my solution)
# print(len(set(list(map(int, input().split())))))  # or print(len(set(input().split())))

# Other solution
# s = input().split()
# a = []
# for i in s:
#     if i not in a:
#         a.append(i)
# print(len(a))

'''
Произведение чисел
Напишите программу для определения, является ли число произведением двух чисел из данного набора, выводящую результат
в виде ответа «ДА» или «НЕТ».

Формат входных данных
В первой строке подаётся число n (0 < n < 1000) – количество чисел в наборе. В последующих n строках вводятся целые
числа, составляющие набор (могут повторяться). Затем следует целое число, которое является или не является произведением
двух каких-то чисел из набора.

Примечание 1. Само на себя число из набора умножиться не может, другими словами, два множителя должны иметь разные
индексы в наборе.
Примечание 2. Для решения задачи используйте вложенные циклы.
'''
# n = int(input())
# numbers = [int(input()) for i in range(n)]
# multiply_number = int(input())
# is_multiplied = 'НЕТ'
#
# # Bad solution
# for i in range(n):
#     for j in range(n):
#         if i != j:
#             if numbers[i] * numbers[j] == multiply_number:
#                 is_multiplied = 'ДА'
#                 break
# print(is_multiplied)
#
# # Better solution
# for i in range(0, n - 1):
#     for j in range(i + 1, n):
#         if numbers[i] * numbers[j] == multiply_number:
#             is_multiplied = 'ДА'
#             break
# print(is_multiplied)

# Other solution
# numbers, multiply = [int(input()) for i in range(int(input()))], int(input())
# for i in range(len(numbers)-1):
#     for j in range(i+1, len(numbers)):
#         if multiply == numbers[i] * numbers[j]:
#             exit(print("ДА"))
# print("НЕТ")

'''
Камень, ножницы, бумага
Тимур и Руслан пытаются разделить фронт работы по курсу "Python для профессионалов". Для этого они решили сыграть
в камень, ножницы и бумагу. Помогите ребятам бросить честный жребий и определить, кто будет делать очередной модуль
нового курса.

Формат входных данных
На вход программе подаются две строки текста, содержащие слова "камень", "ножницы" или "бумага".
На первой строке записан выбор Тимура, на второй – выбор Руслана.

Формат выходных данных
Программа должна вывести результат жеребьёвки, то есть кто победит Тимур, Руслан или они сыграют вничью.
'''
# options = ('камень', 'ножницы', 'бумага')
# first, second = input(), input()
# if first == second:
#     print('ничья')
# elif (first == options[0] and second == options[1]) or (first == options[1] and second == options[2]) or (first == options[2] and second == options[0]):
#     print('Тимур')
# else:
#     print('Руслан')

# Other solution
# m = ['каменькамень', 'ничья', 'каменьножницы', 'Тимур', 'каменьбумага', 'Руслан',
#      'ножницыножницы', 'ничья', 'ножницыбумага', 'Тимур', 'ножницыкамень', 'Руслан',
#      'бумагабумага', 'ничья', 'бумагакамень', 'Тимур', 'бумаганожницы', 'Руслан']
# s = input() + input()
# answer = m.index(s) + 1
# print(m[answer])

# Pure magic!!!
# x, y = input(), input()
# var = ['камень', 'ножницы', 'бумага']
# ans = ['ничья', 'Руслан', 'Тимур']
# print(ans[var.index(x) - var.index(y)])
# Explanation:
# есть список: "ничья", "Тимур", "Руслан", в нём 3 индекса: 0, 1, 2. Однако индексы можно считать и с противоположной
# стороны, тогда добавятся ещё -1 и -2, итого 5 индексов: -2, -1, 0, 1, 2. Индекс "-3" я не учитываю, т.к. он не
# используется в процессе. Далее, на вводе может быть три разных слова: ножницы (0 букв "а"), камень (1 буква "а"),
# бумага (2 буквы "а"). В зависимости от введённых данных вычисляем разницу кол-ва букв "а" между первым и вторым словом
# и эта разница и будет индексом-ключом для решения задачи. Таким образом, если выпадет два одинаковых слова, то и
# разница количества букв "а" будет равно 0

# Other solution
# tim = input()
# rus = input()
# knb = ['камень', 'ножницы', 'бумага']
# winner = ['ничья', 'Руслан', 'Тимур']
#
# win_index = knb.index(tim) - knb.index(rus)
# print(winner[win_index])

'''
Камень, ножницы, бумага, ящерица, Спок 🌶️
На вход программе подаются две строки текста, содержащие по одному слову из перечня "камень", "ножницы", "бумага",
"ящерица" или "Спок". На первой строке записан выбор Тимура, на второй – выбор Руслана.
Программа должна вывести результат жеребьёвки: кто победил - Тимур или Руслан, или они сыграли вничью.
Камень давит Ящерицу, Камень разбивает Ножницы;
Ножницы режут Бумагу, Ножницы обезглавливают Ящерицу;
Бумага покрывает Камень, Бумага подставляет Спока;
Ящер отравляет Спока, Ящер съедает Бумагу;
Спок ломает Ножницы, Спок испаряет Камень.
'''
# t, r = input(), input()
# timur = (-28, -25, -21, -18, -9, -3, 12, 16, 30, 46)
# if ord(t[0]) - ord(r[0]) in timur:
#     print('Тимур')
# elif t == r:
#     print('ничья')
# else:
#     print('Руслан')

# Other solution
# a, b = input()[0], input()[0]   # !!! Pay attention how input is taken
# print('ничья' if a == b else 'Тимур' if a + b in ('кн', 'бк', 'нб', 'кя', 'яС', 'Сн', 'ня', 'яб', 'бС', 'Ск') else 'Руслан')

# Other solution
# timur, ruslan = input(), input()
# variants = ['ящерица', 'Спок', 'ножницы', 'бумага', 'камень']
# answers = ['ничья', 'Руслан', 'Тимур', 'Руслан', 'Тимур']
# timur, ruslan = variants.index(timur), variants.index(ruslan)
# print(timur, ruslan)
# print(answers[timur-ruslan])


# Other solution
# a, b = input()[0], input()[0]
# print('ничья' if a == b else 'Тимур' if a + b in 'нбкяСнябСкн' else 'Руслан')

'''
Орел и решка
Дана строка текста, состоящая из букв русского алфавита "О" и "Р". Буква "О" – соответствует выпадению Орла, а буква "Р"
– Решки. Напишите программу, которая подсчитывает наибольшее количество подряд выпавших Решек.
Примечание. Если выпавших Решек нет, то необходимо вывести число 0.
Sample: ОРРОРОРООРРРО -> 3
'''
# First
# s = input().split('О')
# s1 = [len(i) for i in s]
# print(max(s1))

# Second
# s = input().split('О')
# print(max([len(i) for i in s]))

# Final
# print(max([len(i) for i in input().split('О')]))

# Better other solution
# print(len(max(input().split('О'))))

# Other solution !! Empty strings are always considered to be a substring of any other string, so "" in "abc" will return True
# res = input()
# tmp = ''
# while tmp in res:
#     tmp += 'Р'
# print(len(tmp) - 1)

# One more interesting solution
# word = input()
# x = 0
# for i in range(1, len(word)+1):
#     if i*'Р' in word:
#         x = i
# print(x)


'''
Кремниевая долина 🌶️🌶️
Искусственный интеллект Антон, созданный Гилфойлом, взломал сеть умных холодильников.
Теперь он использует их в качестве серверов "Пегого дудочника". Помогите владельцу фирмы отыскать все зараженные
холодильники.
Для каждого холодильника существует строка с данными, состоящая из строчных букв и цифр, и если в ней присутствует
слово "anton" (необязательно рядом стоящие буквы, главное наличие последовательности букв), то холодильник заражен и
нужно вывести номер холодильника, нумерация начинается с единицы

Формат входных данных
В первой строке подаётся число n – количество холодильников. В последующих n строках вводятся строки,
содержащие латинские строчные буквы и цифры, в каждой строке от 5 до 100 символов.

Формат выходных данных
Программа должна вывести номера зараженных холодильников через пробел. Если таких холодильников нет, ничего выводить не нужно.
Sample:
6
222anton456
a1n1t1o1n1
0000a0000n00t00000o000000n
gylfole
richard
ant0n

1 2 3
'''
# result_list = [input() for _ in range(int(input()))]
# final = []
#
# for i in range(len(result_list)):
#     if result_list[i].find('a') != -1:
#         result_list[i] = result_list[i][result_list[i].find('a') + 1:]
#         if result_list[i].find('n') != -1:
#             result_list[i] = result_list[i][result_list[i].find('n') + 1:]
#             if result_list[i].find('t') != -1:
#                 result_list[i] = result_list[i][result_list[i].find('t') + 1:]
#                 if result_list[i].find('o') != -1:
#                     result_list[i] = result_list[i][result_list[i].find('o') + 1:]
#                     if result_list[i].find('n') != -1:
#                         final.append(i + 1)
# print(*final)

# Solution with regex - long version
# import re
# pattern = re.compile(r'a\w*n\w*t\w*o\w*n\w*')
# final = []
# for i in range(int(input())):
#     el = input()
#     result = re.findall(pattern, el)
#     if result:
#         final.append(i + 1)
# print(*final)

# Shorter version
# import re
# pattern = re.compile(r'a\w*n\w*t\w*o\w*n\w*')
# final = []
# for i in range(int(input())):
#     if re.findall(pattern, input()):
#         final.append(i + 1)
# print(*final)

# Other solution
# for i in range(int(input())):
#     s, virus, x = input(), 'anton', 0
#     for sym in s:
#         if sym == virus[x]:
#             x += 1
#             if x == 5:
#                 print(i + 1, end=' ')
#                 break


# result = re.match(r'AV', 'AV Analytics Vidhya AV')
# print(result)
# print(result.group(0))
#
# result_search = re.search(r'Analytics', 'AV Analytics Vidhya AV')
# print(result_search)
# print(result_search.group(0))
#
# res_findall = re.findall(r'AV', 'AV Analytics Vidhya AV')
# print(res_findall)


'''
Роскомнадзор запретил букву а 🌶️🌶️
Необходимо написать программу, реализующую алгоритм написания этой песни https://www.youtube.com/watch?v=sAuMERnj-FU .
Алгоритм выводит в конце предложения следующую в алфавитном порядке букву, если она встречается в строке текста,
а очередную строку отображает уже без этой буквы.

Формат входных данных
На вход программе подается одно слово, записанное строчными русскими буквами без буквы "ё".
Формат выходных данных
Программа должна вывести в соответствии с указанным алгоритмом строки, количество которых равно количеству разных букв
в строке, которая получается путем конкатенации введенного слова и строки "запретил букву".
Sample Input 1:
роскомнадзор
Sample Output 1:
роскомнадзор запретил букву а
роскомндзор зпретил букву б
роскомндзор зпретил укву в
роскомндзор зпретил уку д
роскомнзор зпретил уку е
роскомнзор зпртил уку з
роскомнор пртил уку и
роскомнор пртл уку к
росомнор пртл уу л
росомнор прт уу м
росонор прт уу н
росоор прт уу о
рср прт уу п
рср рт уу р
с т уу с
т уу т
уу у
# abc = [chr(i + 1072) for i in range(32)] or alpha = [chr(i) for i in range(1072, 1104)]
'''
# phrase = input() + ' запретил букву'
# abc = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
#
# for i in range(len(abc)):  # possible if i in abc:
#     if abc[i] in phrase:
#         print(phrase, abc[i])
#         phrase = phrase.replace(abc[i], '').replace('  ', ' ').strip()




# s = 'Testing PRI/Sec (#434242332;PP:432:133423846,335)'
# s1 = 'Testing PRI/Sec (#434242332;PP:432:133423846,335)'.replace('#', '-').replace(':', '-').replace(';', '-').replace('/', '-')
# print(s1)


# Decimal to binary
# n = int(input())
# b = ''
# while n > 0:
#     b = str(n % 2) + b
#     n = n // 2
# if len(b) < 8:
#     b = ((8 - len(b)) * '0') + b
# print(b)
# or
# for _ in range(8):
#     b = str(n % 2) + b
#     n //= 2
# print(b)

# Cesarus Code with map function
# def rotate_chr(c):
#     rot_by = 3
#     c = c.lower()
#     alphabet = "abcdefghijklmnopqrstuvwxyz"
#
#     if c not in alphabet:
#         return c
#     rotated_pos = ord(c) + rot_by
#
#     if rotated_pos <= ord(alphabet[-1]):
#         return chr(rotated_pos)
#
#     return chr(rotated_pos - len(alphabet))
#
#
# print("".join(map(rotate_chr, "My secret message goes here.")))

# List comprehension with if-else
# y = [print(0) if int(input()) % 2 == 0 else print(1)]


