# for i in range(5):
#     num = int(input("Give me some number: "))
#     print('Квадрат вашего числа равен:', num * num)
# print('Цикл завершен')

# d = {'один': 'one', 'два': 'two', 'три': 'three'}
# for i in d:  # i по очереди принимает значения 'один', 'два', 'три'
#     print(f'{d[i]} это {i}')

# словари можно перебирать отдельно по ключам:
# for key in 'название словаря'.keys():
#     print(key)

# по значению:
# for value in 'название словаря'.values():
#     print(value)

# по ключу и по значению сразу:
# for key, value in 'название словаря'.items():
#     print(key, value)

# for i in range(10):
#     print("Python is awesome!")

# Повторяй за мной 1
# Дано предложение и количество раз, которое его надо повторить.
# Напишите программу, кот. повторяет данное предложение нужное количество раз.
# s = input()
# count = int(input())
#
# for i in range(count):
#     print(s)

# Бывают ситуации, когда переменная цикла не используется в теле цикла.
# В таком случае, вместо того, чтобы давать ей имя, мы можем указать символ нижнего подчеркивания
# for i in range(6):
#     print("AAA")
# for i in range(5):
#     print("BBBB")
# print("E")
# for _ in range(9):  # _ is used when variable doesn't matter. We can also use "i" here
#     print("TTTTT")
# print("G")

# Звездный прямоугольник
# На вход программе подается натуральное число n. n∈[1;20] — высота звездного прямоугольника.
# ∈ - Принадлежность к чему-либо
# Напишите программу, кот. печатает звездный прямоугольник размерами n×19.
# n = int(input())
# for i in range(n):
#     print("*" * 19)

# Для функции range(), есть правило трёх S: S - start, S - stop, S - step
# range(start, stop, step), start по-умолчанию равен 0, step по-умолчанию равен 1
# если мы даем один аргумент, то это stop range(10) - от 0 до 9 (10 не включается)
# если мы даём два аргумента, то это start и stop range(1, 6) - от 1 до 5
# если мы даём три аргумента, то это start, stop, step range(2, 16, 2): 2, 4, 6, 8, 10, 12, 14
# (не забываем что stop не включается)
# step может быть отрицательным, но тогда start должен быть больше чем stop
# чтобы начать отчёт с 1го: for i in range(1, 5): print(i) Вывод: 1 2 3 4
# можно указать шаг: for i in range(1, 8, 2): print(i) Вывод: 1 3 5 7
# шаг в обратном порядке: если указать шаг:"-2" и начать не с 1, а с 20: for i in range(20, 8, -2): print (i)
# Вывод: 20 18 16 ... 10

# Повторяй за мной 2
# Напишите программу, кот. считывает одну строку текста и выводит 10 строк, пронумерованных от 0 до 9,
# каждая с указанной строкой текста.
# input_string = input()
# for i in range(10):
#     print(i, input_string)

# Квадрат числа
# На вход программе подается натуральное число n.
# Напишите программу, кот. для каждого из чисел от 0 до n (включительно) выводит фразу:
# «Квадрат числа [число] равен [число]» (без кавычек).
# n = int(input())
# for i in range(n + 1):
#     print(f"Квадрат числа {i} равен {i ** 2}")

# Звездный треугольник
# На вход программе подается натуральное число n(n≥2) – катет прямоугольного равнобедренного треугольника.
# Напишите программу, которая выводит звездный треугольник в соответствии с примером.
# 3
# ***
# **
# *
# n = int(input())
# for i in range(n):
#     print("*" * n)
#     n -= 1

# Other solution
# n = int(input())
# for i in range(n):
#     print("*" * (n - i))

# Популяция
# На вход программе подается три натуральных числа m,p,n:
# m: стартовое количество организмов;
# p: среднесуточное увеличение в %;
# n: количество дней для размножения.
# Напишите программу, кот. предсказывает размер популяции организмов.
# Программа должна выводить размер популяции в каждый день, начиная с 1 и заканчивая n-м днем.
# m, p, n = int(input()), int(input()), int(input())
# for i in range(n):
#     print(i + 1, m)
#     add_per_day = m * p / 100
#     m += add_per_day

# Последовательность чисел 1
# Даны два целых числа m и n (m≤n). Напишите программу, которая выводит все числа от m до n включительно.
# m, n = int(input()), int(input())
# for i in range(m, n + 1):
#     print(i)

# Other solution
# for i in range(int(input()), int(input())+1):
#     print(i)

# Other solution (вывести элементы итерируемого объекта так, чтобы их разделяли пробелы, but without end=" ")
# print(*range(int(input()), int(input()) + 1), sep='\n')

# Последовательность чисел 2
# Даны два целых числа m и n. Напишите программу, кот. выводит все числа от m до n включительно в порядке возрастания,
# если m < n, или в порядке убывания в противном случае.
# m, n = int(input()), int(input())
# if m < n:
#     for i in range(m, n + 1):
#         print(i)
# else:
#     for i in range(m, n - 1, -1):
#         print(i)

# Other solution
# m, n = int(input()), int(input())
# k = 1 - 2 * (m > n)                 # bool value: True - 1. False - 0
# for i in range(m, n + k, k):
#     print(i)

# Other solution
# m, n, k = int(input()), int(input()), 1
# if not m < n:  # последовательность будет убывающей
#     k = -1
# for i in range(m, n + k, k):
#     print(i)

# Other solution
# m, n = int(input()), int(input())
# print(*[range(m, n - 1, -1), range(m, n + 1)][m < n], sep='\n')

