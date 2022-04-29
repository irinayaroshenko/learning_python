# list1 = ["a", "b", "c", "d"]
# list2 = [1, 2, 3, 4, 5]
# print(list1)   # ['a', 'b', 'c', 'd']
# print(*list1)  # a b c d
# print(" ".join(list1))  # a b c d
# print("::".join(list1))  # a::b::c::d
# print(list2)  # [1, 2, 3, 4, 5]

''' Список чисел
На вход программе подается одно число nn. Напишите программу, которая выводит список [1, 2, 3, ..., n]. '''
# print(list(range(1, int(input()) + 1)))

'''
Список букв
На вход программе подается одно число n. Напишите программу, которая выводит список,
состоящий из n букв английского алфавита ['a', 'b', 'c', ...] в нижнем регистре.'''
# n, abc_list = int(input()), list()
# for i in range(97, n + 97):
#     abc_list += chr(i)
# print(abc_list)

# Other solution
# alphabet = list('abcdefghijklmnopqrstuvwxyz')
# print(alphabet[:int(input())])

# Other solution
# n = int(input())
# s = 'abcdefghijklmnopqrstuvwxyz'
# print(list(s[:n]))

# Other solution
# n = int(input())
# s = ''
# for i in range(n):
#     s += chr(97 + i)
# print(list(s))

'''Check if list contains some element'''
# numbers = [2, 4, 6, 8, 10]
# print("Number 2 is {}in numbers.".format("" if 2 in numbers else "not "))
#
# print([1, 2, 3, 4] + [5, [6], [7], 8])
# print([7, 8] * 3)
# print([0] * 10)

# создание списка методом повторояющихся элементов, когда элементы списка сами являются списками
# lst = [[0]]*10
# lst1 = [[0] * 10]*10
# print(lst)
# print(lst1)
# изменение значения одного вложенного элемента списка привело к изменению значения всех вложенных элементов. Очевидно,
# список в этом случае состоит из указателей на один и тот же вложенный список
# lst[0][0] = 4
# print(lst)
# lst1[0][0] = 2
# print(lst1)

# numbers = [12.5, 3.1415, 2.718, 9.8, 1.414, 1.1618, 1.324]
# print(max(numbers) + min(numbers))  # 13.6618
# print(sum([max(numbers), min(numbers)]))  # 13.6618  Here min & max aregiven as list
# print(sum((max(numbers), min(numbers))))  # 13.6618

'''вывести среднее арифметическое элементов списка evens'''
# evens = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
# average = sum(evens) / len(evens)
# print(average)

'''Дополните приведенный код, так чтобы элемент списка имеющий значение Green
заменился на значение Зеленый, а элемент Violet на Фиолетовый. Далее необходимо вывести полученный список.'''
# rainbow = ['Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Violet']
# rainbow[3] = 'Зеленый'
# rainbow[-1] = 'Фиолетовый'
# rainbow[3::3] = ['Зеленый', 'Фиолетовый']  # step 3
'''Two lines below work correctly if they are present in list once but если в списке Green или Violet будет встречаться
более одного раза, то заменит только первое вхождение, последующие не заменятся.'''
# rainbow[rainbow.index('Green')] = 'Зеленый'  # method 'find' can't be used here because it doesn't work with lists (but works with strings)
# rainbow[rainbow.index('Violet')] = 'Фиолетовый'
# print(rainbow)

'''вывести элементы списка languages в обратном порядке'''
# languages = ['Chinese', 'Spanish', 'English', 'Hindi', 'Arabic', 'Bengali', 'Portuguese', 'Russian', 'Japanese',
#              'Lahnda']
# print(languages[::-1])
# print(list(reversed(languages)))
# languages.reverse()
# print(languages)

'''Дополните приведенный код, используя операторы конкатенации (+) и умножения списка на число (*) так,
чтобы он вывел список: [1, 2, 3, 1, 2, 3, 6, 6, 6, 6, 6, 6, 6, 6, 6, 7, 8, 9, 10, 11, 12, 13].'''
# numbers1 = [1, 2, 3]
# numbers2 = [6]
# numbers3 = [7, 8, 9, 10, 11, 12, 13]
# print(numbers1 * 2 + numbers2 * 9 + numbers3)

# num1 = [1, 2, 3]
# num1[1] = 1.5  # можем использовать индексаторы для установки значений элементов списка, если список не пустой
# print(num1)    # [1, 1.5, 3]
# num2 = []
# num2[0] = 1  # мы не можем использовать индексаторы для установки значений элементов списка, если список пустой
# print(num2)  # IndexError: list assignment index out of range

