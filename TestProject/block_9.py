'''import emoji
print(emoji.emojize("Python is :thumbs_up:"))'''

# Ещё для получения индекса можно использовать enumerate()
# name = 'Python'
# for index, char in enumerate(name):
#     print(index, '=', char)

# s = '01234567891011121314151617'
# for i in range(0, len(s), 5):
#     print(s[i], end='')   # 051217

# s = '01234567891011121314151617'
# for index, char in enumerate(s):
#     print(index, '=', char)

# В столбик 1
# На вход программе подается одна строка. Напишите программу, кот. выводит элементы строки с индексами 0, 2, 4, ... в столбик.
# string = input()
# for i in range(0, len(string), 2):
#     print(string[i])

# Other solution
# a = input()
# for i in a[::2]:
#     print(i)

# В столбик 2
# На вход программе подается одна строка. Напишите программу, кот. выводит в столбик элементы строки в обратном порядке.
# s = input()
# for i in range(1, len(s) + 1):
#     print(s[-i])

# Other solution
# s = input()
# for i in reversed(s):
#     print(i)

# Other solution
# n = input()
# for i in n[::-1]:
#     print(i)

# ФИО
# На вход программе подаются три строки: имя, фамилия и отчество. Напишите программу, кот. выводит инициалы (ФИО).
# i, f, o = input(), input(), input()
# print(f[0], i[0], o[0], sep="")

# Other solution
# a, b, c = input()[0], input()[0], input()[0]
# print(b, a, c, sep="")

# Цифра 1
# На вход программе подается одна строка состоящая из цифр. Напишите программу, кот. считает сумму цифр данной строки.
# My solution 1
# string, summ = input(), 0
# numbers = int(string)
# while numbers != 0:
#     summ += numbers % 10
#     numbers //= 10
# print(summ)

# My solution 2
# string, summ = input(), 0
# for i in range(len(string)):
#     summ += int(string[i])
# print(summ)

# Other solution
# Строка уже сама по себе - массив символов. Значит, мы можем делать for сразу по строке, получая в цикле символы.
# a = input()
# s = 0
# for i in a:
#     s += int(i)
# print(s)

# Цифра 2
# На вход программе подается одна строка.
# Напишите программу, кот. выводит сообщение «Цифра» (без кавычек), если строка содержит цифру.
# В противном случае вывести сообщение «Цифр нет» (без кавычек).

# string = input()
# for i in range(len(string)):
#     if string[i] in "0123456789":
#         print("Цифра")
#         break
# else:
#     print("Цифр нет")

# Other solution
# s = input()
# n = 'Цифр нет'
# for i in s:
#     if i in '0123456789':
#         n = 'Цифра'
#         break
# print(n)

# Other solution
# for c in input():
#     if '0' <= c <= '9':
#         print('Цифра')
#         break
# else:
#     print('Цифр нет')

# Сколько раз?
# На вход программе подается одна строка. Напишите программу, кот. определяет сколько раз в строке
# встречаются символы + и *.

# count_plus, count_asterisk = 0, 0
# for char in input():
#     if char == "+":
#         count_plus += 1
#     if char == "*":
#         count_asterisk += 1
# print(f"Символ + встречается {count_plus} раз")
# print(f"Символ * встречается {count_asterisk} раз")

# Other solution
# s = input()
# print(f"Символ + встречается {s.count('+')} раз")
# print(f"Символ * встречается {s.count('*')} раз")

# Other solution
# n = input()
# for i in ['+', '*']:
#     print(f'Символ {i} встречается {n.count(i)} раз')

# Одинаковые соседи
# На вход программе подается одна строка. Напишите программу, кот. определяет сколько в ней одинаковых соседних символов
# В задании требуется определить сколько раз левый символ строки s равен правому соседнему
# s, count = input(), 0
# for i in range(len(s) - 1):
#     if s[i] == s[i + 1]:
#         count += 1
# print(count)

# The same but counting from the end of string
# s = input()
# f = 0
# for i in range(1, len(s)):
#     if s[i-1] == s[i]:
#         f += 1
# print(f)