# Последовательность чисел 3
# Даны два целых числа m и n (m>n). Напишите программу, кот. выводит все нечетные числа от m до n включительно
# в порядке убывания.
# Примечание. Попробуйте решить задачу двумя способами: с использованием условного оператора if и без него.
# m, n = int(input()), int(input())
# for i in range(m, n - 1, -1):
#     if i % 2 != 0:
#         print(i)

# k = -2 * (m % 2 != 0)
# for i in range(m, n - 1, k):
#     print(i)

# counter = 0
# for i in range(10):
#     num = int(input(f"Enter {10 - i} different numbers: "))
#     if num > 10:
#         counter += 1
# print('Было введено', counter, 'чисел, больших 10.')


# counter1 = 0
# counter2 = 0
# for i in range(10):
#     num = int(input(f"Enter {10 - i} different numbers: "))
#     if num > 10:
#         counter1 = counter1 + 1
#     if num == 0:
#         counter2 = counter2 + 1
# print('Было введено', counter1, 'чисел, больших 10.')
# print('Было введено', counter2, 'нулей.')


# counter = 0
# for i in range(1, 101):
#     if i**2 % 10 == 4:
#         counter += 1
# print(counter)


# total = 0
# for i in range(10):
#     num = int(input(f"Enter {10 - i} different numbers: "))
#     if num > 10:
#         total += num
# print('Сумма чисел больших 10 равна', total)


# total = 0
# for _ in range(1, 101):
#     total += _
# print(total)

# set 'total = 0' if we sum values, e.g. numbers
# total = 0
# for i in range(10):
#     num = int(input(f"Enter {10 - i} numbers one at a time: "))
#     total += num
# print(total / 10)

# set 'total = 1' if we multiply values, e.g. numbers
# total = 1
# for i in range(10):
#     num = int(input(f"Enter {10 - i} numbers one at a time: "))
#     if i > 5:
#         total *= num
# print("Multiplication result: ", total)


# Сигнальная метка (flag) может использоваться, когда надо чтобы одна часть программы узнала о происходящем в другой
# части программы.
# Напишем программу, определяющую, что натуральное число является простым (не имеет делителей, кроме 1 и самого себя):
# num = int(input())
# flag = True
#
# for i in range(2, num):
#     if num % i == 0:        #  если исходное число делится на какое-либо отличное от 1 и самого себя
#         flag = False
#
# if num != 1 and flag:
#     print('Число простое')
# else:
#     print('Число составное')

# Количество чисел
# На вход программе подаются два целых числа a и b (a≤b).
# Напишите программу, кот. подсчитывает количество чисел в диапазоне от a до b включительно,
# куб которых оканчивается на 4 или 9.

# a, b = int(input()), int(input())
# counter = 0
# for i in range(a, b + 1):
#     if i ** 3 % 10 == 4:
#         counter += 1
#     if i ** 3 % 10 == 9:
#         counter += 1
# print(counter)

# Other solution
# counter = 0
# for i in range(int(input()), int(input()) + 1):
#     if i ** 3 % 10 == 4 or i ** 3 % 10 == 9:
#         counter += 1
# print(counter)

# Other solution
# a, b, count = int(input()), int(input()), 0
# for i in range(a, b + 1):
#     if i**3 % 10 in [4, 9]:
#         count += 1
# print(count)

# Сумма чисел
# На вход программе подается натуральное число n, а затем n целых чисел, каждое на отдельной строке.
# Напишите программу, которая подсчитывает сумму введенных чисел.
# n, total = int(input()), 0
# for _ in range(n):
#     num = int(input())
#     total += num
# print(total)

# Other solution
# s = 0
# for i in range(int(input())):
#     s += int(input())
# print(s)

# Асимптотическое приближение
# На вход программе подается натуральное число nn. Напишите программу, которая вычисляет значение выражения:
# (1+ 1/2 + 1/3 + ... + 1/n) −ln(n)
# Примечание. Для вычисления натурального логарифма воспользуйтесь функцией log(n), которая находится в модуле math
# from math import log
#
# n, adding = int(input()), 0
# for i in range(1, n + 1):
#     adding += 1/i
# print(adding - log(n))

# Сумма чисел
# На вход программе подается натуральное число n.
# Напишите программу, кот. подсчитывает сумму тех чисел от 1 до n (включительно),
# квадрат которых оканчивается на 2,5 или 8.
# Примечание. Если таких чисел нет в указанном диапазоне, то следует вывести 0.
# n, sum_of_digits = int(input()), 0
# for i in range(1, n + 1):
#     if i ** 2 % 10 == 2 or i ** 2 % 10 == 5 or i ** 2 % 10 == 8:
#         sum_of_digits += i
# print(sum_of_digits)

# Note. квадраты целых чисел не оканчиваются на 2 и 8 (концовки -- 1, 4, 5, 6, 9, 0),
# поэтому достаточно искать 5 на конце
# n, sum_of_digits = int(input()), 0
# for i in range(1, n + 1):
#     if i ** 2 % 10 == 5:
#         sum_of_digits += i
# print(sum_of_digits)

# Other solution
# n, sum = int(input()), 0
# for i in range(1, n + 1):
#     if i**2 % 10 in [2, 5, 8]:
#         sum += i
# print(sum)

