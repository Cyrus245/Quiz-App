from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz: QuizBrain):
        self.quiz = quiz
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=50, bg=THEME_COLOR)

        # scoreboard
        self.scoreboard = Label(text='Score:0', font=("Arial", 15, "bold"), fg="white", bg=THEME_COLOR)
        self.scoreboard.grid(column=2, row=0, columnspan=1)
        self.scoreboard.config(pady=10)

        # canvas
        self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.canvas.grid(column=1, row=1, columnspan=2, pady=30)
        self.question_text_canvas = self.canvas.create_text(150, 125, text="test text", font=("Arial", 10, "italic"),
                                                            width=270)

        # Button
        right_img = PhotoImage(file='./images/true.png')
        self.correctBtn = Button(image=right_img, highlightthickness=0, command=self.is_ans_true)
        self.correctBtn.grid(column=1, row=2)

        wrong_img = PhotoImage(file='./images/false.png')
        self.wrongBtn = Button(image=wrong_img, highlightthickness=0, command=self.is_ans_false)
        self.wrongBtn.grid(column=2, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        """this method will show the next question in canvas"""

        self.canvas.config(bg="white")
        
        if self.quiz.still_has_questions():
            # updating score text
            self.scoreboard.config(text=f"score:{self.quiz.score}")

            # calling next question method from QuizBrain class instance
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text_canvas, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text_canvas, text="You have ended the quiz")

            # disable the button after ending the quiz
            self.correctBtn.config(state='disabled')
            self.wrongBtn.config(state="disabled")

    def is_ans_true(self):
        self.update_screen(self.quiz.check_answer('True'))

    def is_ans_false(self):
        self.update_screen(self.quiz.check_answer('False'))

    def update_screen(self, answer):
        if answer:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.window.after(1000, self.get_next_question)