# methods append() and extend()
# numbers = [0, 2, 4, 6, 8, 10]
# odds = [1, 3, 5, 7]
# numbers.extend(odds)
# print(numbers)       # [0, 2, 4, 6, 8, 10, 1, 3, 5, 7]
# numbers.append(odds)
# print(numbers)       # [0, 2, 4, 6, 8, 10, 1, 3, 5, 7, [1, 3, 5, 7]]
#
# words1 = ['iq option', 'stepik', 'beegeek']
# words2 = ['iq option', 'stepik', 'beegeek']
# words1.append('python')   # ['iq option', 'stepik', 'beegeek', 'python']
# words2.extend('python')   # ['iq option', 'stepik', 'beegeek', 'p', 'y', 't', 'h', 'o', 'n']
# print(words1)
# print(words2)

'''
Все сразу 1 🌶️
Дополните приведенный код, чтобы он:

Вывел длину списка;
Вывел последний элемент списка;
Вывел список в обратном порядке (вспоминаем срезы);
Вывел YES если список содержит числа 5 и 17, и NO в противном случае;
Вывел список с удаленным первым и последним элементами.
Примечание. Каждый вывод осуществлять с новой строки.'''
# numbers = [2, 6, 3, 14, 10, 4, 11, 16, 12, 5, 4, 16, 1, 0, 8, 16, 10, 10, 8, 5, 1, 11, 10, 10, 12, 0, 0, 6, 14, 8, 2,
#            12, 14, 5, 6, 12, 1, 2, 10, 14, 9, 1, 15, 1, 2, 14, 16, 6, 7, 5]
# print(len(numbers))
# print(numbers[-1])
# print(numbers[::-1])
# if 5 in numbers and 17 in numbers:
#     print("YES")
# else:
#     print("NO")
# print(numbers[1:-1])

'''
Список строк
На вход программе подается натуральное число n, а затем n строк. Напишите программу, кот. создает из указанных строк
список и выводит его.'''
# n, list_of_strings = int(input()), []
# for i in range(n):
#     # s = input()
#     list_of_strings.append(input())
# print(list_of_strings)

# Other solution. It calls 'list comprehension'
# print([input() for _ in range(int(input()))])

'''
Алфавит
Напишите программу, выводящую следующий список:
['a', 'bb', 'ccc', 'dddd', 'eeeee', 'ffffff', ...]
Примечание. Последний элемент списка состоит из 26 символов z.'''
# abc = []
# for i in range(26):
#     # char = chr(97 + i) * (1 + i)
#     # abc.append(char)
#     abc.append(chr(97 + i) * (1 + i))
# print(abc)

'''
Список кубов
На вход программе подается натуральное число n, а затем n целых чисел. Напишите программу, кот. создает из указанных
чисел список их кубов.'''
# cub_list = list()
# for _ in range(int(input())):
#     number = int(input())
#     cub_list.append(number ** 3)
# print(cub_list)

# Other solution
# print([int(input()) ** 3 for i in range(int(input()))])

'''
Список делителей
На вход программе подается натуральное число n.
Напишите программу, кот. создает список состоящий из делителей введенного числа.'''
# n = int(input())
# lst = list()
# for i in range(1, n + 1):
#     if n % i == 0:
#         lst.append(i)
# print(lst)

# Other solution
# n = int(input())
# divisors = []
# Проходим только до половины числа, т к число не может делиться без остатка на большее, чем половина себя.
# После цикла просто добавляем в конец списка само число и выводим
# for i in range(1, n // 2 + 1):
#     if not n % i:  # the same as n % 1 == 0 because False
#         divisors.append(i)
# divisors.append(n)
# print(divisors)

# Other solution
# n = int(input())
# x = [1]
# for i in range(2, n+1):
#     if n % i == 0:
#         x.append(i)
# print(x)

'''
Суммы двух
На вход программе подается натуральное число n≥2, а затем n целых чисел.
Напишите программу, кот. создает из указанных чисел список, состоящий из сумм соседн. чисел (0 и 1, 1 и 2, 2 и 3 и т.д.).'''
# n = int(input())
# number1, lst1 = int(input()), []
# for _ in range(n - 1):
#     number2 = int(input())
#     lst1.append(number1 + number2)
#     number1 = number2
# print(lst1)

'''
Удалите нечетные индексы
На вход программе подается натуральное число n, а затем n целых чисел.
Напишите программу, кот. создает из указанных чисел список, затем удаляет все элементы стоящие по нечетным индексам,
а затем выводит полученный список.
Примечание. Используйте оператор del.'''
# n, lst = int(input()), list()
# for _ in range(n):
#     number = int(input())
#     lst.append(number)
# del lst[1::2]
# print(lst)

'''
k-ая буква слова 🌶️🌶️
На вход программе подается натуральное число n и n строк, а затем число k – номер буквы (нумерация начинается с единицы).
Напишите программу, кот. выводит k-ую букву из введенных строк на одной строке без пробелов.
Примечание. Если некоторые строки слишком короткие, и в них нет символа с заданным номером, то такие строки при выводе
нужно игнорировать.'''
# lst = []
# for _ in range(int(input())):
#     lst.append(input())
# k = int(input())
# for i in lst:
#     if len(i) >= k:
#         print(i[k - 1], end="")