# Факториал
# На вход программе подается натуральное число n (n≤12). Напишите программу, которая вычисляет n!
# Факториал числа — это произведение натуральных чисел от 1 до самого числа (включая данное число).
# Обозначается факториал восклицательным знаком «!».
# 6! = 1 * 2 * 3 * 4 * 5 * 6 = 720
# n, factorial = int(input()), 1
# for i in range(1, n + 1):
#     factorial *= i
# print(factorial)

# Other solution
# from math import factorial
# k = int(input())
# print(factorial(k))

# Без нулей
# Напишите программу, которая считывает 10 чисел и выводит произведение отличных от нуля чисел.
# Примечание. Гарантируется, что хотя бы одно из 10 чисел является ненулевым.
# numbers_multiplication = 1
# for i in range(10):
#     number = int(input())
#     if number != 0:
#         numbers_multiplication *= number
# print(numbers_multiplication)

# Other solution without if
# если число n, подаваемое на вход, равно нулю, то в скобках при верном равенстве будет значение True==1,
# в таком случае имеющее произведение домножается не на 0, а на  0 + 1.
# Если же число n не равно нулю, то в скобках значение False==0, следовательно, произведение домнажается на n + 0
# p = 1
# for _ in range(10):
#     n = int(input())
#     p *= n + (n == 0)
# print(p)

# Other solution
# k if k else 1 означает, если k у нас какое-то число (не ноль), то буде TRUE (и будет использоваться само k),
# иначе будет использоваться единица 1  - в итоге используется при преумножении (либо k, либо 1)
# n = 1
# for _ in range(10):
#     k = int(input()); n *= k if k else 1
# print(n)

# Сумма делителей
# На вход программе подается натуральное число nn. Напишите программу, которая вычисляет сумму всех его делителей.
# Примечание. Функция подсчета суммы всех делителей числа является очень важной в теории чисел.
# n, s = int(input()), 0
# for _ in range(1, n + 1):
#     if n % _ == 0:
#         s += _
# print(s)

# Знакочередующаяся сумма
# На вход программе подается натуральное число n. Напишите программу вычисления знакочередующей суммы:
# 1−2+3−4+5−6+…+(−1)**n+1 * n
# n, s = int(input()), 0
# for i in range(1, n + 1):
#     if i % 2 != 0:
#         s += i
#     else:              # elif i % 2 == 0:
#         s -= i
# print(s)

# Other solution
# n, summ = int(input()), 0
# for i in range(1, n + 1):
#     summ += (-1)**(i+1) * i
# print(summ)

# Other solution
# n = int(input())
# total = 0
# flag = True
# for i in range(1, n + 1):
#     if flag:
#         total += i
#         flag = False
#     else:
#         total -= i
#         flag = True
# print(total)

# Наибольшие числа
# На вход программе подается натуральное число n (n≥2), а затем n различных натуральных чисел, каждое на отдел. строке.
# Напишите программу, которая выводит два наибольших числа, каждое на отдельной строке.
# n, max_value, lst = int(input()), 0, []
# for i in range(n):
#     number = int(input())
#     lst.append(number)
#     if number > max_value:
#         max_value = number
# lst.remove(max_value)
# print(max_value, max(lst), end="\n")

# Without if
# n, lst = int(input()), []
# for i in range(n):
#     number = int(input())
#     lst.append(number)
# m = max(lst)
# k = m
# lst.remove(m)
# print(k, max(lst), sep="\n")

# Other solution
# n, max_value, second_max = int(input()), 0, 0
# for i in range(n):
#     number = int(input())
#     if number > max_value:
#         second_max = max_value
#         max_value = number
#     elif number > second_max:
#         second_max = number
# print(max_value, second_max, sep="\n")

# Only even numbers
# Напишите программу, кот. считывает 10 целых чисел и определяет является ли каждое из них четным или нет.
# Программа должна вывести строку «YES», если все числа четные и «NO» в ином случае.
# count = 0
# for i in range(10):
#     n = int(input())
#     if n % 2 != 0:
#         count += 1
# if count == 0:
#     print("YES")
# else:
#     print("NO")

# Other solution
# flag = "YES"
# for _ in range(5):
#     n = int(input())
#     if n % 2 != 0:
#         flag = "NO"
# print(flag)

# Последовательность Фибоначчи
# Напиш. прогр.,кот. считывает натур. число n (n≤100) и выводит первые n чисел последов-ти Фибоначчи,отделенные пробелом
'''n, a1, a2 = int(input()), 0, 1
for i in range(n):
    if i < 1:
        print(a2, end=' ')
    elif i < 2:
        a2 += a1
        print(a2, end=' ')
        a1 = a2
    else:
        next_number = a1 + a2
        print(next_number, end=' ')
        a1, a2 = a2, next_number'''

# Other solution
'''n, a, b = int(input()), 1, 1
for i in range(n):
    print(a, end=' ')
    a, b = b, a + b'''

# WHILE loop
'''num = int(input())
while num != -1:
    print('Квадрат вашего числа равен:', num * num)
    num = int(input())'''


'''text = input()
total = 0
while text != 'stop':
    num = int(text)
    total += num
    text = input()
print('Сумма чисел равна', total)'''

# До КОНЦА 1
# На вход программе подается последовательность слов, каждое слово на отдельной строке.
# Концом последовательности является слово «КОНЕЦ» (без кавычек). Напишите программу, кот. выводит члены данной
# последовательности.

'''word = input()
while word != "КОНЕЦ":
    print(word)
    word = input()'''

