import random
from question import *
from questions import *

def load_questions():
    questions = []

    for question_data in questions_data:

        questions.append(Question(
            question_data['q'],
            int(question_data['d']),
            question_data['a']
        ))
    random.shuffle(questions)
    return questions


def correct_answers(questions):
    correct = 0

    for question in questions:
        if question.is_correct():
            correct += 1
    return correct


def count_points(questions):
    points = 0

    for question in questions:
        if question.is_correct():
            points += question.get_points()
    return points

