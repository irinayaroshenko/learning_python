# eng_lower_abc = 'abcdefghijklmnopqrstuvwxyz'
# eng_upper_abc = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# ru_lower_abc = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
# ru_upper_abc = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"

# print(len(eng_lower_abc))
# print(chr(ord(eng_lower_abc[0])), ord(eng_lower_abc[0]))
# print(chr(ord(eng_lower_abc[10])), ord(eng_lower_abc[10]))
# print(eng_lower_abc[(eng_lower_abc.find('a') + 10) % 26])

# Encrypt_en
# str_to_encr, k = input(), int(input())
# n = len(eng_lower_abc)
# encrypted = ''

# for i in str_to_encr:
#     if i.isalpha():
#         if i.islower():
#             encrypted += eng_lower_abc[(eng_lower_abc.find(i) + k) % n]
#         if i.isupper():
#             encrypted += eng_upper_abc[(eng_upper_abc.find(i) + k) % n]
#     else:
#         encrypted += i


# Decrypt_en
# str_to_decr, k = input(), int(input())
# n = len(eng_lower_abc)
# encrypted = ''
# for i in str_to_decr:
#     if i.isalpha():
#         if i.islower():
#             encrypted += eng_lower_abc[(eng_lower_abc.find(i) - k) % n]
#         if i.isupper():
#             encrypted += eng_upper_abc[(eng_upper_abc.find(i) - k) % n]
#     else:
#         encrypted += i
#
# print(encrypted)

# Decrypt function for En
# Day, mice. "Year" is a mistake!

# Encrypt_ru
# encr_ru = input()
# k = int(input())
# n = len(ru_lower_abc)
# encrypted = ''
#
# for i in encr_ru:
#     if i.isalpha():
#         if i.islower():
#             encrypted += ru_lower_abc[(ru_lower_abc.find(i) + k) % n]
#         if i.isupper():
#             encrypted += ru_upper_abc[(ru_upper_abc.find(i) + k) % n]
#     else:
#         encrypted += i
#         continue


# Decrypt_ru
# decr_ru = input()
# k = int(input())
# n = len(ru_lower_abc)
# decrypted = ''
#
# for i in decr_ru:
#     if i.isalpha():
#         if i.islower():
#             decrypted += ru_lower_abc[(ru_lower_abc.find(i) - k) % n]
#         if i.isupper():
#             decrypted += ru_upper_abc[(ru_upper_abc.find(i) - k) % n]
#     else:
#         decrypted += i
#         continue
#
# print(decrypted)


'''
Аве, Цезарь 🌶️
На вход программе подается строка текста на английском языке, в которой нужно зашифровать все слова.
Каждое слово строки следует зашифровать с помощью шифра Цезаря (циклического сдвига на длину этого слова).
Строчные буквы при этом остаются строчными, а прописные – прописными.
Примечание. Символы, не являющиеся английскими буквами, не изменяются.

Тестовые данные
Sample Input 1: Day, mice. "Year" is a mistake!
Sample Output 1: Gdb, qmgi. "Ciev" ku b tpzahrl!
Sample Input 2: my name is Python!
Sample Output 2: oa reqi ku Veznut!
'''
# eng_lower_abc = 'abcdefghijklmnopqrstuvwxyz'
# eng_upper_abc = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
#
# str_to_encr = input().split()
# n = len(eng_lower_abc)
# encrypted = ''
#
# for i in str_to_encr:
#     count = 0
#     for j in i:
#         if j.isalpha():
#             count += 1
#
#     for k in i:
#         if k.isalpha():
#             if k.islower():
#                 encrypted += eng_lower_abc[(eng_lower_abc.find(k) + count) % n]
#             if k.isupper():
#                 encrypted += eng_upper_abc[(eng_upper_abc.find(k) + count) % n]
#         else:
#             encrypted += k
#     encrypted += " "
# print(encrypted)

