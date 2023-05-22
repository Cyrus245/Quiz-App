from question_model import Question
from quiz_brain import QuizBrain
from ui import QuizInterface
from data import question_data

question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]

    # passing question text and answer to the question class
    new_question = Question(question_text, question_answer)

    # appending new question to the question bank
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

quiz_UI = QuizInterface(quiz)

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