# Other solution
# n = int(input())
# list1 = []
# for _ in range(n):
#     list1.append(input())
# k = int(input())
# for i in range(n):
#     element = list1[i]
#     print(element[k-1:k], end='')  # При использовании среза lst[i][k-1:k] избавляемся от необходимости проверки условия
# при обращении к символу строки по индексу, если индекс >= длины строки, то возникает ошибка
# "IndexError: string index out of range".
# На основаниие пункта 9.2 курса "Примечание 2. Если первый параметр среза больше второго, то срез создает пустую
# строку", в случае использования среза, ошибки обращения по индексу нет, то есть срез либо вернет подстроку из
# исходной строки, либо пустую строку, если с индексами не повезло

'''
Символы всех строк
На вход программе подается натуральное число n, а затем n строк. Напишите программу, кот. создает список
из символов всех строк, а затем выводит его.'''
# lst = list()
# for _ in range(int(input())):
#     lst.extend(input())
# print(lst)  # ['s', 'g', 'f', 's', 'g', 'd']
# print(*lst)  # s g f s g d

# shopping_list = ['apples', 'pens', 'oatmeal cookies', 'notepad', 'brushes', 'paint', 'appled', 'penk']
# print(max(shopping_list))
# print(min(shopping_list))

'''
Вывод элементов списка с помощью распаковки'''
# numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(*numbers)
'''Вывод элементов списка, каждого на отдельной строке'''
# numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(*numbers, sep='\n')   # 'sep=' not 'end='
'''
Поскольку строки содержат символы, подобно тому, как списки содержат элементы, то мы можем использовать
распаковку строк точно так же, как и распаковку списков. '''
# s = 'Python'
# print(*s)
# print()
# print(*s, sep='\n')

'''
Дополните приведенный код так, чтобы он вывел сумму квадратов элементов списка numbers.'''
# numbers = [1, 78, 23, -65, 99, 9089, 34, -32, 0, -67, 1, 11, 111]
# summ = 0
# lst_square = []
# for i in range(len(numbers)):
#     square = numbers[i] ** 2
#     summ += square
# print(summ)
# or
# for num in numbers:
#     lst_square.append(num ** 2)
# print(sum(lst_square))

# Other solution
# numbers = [1, 78, 23, -65, 99, 9089, 34, -32, 0, -67, 1, 11, 111]
# print(sum([i**2 for i in numbers]))

'''
Значение функции
На вход программе подается натуральное число n, а затем n целых чисел. Напишите программу, кот. для каждого
введенного числа x выводит значение функции f(x) = x**2 + 2x + 1, каждое на отдельной строке.
Программа должна вывести сначала введенные числа, затем пустую строку, а затем соответствующие значения функции.
Примечание. Для первого теста имеем:
f(1) = 1**2 + 2 * 1 + 1 = 4, f(2) = 2**2 + 2 * 2 + 1 = 9, f(3) = 3**2 + 2 * 3 + 1 = 16'''
# n = int(input())
# list1, list2 = [], []
# for _ in range(n):
#     list1.append(int(input()))
# for digit in list1:
#     x = digit ** 2 + 2 * digit + 1  # mathimatically this formula is the same as (x + 1) ** 2
#     list2.append(x)
# print(*list1, sep="\n")
# print()
# print(*list2, sep="\n")
# print(*list1, '', *list2, sep='\n')  # other print version

'''
Remove outliers
При анализе данных, собранных в рамках научного эксперимента, бывает полезно удалить самое большое и самое
маленькое значение.
На вход программе подается натуральное число n, а затем n различных натуральных чисел. Напишите программу, кот.
удаляет наименьшее и наибольшее значение из указанных чисел, а затем выводит оставшиеся числа каждое на отдельной
строке, не меняя их порядок.'''
# n = int(input())
# lst = list()
# for _ in range(n):
#     lst.append(int(input()))
# lst.remove(max(lst))  # via remove
# lst.remove(min(lst))
# del lst[lst.index(max(lst))]  # via del
# del lst[lst.index(min(lst))]
# print(*lst, sep="\n")

'''
Без дубликатов
На вход программе подается натуральное число n, а затем n строк. Напишите программу, кот. выводит только уникальные
строки, в том же порядке, в котором они были введены.
Примечание. Считайте, что все строки состоят из строчных символов.'''
# n = int(input())
# lst = []
# for _ in range(n):
#     k = input()
#     if k not in lst:
#         lst.append(k)
# print(*lst, sep='\n')

'''
Google search - 1
На вход программе подается натуральное число n, затем n строк, затем еще одна строка — поисковый запрос.
Напишите программу, кот. выводит все введенные строки, в которых встречается поисковый запрос.
Примечание. Поиск не должен быть чувствителен к регистру символов.'''
# lst = []
# for _ in range(int(input())):
#     lst.append(input())
# search = input().lower()
# for i in range(len(lst)):
#     if search in lst[i].lower():
#         print(lst[i])

# Other solution
# base = [input() for _ in range(int(input()))]
# search = input().casefold()
# for text in base:
#     if search in text.casefold():
#         print(text)

