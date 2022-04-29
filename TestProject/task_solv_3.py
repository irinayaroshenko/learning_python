# string = "some text here"
# string1 = "12345"
# string2 = "3.1415"
# n = int(string)   can't transform such str to int => returns Error: invalid literal
# n1, n2 = int(string1), float(string2)
# print(n1, n2)

# Operators to work with int: +, -, *, /, //, %, **
# a = 13
# b = 7
#
# total = a + b
# diff = a - b
# prod = a * b
# div1 = a / b
# div2 = a // b
# mod = a % b
# exp = a ** b
#
# print(a, '+', b, '=', total)
# print(a, '-', b, '=', diff)
# print(a, '*', b, '=', prod)
# print(a, '/', b, '=', div1)
# print(a, '//', b, '=', div2)
# print(a, '%', b, '=', mod)
# print(a, '**', b, '=', exp)

# Для удобного чтения чисел можно использовать символ подчеркивания.
# num1 = 25_000_000_000
# num2 = 50000000000
# print(num1, num2, sep='\n')

# Operators to work with float: +, -, *, /, **
# a = 13.5
# b = 2.0
#
# total = a + b
# diff = a - b
# prod = a * b
# div = a / b
# exp = a ** b
#
# print(a, '+', b, '=', total)
# print(a, '-', b, '=', diff)
# print(a, '*', b, '=', prod)
# print(a, '/', b, '=', div)
# print(a, '**', b, '=', exp)

# Implicit conversion
# Any int can be used where you assume to be float because (when needed) Python automatically convert int to float
# 10 / 5 returns 2.0
# Explicit conversion
# float CANNOT be converted to int implicitly. Thus, we need explicitly convert float to int
# num4 = 17.38
# print(int(num4))

# Pay attention!!!
# Conversion float to int is made with rounding to 0
# num5 = 1.7
# num6 = -1.7
# print(int(num5))
# print(int(num6))

# BUT convert float to int is NOT the same as round float numbers. It needs additional commands

# Напишите программу, кото. считывает длины двух катетов в прямоугольном треугольнике и выводит его площадь
# a = float(input())
# b = float(input())
# s = 0.5 * a * b
# print(s)

# Две старушки идут навстречу друг другу с постоянными скоростями V1 и V2 км/ч.
# Определите, через какое время старушки встретятся, если расстояние между ними равно S км.
# На вход программе подаются три числа с плавающей точкой S, V1, V2, каждое на отдельной строке.
# Программа должна вывести одно число в соответствии с условием задачи. Это очень быстрые старушки.
# s, v1, v2 = float(input()), float(input()), float(input())
# t = s / (v1 + v2)
# print(t)

# Напишите программу, кот. считывает с клавиатуры одно число и выводит обратное ему.
# Если введённое с клавиатуры число – ноль, то вывести «Обратного числа не существует». Обратное n - это 1 / n
# n = float(input())
# if n == 0:
#     print("Обратного числа не существует")
# else:
#     print(1 / n)

# 451 градус по Фаренгейту
# Напишите программу, кот. определяет, какой температуре по шкале Цельсия соответствует указанное значение
# по шкале Фаренгейта.
# Fareng = float(input())
# Cels = 5 / 9 * (Fareng - 32)
# print(Cels)

# На вход программе подается число n – количество собачьих лет. Напишите программу, кот. вычисляет возраст собаки
# в человеческих годах.
# Примечание.
# В течение первых двух лет собачий год равен 10.5 человеческим годам.
# После этого каждый год собаки равен 4 человеческим годам.
# n = int(input())
# if n <= 2:
#     print(n * 10.5)
# elif n > 2:
#     print((n - 2) * 4 + 21)

# Дано положительное действительное число. Выведите его первую цифру после десятичной точки.
# n = float(input())
# k = int(n)
# print(int((n - k) * 10))
# # or
# print(int(n * 10 % 10))

# Дробная часть
# Дано положительное действительное число. Выведите его дробную часть.
# n = float(input())
# k = int(n)
# print(n - k)

# a, b, c, d, e = int(input()), int(input()), int(input()), int(input()), int(input())
# print(f"Наименьшее число = {min(a,b,c,d,e)}")
# print(f"Наибольшее число = {max(a,b,c,d,e)}")

