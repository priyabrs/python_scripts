import random

class QuizBrain():
    def __init__(self, question_list) -> None:
        self.question_num = 0
        self.question_list = question_list
        self.score = 0

    def next_question(self) -> str:
        current_question = self.question_list[self.question_num]
        self.question_num += 1
        user_answer = input(f'Q.{self.question_num}: {current_question.text} (True/False): ')
        self.check_answer(user_answer, current_question.answer)

    def still_has_questions(self) -> bool:
        return self.question_num < len(self.question_list)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print('Your answer is right.', end='')
        else:
            print(f'Your answer is wrong.', end='')
        print(f' Correct answer is {correct_answer}')
        print(f'your current score is {self.score}/{self.question_num}\n')

    def shuffle_questions(self) -> None:
        random.shuffle(self.question_list)