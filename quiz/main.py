from replit import clear
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
import random


def get_question_models(list):
    qobj_list = []
    for q_ans in question_data:
        text =  q_ans['text']
        answer = q_ans['answer']
        question_obj = Question(text, answer)
        qobj_list.append(question_obj)
    return qobj_list
    # return [Question(q_ans['text'],q_ans['answer']) for q_ans in question_data]

def main():
    question_obj_list = get_question_models(random.shuffle(question_data))
    qb_obj = QuizBrain(question_obj_list)
    qb_obj.shuffle_questions()
    while qb_obj.still_has_questions():
        qb_obj.next_question()

if __name__ == '__main__':
    clear()
    main()