# Сортировка трёх
# Напишите программу, кот. упорядочивает три числа от большего к меньшему.
# Программа должна вывести 3 числа, каждое на отдельной строке, упорядоченных от большего к меньшему.
# a, b, c = int(input()), int(input()), int(input())
# min_value = min(a, b, c)
# max_value = max(a, b, c)
# mid_value = 0
# if min_value == a and max_value == b:
#     mid_value = c
# elif min_value == a and max_value == c:
#     mid_value = b
# elif min_value == b and max_value == c:
#     mid_value = a
# elif min_value == b and max_value == a:
#     mid_value = c
# elif min_value == c and max_value == a:
#     mid_value = b
# elif min_value == c and max_value == b:
#     mid_value = a
# print(max_value, mid_value, min_value, sep="\n")

# other solution
# a, b, c = int(input()), int(input()), int(input())
# print(max(a, b, c), ((a + b + c) - (max(a, b, c) + min(a, b, c))), min(a, b, c))

# Интересное число
# Назовем число интересным, если в нем разность макс и мин цифры равняется средней по величине цифре.
# Напишите программу, кот. определяет интересное число или нет.
# Если число интересное, следует вывести – «Число интересное» иначе «Число неинтересное».
# На вход программе подается целое трехзначное число
# x = int(input())
# x1 = x // 100
# x2 = x // 10 % 10
# x3 = x % 10
# max_value = max(x1, x2, x3)
# min_value = min(x1, x2, x3)
# mid_value = (x1 + x2 + x3) - (max_value + min_value)
# if max_value - min_value == mid_value:
#     print("Число интересное")
# else:
#     print("Число неинтересное")

# Абсолютная сумма
# Даны пять чисел a1, a2, a3, a4, a5. Напишите програ., кот. вычисляет сумму их модулей |a1| + |a2| + |a3| +|a4| + |a5|
# На вход программе подается пять действительных чисел, каждое на отдельной строке.
# Программа должна вывести одно число – сумму модулей введёных чисел
# a1, a2, a3, a4, a5 = float(input()), float(input()), float(input()), float(input()), float(input())
# print(abs(a1) + abs(a2) + abs(a3) + abs(a4) + abs(a5))

# !!! It's possible take abs value as input: a = abs(float(input()))  !!!


# Манхэттенское расстояние
# Прогуливаясь по Манхэттену, вы не можете попасть из точки А в точку Б по кратчайшему пути.
# Если только вы не умеете проходить сквозь стены, вам обязательно придется идти вдоль его параллельно-перпендикулярных
# улиц.
# На плоскости манхэттенское расстояние между двумя точками (p1;p2) и (q1;q2) определяется так |p1-q1|+|p2-q2|.
# Напишите программу определяющую манхэттенское расстояние между двумя точками, координаты которых заданы.
# На вход программе подается четыре целых числа, каждое на отдельной строке - p1, p2, q1, q2
# Программа должна вывести одно число – манхэттенское расстояние
# p1, p2, q1, q2 = int(input()), int(input()), int(input()), int(input())
# manch_dist = abs(p1 - q1) + abs(p2 - q2)
# print(manch_dist)

# x = int(input())
# hours = x // 60   # it was (x // 60) % 24 but % 24 doesn't change anything
# mins = x % 60
# print(x, "мин - это", hours, "час", mins, "минут.")

# Possible to use
# print("Access granted" if input() == input() else "Access not granted")

# print("Access", "granted", sep=" " if input() == input() else " not ")

# Compare the view of output
# https://pythonist.ru/priemy-python-kotorym-redko-uchat/?utm_source=telegram&utm_medium=pythonist
my_list = [1, 2, 3, 5, 7]
for i in my_list:
    print(i)    # column of numbers

my_list = [1, 2, 3, 5, 7]
for i in my_list:
    print(i, end=" ")     # 1 2 3 5 7

print("\n", '*' * 10, "\n")

my_list = [1, 2, 3, 5, 7]
print(*my_list)          # 1 2 3 5 7 - does the same as above but without for loop