'''методы casefold and lower вернут разное, при определённых обстоятельствах: например, это важно при нормализации
текста с редкими/уникальными символами из многих письменных языков (а если бы мы пользовались только ASCII, то нам бы
было без разницы какой метод использовать), т.е. почти всегда. Попробуй запустить следующий код:'''
# some_string = "Fluß"
# print(some_string.lower())
# print(some_string.casefold())

'''
Google search - 2 🌶️🌶️
На вход программе подается натуральное число n, затем n строк, затем число k — количество поисковых запросов,
затем k строк — поисковые запросы.
Напишите программу, кот. выводит все введенные строки, в которых встречаются все поисковые запросы.
Примечание. Поиск не должен быть чувствителен к регистру символов.'''

# lst1, search_lst = [], []
# lst2 = []
# for _ in range(int(input())):
#     lst1.append(input())
# for _ in range(int(input())):
#     search_lst.append(input().lower())
#
# for i in range(len(lst1)):
#     if search_lst[0] in lst1[i].lower():
#         lst2.append(lst1[i])
#
# for j in range(1, len(search_lst) + 1):
#     for k in range(len(lst2)):
#         if search_lst[j] not in lst2[k].lower():
#             del lst2[k]      # You can't do this way cause deleted element shifts the list and we get error
# print(lst2)

# My solution
# lst1, search_lst, lst2 = [], [], []
#
# for _ in range(int(input())):
#     lst1.append(input())
# for _ in range(int(input())):
#     search_lst.append(input().lower())
#
# for i in range(len(lst1)):
#     present_in_lst1 = True
#     for j in range(len(search_lst)):
#         if search_lst[j] not in lst1[i].lower():
#             present_in_lst1 = False
#             break
#     if present_in_lst1:
#         lst2.append(lst1[i])
# print(*lst2, sep="\n")

# Other solution
# s = [input() for _ in range(int(input()))]
# d = [input() for _ in range(int(input()))]
# for i in s:
#     for j in d:
#         if j.lower() not in i.lower():
#             break
#     else:
#         print(i)

'''
Negatives, Zeros and Positives
На вход программе подается натуральное число nn, а затем nn целых чисел. Напишите программу, которая сначала выводит
все отрицательные числа, затем нули, а затем все положительные числа, каждое на отдельной строке.
Числа должны быть выведены в том же порядке, в котором они были введены.'''
# list_evens, list_odds, list_zero = [], [], []
# for i in range(int(input())):
#     x = int(input())
#     if x < 0:
#         list_odds.append(x)
#     elif x == 0:
#         list_zero.append(x)
#     else:
#         list_evens.append(x)
# print(*list_odds, *list_zero, *list_evens, sep="\n")

# s = 'Python is the most powerful language'
# words = s.split()
# print(words)
#
# numbers = input().split()  # 12 334 5465 7 53 2 2 4 5 56
# print(numbers)             # ['12', '334', '5465', '7', '53', '2', '2', '4', '5', '56'] list of strings, not int
#
# for i in range(len(numbers)):
#     numbers[i] = int(numbers[i])
# print(numbers)            # [12, 334, 5465, 7, 53, 2, 2, 4, 5, 56] now we transform strings to int

# ip = '192.168.1.24'
# numbers_ip = ip.split('.')    # указываем явно разделитель
# print(numbers_ip)             # ['192', '168', '1', '24']
#
# words = ['Python', 'is', 'the', 'most', 'powerful', 'language']
# print(''.join(words))
# print('*'.join(words))
# print('-'.join(words))
# print('?'.join(words))
# print('!'.join(words))
# print('*****'.join(words))
# print('abc'.join(words))
# print('123'.join(words))

'''
Существует большая разница между результатами вызова методов s.split() и s.split(' ').
Разница в поведении проявляется, когда строка содержит несколько пробелов между словами.'''
# s = 'Python    is   the  most  powerful  language'
# words1 = s.split()
# words2 = s.split(' ', maxsplit=4)
# words3 = s.split(' ')
# print(words1)
# print(words2)
# print(words3)

'''Methods work only with strings, not with int'''
# print([1, 2].split()) # AttributeError: 'list' object has no attribute 'join'
# print([1, 2].join([3, 4, 5])) # AttributeError: 'list' object has no attribute 'join'

# print(['abc', '1234'].split())   # AttributeError: 'list' object has no attribute 'split'
# print([1, 2].join([3, 4, 5]))    # AttributeError: 'list' object has no attribute 'join'

# s = 'BEEGEEK'
# chars = list(s)
# print(chars)  # ['B', 'E', 'E', 'G', 'E', 'E', 'K']
# s = '**'.join(chars)
# print(s)      # B**E**E**G**E**E**K

'''
Построчный вывод
На вход программе подается строка текста. Напишите программу, которая выводит слова введенной строки в столбик.'''
# s = input().split()
# print('\n'.join(s))

