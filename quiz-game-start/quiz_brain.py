class QuizBrain:
    def __init__(self, question_list):
        self.question_list = question_list
        self.question_number = 0
        self.points = 0

    def ask_question(self):
        user_answer = input(f"Q.{self.question_number + 1}: {self.question_list[self.question_number].text}(True/False): ")
        self.check_answer(user_answer)
    
    def check_answer(self, user_answer):
        if(user_answer == self.question_list[self.question_number].answer):
            print("That was correct!")
            self.points += 1
        else:
            print("That was wrong!")
        self.question_number += 1
        self.next_question()

    def next_question(self):
        if(self.question_number >= (len(self.question_list) - 1)):
            print(f"End of Quiz, Total points are {self.points}/ {self.question_number}")
        else:
            print(f"Total points are {self.points}/{self.question_number}, Next Question: ")
            print("\n")
            self.ask_question()