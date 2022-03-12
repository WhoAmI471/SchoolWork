from random import *


def get_word(path):
    with open(path, 'r', encoding='utf-8') as file:
        lines = file.read()
        words = lines.splitlines()
    return words

def shuffle_word(word):
    word_list = list(word)
    shuffle(word_list)
    return ''.join(word_list)

def save_score(path, player_name, player_score):
    with open(path, 'a', encoding='utf-8') as file:
        file.write(f'{player_name} {player_score}\n')

def get_statistics(path):
    scores = []

    with open(path, 'r', encoding='utf-8') as file:
        for line in file:
            score = line.strip().split(' ')[-1]
            scores.append(int(score))

    max_score = max(scores)
    len_score = len(scores) - 1

    return {'max': max_score, 'len': len_score}
