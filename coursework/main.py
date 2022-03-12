from utils import load_random_word
from player import Player


def main():

    right = 0
    game_is_on = True
    main_word = load_random_word()

    user_name = input('Введите имя игрока\n')

    player = Player(user_name)

    print(f'\nПривет, {user_name}!')
    
    word = main_word.word
    count_word = main_word.count_subwords()

    print(
        f'Составьте {count_word} слов из слова {word}\n'
        'Слова должны быть не короче 3 букв\n'
        'Чтобы закончить игру, угадайте все слова или напишите "stop"\n'
        'Поехали, ваше первое слово?'
    )
    
    while game_is_on:
        
        user_input = input()

        if main_word.has_subword(user_input) and not player.has_uses(user_input):
            right += 1
            player.add_word(user_input)
            print('Верно')
        elif right == int(count_word) or user_input.lower() in ('stop','стоп'):
            game_is_on = False
            break 
        else:
            print('Неверно или это слово уже было')

    print(
        'Игра завершена!\n'
        f'Вы угадали {player.count_words()} слов!'
    )

        
main()