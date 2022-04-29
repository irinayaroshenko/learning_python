import random
from time import sleep

# again = 'д'
# while again.lower() == 'д':
#     print('Бросаем кубики... ')
#     print('Значения граней:')
#     print(random.randint(1, 6))
#     print(random.randint(1, 6))
#     again = input('Бросить кубики еще раз? (д = да, н = нет): ')

# num = random.getrandbits(10)
# print(num)

'''
Угадайка чисел
Описание проекта: программа генерирует случайное число в диапазоне от 1 до 100 и просит пользователя угадать это
число. Если догадка пользователя больше случайного числа, то программа должна вывести сообщение
'Слишком много, попробуйте еще раз'. Если догадка меньше случайного числа, то программа должна вывести сообщение
'Слишком мало, попробуйте еще раз'. Если пользователь угадывает число, то программа должна поздравить его и вывести
сообщение 'Вы угадали, поздравляем!'.
'''
# num = random.randint(1, 100)
# guess = int(input("Guess the number: "))
#
# while True:
#     if guess > num:
#         guess = int(input("Слишком много, попробуйте еще раз"))
#     elif guess < num:
#         guess = int(input("Слишком мало, попробуйте еще раз"))
#     else:
#         print("Вы угадали, поздравляем!")
#         break

# def guess_number():
#     guess = int(input("Guess the number: "))
#     left = 1
#     right = 100
#     middle = (left + right) // 2
#     number = random.randint(1, 100)
#     while True:
#         if number == middle:
#             return "Вы угадали, поздравляем!"
#             # print("Вы угадали, поздравляем!")
#             # break
#         elif middle < number:
#             left = middle + 1
#             middle = (left + right) // 2
#             number = int(input("Слишком мало, попробуйте еще раз"))
#         else:
#             right = middle - 1
#             middle = (left + right) // 2
#             number = int(input("Слишком мало, попробуйте еще раз"))


# guess = int(input("Guess the number: "))
# print(guess_number())

# def is_valid(str_input):
#     return str_input.isdigit() and 0 < int(str_input) < 101
#
#
# num = random.randint(1, 100)
# try_count = 1
# print('Добро пожаловать в числовую угадайку')
#
# while True:
#     guess = input('Введите целое число от 1 до 100: ')
#     if is_valid(guess):
#         guess = int(guess)
#         break
#     else:
#         print('А может быть все-таки введем целое число от 1 до 100?')
#
# while guess != num:
#     if guess < num:
#         try_count += 1
#         guess = int(input('Ваше число меньше загаданного, попробуйте еще разок:\n'))
#     else:
#         try_count += 1
#         guess = int(input('Ваше число больше загаданного, попробуйте еще разок:\n'))
#
# print(f'Вы угадали с {try_count} попыток, поздравляем!\nСпасибо, что играли в числовую угадайку. Еще увидимся...')



'''
Тимур и его числа
Тимур загадал число от 1 до n. За какое наименьшее количество вопросов (на которые Тимур отвечает "больше" или "меньше")
Руслан может гарантированно угадать число Тимура?
Формат входных данных
На вход программе подается натуральное число n.
Формат выходных данных
Программа должна вывести наименьшее количество вопросов, которых гарантированно хватит Руслану, чтобы угадать число Тимура.

Поскольку на каждой итерации мы отбрасываем половину чисел, то гарантировано угадаем задуманное число за величину,
равную log2(n) (двоичный логарифм) округленную до целого в большую сторону
'''
# from math import log2, ceil
# n = int(input())
# questions = log2(n)
# print(ceil(questions))


'''
Магический шар 8
Описание проекта: магический шар 8 (шар судьбы) — шуточный способ предсказывать будущее.
Программа должна просить пользователя задать некий вопрос, чтобы случайным образом на него ответить.
'''
# answers = ["Бесспорно", "Мне кажется - да", "Пока неясно, попробуй снова", "Даже не думай",
#            "Предрешено", "Вероятнее всего", "Спроси позже", "Мой ответ - нет",
#            "Никаких сомнений", "Хорошие перспективы", "Лучше не рассказывать", "По моим данным - нет",
#            "Можешь быть уверен в этом", "Да", "Сконцентрируйся и спроси опять", "Весьма сомнительно"]
# print("Привет Мир, я магический шар, и я знаю ответ на любой твой вопрос.")
# name = input("Как тебя зовут?\n")
# print(f"Привет, {name.title()}!")
#
# while True:
#     ask_question = input("Что бы ты хотел узнать?\n")
#     print(random.choice(answers))
#     next_question = input("Хочешь задать другой вопрос? (Ответ: Да/да или Нет/нет)\n")
#     if next_question.lower() == "да":
#         continue
#     elif next_question.lower() == "нет":
#         print("Возвращайся если возникнут вопросы!")
#         break
    # else:
    #     next_question = input("Не совсем понятен твой ответ. Хочешь задать другой вопрос? (Ответ: Да/да или Нет/нет)\n")