# Other solution
# == это логический оператор, условие (s[ i ]== s[ i+1]) либо верно либо неверно.
# оно может вернуть 0 или 1. соответственно, здесь счетчик увеличиться на единицу только от верного варианта
# s, count = input(), 0
# for i in range(1, len(s)):
#     count += s[i] == s[i-1]
# print(count)

# Гласные и согласные
# На вход программе подается одна строка с буквами русского языка.
# Напишите программу, которая определяет количество гласных и согласных букв.
# Примечание. В русском языке 10 гласных букв (а, у, о, ы, и, э, я, ю, ё, е)
# и 21 согласная буква (б, в, г, д, ж, з, й, к, л, м, н, п, р, с, т, ф, х, ц, ч, ш, щ).
# s = input()
# vowels, consonants = 0, 0
# for i in s.lower():
#     if i in "ауоыиэяюёе":
#         vowels += 1
#     elif i in "бвгджзйклмнпрстфхцчшщ":
#         consonants += 1
# print(f"Количество гласных букв равно {vowels}")
# print(f"Количество согласных букв равно {consonants}")

# Other but not better solution
# s = input()
# son, cons = 0, 0
# for c in s:
#     if c in ('ауоыиэяюёеАУОЫИЭЯЮЁЕ'):
#         son += 1
#     if c in ('бвгджзйклмнпрстфхцчшщБВГДЖЗЙКЛМНПРСТФХЦЧШЩ'):
#         cons += 1
# print('Количество гласных букв равно', son)
# print('Количество согласных букв равно', cons)

# Decimal to Binary
# На вход программе подается натуральное число, записанное в десятичной системе счисления.
# Напишите программу, кот. переводит данное число в двоичную систему счисления.
# 19/2 = 9 с остатком 1
# 9/2 = 4 c остатком 1
# 4/2 = 2 без остатка 0
# 2/2 = 1 без остатка 0
# 1/2 = 0 с остатком 1
# делим каждое частное на 2 и записываем остаток в конец двоичной записи.
# Продолжаем деление до тех пор, пока в частном не будет 0. Результат записываем справа налево.
# То есть нижняя цифра (1) будет самой левой и т. д. В результате получаем число 19 в двоичной записи: 10011.
# decimal, string = int(input()), ""
# while decimal != 0:
#     string += str(decimal % 2)
#     decimal //= 2
# for i in reversed(string):
#     print(i, end="")

# Other solution
# Using cat
# при сложении (конкатенации) строк важен порядок. При написанном варианте число в двоичной системе счисления идёт
# в нужном порядке
# a, b = int(input()), ""
# while a > 0:
#     b = str(a % 2) + b
#     a //= 2
# print(b)

# To understand solution above use http://pythontutor.com/ to visualize code
# a, b, c = int(input()), "", ""
# while a > 0:
#     k = str(a % 2)
#     b = k + b
#     c = c + k
#     a //= 2
# print(b, c, sep="\n")

# s = "In 2010, someone paid 10k Bitcoin for two pizzas."
# print(s[:13])
# print(s[-9::-1])
# print(s[::7])

# Палиндром
# На вход программе подается одно слово, записанное в нижнем регистре.
# Напишите программу, кот. определяет является ли оно палиндромом.
# s = input()
# if s[:] == s[::-1]:
#     print("YES")
# else:
#     print("NO")

# The same but shorter
# n = input()
# print('YES' if n == n[::-1] else 'NO')

# Делаем срезы 1
# На вход программе подается одна строка. Напишите программу, которая выводит:
# общее количество символов в строке;
# исходную строку повторенную 3 раза;
# первый символ строки;
# первые три символа строки;
# последние три символа строки;
# строку в обратном порядке;
# строку с удаленным первым и последним символом.
# s = input()
# print(len(s))
# print(s * 3)
# print(s[0])
# print(s[:3])
# print(s[-3:])
# print(s[::-1])
# print(s[1:-1])
#
# print(len(s), s * 3, s[0], s[:3], s[-3:], s[::-1], s[1:-1], sep="\n")