# Other solution
# s = input().split()
# print(*s, sep="\n")

# Other solution
# print('\n'.join(input().split()))

'''
Инициалы
На вход программе подается строка текста, содержащая имя, отчество и фамилию человека. Напишите программу, кот.
выводит инициалы человека.'''
# words = input().split()
# print(words[0][0], words[1][0], words[2][0], sep='.', end='.')
# # or with for-loop
# for letter in words:
#     print(letter[0], end='.')
#
# # Other solution
# name = input().split()
# print(f'{name[0][0]}.{name[1][0]}.{name[2][0]}.')
#
# # Other solution
# [print(s[0], end='.') for s in input().split()]

'''
Windows OS
В операционной системе Windows полное имя файла состоит из буквы диска, после которого ставится двоеточие и
символ  "\",  затем через такой же символ перечисляются подкаталоги (папки), в которых находится файл,
в конце пишется имя файла (C:\Windows\System32\calc.exe).
На вход программе подается одна строка с корректным именем файла в операционной системе Windows.
Напишите программу, кот. разбирает строку на части, разделенные символом "\". Каждую часть вывести в отдельной строке.'''
# s = input()
# print('\n'.join(s.split('\\')))
# # or
# print('\n'.join(input().split('\\')))
#
# # Other solution
# print(input().replace('\\', '\n'))
#
# # Other solution
# print(*(input().split(chr(92))), sep='\n')

'''
Корректный ip-адрес
На вход программе подается строка текста, содержащая 4 целых числа разделенных точкой.
Напишите программу, кот. определяет является ли введенная строка текста корректным ip-адресом.
Программа должна вывести «ДА», если введеная строка является корректным ip-адресом, и «НЕТ» — в противном случае.
Примечание. ip-адрес является корректным, если все 4 числа находятся в диапазоне от 0 до 255 включительно.
'''
# ip_list = input().split(".")
# for i in ip_list:
#     if int(i) > 255 or int(i) < 0:
#         print("НЕТ")
#         break
# else:
#     print("ДА")

# Other solution
# ip = input().split('.')
# for i in ip:
#     if int(i) not in range(0, 256):
#         print('НЕТ')
#         break
# else:
#     print('ДА')

'''
Добавь разделитель
На вход программе подается строка текста и строка разделитель.
Напишите программу, кот. вставляет указанный разделитель между каждым символом введенной строки текста.
'''
# This solution ok except divider in the end
# text, divider = input(), input()
# for i in text:
#     print(i, divider, sep="", end="")

# text, divider = input(), input()
# text_list = list()
# for i in text:
#     text_list.extend(i)
# print(divider.join(text_list)) or # print(*text_list, sep=divider)

# Other solution
# Функцию join() можно использовать, чтобы разбить строку по определенному разделителю.
# Если передать в качестве аргумента функции строку, то она будет разбита по символам с определенным разделителем.
# text, divider = input(), input()
# print(divider.join(text))

# Other solution
# print(*input(), sep=input())

'''
Количество совпадающих пар
На вход программе подается строка текста, содержащая натуральные числа. Из данной строки формируется список чисел.
Напишите программу, кот. подсчитывает, сколько в полученном списке пар элементов, равных друг другу.
Считается, что любые два элемента, равные друг другу образуют одну пару, которую необходимо посчитать.
'''
# nums = input().split()
# counter = 0
#
# for i in range(len(nums)):
#     for j in range(i + 1, len(nums)):
#         if nums[i] == nums[j]:
#             counter += 1
# print(counter)

# Other solution
'''
берем элемент из списка. Считаем, сколько искомых пар можно составить с этим элементом. Встать с ним в пару может
только число, равное ему. Количество таких чисел считаем при помощи метода count. Но при подсчете учитывается
наш первый элемент пары: встать в пару сам с собой он не может, поэтому вычитаем единицу.
Повторяем подсчет для всех элементов списка.
В конце учитываем, что каждая пара посчитана нами дважды.
'''
# nums = input().split()
# equal_pairs = 0
# for num in nums:
#     equal_pairs += nums.count(num) - 1
# print(equal_pairs // 2)

# for i in nums:
#     digits.append(int(i))
# print(digits)
# for j in digits:
#     print(digits.count(j) // 2)

'''
Все сразу 2 🌶️
Дополните приведенный код, чтобы он:
numbers = [8, 9, 10, 11]
Заменил второй элемент списка на 17;
Добавил числа 4, 5 и 6 в конец списка;
Удалил первый элемент списка;
Удвоил список;
Вставил число 25 по индексу 3;
Вывел список, с помощью функции print()
'''
# numbers = [8, 9, 10, 11]
# numbers[1] = 17
# numbers.extend([4, 5, 6])
# numbers.pop(0)
# numbers *= 2
# numbers.insert(3, 25)
# print(numbers)

