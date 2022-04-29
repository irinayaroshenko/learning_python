'''
Максимум в таблице
На вход программе подаются два натур. числа n и m — количество строк и столбцов в матрице, затем n строк по m целых
чисел в каждой, отделенных символом пробела.
Напишите программу, кот. находит индексы (строку и столбец) первого вхождения максимального элемента.
Формат выходных данных
Программа должна вывести два числа: номер строки и номер столбца, в которых стоит наибольший элемент таблицы.
Если таких элементов несколько, то выводится тот, у которого меньше номер строки, а если номера строк равны то тот,
у которого меньше номер столбца.

Примечание. Считайте, что нумерация строк и столбцов начинается с нуля.
'''
# n, m = int(input()), int(input())
# matrix = [[int(j) for j in input().split()] for _ in range(n)]
# max_value = matrix[0][0]
# row, column = 0, 0
# for i in range(n):
#     for j in range(m):
#         if matrix[i][j] > max_value:
#             max_value = matrix[i][j]
#             row = i
#             column = j
# print(row, column)

# Other solution
# n, m = int(input()), int(input())
# nums = []
# for _ in range(n):
#     nums.extend(int(i) for i in input().split())
# print(nums.index(max(nums)) // m, nums.index(max(nums)) % m)

# To find max value of matrix wit max and key=
# val = max(max(matrix, key=max))
# print(val)

'''
Обмен столбцов
Напишите программу, кот. меняет местами столбцы в матрице.
На вход программе на разных строках подаются два натуральных числа n и m — количество строк и столбцов в матрице,
затем элементы матрицы построчно через пробел, затем числа i и j — номера столбцов, подлежащих обмену.
Input:
3
4
11 12 13 14
21 22 23 24
31 32 33 34
0 1
Output:
12 11 13 14
22 21 23 24
32 31 33 34
'''
# n, m = int(input()), int(input())
# matrix = [list(map(int, input().split())) for _ in range(n)]
# col1, col2 = (int(i) for i in input().split())
#
# for i in range(n):
#     matrix[i][col1], matrix[i][col2] = matrix[i][col2], matrix[i][col1]
# [print(*i) for i in matrix]

# Other solution
# n, m = int(input()), int(input())
# lst = [list(map(int, input().split())) for _ in range(n)]
# i, j = (map(int, input().split()))
# for k in lst:
#     k[i], k[j] = k[j], k[i]
#     print(*k)

'''
Симметричная матрица
Напишите программу, кот. проверяет симметричность квадратной матрицы относительно главной диагонали.

На вход программе подаётся натуральное число n — количество строк и столбцов в матрице, затем элементы матрицы построчно
через пробел.
Программа должна вывести YES, если матрица симметрична относительно главной диагонали, и слово NO в противном случае.
Input:
5
5 3 7 1 5
3 5 4 5 7
7 4 4 8 4
1 5 8 5 1
5 7 4 1 5
Output:
YES

Input:
3
0 1 2
1 2 7
2 3 4
Output:
NO
'''
# n = int(input())
# matrix = [list(map(int, input().split())) for _ in range(n)]
# matrix1 = [[matrix[j][i] for j in range(n)] for i in range(n)]
# if matrix == matrix1:
#     print('YES')
# else:
#     print('NO')

# My other solution
# def symmetric_matrix(mtrx, num):
#     for i in range(num):
#         for j in range(num):  # here better range(i + 1, num)
#             if mtrx[i][j] != mtrx[j][i]:
#                 return 'NO'
#     return 'YES'

# Other solution
# n = int(input())
# matrix = [input().split() for _ in range(n)]
# result = 'YES'
#
# for i in range(n):
#     for j in range(i + 1, n):
#         if matrix[i][j] != matrix[j][i]:
#             result = 'NO'
#             break
#     if result == 'NO':
#         break
# print(result)

'''
Обмен диагоналей
Дана квадратная матрица чисел. Напишите программу, кот. меняет местами элементы, стоящие на главной и побочной
диагонали, при этом каждый элемент должен остаться в том же столбце (то есть в каждом столбце нужно поменять местами
элемент на главной диагонали и на побочной диагонали).
Input:
3
1 2 3
4 5 6
7 8 9
Output:
7 2 9 
4 5 6 
1 8 3
Input2:
5
2 2 3 1 3
4 6 6 7 5
7 8 9 7 8
4 5 6 4 5
1 2 3 1 2
Output2:
1 2 3 1 2
4 5 6 4 5
7 8 9 7 8
4 6 6 7 5
2 2 3 1 3
'''
# n = int(input())
# matrix = [list(map(int, input().split())) for _ in range(n)]
# for i in range(n):
#     matrix[i][i], matrix[n - i - 1][i] = matrix[n - i - 1][i], matrix[i][i]
#
# [print(*i) for i in matrix]