# Other solution
# abc = 'abcdefghijklmnopqrstuvwxyz'
# ABC = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# s = input().split()
# string = ''
#
# for e in s:
#     step = len([i for i in e if i.isalpha()])
#     for c in e:
#         if c in abc:
#             string += abc[(abc.find(c) + step) % 26]
#         elif c in ABC:
#             string += ABC[(ABC.find(c) + step) % 26]
#         else:
#             string += c
#     string += ' '
#
# print(string[:-1])


# Transform binary number and others to 10-base system numbers
'''
https://stepik.org/lesson/349851/step/9?unit=333706 Theory on bin, oct, hex
'''
# print(int('111111', base=2))
# print(int('2AF', base=16))
# print(int('1AF2', base=16))
# print(0x1AF2)
# print(bin(513))
#
# print(bin(10))  # 0b1010 приставка 0b сигнализирует о том, что число представлено в двоичной системе счисления
# print(oct(150))  # 0o226 приставка 0o сигнализирует о том, что число представлено в восьмеричной системе счисления
# print(hex(18765))  # 0x494d приставка 0x сигнализирует о том, что число представлено в шестнадцатеричной системе счисления

'''
Примечания
Примечание 1. Если нам требуется избавиться от приставок 0b, 0o, 0x, то мы можем воспользоваться строковым срезом:

num = 127

bin_num = bin(num)  # 0b1111111
oct_num = oct(num)  # 0o177
hex_num = hex(num)  # 0x7f

print(bin_num[2:])  # 1111111
print(oct_num[2:])  # 177
print(hex_num[2:])  # 7f
Примечание 2. Обратите внимание, что функция hex() возвращает шестнадцатеричное число с маленькими символами
a, b, c, d, e, f. Для преобразования к верхнему регистру можно использовать строковый метод upper():

num = 127432

hex_num = hex(num)          # 0x1f1c8
print(hex_num[2:].upper())  # 1F1C8
'''


'''
BOH
На вход программе подается натуральное число в десятичной системе счисления.
Напишите программу, которая переводит его в двоичную, восьмеричную и шестнадцатеричную системы счисления.

Примечание 1. Используйте встроенные функции bin(), oct(), hex().
Примечание 2. Для шестнадцатеричной системы счисления используйте заглавные буквы A, B, C, D, E, F.
Примечание 3. BOH = Binary, Octal, Hex.
'''
# def bon(number):
#     bin_num = bin(number)
#     oct_num = oct(number)
#     hex_num = hex(number)
#     return bin_num[2:], oct_num[2:], hex_num[2:].upper()
#
#
# n = int(input())
# print(*bon(n), sep="\n")


'''
Угадайка слов
Описание проекта: программа загадывает слово, а пользователь должен его угадать. Изначально все буквы слова неизвестны.
Также рисуется виселица с петлей. Пользователь предлагает букву, которая может входить в это слово.
Если такая буква есть в слове, то программа ставит букву столько раз, сколько она встречается в слове.
Если такой буквы нет, к виселице добавляется круг в петле, изображающий голову.
Пользователь продолжает отгадывать буквы до тех пор, пока не отгадает всё слово.
За каждую неудачную попытку добавляется еще одна часть туловища висельника (обычно их 6: голова, туловище, 2 руки, 2 ноги)

Составляющие проекта:
Целые числа (тип int);
Переменные;
Ввод / вывод данных (функции input() и print());
Условный оператор (if/elif/else);
Цикл while;
Бесконечный цикл;
Операторы break, continue;
Создание пользовательских функций;
Списочные выражения;
Работа с модулем random для генерации случайных чисел.
'''
from random import choice
from time import sleep
word_list = ['сердце', 'движение', 'материал', 'неделя', 'чувство', 'газета',
        'причина', 'основа', 'товарищ', 'культура', 'данные', 'мнение', 'документ',
        'институт', 'проект', 'встреча', 'директор', 'служба', 'судьба', 'девушка',
        'очередь', 'состав', 'количество', 'событие', 'объект', 'создание', 'значение',
        'период', 'искусство', 'структура', 'пример', 'исследование', 'гражданин',
        'начальник', 'принцип', 'воздух', 'характер', 'борьба', 'использование',
        'размер', 'образование', 'мальчик', 'представитель', 'участие', 'девочка',
        'политика', 'картина', 'доллар', 'территория', 'изменение', 'направление',
        'рисунок']