# До КОНЦА 2
# На вход программе подается последовательность слов, каждое слово на отдельной строке.
# Концом последовательности является слово «КОНЕЦ» или «конец» (большими или маленькими буквами, без кавычек).
# Напишите программу, кот. выводит члены данной последовательности.

# while word.lower() != "конец":     one more way
# если мы используем оператор or,
# то цикл продолжится, если будет выполнено хотя бы одно из условий. Даже если оно противоречит другому.
# while word != "КОНЕЦ" or word != "конец":
'''word = input()
while word != "КОНЕЦ" and "конец":
    print(word)
    word = input()'''

# !!!!
'''если проверка на соответствие, и дальнейшее выполнение кода, ведущего к выходу из цикла, то будет использоваться
 оператор or
if my_variable == 'КОНЕЦ' or my_variable == 'конец':
    pass
т.к. в таком случае достаточно чтобы истиной была любая часть этого выражения
если же идет проверка на не соответствие, и дальнейшее выполнение основного тела цикла, то тут нужен будет and
if my_variable != 'КОНЕЦ' and my_variable != 'конец':
    pass'''
# !!!!

# Mutable and Immutable types
# tuple, str, int, float, frozenset - immutable
# list, dict, set and others - mutable

# Количество членов
# На вход программе подается последовательность слов, каждое слово на отдельной строке.
# Концом последовательности является одно из трех слов: «стоп», «хватит», «достаточно» (маленьк. буквами, без кавычек).
# Напишите программу, кот. выводит общее количество членов данной последовательности.
'''text, count = input(), 0
# while text != "стоп" and text != "хватит" and text != "достаточно":
while text not in ("стоп", "хватит", "достаточно"):
    count += 1
    text = input()
print(count)'''

# Пока делимся
# На вход программе подается последовательность целых чисел делящихся на 7, каждое число на отдельной строке.
# Концом последовательности является любое число не делящееся на 7. Напишите программу,
# кот. выводит члены данной последовательности.
'''number = int(input())
while number % 7 == 0:
    print(number)
    number = int(input())'''

# Сумма чисел
# На вход программе подается последовательность целых чисел, каждое число на отдельной строке.
# Концом последовательности является любое отрицательное число.
# Напишите программу, кот. выводит сумму всех членов данной последовательности.
'''n, num_sum = int(input()), 0
while not n < 0:
    num_sum += n
    n = int(input())
print(num_sum)'''

# Количество пятерок
# На вход программе подается последовательность целых чисел от 1 до 5, характеризующее оценку ученика,
# каждое число на отдельной строке. Концом последовательности является любое отрицательное число,
# либо число больше 5. Напишите программу, кот. выводит количество пятерок.
'''num, count = int(input()), 0
while -1 < num < 6:
    while num == 5:
        count += 1
    num = int(input())
print(count)'''

# Ведьмаку заплатите чеканной монетой
# Всем известно, что ведьмак способен одолеть любых чудовищ, однако его услуги обойдутся недешево,
# к тому же ведьмак не принимает купюры, он принимает только чеканные монеты.
# В мире ведьмака существуют монеты с номиналами 1,5,10,25.
# Напишите программу, кот. определяет какое минимальное количество чеканных монет нужно заплатить ведьмаку.
'''coins, count = int(input()), 0
while coins >= 25:
    count += 1
    coins -= 25
while coins >= 10:
    count += 1
    coins -= 10
while coins >= 5:
    count += 1
    coins -= 5
while coins >= 1:
    count += 1
    coins -= 1
print(count)'''

# Other solution without loop
'''coins = int(input())
print(coins // 25 + (coins % 25) // 10 + ((coins % 25) % 10) // 5 + ((coins % 25) % 10) % 5)

# Other solution
n = int(input())
total = 0
for i in (25, 10, 5, 1):
    while n // i > 0:
        total += 1
        n -= i
print(total)'''

'''num = int(input())
has_seven = False  # сигнальная метка

while num != 0:
    last_digit = num % 10
    if last_digit == 7:
        has_seven = True
    num = num // 10

if has_seven:
    print('YES')
else:
    print('NO')'''

# Обратный порядок 1
# Дано натуральное число. Напишите программу, которая выводит его цифры в столбик в обратном порядке.
'''n = int(input())
while n != 0:
    print(n % 10)
    n = n // 10'''

# Обратный порядок 2
# Дано натуральное число. Напишите программу, которая меняет порядок цифр числа на обратный.
'''n = int(input())
while n != 0:
    print(n % 10, end="")
    n = n // 10'''

# max и min
# Дано натуральное число n (n≥10). Напишите программу, кот. определяет его максимальную и минимальную цифры.
'''n = input()
print("Максимальная цифра равна", max(n))
print("Минимальная цифра равна", min(n))'''

# Solution with while
'''n, big, small = int(input()), 0, 9
while n != 0:
    if n % 10 > big:
        big = n % 10
    if n % 10 < small:
        small = n % 10
    n = n // 10
print("Максимальная цифра равна", big)
print("Минимальная цифра равна", small)'''

# Все вместе
# Дано натуральное число. Напишите программу, которая вычисляет:
# сумму его цифр;
# количество цифр в нем;
# произведение его цифр;
# среднее арифметическое его цифр;
# его первую цифру;
# сумму его первой и последней цифры.
'''n = int(input())
sum_digits, total_digits, multipl_digits, first_digit = 0, 0, 1, 0
last_digit = n % 10
while n != 0:
    sum_digits += n % 10
    total_digits += 1
    multipl_digits *= n % 10
    if 0 <= n <= 9:
        first_digit = n
    n //= 10
print(sum_digits, total_digits, multipl_digits, sum_digits / total_digits, first_digit, first_digit + last_digit, sep="\n")'''

