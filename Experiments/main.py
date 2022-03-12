from fu import *


def main():
    score = 0

    print('Введите ваше имя')
    user_name = input()

    words = get_word_from_file('c:\PyProjects\First\words')

    for word in words:

        word_shuffled = shuffle_word(word)
        print(f'Угадайте слово: {word_shuffled}')

        user_input = input()

        if user_input == word:
            score += 10
            print('Верно')
        else:
            print(f'Неверно! Верный ответ – {word}.')

    save_player_score('c:\PyProjects\First\history', user_name, score)
    get_statistics_from_file('c:\PyProjects\First\history')

main()



