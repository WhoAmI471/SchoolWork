from random import *

morze = {
    "a": ".-",
    "b": "-...",
    "c": "-.-.",
    "d": "-..",
    "e": ".",
    "f": "..-.",
    "g": "--.",
    "h": "....",
    "i": "..",
    "j": ".---",
    "k": "-.-",
    "l": ".-..",
    "m": "--",
    "n": "-.",
    "o": "---",
    "p": ".--.",
    "q": "--.-",
    "r": ".-.",
    "s": "...",
    "t": "-",
    "u": "..-",
    "v": "...-",
    "w": ".--",
    "x": "-..-",
    "y": "-.--",
    "z": "--..",
}
words = ['code', 'bit', 'list', 'soul', 'next']
answers = []

input(
    'Сегодня мы потренируемся расшифровывать азбуку Морзе\n'
    'Нажмите Enter и начнем'
    )

def get_word(words):
    sentence = choice(words)
    return sentence

def morse_encode(sentence):
    word = ''
    for i in sentence:
        word += morze[i]
        word += ' '
    return word

def print_statistics(answers):
    right = 0
    Wrong = 0

    for i in answers:
        if i:
            right += 1
        elif not i:
            Wrong += 1

    print(f'Всего задачек: {len(words)}')
    print(f'Отвечено верно: {right}')
    print(f'Отвечено неверно: {Wrong}')

for i in range(len(words)):
    get = get_word(words)
    print(f'Слово {i + 1} - {morse_encode(get)}')
    user_input = input()
    user = ''

    for i in user_input:
        user += morze[i]
        user += ' '

    if user == morse_encode(get):
        print(f'Верно, {get}!')
        answers.append(True)
    else:
        print(f'Неверно, {get}!')
        answers.append(False)

print_statistics(answers)