# Делаем срезы 2
# На вход программе подается одна строка. Напишите программу, которая выводит:
# третий символ этой строки;
# предпоследний символ этой строки;
# первые пять символов этой строки;
# всю строку, кроме последних двух символов;
# все символы с четными индексами;
# все символы с нечетными индексами;
# все символы в обратном порядке;
# все символы строки через один в обратном порядке, начиная с последнего.
# s = input()
# print(s[2], s[-2], s[:5], s[:-2], s[::2], s[1::2], s[::-1], s[::-2], sep="\n")

# Две половинки
# На вход программе подается строка текста.
# Напишите программу, кот. разрежет ее на две равные части, переставит их местами и выведет на экран.
# Примечание. Если длина строки нечетная, то длина первой части должна быть на один символ больше.
'''s = input()
k = len(s) // 2 + 1  # for длина строки нечетная
m = len(s) // 2      # for длина строки четная
if len(s) % 2 == 0:
    print(s[m:] + s[:m])
else:
    print(s[k:] + s[:k])'''

# Для разрезания строки вне зависимости от чётности-нечётности (без if):
# делим длину на 2 без остатка, потом прибавляем остаток от деления на 2
# s = input()
# c = len(s) // 2 + len(s) % 2
# print(s[c:]+s[:c])

# Other solution
# s = input()
# print(s[(len(s) + 1) // 2:] + s[:(len(s) + 1) // 2])

# Other solution
# s = input()
# a = len(s) // 2
# print(s[-a:] + s[:-a])

# Заглавные буквы
# На вход программе подается строка состоящая из имени и фамилии человека, разделенных одним пробелом.
# Напишите программу, кот. проверяет, что имя и фамилия начинаются с заглавной буквы.
# Примечание. Строка содержит только буквы.



# Электронные часы
# Дано число n. С начала суток прошло n минут.
# Определите, сколько часов и минут будут показывать электронные часы в этот момент.
# Программа должна вывести два числа: количество часов (от 0 до 23) и количество минут (от 0 до 59).
# Учтите, что число n может быть больше, чем количество минут в сутках.
'''n = int(input())
hours = n // 60
minutes = n % 60
print(hours, minutes)'''
# or
'''print(n // 60, n % 60)'''

'''Следующее и предыдущее
Напишите программу, кот. считывает целое число и выводит текст, аналогичный приведенному в примере (пробелы важны!)
Input: 1534
Output:
The next number for the number 1534 is 1535.
The previous number for the number 1534 is 1533.'''

# n = int(input())
# print(f"The next number for the number {n} is {n + 1}.")
# print(f"The previous number for the number {n} is {n - 1}.")

'''Парты
В школе решили набрать три новых математических класса. Так как занятия по математике у них проходят в одно и то же
время, было решено выделить кабинет для каждого класса и купить в них новые парты.
За каждой партой может сидеть не больше двух учеников.
Известно количество учащихся в каждом из трёх классов. Сколько всего нужно закупить парт, чтобы их хватило на всех
учеников? Программа получает на вход три натуральных числа: количество учащихся в каждом из трех классов.'''
# n1, n2, n3 = int(input()), int(input()), int(input())
# tables = (n1 + n2 + n3 + 1) // 2
# print(tables)

'''Шнурки
Обувная фабрика собирается начать выпуск элитной модели ботинок. Дырочки для шнуровки будут расположены в два ряда,
расстояние между рядами равно aa, а расстояние между дырочками в ряду bb. Количество дырочек в каждом ряду равно NN.
Шнуровка должна происходить элитным способом “наверх, по горизонтали в другой ряд, наверх, по горизонтали и т.д.”.
Кроме того, чтобы шнурки можно было завязать элитным бантиком, длина свободного конца шнурка должна быть ll.
Какова должна быть длина шнурка для этих ботинок?
Программа получает на вход четыре натуральных числа aa, bb, ll и NN - именно в таком порядке -
и должна вывести одно число - искомую длину шнурка.
Sample Input: 2 1 3 4
Sample Output: 26'''
# aa, bb, ll, NN = int(input()), int(input()), int(input()), int(input())
# aa_quantity = NN * 2 - 1
# bb_quantity = NN * 2 - 2
# laces_length = aa_quantity * aa + bb_quantity * bb + ll * 2
# print(laces_length)