'''
del удаляет, рор вырезает. Поп надо использовать, если это значение надо куда-то возвращять.
pop() вырезает если вы зададите это выражение переменной. x =[1,2,3] y = x.pop(0) print(y) >>>1 Это полезно в задачах,
где надо вырезать значение по индексу и вставить его в другое место. А если не задавать значение переменной,
то я думаю разницы с del нет.
'''

'''
Переставить min и max
На вход программе подается строка текста, содержащая различные натуральные числа, разделенные символом пробела.
Из данной строки формируется список чисел. Напишите программу, которая меняет местами минимальный и максимальный
элемент этого списка.
Примечание. Используйте подходящие встроенные функции и списочные методы.
'''
# numbers = input().split()
# for i in range(len(numbers)):
#     numbers[i] = int(numbers[i])
#
# min_number = min(numbers)
# min_number_index = numbers.index(min_number)
# max_number = max(numbers)
# max_number_index = numbers.index(max_number)
#
# numbers[max_number_index] = min_number
# numbers[min_number_index] = max_number
# print(*numbers)

# Other solution
# s = input().split()
# for i in range(len(s)):
#     s[i] = int(s[i])
# ind_max, ind_min = s.index(max(s)), s.index(min(s))
# s[ind_min], s[ind_max] = s[ind_max], s[ind_min]
# print(*s)

# Other solution
'''
в функции min и max можно подать аргумент key = int для преобразования элементов в натуральные числа:
'''
# s = input().split()
# s_min = min(s, key=int)
# s_max = max(s, key=int)
# i_min = s.index(s_min)
# i_max = s.index(s_max)
# s[i_max] = s_min
# s[i_min] = s_max
# print(*s)

'''
Количество артиклей
На вход программе подается строка, содержащая английский текст. Слова текста разделены символом пробела.
Напишите программу, кот. подсчитывает общее количество артиклей: 'a', 'an', 'the' и выводит вместе с поясняющим текстом.
Примечание. Артикли могут начинаться с заглавной буквы 'A', 'An', 'The'.
Text sample:
William Shakespeare was born in the town of Stratford, England, in the year 1564. When he was a young man, Shakespeare 
moved to the city of London, where he began writing plays. His plays were soon very successful, and were enjoyed both 
by the common people of London and also by the rich and famous. In addition to his plays, Shakespeare wrote many short 
poems and a few longer poems. Like his plays, these poems are still famous today.
'''
# text = input().lower().split()
# a_an_the = text.count('a') + text.count('the') + text.count('an')
# print(f"Общее количество артиклей: {a_an_the}")
# or
# print(f"Общее количество артиклей: {text.count('a') + text.count('the') + text.count('an')}")

'''
Взлом Братства Стали 🌶️
Немалоизвестный в пустошах Мохаве Курьер забрел в Хидден-Вэли – секретный бункер Братства Стали, и любезно соглашается
помочь им в решении их проблем. Одной из такой проблем являлся странный компьютерный вирус, который проявлялся в виде
появления комментариев к программам на терминалах Братства Стали. Известно, что программисты Братства никогда не
оставляют комментарии к коду, и пишут программы на Python, поэтому удаление всех этих комментариев никак не навредит им.
Помогите писцу Ибсену удалить все комментарии из программы.

Формат входных данных
На первой строке вводится символ решётки и сразу же натуральное число n — количество строк в программе, не считая первой.
Далее следует n строк кода.

Формат выходных данных
Нужно вывести те же строки, но удалить комментарии и символы пустого пространства в конце строк.
Пустую строку вместо первой строки ввода выводить не надо.

Sample Input:
#12
print("Введите своё имя")
name = input()
print("Введите пароль, если имеется")    # ахахахах вам не поймать меня
password = input()
if password == "hoover":
    print("Здравствуйте, рыцарь", name)         #долой Макнамару
elif password == "noncr":
    print("Здравствуйте, паладин", name)
elif password == "gelios":
    print("Здравствуйте, старейшина", name)          #Элайджа вперёд
else:
    print("Здравствуйте, послушник", name)

Sample Output:
print("Введите своё имя")
name = input()
print("Введите пароль, если имеется")
password = input()
if password == "hoover":
    print("Здравствуйте, рыцарь", name)
elif password == "noncr":
    print("Здравствуйте, паладин", name)
elif password == "gelios":
    print("Здравствуйте, старейшина", name)
else:
    print("Здравствуйте, послушник", name)
'''
# n = input().split("#")
#
# for _ in range(int(n[1])):
#     s = input()
#     if "#" in s:
#         s = s[:s.index("#")]
#     print(s.rstrip())


'''
Дополните приведенный код, используя списочное выражение, так, чтобы получить список всех чисел палиндромов
от 100 до 1000.
'''
# p_list = [str(i) for i in range(100, 1001)]
# palindromes = [int(i) for i in p_list if i == i[::-1]]
# print(palindromes)

# Other solution
# p = [i for i in range(100, 1001) if str(i) == str(i)[::-1]]
# palindromes = [i for i in range(101, 1001) if i % 10 == i // 100]
# print(p)

