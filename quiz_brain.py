import html


class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list
        self.current_question = None

    def still_has_questions(self):
        """this method will check still any question left  in question bank"""
        return self.question_number < len(self.question_list)

    def next_question(self):
        """this method will return next question number and question text"""
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1

        # unscaping html content from question text
        q_text = html.unescape(self.current_question.text)
        return f"Q.{self.question_number}: {q_text}"
        # user_answer = input(f"Q.{self.question_number}: {q_text} (True/False): ")
        # self.check_answer(user_answer)

    def check_answer(self, user_answer):
        """this method will check the answer is correct or not """

        correct_answer = self.current_question.answer
        if user_answer.lower() == correct_answer.lower():
            self.score += 1

            return True
        else:

            return False
