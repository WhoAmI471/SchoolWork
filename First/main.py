from work_functions import *


def main():
    score = 0

    print('Введите ваше имя')
    user_name = input()

    words = get_word('words.txt')

    for word in words:

        word_shuffled = shuffle_word(word)
        print(f'Угадайте слово: {word_shuffled}')

        user_input = input()

        if user_input == word:
            score += 10
            print('Верно! Вы получаете 10 очков.')
        else:
            print(f'Неверно! Верный ответ – {word}.')

    save_score('history.txt', user_name, score)

    statistics = get_statistics('history.txt')

    print(
        f'Всего игр сыграно: {statistics.get("len")}\n'
        f'Максимальный рекорд: {statistics.get("max")}'
    )

main()