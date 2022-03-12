print('Привет! Предлагаю проверить свои знания английского!')
user_name = str(input('Расскажи, как тебя зовут!'))
print(f'Привет, {user_name}, начинаем тренировку!')


# первый вопрос
print('My name ___ Vova')

answer1 = str(input())
correct_answer1 = str('is')

print(f'My name {answer1} Vova')

if answer1 == correct_answer1:
    is_correct1 = True
else:
    is_correct1 = False
if is_correct1 == True:
    print('Ответ верный!')
    print('Вы получаете 10 баллов!')
else:
    print('Неправильно.')
    print(f'Правильный ответ: {correct_answer1}')


# второй вопрос
print('I ___ a coder')

answer2 = str(input())
correct_answer2 = str('am')

print(f'I {answer2} a coder')

if answer2 == correct_answer2:
    is_correct2 = True
else:
    is_correct2 = False
if is_correct2 == True:
    print('Ответ верный!')
    print('Вы получаете 10 баллов!')
else:
    print('Неправильно.')
    print(f'Правильный ответ: {correct_answer2}')


# третий вопрос
print('I live ___ Moscow')

answer3 = str(input())
correct_answer3 = str('in')\

print(f'I live {answer3} Moscow')

if answer3 == correct_answer3:
    is_correct3 = True
else:
    is_correct3 = False
if is_correct3 == True:
    print('Ответ верный!')
    print('Вы получаете 10 баллов!')
else:
    print('Неправильно.')
    print(f'Правильный ответ: {correct_answer3}')


# вывод результата
right = 0

if is_correct1 == True:
    right += 1
if is_correct2 == True:
    right += 1
if is_correct3 == True:
    right += 1

score = 0

if is_correct1 == True:
    score += 10
if is_correct2 == True:
    score += 10
if is_correct3 == True:
    score += 10

percent = int(float(score / 30) * 100)

print(f'Вот и все, {user_name}!')
print(f'Вы ответили на {right} вопросов из 3 верно.')
print(f'Вы заработали {score} баллов.')
print(f'Это {percent} процентов.')






