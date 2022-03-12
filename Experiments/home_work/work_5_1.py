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
    'Нажмите Enter и начнем\n'
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
    answers_total = len(answers)
    answers_correct = sum(answers)
    answers_incorrect = answers_total - answers_correct
    
    print(
        f'Всего задачек: {answers_total}\n'
        f'Отвечено верно: {answers_correct}\n'
        f'Отвечено неверно: {answers_incorrect}\n'
        )

for i in range(len(words)):
    get = get_word(words)
    print(f'Слово {i + 1} - {morse_encode(get)}')
    user_input = input()

    if get == user_input:
        print(f'Верно, {get}!\n')
        answers.append(True)
    else:
        print(f'Неверно, {get}!\n')
        answers.append(False)

print_statistics(answers)



