# В купе-вагоне имеется 9 купе с 4 местами в каждом.
# Напишите прогу, кот. определяет номер купе, в кот. находится место с заданным номером (нумерация мест нач. с 1)

# seat_number = int(input(">"))
# box_number = (seat_number + 3) // 4
# print(box_number)

# num_1 = int(input("Give me 2-digits number: "))
# first_digit_of_number = num_1 // 10
# second_digit_of_number = num_1 % 10
# print(f"First digit of number '{num_1}' is {first_digit_of_number}.")
# # print("First digit =", first_digit_of_number)
# print(f"Second digit of number '{num_1}' is {second_digit_of_number}.")
# # print("Second digit =", second_digit_of_number)
# print(f"Sum of digits for number '{num_1}' is {first_digit_of_number + second_digit_of_number}.")
# print("Sum of digits =", first_digit_of_number + second_digit_of_number)

# Напишите программу, которая печатает число, образованное при перестановке цифр двузначного числа
# num_2 = int(input("Your number: "))
# print("Vice versa number: ", num_2 % 10, num_2 // 10, sep="")
# print("Needed number:", (num_2 % 10) * 10 + num_2 // 10)

# Напишите программу, в кот. вводится трёхзначное число и кот. выводит на экран его цифры (через запятую)
# num_3 = int(input("Give me 3-digit number: "))
# dig1 = num_3 // 100
# dig2 = (num_3 % 100) // 10
# dig3 = num_3 % 10
# print("Number", num_3, "digits are:", dig1, dig2, dig3)
# print(dig1, dig2, dig3, sep=", ")

# same task but get numbers as str and access every digit as list
# num = input("Number: ")
# a = num[0]
# b = num[1]
# c = num[2]
# print(a, b, c, sep=", ")

# Последняя цифра: (num // 10**0) % 10
# Предпоследняя цифра: (num // 10**1) % 10
# Предпредпоследняя цифра: (num // 10**2) % 10
# .....
# Вторая цифра: (num // 10**(n-2)) % 10
# Первая цифра: (num // 10**(n-1)) % 10

# !!!!! Cool!
# a, b, c, d, e = input()
# print(a, b, c, d, e)

# one more case
# n = int(123)
# name1 = (n // 10**2) % 10
# name2 = (n // 10**1) % 10
# name3 = (n // 10**0) % 10
# print(name1, name2, name3)  # 1 2 3
# print(name3, name2, name1)  # 3 2 1

# number = int(input())
# print("Цифра в позиции тысяч равна", number // 1000)
# print("Цифра в позиции сотен равна", (number // 100) % 10)
# print("Цифра в позиции десятков равна", (number % 100) // 10)
# print("Цифра в позиции единиц равна", number % 10)

# программу, кот. считывает целое положит. число n,n∈[1;9] и выводит значение числа n+{nn}+{nnn}
# Пример: input = 1, output = 1 + 11 + 111 = 1231+11+111=123
# n = int(input())
# nn = n * 10 + n
# nnn = n * 100 + nn
# print(f"{n + nn + nnn}")

# other solution of task above
# a = input()
# a1 = int(a)
# a2 = int(a + a)
# a3 = int(a + a + a)
# print(a1 + a2 + a3)

# word = input()
# if word == "Python":
#     print("Yes")
# else:
#     print("No")
#
# number = int(input())
# a = number // 10
# b = number % 10
# if a == b:
#     print("Equal")
# else:
#     print("Not equal")

# Напишите программу, кот. считывает 3 числа и подсчитывает кол-во чётных чисел
# num1, num2, num3 = int(input()), int(input()), int(input())
# counter = 0
# if num1 % 2 == 0:
#     counter += 1
# if num2 % 2 == 0:
#     counter += 1
# if num3 % 2 == 0:
#     counter += 1
# print(counter)

# 2nd solution
# num1, num2, num3 = int(input()), int(input()), int(input())
# counter = int(num1 % 2 == 0) + int(num2 % 2 == 0) + int(num3 % 2 == 0)
# print(counter)

# 3rd solution
# num1, num2, num3 = int(input()), int(input()), int(input())
# odd_count = num1 % 2 + num2 % 2 + num3 % 2
# print(3 - odd_count)

# 4th solution
# n1, n2, n3 = int(input()), int(input()), int(input())
# a1 = n1 % 2
# a2 = n2 % 2
# a3 = n3 % 2
# print(3 - a1 - a2 - a3)

# Напишите программу, кот. проверяет, что для заданного 4-хзначного числа выполняется следующее соотношение:
# сумма первой и последней цифр равна разности второй и третьей цифр.
# num = int(input())
# n1 = num // 1000
# n2 = num // 100 % 10
# n3 = num % 100 // 10
# n4 = num % 10
# if n1 + n4 == n2 - n3:
#     print("ДА")
# else:
#     print("НЕТ")

# Напишите программу, кот. определяет наименьшее из 4 чисел
# bad solution
# a, b, c, d = int(input()), int(input()), int(input()), int(input())
# if a < b and a < c and a < d:
#     print(a)
# if b < c and b < d and b < a:
#     print(b)
# if c < d and c < a and c < b:
#     print(c)
# if d < a and d < b and d < c:
#     print(d)

# better solution
# a, b, c, d = int(input()), int(input()), int(input()), int(input())
# ab = 0
# cd = 0
# if a < b:
#     ab = a
# else:
#     ab = b
# if c < d:
#     cd = c
# else:
#     cd = d
# if ab < cd:
#     print(ab)
# else:
#     print(cd)

# better solution
# a, b, c, d = int(input()), int(input()), int(input()), int(input())
# if a < b:
#     a = a
# else:
#     a = b
# if c < d:
#     c = c
# else:
#     c = d
# if a < c:
#     print(a)
# else:
#     print(c)

# Напишите программу, кот, считывает 3 числа и подсчитывает сумму только положительных чисел
# a, b, c = int(input()), int(input()), int(input())
# if a > 0:
#     a = a
# else:
#     a = 0
# if b > 0:
#     b = b
# else:
#     b = 0
# if c > 0:
#     c = c
# else:
#     c = 0
# n = a + b + c
# if n > 0:
#     print(n)
# else:
#     print(0)

# Напишите программу, кот. определяет, является ли заданное натуральное число 3-значным
# n = int(input())
# if 99 < n < 1000:
#     print("It's 3-digit number.")
# else:
#     print("It's NOT a 3-digit number.")

# Напишите программу, кот. проверяет, что все 3 цифры натурального 3-значного числа различны
n = int(input())
n1 = n // 100
n2 = (n % 100) // 10
n3 = n % 10
if (n1 != n2 and n1 != n3) and n2 != n3:
    print("All digits are different.")
else:
    print(f"Some digits in {n} are the same.")

# Напишите программу, кот. по координатам точки, не лежащей на осях координат, определяет номер координатной четверти,
# в кот. она находится
x = int(input())
y = int(input())

if x > 0 and y > 0:
    print("1st Quarter.")
if x < 0 and y > 0:
    print("2nd Quarter.")
if x < 0 and y < 0:
    print("3rd Quarter.")
if x > 0 and y < 0:
    print("4th Quarter.")