'''
Списочное выражение 1
На вход программе подается натуральное число n. Напишите программу, использующую списочное выражение, кот. создает
список содержащий квадраты чисел от 1 до n, а затем выводит его элементы построчно, то есть каждый на отдельной строке.
Примечание. Для вывода элементов списка используйте цикл for.
'''
# lst = [i ** 2 for i in range(1, int(input()) + 1)]
# print(*lst, sep="\n")
# or
# print(*[i ** 2 for i in range(1, int(input()) + 1)], sep='\n')

'''
Списочное выражение 2
На вход программе подается строка текста, содержащая целые числа, разделенные символом пробела.
Напишите программу, использующую списочное выражение, которая выведет кубы указанных чисел также на одной строке.
Примечание 1. Для вывода элементов списка используйте цикл for.
Примечание 2. Используйте метод split().
'''
# print(*[int(i) ** 3 for i in input().split()])

'''
В одну строку 1
На вход программе подается строка текста, содержащая слова, разделенные символом пробела.
Напишите программу, которая выводит слова введенной строки в столбик.
'''
# print(*[i for i in input().split()], sep="\n")
# or
# print(*input().split(),sep='\n')
# or
# print(input().replace(" ","\n"))
# or
# print("\n".join(input().split()))

'''
В одну строку 2
На вход программе подается строка текста.
Напишите программу, использующую списочное выражение, которая выводит все цифровые символы данной строки.
Sample Input 1:
Число Pi примерно равно 3.1415
Sample Output 1:
31415
'''
# print(*(i for i in input() if i.isdigit()), sep="")

'''
В одну строку 3
На вход программе подается строка текста, содержащая целые числа, разделенные символом пробела.
Напишите программу, использующую списочное выражение, которая выведет квадраты четных чисел,
которые не оканчиваются на цифру 4.
'''
# for i in input().split():
#     if (int(i) ** 2) % 10 != 4 and int(i) % 2 == 0:
#         print(int(i) ** 2)

# print(*[(int(i) ** 2) for i in input().split() if (int(i) ** 2) % 10 != 4 and int(i) % 2 == 0])
# or
# это окончания чётных чисел, квадраты которых не оканчиваются на 4.
# Если чётное число оканчивается на 2 или 8, то его квадрат оканчивается на 4
# print(*[int(i) ** 2 for i in input().split() if i[-1] in "046"])

# print(*dir(list()))

# a = [5, 1, 4, 2, 8]
# a = [17, 24, 91, 96, 67, -27, 79, -71, -71, 58, 48, 88, 88, -16, -78, 96, -76, 56, 92, 1, 32, -17, 36, 88, -61, -97,
#      -37, -84, 50, 47, 94, -6, 52, -76, 93, 14, -32, 98, -65, -16, -9, -68, -20, -40, -71, 93, -91, 44, 25, 79, 97, 0,
#      -94, 7, -47, -96, -55, -58, -78, -78, -79, 75, 44, -56, -41, 38, 16, 70, 17, -17, -24, -83, -74, -73, 11, -26, 63,
#      -75, -19, -13, -51, -74, 21, -8, 21, -68, -66, -84, -95, 78, 69, -29, 39, 38, -55, 7, -11, -26, -62, -84]
# n = len(a)
#
# for i in range(n - 1):
#     flag = True
#     for j in range(n - i - 1):
#         if a[j] > a[j + 1]:
#             a[j], a[j + 1] = a[j + 1], a[j]
#             flag = False
#     if flag:
#         break
#
# print(a)


'''
Отсортируйте список по возрастанию, реализовав алгоритм сортировки выбором.
'''
# a = [5, 1, 4, 2, 8, 3]
# n = len(a)
#
# for i in a[:n]:
#     max_val = max(a[:n])
#     max_val_idx = a.index(max_val)
#     a[max_val_idx], a[n-1] = a[n-1], a[max_val_idx]
#     n -= 1
# print(a)

# Other solution
# for i in range(n - 1):
#     i_max = a.index(max(a[:n - i]))
#     a[i_max], a[-i-1] = a[-i-1], a[i_max]
# print(a)


# print(*(letter[0] for letter in input().split()), sep='.', end=".")
# Example Input:
# Владимир Семенович Высоцкий
# Example output:
# В.С.В.


# Insertion sort
# a = [1, 7, -3, 9, 0, -67, 34, 12, 45, 1000, 6,  8, -2, 99]
# n = len(a)
#
# for i in range(1, n):
#     elem = a[i]  # первый элемент из неотсортированной части списка
#     j = i
#     while j >= 1 and a[j - 1] > elem:
#         a[j] = a[j - 1]
#         j -= 1
#     a[j] = elem
#
# print('Отсортированный список:', a)

'''Список четных'''
# На вход программе подается четное число n, n≥2. Напишите программу, кот. выводит список четных чисел
#  [2, 4, 6, ..., n].
# print([i for i in range(2, int(input()) + 1, 2)])