# Вторая цифра
# Дано натуральное число n(n>9). Напишите программу, кот. определяет его вторую (с начала) цифру.
'''n = int(input())
while n != 0:
    if 10 <= n <= 99:
        digit = n % 10
    n //= 10
print(digit)'''

# Other solution
'''x = input()
print(list(x)[1])'''

# Одинаковые цифры
# Дано натуральное число. Напишите программу, кот. определяет, состоит ли указанное число из одинаковых цифр.
# n, same = int(input()), True
# while not n <= 9:
#     if not n % 10 == n // 10 % 10:
#         same = False
#     n //= 10
# if same:
#     print("YES")
# else:
#     print("NO")

# Other solution
# k = input()
# if max(k) == min(k):       # the same: print('YES' if max(x) == min(x) else 'NO')
#     print("YES")
# else:
#     print("NO")

# Other solution
# n = int(input())
# m = n % 10
# answer = 'YES'
# while n != 0:
#     if m != n % 10:
#         answer = 'NO'
#     n //= 10
# print(answer)

# Other solution: сравнение количества первого элемента в строке с длиной строки
'''numbers = input()
print('YES' if numbers.count(numbers[0]) == len(numbers) else 'NO')'''

# Упорядоченные цифры 🌶️
# Дано натуральное число. Напишите программу, кот. определяет, является ли последовательность его цифр при просмотре
# справа налево упорядоченной по неубыванию. Example: 5321 - YES, 4851 - NO
'''n, answer = int(input()), "YES"
while n != 0:
    if n % 10 > n // 10 % 10:
        answer = "NO"
    if 9 < n < 100:
        n //= 100
    n //= 10
print(answer)'''

# Shorter solution
'''n, answer = int(input()), "YES"
while n > 9:
    if n % 10 > n // 10 % 10:
        answer = "NO"
    n //= 10
print(answer)'''

# Other solution
'''n = int(input())
f = 'NO'
while n % 10 <= n // 10 % 10:
    n //= 10
    if n < 10:
        f = 'YES'
print(f)'''

# Other solution
'''n = int(input())
while n % 10 <= n // 10 % 10:
    n //= 10
print('YES' if n < 10 else 'NO')'''

# Наименьший делитель
# На вход программе подается число n>1. Напишите программу, кот. выводит его наименьший отличный от 1 делитель.
# Примечание. Используйте оператор break.
'''n = int(input())
for i in range(2, n + 1):
    if n % i == 0:
        break
print(i)'''

# Solution with while
'''n, i = int(input()), 2
while n % i != 0:
    i += 1
print(i)'''

# Other solution
# пока есть остаток от деления, условие True. как только остаток равен 0, то условие False и не нужно больше искать
# делители. всегда то, что не ноль - True, а ноль - False. в условие спрашивается True(1) или False(0)
'''n, div = int(input()), 2
while n % div:
    div += 1
print(div)'''

# Следуй правилам
# На вход подается натуральное число n. Напишите программу, кот. выводит числа от 1 до n включит. за исключением:
# чисел от 55 до 99 включительно;
# чисел от 1717 до 3737 включительно;
# чисел от 7878 до 8787 включительно.
# Примечание. Используйте оператор continue.
'''n = int(input())
for i in range(1, n + 1):
    if 5 <= i <= 9:
        continue
    elif 17 <= i <= 37:
        continue
    elif 78 <= i <= 87:
        continue
    print(i)'''

# Solution with while
'''n, i = int(input()), 1
while i != n + 1:
    if 5 <= i <= 9 or 17 <= i <= 37 or 78 <= i <= 87:
        i += 1
        continue
    print(i)
    i += 1'''

'''a, b = int(input()), int(input())
total = 0
for i in range(a, b + 1):
    if ((i ** 3) % 10) % 4 == 0 or ((i ** 3) % 10) % 9 == 0:
        total += 1
print(total)'''

# num = int(input())
# flag = True
#
# for i in range(2, num):
#     if num % i == 0:
#         flag = False
# if num > 1 and flag:
#     print('Число простое')
# else:
#     print('Число составное')

# Ревью кода-1 🌶️🌶️
# На обработку поступает последовательность из 10 целых чисел.
# Известно, что вводимые числа по абсолютной величине не превышают 10^6.
# Нужно написать программу, кот. выводит количество неотрицательных чисел последовательности и их произведение.
# Если неотрицательных чисел нет, требуется вывести на экран «NO».
# Найдите все ошибки в этой программе (их ровно 4). Известно, что каждая ошибка затрагивает только одну строку
# и может быть исправлена без изменения других строк.
# Примечание 1. Число x не превышает по абсолютной величине 10^6, если -10^6 ≤x ≤10^6.
# Примечание 2. При необходимости вы можете добавить необходимые строки кода.
# Origin
# count = 0
# p = 0
# for i in range(1, 10):
#     x = int(input())
#     if x > 0:
#         p = p * x
#         count = count + 1
# if count > 0:
#     print(x)
#     print(p)
# else:
#     print('NO')

# Review
'''count = 0
p = 1
for i in range(10):
    x = int(input())
    if x > -1:
        p *= x
        count += 1
if count > 0:
    print(count)
    print(p)
else:
    print('NO')'''