# s = 'foo bar foo baz foo qux'
# print(s.strip())
# print(s.lstrip())
# print(s.lstrip("fo"))
# print(s.rstrip())
# print(s.rstrip("oo ux"))

# Количество слов
# На вход программе подается строка текста, состоящая из слов, разделенных ровно одним пробелом.
# Напишите программу, кот. подсчитывает количество слов в ней.
# Примечание 1. Строка текста не содержит пробелов в начале и конце.
# Примечание 2. Используйте для решения задачи метод count.
# s = input()
# print(s.count(" ") + 1)

# Other solution
# .split()
# Splits the string at the specified separator, and returns a list
# print(len(input().split()))

'''Очень странные дела
Джим Хоппер с помощью радиоприемника пытается получить сообщение Оди. На приемник ему поступает n различных
последовательностей кода Морзе. Декодировав их, он получает последовательности из цифр и строчного латинского алфавита,
при этом во всех сообщениях Оди содержится число 11, причем минимум 3 раза. Помогите определить Джиму количество
сообщений от Оди.
Формат входных данных
В первой строке подаётся число n – количество сообщений; в последующих n строках вводятся строки,
содержащие латинские строчные буквы и цифры.
Формат выходных данных
Программа должна вывести количество строк в которых содержится число 11 минимум 3 раза.
Примечание: Числа 11 необязательно должны быть разделены другими символами,
нужно подсчитать вхождение последовательности символов "11", т.е. например в строке "111" содержится одна такая
последовательность, в то время как в "1111" их уже две.'''
# n, count = int(input()), 0
# for i in range(n):
#     s = input()
#     if s.count("11") > 2:
#         count += 1
# print(count)

'''Other solution'''
# count = 0
# for i in range(int(input())):
#     if input().count('11') >= 3:
#         count += 1
# print(count)

'''
Количество цифр
На вход программе подается строка текста. Напишите программу, кот. подсчитывает количество цифр в данной строке.'''
# count = 0
# for i in input():
#     if i.isdigit():
#         count += 1
# print(count)

# Other solution
'''В цикле счётчик перебирает значения от 0 до 9 включительно, то есть это все цифры;
в след строчке переменная counter увеличивается на количество символов i в строке, например, если в n три единицы,
то когда цикл дойдет до i = 1, строка count += n.count(str(i)) увеличит count на три, тк в n три символа "1"
'''
# n = input()
# counter = 0
# for i in range(10):
#     counter += n.count(str(i))
# print(counter)

# Other solution
# s = input()
# k = 0
# for c in '1234567890':
#     k += s.count(c)
# print(k)

# Other solution
# k = 0
# for c in input():
#     if '0' <= c <= '9':
#         k += 1
# print(k)

# Other solution
# s = input()
# count = 0
# for i in range(len(s)):
#     if s[i] in '1234567890':
#         count += 1
# print(count)

'''
.com or .ru
На вход программе подается строка текста. Напишите программу, кот. проверяет, что строка заканчивается подстрокой
.com или .ru.

Формат выходных данных
Программа должна вывести «YES» если введенная строка заканчивается подстрокой .com или .ru и «NO» в противном случае.'''
#
# if input().endswith((".com", ".ru")):
#     print("YES")
# else:
#     print("NO")

# Other solution
# print('YES' if input().endswith(('.com', '.ru')) else 'NO')

'''
Самый частотный символ
На вход программе подается строка текста: может содержать строчные и заглавные буквы английского и русского алфавита,
а также цифры.
Напишите программу, кот. выводит на экран символ, кот. появляется наиболее часто.
Примечание 1. Если таких символов несколько, следует вывести последний по порядку символ.
Примечание 2. Следует различать заглавные и строчные буквы, а также буквы русского и английского алфавита.'''

# s, frequency, most_freq_char = input(), 0, "a"
# for char in s:
#     k = s.count(str(char))
#     if k >= frequency:
#         frequency = k
#         most_freq_char = str(char)
# print(most_freq_char)

# Other solution
# a = input()[::-1]
# z = max(a, key=a.count)
# print(z)

