print('Привет! Предлагаю проверить свои знания английского!')
user_name = str(input('Расскажи, как тебя зовут!\n'))
print(f'Привет, {user_name}, начинаем тренировку!')

correct_answers = 0

# Первый вопрос.
question1 = 'My name ___ Vova\n'
correct_answer1 = 'is'
answer = input(question1)

if answer == correct_answer1:
    correct_answers += 1
    print('Ответ верный!\nВы получаете 10 баллов!')
else:
    print(f'Неправильно.\nПравильный ответ: {correct_answer1}')

# Второй вопрос.
question2 = 'I ___ a coder\n'
correct_answer2 = 'am'
answer = input(question2)

if answer == correct_answer2:
    correct_answers += 1
    print('Ответ верный!\nВы получаете 10 баллов!')
else:
    print(f'Неправильно.\nПравильный ответ: {correct_answer2}')

# Третий вопрос.
question3 = 'I live ___ Moscow\n'
correct_answer3 = 'in'
answer= input(question3)

if answer == correct_answer3:
    correct_answers += 1
    print('Ответ верный!\nВы получаете 10 баллов!')
else:
    print(f'Неправильно.\nПравильный ответ: {correct_answer3}')

# Баллы пользователя.
score = correct_answers * 10

# Проценты.
percent = int(float(score / 30) * 100)

print(
    f'Вот и все, {user_name}!\n'
    f'Вы ответили на {correct_answers} вопросов из 3 верно.\n'
    f'Вы заработали {score} баллов.\n'
    f'Это {percent} процентов.'
)