# My solution before review
'''count, multiply = 0, 1
for i in range(10):
    x = int(input())
    if x > -1:
        count += 1
        multiply *= x
if count > 0:
    print(count, multiply, sep="\n")
else:
    print("NO")'''

# Ревью кода-2 🌶️🌶️
# На обработку поступает последовательность из 10 целых чисел.
# Известно, что вводимые числа по абсолютной величине не превышают 10^6.
# Нужно написать программу, кот. выводит на экран сумму всех отрицательных чисел последовательности
# и максимальное отрицательное число в последовательности.
# Если отрицательных чисел нет, требуется вывести на экран «NO».
# Найдите все ошибки в этой программе (их ровно 5). Известно, что каждая ошибка затрагивает только одну строку
# и может быть исправлена без изменения других строк.
# Примечание 1. Число x не превышает по абсолютной величине 10^6, если -10^6 ≤x ≤10^6.
# Примечание 2. При необходимости вы можете добавить необходимые строки кода.
# Origin
'''summ, max_value = 0, 0
for i in range(5):
    x = int(input())
    if x < 0:
        summ += x
        if x > -10 ** 6:
            max_value = x
print(summ, max_value)'''


# Ревью кода-4 🌶️🌶️
# На обработку поступает натуральное число.
# Нужно написать программу, кот. выводит на экран максимальную цифру числа, кратную 3.
# Если в числе нет цифр, кратных 3, требуется на экран вывести «NO».
# Найдите все ошибки в этой программе (их ровно 5). Известно, что каждая ошибка затрагивает только одну строку
# и может быть исправлена без изменения других строк.
# Примечание 1. Число 0 делится на любое натуральное число.
# Примечание 2. При необходимости вы можете добавить нужные строки кода.
'''n, max_digit = int(input()), -1
while n > 0:
    if n % 10 in (0, 3, 6, 9):
        if n % 10 > max_digit:
            max_digit = n % 10
    n //= 10
if max_digit >= 0:
    print(max_digit)
else:
    print("NO")'''

# Origin
'''n = int(input())
max_digit = n % 10
while n > 0:
    digit = n % 10
    if digit % 3 == 0:
        if digit < max_digit:
            digit = max_digit
    n = n % 10
if max_digit == 0:
    print('NO')
else:
    print(max_digit)'''

'''n = int(input())
max_digit = -1  # -1
while n > 0:
    digit = n % 10
    if digit % 3 == 0:
        if digit > max_digit:    # >
            max_digit = digit    #
    n = n // 10                  # //
if max_digit < 0:                # <
    print('NO')
else:
    print(max_digit)'''

# Ревью кода-5 🌶️
# На обработку поступает натуральное число. Нужно написать программу, кот. выводит на экран первую цифру числа.
# Найдите все ошибки в этой программе (их ровно 2).
'''n = int(input())
while n > n % 10:
    n //= 10
print(n)'''

# Origin
'''n = int(input())
while n > 0:
    n %= 10
print(n)'''

# Ревью кода-6
# На обработку поступает натуральное число.
# Нужно написать программу, кот, выводит на экран произведение цифр введенного числа.
# Найдите все ошибки в этой программе (их ровно 3).
# Solution
'''n, product = int(input()), 1
while n > 0:
    product *= n % 10
    n //= 10
print(product)'''

# Origin
'''n = input()
product = n % 10
while n >= 10:
    digit = n % 10
    product = product * digit
    n //= 10
print(product)'''

# Nested loops
'''for seconds in range(60):
    print(seconds)

for minutes in range(60):
    for seconds in range(60):
        print(minutes, ':', seconds)

for hours in range(24):
    for minutes in range(60):
        for seconds in range(60):
            print(hours, ':', minutes, ':', seconds)'''

# for i in range(3):
#     for j in range(3):
#         for k in range(3):
#             print(i, j, k)

# Если необходимо добиться прерывания внешнего цикла из-за выполнения условия во внутреннем, то стоит сделать это через
# flag

'''for i in range(6):
    for j in range(8):
        print("*", end="")
    print()

for i in range(6):
    for j in range(i + 1):
        print("*", end="")
    print()'''

'''from time import *
for hours in range(24):
    for minutes in range(60):
        for seconds in range(60):
            print(hours, ':', minutes, ':', seconds, end='')
            sleep(1)
            print(end='\r')   '''
# end = ('\r') - это возрат каретки к началу строки, для того чтобы печатолось поверх введённого, а не с новой строки

# Таблица-1
# Дано натуральное число n (n≤ 9). Напишите программу, кот. печатает таблицу размером n×3, состоящую из данного числа
# (числа отделены одним пробелом).
# Примечание. В конце строки может быть пробел.
# n = int(input())
# for i in range(n):
#     for j in range(3):
#         print(n, end=" ")
#     print()

# Does the same without nested loop
# m = int(input())
# for _ in range(m):
#     print(m, m, m)

# Таблица-1
# Дано натуральное число n (n≤ 9). Напишите программу, кот. печатает таблицу размером n×5, где в i-ой строке указано
# число i (числа отделены одним пробелом).
# Примечание. В конце строки может быть пробел.
'''n = int(input())
for i in range(1, n + 1):
    for j in range(5):
        print(i, end=" ")
    print()'''

# Таблица-3
# Дано натуральное число n (n≤ 9). Напишите программу, кот. печатает таблицу сложения для всех чисел от 1 до n
# в соответствии с примером.
# Примечание. В конце строки может быть пробел.
'''n = int(input())
for i in range(1, n + 1):
    for j in range(1, 10):
        print(i, "+", j, "=", i + j)
    print()'''