'''
Сумма двух списков
На вход программе подаются две строки текста, содержащие целые числа, разделенные символом пробела.
Из данных строк формируются списки чисел L и M.
Напишите программу, кот. создает третий список, элементами которого являются суммы соответствующих элементов
списков L и M. Далее программа должна вывести каждый элемент полученного списка на одной строке через 1 пробел.
Примечание. Количество чисел в обеих строках одинаковое.
'''
# l, m = input().split(), input().split()
# n = []
# for i in range(len(l)):
#     n.append(int(l[i]) + int(m[i]))
# print(*n)

'''
Сумма чисел
На вход программе подается строка текста, содержащая натуральные числа, разделенные символом пробела.
Напишите программу, кот. вставляет между каждым числом знак +, а затем вычисляет сумму полученных чисел.
Примечание. Строковый метод join() работает только со списком строк.
'''
# lst = input().split()
#
# for i in range(len(lst)):
#     lst[i] = int(lst[i])
# print(*lst, sep='+', end='')
# print(f"={sum(lst)}")

# Other solution
# n = [int(i) for i in input().split()]
# print(*n, sep='+', end='=')
# print(sum(n))

'''
Валидный номер 🌶️🌶️
На вход программе подается строка текста.
Напишите программу, кот. определяет является ли введенная строка корректным телефонным номером.
Строка текста является корректным телефонным номером если она имеет формат:
abc-def-hijk или
7-abc-def-hijk
где a, b, c, d, e, f, h, i, j, k – цифры от 0 до 9.

Программа должна вывести «YES» если строка является корректным телефонным номером и «NO» в противном случае.
Примечание. Телефонный номер должен содержать только цифры и символ -, а количество цифр в каждой группе должны
быть правильным.
'''
# s = input().split('-')
#
# if not ''.join(s).isdigit() or len(s) not in (3, 4):
#     print("NO")
# elif len(s) == 4 and not s[0] == '7':
#     print("NO")
# elif len(s) == 4 and len(s[1]) == 3 and len(s[2]) == 3 and len(s[3]) == 4:
#     print("YES")
# elif len(s) == 3 and len(s[0]) == 3 and len(s[1]) == 3 and len(s[2]) == 4:
#     print("YES")
# else:
#     print("NO")

# Other solution
# s1 = [i for i in input().split('-')]
# s2 = [len(i) for i in s1 if i.isdigit()]
# print('YES' if s2 == [1, 3, 3, 4] and s1[0] == '7' or s2 == [3, 3, 4] else 'NO')

# Other solution
# n = input().split("-")
# c = [len(i) for i in n]
# if c == [3, 3, 4] and ''.join(n).isdigit():
#     print("YES")
# elif c == [1, 3, 3, 4] and ''.join(n).isdigit() and n[0] == '7':
#     print("YES")
# else:
#     print("NO")

# Other solution
# n = input().split('-')
# if n[0] == '7':
#     del n[0]
# if [len(i) for i in n] == [3, 3, 4] and ''.join(n).isdigit():
#     print('YES')
# else:
#     print('NO')

# Other solution
# s = input()
# if s.startswith('7-'):
#     s = s[2:]
# print('YES' if s[3] == '-' and s[7] == '-' and s.replace('-', '').isdigit() and len(s) == 12 else 'NO')

'''
Самый длинный
На вход программе подается строка текста.
Напишите программу, использующую списочное выражение, которая находит длину самого длинного слова.
'''
# s = [len(i) for i in input().split()]
# print(max(s))

# Other solution
# print(max(len(i) for i in input().split()))

'''
Молодежный жаргон
На вход программе подается строка текста.
Напишите программу, использующую списочное выражение, которая преобразует каждое слово введенного текста в
"молодежный жаргон" по следующему правилу: 
первая буква каждого слова удаляется и ставится в конец слова; 
затем в конец слова добавляется слог "ки".
'''

# s = []
# for i in input().split():
#     s.append(i[1:] + i[0] + 'ки')
# print(*s)

# print(*[i[1:] + i[0] + 'ки' for i in input().split()])

# n = int(input())  # Google search - 2
# lst = []
# zap = []
# for i in range(n):
#     lst.append(input())
# k = int(input())
# for j in range(k):
#     zap.append(input())
# for e in range(len(lst)):
#     for p in range(len(zap)):
#         count = 0
#         if zap in lst:
#             count += 1
#             if count == k:
#                 print(lst[e])
#
# print(count)
# print(lst)
# print(zap)


# n = int(input())  # Google search - 2
# lst = []
# zap = []
# for i in range(n):
#     lst.append(input().lower())
# k = int(input())
# for j in range(k):
#     zap.append(input())
# for e in range(len(lst)):
#     for p in range(len(zap)):
#         count = 0
#         if zap[p] in lst[e]:
#             count += 1
#             if count == k:
#                 print(lst[e])
#
# print(count)
# print(lst)
# print(zap)

import random

chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!#$%&*+-=?@^_()'
print(*[random.choice(chars) for _ in range(10)], sep="")