# def magic_ball():
#     answers = ["Бесспорно", "Мне кажется - да", "Пока неясно, попробуй снова", "Даже не думай",
#                "Предрешено", "Вероятнее всего", "Спроси позже", "Мой ответ - нет",
#                "Никаких сомнений", "Хорошие перспективы", "Лучше не рассказывать", "По моим данным - нет",
#                "Можешь быть уверен в этом", "Да", "Сконцентрируйся и спроси опять", "Весьма сомнительно"]
#     print("Привет Мир, я магический шар, и я знаю ответ на любой твой вопрос.")
#     name = input("Как тебя зовут, друг?\n")
#     print(f"Привет, {name.title()}!")
#
#     while True:
#         ask_question = input("Что бы ты хотел узнать?\n")
#         print(f"Ответом на твой вопрос '{ask_question}' будет: {random.choice(answers)}")
#         next_question = input("Хочешь задать другой вопрос? (Ответ: Да/да или Нет/нет)\n")
#         if next_question.lower() == "да":
#             continue
#         elif next_question.lower() == "нет":
#             return print("Возвращайся если возникнут вопросы!")


'''Password Generator'''

# digits = '0123456789'
# lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
# uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# punctuation = '!#$%&*+-=?@^_()'
# chars = ''
#
# quantity = int(input('How many passwords do You want to generate?\n'))
# sleep(0.1)
# length = int(input('How many symbols should be in a password?\n'))
# sleep(0.1)
# ask_digits = input(f"Do You want to use digits {digits} in your password? (Y/y - yes, N/n - no)\n")
# sleep(0.1)
# ask_low_lett = input("Do You want to use lowercase letters? (Y/y - yes, N/n - no)\n")
# sleep(0.1)
# ask_up_lett = input("Do You want to use UPPERCASE letters? (Y/y - yes, N/n - no)\n")
# sleep(0.1)
# ask_punc = input(f"Do You want to use punctuation {punctuation}? (Y/y - yes, N/n - no)\n")
# sleep(0.1)
# ask_vcc = input("Do You want to exclude Visually Confusable Characters like 'il1Lo0O'? (Y/y - yes, N/n - no)\n")
#
# if ask_digits.lower() == 'y':
#     chars += digits
# if ask_low_lett.lower() == 'y':
#     chars += lowercase_letters
# if ask_up_lett.lower() == 'y':
#     chars += uppercase_letters
# if ask_punc.lower() == 'y':
#     chars += punctuation
# if ask_vcc.lower() == 'y':
#     for c in 'il1Lo0O':
#         chars = chars.replace(c, '')


# def generate_password(length, chars):
#     return print(*(random.choice(chars) for _ in range(length)), sep="")
#
#
# for _ in range(quantity):
#     print(f"Your password {_ + 1}:")
#     generate_password(length, chars)


def data_for_password():
    digits = '0123456789'
    lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
    uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    punctuation = '!#$%&*+-=?@^_()'
    characters = ''

    ask_digits = input(f"Do You want to use digits {digits} in your password? (Y/y - yes, N/n - no)\n")
    sleep(0.1)
    ask_low_lett = input("Do You want to use lowercase letters? (Y/y - yes, N/n - no)\n")
    sleep(0.1)
    ask_up_lett = input("Do You want to use UPPERCASE letters? (Y/y - yes, N/n - no)\n")
    sleep(0.1)
    ask_punc = input(f"Do You want to use punctuation {punctuation}? (Y/y - yes, N/n - no)\n")
    sleep(0.1)
    ask_vcc = input("Do You want to exclude Visually Confusable Characters like 'il1Lo0O'? (Y/y - yes, N/n - no)\n")

    if ask_digits.lower() == 'y':
        characters += digits
    if ask_low_lett.lower() == 'y':
        characters += lowercase_letters
    if ask_up_lett.lower() == 'y':
        characters += uppercase_letters
    if ask_punc.lower() == 'y':
        characters += punctuation
    if ask_vcc.lower() == 'y':
        for c in 'il1Lo0O':
            characters = characters.replace(c, '')
    return characters


def generate_password(length, characters):
    print(*[random.choice(characters) for _ in range(length)], sep="")
    return print(random.shuffle(*[random.choice(characters) for _ in range(length)]), sep="")


quantity = int(input('How many passwords do You want to generate?\n'))
sleep(0.1)
length = int(input('How many symbols should be in a password?\n'))
sleep(0.1)
chars = data_for_password()
generate_password(length, chars)

for _ in range(quantity):
    print(f"Your password {_ + 1}:")
    generate_password(length, chars)