'''
Первое и последнее вхождение
На вход программе подается строка текста. Если в этой строке буква «f» встречается только один раз, выведите её индекс.
Если она встречается два и более раз, выведите индекс её первого и последнего вхождения на одной строке,
разделенных символом пробела. Если буква «f» в данной строке не встречается, следует вывести «NO».'''
# s = input().lower()
# if s.count("f") == 1:
#     print(s.find("f"))
# elif s.count("f") > 1:
#     print(s.find("f"), s.rfind("f"))
# else:
#     print("NO")

# Other solution
# если f не найдена в строке к которой применяется метод то .find возвращает -1
# s = input()
# if s.find('f') == -1:
#     print('NO')
# elif s.find('f') == s.rfind('f'):
#     print(s.find('f'))
# else:
#     print(s.find('f'), s.rfind('f'))

'''
Удаление фрагмента
На вход программе подается строка текста, в которой буква «h» встречается минимум два раза.
Напишите программу, кот. удаляет из этой строки первое и последнее вхождение буквы «h»,
а также все символы, находящиеся между ними.'''
# s = input()
# print(s[:s.find("h")] + s[s.rfind("h") + 1:])

# Other solution
# s = input()
# print(s.replace(s[s.find('h'):s.rfind('h')+1], ""))

# year = 2010
# price = "10k"
# currency = "Bitcoin"
# s = 'In {0}, someone paid {1} {2} for two pizzas.'.format(year, price, currency)
# print(s)
#
# print('In {0}, someone paid {1} {2} for two pizzas.'.format(year, price, currency))
# print(f"In {2010}, someone paid {'10k'} {'Bitcoin'} for two pizzas.")

# year = 2010
# amount = '10K'
# currency = 'Bitcoin'
#
# print(f'In {year}, someone paid {amount} {currency} for two pizzas.')
#
# num1 = ord('A')
# num2 = ord('$')
# num3 = ord('b')
# print(num1, num2, num3)
#
# chr1 = chr(65)
# chr2 = chr(75)
# chr3 = chr(110)
# print(chr1, chr2, chr3)
#
# for i in range(100):
#     print(chr(ord('А')-50 + i), end=" ")

# Символы в диапазоне
# На вход программе подаются два числа a и b.
# Напишите программу, которая для каждого кодового значения в диапазоне от a до b (включительно), выводит
# соответствующий ему символ из таблицы символов Unicode.
# a, b = int(input()), int(input())
# for char in range(a, b + 1):
#     print(chr(char), end=" ")

# Простой шифр
# На вход программе подается строка текста. Напишите программу, кот. переводит каждый ее символ в соответствующий
# ему код из таблицы символов Unicode, разделенных одним символом пробела.
# s = input()
# for char in s:
#     print(ord(char), end=" ")

# Other solution
# print(*(ord(i) for i in input()))

'''
Шифр Цезаря 🌶️
Легион Цезаря, созданный в 23 веке на основе Римской Империи не изменяет древним традициям и использует шифр Цезаря.
Это их и подвело, ведь данный шифр очень простой. Однако в постапокалипсисе люди плохо знают все тонкости довоенного
мира, поэтому ученые из НКР не могут понять как именно нужно декодировать данные сообщения.
Напишите программу для декодирования этого шифра.

Формат входных данных
В первой строке дается число n (1≤ n≤ 25) – сдвиг; во второй строке даётся закодированное сообщение в виде
строки со строчными латинскими буквами.

Формат выходных данных
Программа должна вывести одну строку – декодированное сообщение.
Обратите внимание, что нужно декодировать сообщение, а не закодировать.
Sample Input 1:
1
bwfusvfupdbftbs
Sample Output 1:
avetruetocaesar
Sample Input 2:
14
fsfftsfufksttskskt
Sample Output 2:
rerrfergrweffewewf
'''
# n, code = int(input()), input()
# for char in code:
#     if (ord(char) - n) < 97:
#         k = 123 - (n - (ord(char) - 97))
#         print(chr(k), end="")
#     else:
#         k = ord(char) - n
#         print(chr(k), end="")

# Other solution
# n, code = int(input()), input()
# for char in code:
#     k = ord(char) - n
#     if k < 97:
#         k += 26
#     print(chr(k), end="")

