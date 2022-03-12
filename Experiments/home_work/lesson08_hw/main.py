from questions import *
from utils import *


def main():
    questions = load_questions()

    for question in questions:

        print(question.build_question())
        question.user_answer = input()

        if question.is_correct():
            print(question.build_positive_feedback())
        else:
            print(question.build_negative_feedback())

    correct = correct_answers(questions)
    points = count_points(questions)

    print(
        'Вот и всё!\n'
        f'Отвечено {correct} вопроса из {len(questions)}\n'
        f'Набрано баллов: {points}'
        )

main()
