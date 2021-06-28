from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.text_box = Canvas(width=300, height=250, bg="white", highlightthickness=0, bd=0)
        self.text_box.grid(row=1, column=0, columnspan=2, padx=20, pady=20)

        self.question_text = self.text_box.create_text(150, 125, text=f"Test",
                                                       font=("Arial", 15, "italic"), width=280)

        self.score = Label(text=f"Score: _", font=("Arial", 12, "normal"), bg=THEME_COLOR, fg="white")
        self.score.grid(row=0, column=1, padx=20, pady=20)

        self.false_image = PhotoImage(file="images/false.png")
        self.true_image = PhotoImage(file="images/true.png")

        self.false_button = Button(image=self.false_image, highlightthickness=0, bd=0, command=self.check_answer_true)

        self.false_button.grid(row=2, column=0, padx=20, pady=20)

        self.true_button = Button(image=self.true_image, highlightthickness=0, bd=0, command=self.check_answer_false)
        self.true_button.grid(row=2, column=1, padx=20, pady=20)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        if self.quiz.still_has_questions():
            self.text_box.config(bg="white")
            self.score.config(text=f"Score: {self.quiz.score}")
            question = self.quiz.next_question()
            self.text_box.itemconfig(self.question_text, text=question)
        else:
            self.text_box.config(bg="white")
            self.text_box.itemconfig(self.question_text, text=f"Congratulations for completing the quiz!"
                                                              f"\nYour final score is: "
                                                              f"{self.quiz.score}/{len(self.quiz.question_list)}",
                                     justify="center")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")
            
    def check_answer_true(self):
        answer = self.quiz.check_answer("True")
        self.give_feedback(answer)

    def check_answer_false(self):
        answer = self.quiz.check_answer("False")
        self.give_feedback(answer)

    def give_feedback(self, answer):
        if answer:
            print("Answer Correct, should be green")
            self.text_box.config(bg="green")
        else:
            print("Answer Wrong, should be red")
            self.text_box.config(bg="red")

        self.window.after(1000, func=self.get_next_question)

