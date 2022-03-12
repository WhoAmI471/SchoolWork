questions = ['My name ___ Vova', 'I ___ a coder', 'I live ___ Moscow']
answers = ['is', 'am', 'in']

user_input = input('Привет!\nПредлагаю проверить свои знания английского!\nНаберите "ready", чтобы начать!\n')
correct_answers = 0
question = len(questions)

if user_input != 'ready':
    print('Кажется, вы не хотите играть. Очень жаль:(')
else:
    for i in range(len(questions)):
        user_answer = input(f'{questions[i]} \n')

        if user_answer == answers[i]:
            print('Ответ верный!')
            correct_answers += 1

        else:
            print(f'Неправильно. Правильный ответ: {answers[i]}')
            
    percent = int(float(correct_answers / 3) * 100)

    print('Вот и все!\n',
         f'Вы ответили на {correct_answers} вопросов из {question} верно, это {percent} процентов.'
         )


