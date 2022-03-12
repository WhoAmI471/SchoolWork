import random


def get_word_from_file(path):
    with open(path, 'r', encoding='utf-8') as f:
        lines = f.read()
        words = lines.splitlines()

    return words


def shuffle_word(word):
    word_as_list = list(word)
    random.shuffle(word_as_list)
    return ''.join(word_as_list)


def save_player_score(path, player_name, player_score):
    with open(path, 'a', encoding='utf-8') as fp:
        fp.write(f'{player_name} {player_score}\n')


def get_statistics_from_file(path):
    scores = []

    with open(path, 'a', encoding='utf-8') as f:
        for line in f:
            score = line.strip().split(' ')[-1]
            scores.append(int(score))

    max_score = max(scores)
    len_score = len(scores) - 1

    return {'max': max_score, 'len': len_score}
    