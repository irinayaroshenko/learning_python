# Strings
# Note: переменные можно объявлять не давая им значения:
# s: str # строковая
# i: int # целая
# f: float # вещественная
# b: bool # булевая
# print('"Python is a great language!", ' + 'said Fred. ' + '"I ' + "don't" + ' ever remember having this much fun before."')

# firstname = input()
# lastname = input()
# print("Hello " + firstname + " " + lastname + "!" + " " + "You just delved into Python")
# print(f"Hello {firstname} {lastname}! You just delved into Python")

# fc = input()
# print("Футбольная команда " + fc + " имеет длину " + str(len(fc)) + " символов")
# print(f"Футбольная команда {fc} имеет длину {len(fc)} символов")


# Три города
# Даны названия трех городов. Напишите программу, кот. определяет самое короткое и самое длинное название города
# Примечание. Гарантируется, что длины названий всех трех городов различны.
# city1, city2, city3 = input(), input(), input()
# short = min(len(city1), len(city2), len(city3))
# long = max(len(city1), len(city2), len(city3))
# if len(city1) == short:
#     if len(city2) == long:
#         print(city1, city2, sep="\n")
#     else:
#         print(city1, city3, sep="\n")
#
# if len(city2) == short:
#     if len(city1) == long:
#         print(city2, city1, sep="\n")
#     else:
#         print(city2, city3, sep="\n")
#
# if len(city3) == short:
#     if len(city1) == long:
#         print(city3, city1, sep="\n")
#     else:
#         print(city3, city2, sep="\n")

# Use 'key=len' to print string value of min or max
# print(min(city1, city2, city3, key=len))

# Арифметические строки
# Вводятся 3 строки в случайном порядке. Напишите программу, кот. выясняет можно ли из длин этих строк построить
# возрастающую арифметическую прогрессию.
# Formula: (2b-c-a)(2c-b-a)(2a-b-c) = 0
# a, b, c = input(), input(), input()
# min_value = min(len(a), len(b), len(c))
# max_value = max(len(a), len(b), len(c))
# mid_value = (len(a) + len(b) + len(c)) - (min_value + max_value)
# if mid_value - min_value == max_value - mid_value:
#     print("YES")
# else:
#     print("NO")
# print(min_value, mid_value, max_value)

# Other solution
# a, b, c = len(input()), len(input()), len(input())
# middle = (a + b + c) - (max(a, b, c) + min(a, b, c))
# if max(a, b, c) - middle == middle - min(a, b, c):
#     print("YES")
# else:
#     print("NO")

# Better solution
# a, b, c = len(input()), len(input()), len(input())
# if (a + b + c) % 3 == 0:
#     print("YES")
# else:
#     print("NO")

# Цвет настроения синий
# Напишите программу, кот. считывает одну строку, после чего выводит «YES», если в введенной строке есть
# подстрока «синий» и «NO» в противном случае.
# s = input()
# if "синий" in s:
#     print("YES")
# else:
#     print("NO")

# Отдыхаем ли?
# Напишите программу, которая считывает одну строку, после чего выводит «YES», если в введённой строке
# есть подстрока «суббота» или «воскресенье», и «NO» в противном случае.
# s = input()
# if "суббота" in s or "воскресенье" in s:    # pay attention!!! 'in s' need to be used twice
#     print("YES")
# else:
#     print("NO")

# Корректный email
# Будем считать email адрес корректным, если в нем есть символ собачки (@) и точки.
# Напишите программу проверяющую корректность email адреса.
# На вход программе подаётся одна строка – email адрес.
# Программа должна вывести строку «YES», если email адрес является корректным и «NO» в ином случае.
# Примечание. Наличие символов @ и . недостаточно для корректности email адреса,
# однако их отсутствие гарантировано влечёт за собой неверный email.
email_address = input()
if "@" in email_address and "." in email_address:
    print("YES")
else:
    print("NO")
