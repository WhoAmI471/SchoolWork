import utils

questions = utils.load_questions()
points, correct, incorrect = 0, 0, 0
question_asked = 0

while True:

    utils.show_field(questions)

    user_input = input().title()
    user_data = utils.parse_input(user_input)

    if not user_data:
        print('Такого вопроса нет, попробуйте еще раз!\n')
        continue

    category, point = user_data['category'], user_data['point']

    question = questions[category][point]

    if question['asked']:
        print('Ты это спрашивал')
        continue

    utils.show_question(question['question'])

    user_answer = input().lower()

    if user_answer == question['answer']:
        print('Ответ верный\n')
        points += int(point)
        correct += 1
    else:
        print('Ответ неверный\n')
        points -= int(point)
        incorrect += 1

    question['asked'] = True
    question_asked +=1

    if question_asked == 9:
        break

utils.show_stats(points, correct, incorrect)
utils.save_results_to_file(points, correct, incorrect)