'''
Задача «Шахматная доска»

Условие
Заданы две клетки шахматной доски. Если они покрашены в один цвет, то выведите слово YES, а если в разные цвета — то NO.
 Программа получает на вход четыре числа от 1 до 8 каждое, задающие номер столбца и номер строки сначала для первой
 клетки, потом для второй.'''
# сумма чисел, задающих клетку для одного цвета четная, а для другого - нечетная
# a, b, c, d = int(input()), int(input()), int(input()), int(input())
# if (a + b) % 2 == 0 and (c + d) % 2 == 0:
#     print("YES")
# elif (a + b) % 2 != 0 and (c + d) % 2 != 0:
#     print("YES")
# else:
#     print("NO")

# Other solution
# a, b, a1, b1 = int(input()), int(input()), int(input()), int(input())
# if (a+b) % 2 == (a1+b1) % 2:
#     print('YES')
# else:
#     print('NO')

# Other solution
# if (a + b + c + d) % 2 == 0:
#     print('YES')
# else:
#     print('NO')

# s1 = 'abc'
# s2 = '123'
# s3 = ''
# s4 = 'ыпып'
# s5 = '#$%^'
#
# print(s1.isalnum())
# print(s2.isalnum())
# print(s3.isspace())
# print(s4.isalpha())
# print(s5.isupper())

'''
Каждый третий
На вход программе подается строка текста. Напишите программу, кот. удаляет из нее все символы с индексами кратными 3,
то есть символы с индексами 0, 3, 6, ....'''
# s = input()
# for i in range(len(s)):
#     if i % 3 == 0:
#         continue
#     else:
#         print(s[i], end="")

# Shorter solution
# s = input()
# for i in range(len(s)):
#     if i % 3 != 0:
#         print(s[i], end='')

# Other solution
# s = input()
# a = (s[::3])
# for i in range(len(a)):
#     s = s.replace(a[i], '', 1)
# print(s)

'''Замени меня полностью
На вход программе подается строка текста. Напишите программу, которая заменяет все вхождения цифры 1 на слово «one».'''
# s = input()
# print(s.replace("1", "one"))

'''
Удали меня полностью
На вход программе подается строка текста. Напишите программу, которая удаляет все вхождения символа «@».'''
# print(input().replace("@", ""))

'''
Второе вхождение
На вход программе подается строка текста. Напишите программу, которая выводит индекс второго вхождения буквы «f».
Если буква «f» встречается только один раз, выведите число -1, а если не встречается ни разу, выведите число -2.'''
# s = input()
# if s.count("f") == 1:
#     print(-1)
# elif s.count("f") == 0:
#     print(-2)
# elif s.count("f") > 1:
#     s2 = s.replace("f", "J", 1)
#     print(s2.find("f"))

# Other solution
'''в параметры s.find() передаем поиск необходимого символа - 'f', но т.к. нам нужен второй символ, а не первый,
то вторым параметром передаем индекс, с которого нужно начинать поиск - s.find('f') + 1. Соответственно ищем уже второй
символ'''
'''У find есть замечательное свойство: "Если вызвать метод find с тремя параметрами S.find(T, a, b), то поиск будет
осуществляться в срезе S[a:b]. Если указать только два параметра S.find(T, a), то поиск будет осуществляться
в срезе S[a:], то есть начиная с символа с индексом a и до конца строки. Метод S.find(T, a, b) возращает индекс
в строке S, а не индекс относительно"'''
# s = input()
# if s.count('f') == 0:
#     print(-2)
# elif s.count('f') == 1:
#     print(-1)
# else:
#     print(s.find('f', s.find('f') + 1))

'''Переворот
На вход программе подается строка текста в которой буква «h» встречается как минимум два раза.
Напишите программу, кот. возвращает исходную строку и переворачивает последовательность символов,
заключенную между первым и последним вхождением буквы «h».'''
s = input()
print(s[:s.find("h") + 1])  # slice from start of string to first "h" including
print(s[s.rfind("h") - 1:s.find("h"):-1])  # reversed slice from 1st "h" to last "h" including
print(s[s.rfind("h"):])  # slice from last "h" to the end of string
print(s[:s.find("h") + 1] + s[s.rfind("h") - 1:s.find("h"):-1] + s[s.rfind("h"):])
