import json


def load_questions():
    file = open("C:\PyProjects\Experiments\home_work\lesson07_hw\questions.json", encoding='UTF-8')
    data = json.load(file)
    file.close()
    return data


def show_field(questions):

    for category_name, category_questions in questions.items():
        print((category_name.ljust(12)), end='')
        for point , questions_data in category_questions.items():
            asked = questions_data['asked']
            if not asked:
                print(point.ljust(3), end=' ')
            else:
                print('  '.ljust(3), end=' ')
        print()


def parse_input(user_input):
    user_data = user_input.split(' ')

    if len(user_data) != 2:
        return False

    if user_data[0].isdigit():
        return False

    if user_data[0] not in 'Транспорт Животные Еда':
        return False

    if user_data[1].isalpha():
        return False

    if user_data[1] not in '100 200 300':
        return False
        
    return {'category': user_data[0], 'point': user_data[1]}


def show_question(question):
    print(f'Слово {question} в переводе означает')


def show_stats(points, correct, incorrect):
    print(
        'У нас закончились вопросы!\n'
        '\n'
        f'Ваш счет: {points}\n'
        f'Верных ответов: {correct}\n'
        f'Неверных ответов: {incorrect}'
        )


def save_results_to_file(points, correct, incorrect):

    with open(r"C:\PyProjects\Experiments\home_work\lesson07_hw\results.json", "r") as file:
        results = json.load(file)

    results.append({'points': points, 'correct': correct, 'incorrect': incorrect})

    with open(r"C:\PyProjects\Experiments\home_work\lesson07_hw\results.json", "w") as file:
        json.dump(results, file)


