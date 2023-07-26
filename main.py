"""
Purpose: Create a GUI true/false quizzing game with 10 random questions on random topics
Tools: Open Trivia Database
"""
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from ui import QuizInterface

#Set up the list of Question Objects
question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

#Initiate the game
quiz = QuizBrain(question_bank)
quiz_ui = QuizInterface(quiz)

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
