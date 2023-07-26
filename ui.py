#Create the GUI for the program
from tkinter import *
from quiz_brain import QuizBrain


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        #Theme color of the program
        THEME_COLOR = "#375362"

        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.score_label = Label(text=f"Score: {self.quiz.score}", bg=THEME_COLOR, fg="white")
        self.score_label.grid(column=1, row=0)

        self.canvas = Canvas(width=300, height=250, bg="White")
        self.text = self.canvas.create_text(150, 125,
                                            width= 280,
                                            text="Insert question here",
                                            font=("Arial", 20, "italic"),
                                            fill=THEME_COLOR)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=40)

        right_img = PhotoImage(file="images/true.png")
        wrong_img = PhotoImage(file="images/false.png")

        #Note: Use lambda to pass parameters to the buttons
        self.right_button = Button(image=right_img, highlightthickness=0,
                                   borderwidth=0, bg=THEME_COLOR, command=lambda: self.button("True"))
        self.right_button.grid(column=0, row=2)

        self.wrong_button = Button(image=wrong_img, highlightthickness=0,
                                   borderwidth=0, bg=THEME_COLOR, command=lambda: self.button("False"))
        self.wrong_button.grid(column=1, row=2)

        #Start the game
        self.next_question()

        self.window.mainloop()

    #Update score and display the next question or end the game and disable the buttons
    def next_question(self):
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            self.canvas.itemconfig(self.text, text=self.quiz.next_question())
        else:
            self.canvas.itemconfig(self.text, text="You've reached the end of the quiz.")
            self.right_button.config(state="disabled")
            self.wrong_button.config(state="disabled")

    #Check the answer and display red/green for 1s after the user click them
    def button(self, answer):
        color = "red"
        if self.quiz.check_answer(answer):
            color = "green"
        self.canvas.config(bg=color)
        self.window.after(1000, self.reset)

    #Set the red/green back to normal and get the next question
    def reset(self):
        self.canvas.config(bg="white")
        self.next_question()