def get_word():
    return choice(word_list).upper()


# функция получения текущего состояния
def display_hangman(tries):
    stages = [  # финальное состояние: голова, торс, обе руки, обе ноги
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                ''',
                # голова, торс, обе руки, одна нога
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                ''',
                # голова, торс, обе руки
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                ''',
                # голова, торс и одна рука
                '''
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                ''',
                # голова и торс
                '''
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                ''',
                # голова
                '''
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                ''',
                # начальное состояние
                '''
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                '''
    ]
    return stages[tries]


def again():
    answer = input('Хотите сыграть снова? д/Д или н/Н\n').lower()
    if answer == 'д':
        return play(get_word())
    elif answer == 'н':
        return print('Спасибо за игру!')


def play(word):
    word_completion = '_' * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6
    wait = 0.5

    print('Давайте играть в угадайку слов!')
    sleep(wait)
    print('У вас 6 попыток и виселица пока пуста\n', display_hangman(tries))
    sleep(wait)
    print(f'Слово состоит из {len(word)} букв: {word_completion}')
    sleep(wait)

    while not guessed and tries != 0:
        a = input('Введите букву или слово целиком на русском: ').upper()
        sleep(wait)
        while not a.isalpha():
            print('--Введен некорректный символ/-лы или другой язык--')
            sleep(wait)
            a = input('Введите букву или слово целиком на русском: ').upper()

        while word_completion != word:
            if len(a) == 1:
                if a in guessed_letters:
                    print(f'Эту букву вы уже называли: {guessed_letters}.\nОсталось {tries} попыток.\n{word_completion}')
                    break
                elif a in word and a not in word_completion:
                    for i in range(len(word)):
                        if word[i] == a:
                            word_completion = word_completion[:i] + a + word_completion[i + 1:]
                    guessed_letters.append(a)
                    print(f'Вы угадали. Эта буква есть в слове:\n{word_completion}.\nОсталось {tries} попыток.'
                          f'\nНазванные буквы: {guessed_letters}')
                    if word_completion == word:
                        guessed = True
                        break
                    break
                elif a not in word:
                    print('Такой буквы нет в загаданном слове.')
                    guessed_letters.append(a)
                    tries -= 1
                    print(display_hangman(tries), f'\nОсталось {tries} попыток.\n{word_completion}'
                                                  f'\nНазванные буквы: {guessed_letters}')
                    break
            elif len(a) > 1:
                if a != word:
                    guessed_words.append(a)
                    tries -= 1
                    print(f'Это неверное слово..\nОсталось {tries} попыток.\n{word_completion}'
                          f'\nНазванные буквы: {guessed_letters}')
                    print(display_hangman(tries))
                    break
                elif a in guessed_words:
                    print(f'Это слово вы уже называли: {guessed_words}.\nОсталось {tries} попыток.\n{word_completion}')
                    break
                else:
                    guessed = True
                    break

    if tries == 0:
        print(display_hangman(tries))
        print(f'Вы не угадали :(\nЗагаданное слово - {word}')
        sleep(wait)
        again()

    if guessed:
        print(f'Поздравляем, вы угадали слово! Вы победили!\nУгаданное слово - {word}.')
        sleep(wait)
        again()


# play(get_word())


# guessed = False
# tries = 5
# while not guessed and tries != 0:
#     a = int(input())
#     tries = 5
#     if a > 5:
#         print('Still False')
#     elif a == 5:
#         tries -= 5
#     else:
#         print('Guessed is True')
#         guessed = True
# print('Finish')


# word = 'abcabca'
# w_compl = '_______'
# while word != w_compl:
#     a = input('Give letter: ')
#     if a in word and a not in w_compl:
#         # while word.count(a) != w_compl.count(a):
#         for i in range(len(word)):
#             if word[i] == a:
#                 w_compl = w_compl[:i] + a + w_compl[i + 1:]
#         print(w_compl, word)

'''
Задача 01 из ITEA.
Lesson 1, video 02:49:08

Копейки
На вход подается целое число от 1 до 99.
Надо вывести правильное склонение:
1 - копейка
2, 3, 4 - копейки
5, 6, 7, 8, 9, 0 ... 11, 12, 13 ... 20, 30, 40 ... 90 - копеек
Например:
У вас 1 копейка.
У вас 2 копейки.
У вас 5 копеек.
У вас 11 копеек.
У вас 31 копейка.
У вас 55 копеек.
'''
# n = int(input("How many coins do you have?\n"))
# ka, jki, eek = 'копейка', 'копейки', 'копеек'
# if 5 <= n <= 20:
#     print(f'У вас {n} {eek}.')
# elif n % 10 == 1:
#     print(f'У вас {n} {ka}.')
# elif 2 <= n % 10 <= 4:
#     print(f'У вас {n} {jki}.')
# else:
#     print(f'У вас {n} {eek}.')

# With 3 conditions
# coins = int(input())
# if 4 < coins < 21 or 4 < coins % 10 < 10 or coins % 10 == 0:
#     print(coins, 'копеек')
# elif coins % 10 == 1:
#     print(coins, 'копейка')
# elif 1 < coins % 10 < 5:
#     print(coins, 'копейки')

# for i in range(1, 100):
#     ka, jki, eek = 'копейка', 'копейки', 'копеек'
#     if 5 <= i <= 20:
#         print(f'У вас {i} {eek}.')
#     elif i % 10 == 1:
#         print(f'У вас {i} {ka}.')
#     elif 2 <= i % 10 <= 4:
#         print(f'У вас {i} {jki}.')
#     else:
#         print(f'У вас {i} {eek}.')


'''
Задача из ITEA.
Lesson 1, video 02:53:04

Гривны и копейки
На вход подается два целых числа: гривны (от 1 до 999) и копейки (от 0 до 99).
Вывести введенное количество и правильное склонение.
Пример:
1, 85 - 1 гривна 85 копеек или 1 гривна, 85 копеек
568, 20 - 568 гривен 20 копеек
0, 24 - 24 копейки
173, 0 - 173 гривны
0, 0 - У вас нет денег :(
'''
def coins(coins):
    ka, jki, eek = 'копейка', 'копейки', 'копеек'
    if 4 < coins < 21 or 4 < coins % 10 < 10 or coins % 10 == 0:
        print(coins, eek)
    elif coins % 10 == 1:
        print(coins, ka)
    elif 1 < coins % 10 < 5:
        print(coins, jki)


def hryvnya(hrn):
    na, ny, ven = 'гривна', 'гривны', 'гривен'
    if 4 < hrn < 21 or 4 < hrn % 10 < 10 or hrn % 10 == 0:
        print(hrn, ven, end=', ')
    elif hrn % 10 == 1:
        print(hrn, na, end=', ')
    elif 1 < hrn % 10 < 5:
        print(hrn, ny, end=', ')


hr, kop = int(input()), int(input())
if hr > 0 and kop > 0:
    hryvnya(hr), coins(kop)
elif hr > 0 and kop < 1:
    hryvnya(hr)
    # if 4 < hr < 21 or 4 < hr % 10 < 10 or hr % 10 == 0:
    #     print(hr, ven)
    # elif hr % 10 == 1:
    #     print(hr, na)
    # elif 1 < hr % 10 < 5:
    #     print(hr, ny)
elif hr < 1 and kop > 0:
    coins(kop)
    # if 4 < coins < 21 or 4 < coins % 10 < 10 or coins % 10 == 0:
    #     print(coins, eek)
    # elif coins % 10 == 1:
    #     print(coins, ka)
    # elif 1 < coins % 10 < 5:
    #     print(coins, jki)
else:
    print('У вас нет денег :(')
