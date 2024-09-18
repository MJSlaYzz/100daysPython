from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
import random
from os import system

question_bank = []

for question in question_data:
    new_question = Question(question["text"], question["answer"])
    question_bank.append(new_question)

system("cls")
random.shuffle(question_bank)
quiz = QuizBrain(question_bank)
quiz.ask_question()

