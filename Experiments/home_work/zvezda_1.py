# Часть 2. Задание со звездочкой.
questions = ['My name ___ Vova', 'I ___ a coder', 'I live ___ Moscow']
answers = ['is', 'am', 'in']

question = len(questions)
score = 0
correct_answers = 0


user_input = input('Привет!\n'
                   'Предлагаю проверить свои знания английского!\n'
                   'Наберите "ready", чтобы начать!\n')
if user_input != 'ready':
    print('Кажется, вы не хотите играть. Очень жаль:(')
else:
    for i in range(len(questions)):
        right = 3

        while True:
            user_answer = input(f'{questions[i]} \n')

            if user_answer != answers[i] and right != 1:
                right -= 1
                print(f'Осталось попыток: {right}, попробуйте еще раз!')
                right -= 1
            elif user_answer == answers[i]:
                score += right
                correct_answers += 1
                print('Ответ верный!\n')
                break
            elif right == 1:
                score += 0
                print(f'Увы, но нет. Верный ответ: {answers[i]}\n')
                break
            else:
                correct_answers += 1
                score += 3
                print('Ответ верный!\n')
    print('Вот и все!\n'
         f'Вы ответили на {correct_answers} вопросов из {question} верно.\n' 
         f'Вы набрали {score} баллов.'
         )
         


