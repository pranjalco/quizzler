from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT = "Arial"


class QuizUi:

    def __init__(self, quiz_brain: QuizBrain):
        # self.score = 0
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.score_label = Label(text=f"Score:{self.quiz.score}", bg=THEME_COLOR, fg="white", font=(FONT, 12, "normal"))
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.canvas_text = self.canvas.create_text(150,
                                                   125,
                                                   width=280,
                                                   text="Some question text",
                                                   fill=THEME_COLOR,
                                                   font=(FONT, 20, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=30)

        self.false_i = PhotoImage(file="./images/false.png")
        self.false_button = Button(image=self.false_i, highlightthickness=0, bg=THEME_COLOR, command=self.false_answer)
        self.false_button.grid(row=2, column=0)

        self.true_i = PhotoImage(file="./images/true.png")
        self.true_button = Button(image=self.true_i, bg=THEME_COLOR, highlightthickness=0, command=self.true_answer)
        self.true_button.grid(row=2, column=1)

        self.na_l = Label(text="Created by Pranjal Sarnaik", bg=THEME_COLOR, fg="white", font=(FONT, 12, "normal"))
        self.na_l.grid(row=3, column=1, pady=20)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        if self.quiz.still_has_questions():
            self.canvas.config(bg="white")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.canvas_text, text=q_text)
            self.score_label.config(text=f"Score:{self.quiz.score}")
        else:
            self.canvas.config(bg="white")
            self.score_label.config(text=f"Score: {self.quiz.score}")
            self.canvas.itemconfig(self.canvas_text, text=f"The End\nYour final score is {self.quiz.score}")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_answer(self):
        answer_by_user = "true"
        true_or_false = self.quiz.check_answer(answer_by_user)
        self.give_feedback(true_or_false)

        # self.get_next_question()
        # self.score_label.config(text=f"Score:{self.quiz.score}")

    def false_answer(self):
        answer_by_user = "false"
        true_or_false = self.quiz.check_answer(answer_by_user)
        self.give_feedback(true_or_false)

        # self.get_next_question()
        # self.score_label.config(text=f"Score:{self.quiz.score}")

    def give_feedback(self, true_or_false):
        if true_or_false:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