# Звездный треугольник 🌶️🌶️
# Дано нечетное натуральное число n. Напишите программу, кот. печатает равнобедренный звездный треугольник с основанием,
# равным n в соответствии с примером:
# *
# **
# ***
# ****
# ***
# **
# *
# Примечание. Используйте вложенный цикл for.
'''n = int(input())
for i in range(1):
    for j in range(n // 2 + 1):
        print("*" * (j + 1))
    for k in range(n // 2):
        print("*" * (n // 2 - k))'''

# How it works?
'''n = int(input())
for i in range(1, n + 1):
    print('*' * min(i, n - i + 1))'''

# Численный треугольник 1
# Дано натуральное число nn. Напишите программу, которая печатает численный треугольник в соответствии с примером:
# 1
# 22
# 333
# 4444
# 55555
# ...
# Примечание. Используйте вложенный цикл for.
# With one loop
'''n = int(input())
for i in range(n):
    print((i + 1) * str(i + 1))'''

# With nested loop
'''for i in range(1, int(input()) + 1):
    for j in range(i):
        print(i, end='')
    print()'''

# 12 месяцев
# Решите уравнение в натуральных числах 28n + 30k + 31m = 365
# Примечание. Используйте вложенный цикл for. В первую очередь запишите решение с наименьшим значением n.
'''for n in range(1, 14):
    for k in range(1, 13):
        for m in range(1, 12):
            if 28 * n + 30 * k + 31 * m == 365:
                print(f"n = {n}, k = {k}, m = {m}")'''

# Старинная задача
# Имеется 100 рублей. Сколько быков, коров и телят можно купить на все эти деньги,
# если плата за быка – 10 рублей, за корову – 5 рублей, за теленка – 0.5 рубля и надо купить 100 голов скота?
# Примечание. Используйте вложенный цикл for.
'''for x in range(1, 101):
    for y in range(1, 101):
        for z in range(1, 101):
            if x * 10 + y * 5 + z * 0.5 == 100 and x + y + z == 100:
                print('Быков:', x, 'Коров:', y, 'Телят:', z)'''

# Other solution
'''for b in range(11):
    for k in range(21):
        for t in range(201):
            if 10 * b + 5 * k + 0.5 * t == 100:
                if b + k + t == 100:
                    print(b, k, t)'''

# Гипотеза Эйлера о сумме степеней
# В 1769 году Леонард Эйлер сформулировал обобщенную версию Великой теоремы Ферма, предполагая,
# что по крайней мере n энных степеней необходимо для получения суммы, которая сама является энной степенью для n>2.
# Напишите программу для опровержения гипотезы Эйлера (продержавшейся до 1967 года),
# и найдите 4 положительных целых числа, сумма 5-х степеней кот-х равна 5-й степени другого положительного целого числа.
# Таким образом, найдите пять натуральных чисел a,b,c,d,e удовлетворяющих условию:
# a^5+b^5+c^5+d^5=e^5.
# В ответе укажите сумму a+b+c+d+e.
# Примечание 1. Используйте вложенный цикл for.
# Примечание 2. Считайте, что числа a,b,c,d,e не превосходят 150.
# Примечание 3. Программа может работать дольше чем обычно.
# В зависимости от способа решения задачи на выполнение программы может уходить до нескольких минут.
# Попробуйте сократить количество вложенных циклов.
# Executes very-very long.
'''for a in range(1, 151):
    for b in range(1, 151):
        for c in range(1, 151):
            for d in range(1, 151):
                for e in range(1, 151):
                    if a ** 5 + b ** 5 + c ** 5 + d ** 5 == e ** 5:
                        print(f"a + b + c + d = {a} + {b} + {c} + {d} = {a + b + c + d}")'''

# Other solution. Executes 25-30 sec
'''for a in range(1, 151):
    for b in range(a + 1, 151):
        for c in range(b + 1, 151):
            for d in range(c + 1, 151):
                e = int(((a ** 5) + (b ** 5) + (c ** 5) + (d ** 5)) ** 0.2)
                if e ** 5 == int((a ** 5) + (b ** 5) + (c ** 5) + (d ** 5)):
                    print(a + b + c + d + e)'''

# Численный треугольник 3
# Дано натуральное число n. Напишите программу, кот. печатает численный треугольник с высотой равной n, в соответствии
# с примером:
# 1
# 2 3
# 4 5 6
# 7 8 9 10
# 11 12 13 14 15
# 16 17 18 19 20 21
# ...
'''n, total = int(input()), 0
for i in range(1, n + 1):
    for j in range(i):
        total += 1
        print(total, end=" ")
    print()'''

# Other solution
'''n = int(input())
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print((i - 1) * i // 2 + j, end=' ')
    print()'''

# Численный треугольник 4
# Дано натуральное число n. Напишите программу, кот. печатает численный треугольник с высотой равной n, в соответствии
# с примером:
# 1
# 121
# 12321
# 1234321
# 123454321
# ...
'''for i in range(1, int(input()) + 1):
    for j in range(1, i + 1 + (i - 1)):
        if j <= i:
            _ = j
            print(j, end="")
        else:
            _ -= 1
            print(_, end="")
    print()'''

# Other solution
'''num = int(input())
for i in range(1, num + 1):
    for j in range(1, i + 1):
        print(j, end='')
    for k in range(i - 1, 0, -1):
        print(k, end='')
    print()'''