'''
Зеркальное отображение
Дана квадратная матрица чисел. Напишите программу, кот. зеркально отображает её элементы относительно горизонтальной оси
симметрии.
Input:
4
1 2 3 4
5 6 7 8
8 6 4 2
3 4 5 6
Output:
3 4 5 6
8 6 4 2
5 6 7 8
1 2 3 4
Input2:
3
1 2 3
4 5 6
7 8 9
Output2:
7 8 9
4 5 6
1 2 3
'''
# n = int(input())
# matrix = [list(map(int, input().split())) for _ in range(n)]
#
# for i in range(n // 2):
#     matrix[i], matrix[n - i - 1] = matrix[n - i - 1], matrix[i]
# [print(*i) for i in matrix]

# Other solution
# n = int(input())
# matrix = [[int(_) for _ in input().split()] for _ in range(n)]
# matrix.reverse()
# for row in matrix:
#     print(*row)

'''
Поворот матрицы
Напишите программу, кот. поворачивает квадратную матрицу чисел на 90 град. по часовой стрелке.
На вход программе подаётся натуральное число n — количество строк и столбцов в матрице, затем элементы матрицы
построчно через пробел.
Input:
3
1 2 3
4 5 6
7 8 9
Output:
7 4 1 
8 5 2 
9 6 3
Input2:
4
1 9 4 2
3 8 1 5
6 7 4 6
1 9 7 8
Output2:
1 6 3 1
9 7 8 9
7 4 1 4
8 6 5 2
'''
# n = int(input())
# matrix = [list(map(int, input().split())) for _ in range(n)]
# matrix90 = [[matrix[n - j - 1][i] for j in range(n)] for i in range(n)]
# [print(*i) for i in matrix90]

# My other solution
# n = int(input())
# matrix = [list(map(int, input().split())) for _ in range(n)]
# for i in range(n):
#     for j in range(n):
#         print(matrix[n - j - 1][i], end=' ')
#     print()

# Other solution
# matrix = []
#
# for _ in range(int(input())):
#     matrix.append([int(x) for x in input().split()])
#
# for row in zip(*matrix[::-1]):
#     print(*row)

# Other solution
# n = int(input())
# matrix = [list(map(int, input().split())) for _ in range(n)]
# matrix1 = [[matrix[j][i] for j in range(n)] for i in range(n)]
# for i in matrix1:
#     print(*i[::-1])

'''
Ходы коня
На шахматной доске 8×8 стоит конь.
Напишите программу, кот. отмечает положение коня на доске и все клетки, которые бьет конь.
Клетку, где стоит конь, отметьте английской буквой N, клетки, которые бьет конь, отметьте символами *, остальные клетки
заполните точками.

Формат входных данных
На вход программе подаются координаты коня на шахматной доске в шахматной нотации (то есть в виде e4, где сначала
записывается номер столбца (буква от a до h, слева направо), затем номеру строки (цифра от 1 до 8, снизу вверх)).

Формат выходных данных
Программа должна вывести на экран изображение доски, разделяя элементы пробелами.
Input: f3
Output
. . . . . . . .
. . . . . . . .
. . . . . . . .
. . . . * . * .
. . . * . . . *
. . . . . N . .
. . . * . . . *
. . . . * . * .
'''
# matrix = [['.' for _ in range(8)] for _ in range(8)]
# abc = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7}
# horse = input()
# row_coord = abc[horse[0]]
# line_coord = 8 - int(horse[1])
#
# matrix[line_coord][row_coord] = 'N'
# # for i in matrix:
# #     print(*i)
#
# for i in range(8):
#     for j in range(8):
#         if abs(line_coord - i) == 2 and abs(row_coord - j) == 1:
#             matrix[i][j] = '*'
#         elif abs(line_coord - i) == 1 and abs(row_coord - j) == 2:
#             matrix[i][j] = '*'
#
# for i in matrix:
#     print(*i)
# n = int(input())
# lst = []
#
# for i in range(n):
#     k = int(input())
#     lst.append(k)
#
# print(lst)
#
# marks = [int(input()) for _ in range(int(input()))]
# if 0 in marks:
#     print("YES")
# else:
#     print("NO")
#
# print(max(marks))

tempr = [int(input()) for _ in range(int(input()))]

print(min(tempr))
print('YES' if min(tempr) < -15 else 'NO')
# if min(tempr) < -15:
#     print(min(tempr), 'NO')
# else:
#     print(min(tempr), 'YES')