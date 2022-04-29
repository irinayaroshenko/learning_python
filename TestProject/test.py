# import asyncio
#
# async def main():
#     print("Hello...")
#     await asyncio.sleep(1.5)
#     print("... World!")

# print("Hello World!")
# print("hello", "another", "word")
# print("1", "2", "3", "4")
# print()           # prints empty line
# print("Something else", "1 mln", "times")
# print("Hello, \"Windows\"")  # ekranirovanie. Put \ before element you want to be in text
# print("What's your name? ")
# name = input()
# print(name)

# print("a", "b", "c", sep="*")
# print("d", "e", "f", "g", sep="-")
# print("1", "2", "3", end="@_@")
# print("14", "5", "9", end="Here it is!\n")
# print('a', 'b', 'c', sep='*', end='_finish_')
# print('d', 'e', 'f', sep='**', end='^__^')
# print('g', 'h', 'i', sep='+', end='%')
# print('j', 'k', 'l', sep='-', end='#')
# print('m', 'n', 'o', sep='/', end='!\n')
# print('a', 'b', 'c', sep='', end='')
# print()
# print('Python', '\n', 'Rules', '\n', '4ever', sep='', end='!\n')
# print('Python\n', 'rules\n', '4ever', sep='', end='!')
# print()
# print('a', 'b', 'c', sep='*')
# print('d', 'e', 'f', sep='**', end='')
# print('g', 'h', 'i', sep='+', end='%')
# print('j', 'k', 'l', sep='-', end='\n')
# print('m', 'n', 'o', sep='/', end='!')
# print('p', 'q', 'r', sep='1', end='%')
# print('s', 't', 'u', sep='&', end='\n')
# print('v', 'w', 'x', sep='%')
# print('y', 'z', sep='/', end='!')

# separator = input()
# one = input()
# two = input()
# three = input()
# print(one, two, three, sep=separator)
#
# a, b, c = int(input()), int(input()), int(input())

# a = int(input())
# V = a ** 3
# S = 6 * a ** 2
# print(f"Объем = {V}")
# print(f"Площадь полной поверхности = {S}")

# a, b = int(input("Number_1 = ")), int(input("Number_2: "))
# print(f"Sum of {a} + {b} = {a+b}")

# x = 2 // 5
# print(x)
#
# b1, q, n = int(input()), int(input()), int(input())
# b_n = b1 * q ** (n -1)
# print(b_n)
#
# n, k = int(input()), int(input())
# students_get = k // n
# fruits_left_in_basket = k % n
# print(students_get)
# print(fruits_left_in_basket)

# Танос намеревается уничтожить половину населения Вселенной.
# если население является нечетным числом, то титан округлит количество выживших в большую сторону.
# My solution
# n = int(input())
#
# if n % 2 == 0:
#     print(f"{n // 2}")
# else:
#     print(f"{(n // 2) + 1}")

# Better solution from course
# k = int(input()) + 1
# print(f"{k // 2}")

# В купе-вагоне имеется 9 купе с 4 местами в каждом.
# Напишите прогу, кот. определяет номер купе, в кот. находится место с заданным номером (нумерация мест начинается с 1)

seat_number = int(input())
box_number = (seat_number + 3) // 4
print(box_number)


x = int(input())
y = int(input())
if x > 0:
    if y > 0:
        print('Первая четверть')
    else:
        print('Четвертая четверть')
else:
    if y > 0:
        print('Вторая четверть')
    else:
        print('Третья четверть')