# Other solution
'''for i in range(1, int(input()) + 1):
    for j in range(1, i * 2):
        print(i - abs(i - j), end='')
    print()'''

# Делители-1 🌶️
# На вход программе подается два натуральных числа a и b (a< b).
# Напишите программу, кот. находит натуральное число из отрезка [a;b] с максимальной суммой делителей.
# Формат входных данных
# На вход программе подаются два числа, каждое на отдельной строке.
# Формат выходных данных
# Программа должна вывести два числа на одной строке, разделенных пробелом:
# число с максимальной суммой делителей и сумму его делителей.
# Примечание. Если таких чисел несколько, то выведите наибольшее из них.

# Найти СУММУ делителей, а не количество делителей
'''a, b, summ, max_sum = int(input()), int(input()), 0, 0
for i in range(a, b + 1):
    for j in range(1, i + 1):
        if i % j == 0:
            summ += j
        if summ >= max_sum:
            max_sum = summ
            k = j
    summ = 0
print(k, max_sum)'''

# Если бы надо было найти максимальное количество делителей числа
# a, b, count, summ = int(input()), int(input()), 0, 0
# max_count, max_count_sum = 0, 0
# for i in range(a, b + 1):
#     for j in range(1, i + 1):
#         if i % j == 0:
#             count += 1
#             summ += j
#     if count > max_count:
#         max_count = count
#         max_count_sum = summ
#         k = j
#         count, summ = 0, 0
#     if count == max_count and k < j:
#         k = j
#         max_count_sum = summ
#         count, summ = 0, 0
#     count, summ = 0, 0
# print(k, max_count_sum)

# Делители-2
# На вход программе подается натуральное число n.
# Напишите программу, выводящую графическое изображение делимости чисел от 1 до n включительно.
# В каждой строке надо напечатать очередное число и столько символов «+», сколько делителей у этого числа.
# Example:
# Input: 5
# Output:
# 1+
# 2++
# 3++
# 4+++
# 5++
'''n, count = int(input()), 0
for i in range(1, n + 1):
    count = 0
    for j in range(1, i + 1):
        if i % j == 0:
            count += 1
    print(j, count * "+", sep="")'''

# Other solution - without counter
'''n = int(input())
for i in range(1, n + 1):
    print(i, end="")
    for j in range(1, i+1):
        if i % j == 0:
            print("+", end="")
    print()'''

# Цифровой корень
# На вход программе подается натуральное число n. Напишите программу, кот. находит цифровой корень данного числа.
# Цифровой корень числа n получается следующим образом: если сложить все цифры этого числа, затем все цифры
# найденной суммы и повторить этот процесс, то в результате будет получено однозначное число (цифра), которое
# и называется цифровым корнем данного числа.

# Примечание. Используйте вложенные циклы while.
# Example: Input: 192, Output: 3
# n = int(input())
# while n > 9:
#     summ = 0
#     while n > 0:
#         summ += n % 10
#         n //= 10
#     n = summ
# print(n)

'''Необходимо находить сумму всех цифр числа, пока конечный результат будет
не более 9. Дополнительная переменная необязательна. Если число однозначное,
то сумма его цифр равна самому числу. Для простоты программы, мы просто отделяем
последнюю цифру от числа и прибавляем к оставшимся. Например, для числа 129:
"разрезаем" его на 12 и 9, складываем и получаем 21. Повторяем еще раз, пока
конечная сумма будет не более 9.'''
# n = int(input())
# while n > 9:
#     n = n // 10 + n % 10
# print(n)

# n = int(input())
# while n > 9:
#     summ = 0
#     while n > 0:
#         summ += n % 10
#         n //= 10
#     n = summ
# print(n)

'''У цифрового корня есть свойство:
если из суммы всех цифр вычитать 9 до тех пор, пока не получится одна цифра, она и будет корнем.'''
# n = int(input())
# s = 0
# while n > 0:
#   s += n%10
#   if s > 9:
#     s -= 9
#   n //= 10
# print(s)

'''Цифровой корень это число по модулю 9 или же в случае, если число делится на 9 нацело, то цифровой корень это 9'''
# n = int(input())
# if n % 9 != 0:
#     print(n % 9)
# else:
#     print(9)

# Сумма факториалов
# Дано натуральное число n. Напишите программу, кот. выводит значение суммы 1!+2!+3!+…+n!.
# Примечание 1. Факториалом натурального числа n называется произведение всех натуральных чисел от 1 до n, то есть
# n!=1⋅2⋅3⋅…⋅n
# Примечание 2. Задачу можно решить без вложенного цикла. Напишите две версии программы =)
'''factorials_sum = 0
for i in range(1, int(input()) + 1):
    factorial = 1
    for j in range(1, i + 1):
        factorial *= j
    factorials_sum += factorial
print(factorials_sum)'''

'''sum_of_factorials, factorial = 0, 1
for i in range(1, int(input()) + 1):
    factorial *= i
    sum_of_factorials += factorial
print(sum_of_factorials)'''

# Простые числа
# На вход программе подается два натуральных числа a и b (a < b). Напишите программу, кот. находит все простые числа
# от a до b включительно.
# Примечание. Число 1 простым не является. Простые числа делятся только на 1 и на себя само.
# a, b = int(input()), int(input())
# for i in range(a, b + 1):
#     for j in range(2, i):
#         if i % j == 0:
#             continue
#         else:
#             print(i)



    # if i % 2 == 0:
    #     continue
    # if i == 1:
    #     continue
    # else:
    #     print(i)