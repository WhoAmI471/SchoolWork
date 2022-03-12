easy = {'time':'время', 'small':'маленький', 'home':'дом', 'read':'читать', 'big':'большой'}
medium = {'justice':'справедливость', 'profit':'выгода', 'dream':'мечтать', 'event':'событие', 'mysterious':'загадочный'}
hard = {'research':'исследование', 'review':'обзор', 'success':'успех', 'immortal':'бессмертный', 'correct':'правильный'}

levels = {
    0: "Нулевой", 
    1: "Так себе", 
    2: "Можно лучше", 
    3: "Норм", 
    4: "Хорошо", 
    5: "Отлично",
}

answers = {}
words = {}
result = {}
right = 0

print(
    'Выберите уровень сложности\n'
    'Лёгкий, средний, сложный'
    )

user_input = input().lower()
if 'лёгкий' == user_input:
    words = easy
elif 'средний' == user_input:
    words = medium
elif 'сложный' == user_input:
    words = hard

print('Выбран уровень сложности, мы предложим 5 слов, подберите перевод')
input('нажмите Enter\n') 

for k, v in words.items():
    print(f'{k}, {len(v)} букв, начинается на {v[0]}...')

    user_input = input()
    if v == user_input:
        print(f'Верно, {k} это {v}.')
        result[k] = True
        
    else:
        print(f'Неверно. {k} это {v}.')
        result[k] = False

print('\nПравильно отвечены слова:')
for k, v in result.items():
    if v:
        print(k)
        right += 1

print('\nНе правильно отвечены слова:')
for k, v in result.items():
    if not v:
        print(k)

print(f'Ваш ранг: {levels[right]}')
