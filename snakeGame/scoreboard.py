# Made at day 21 #
from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 17, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0 # made on day 24
        self.goto(0, 270)
        self.hideturtle()
        self.color("White")
        self.update_score()
    
    def add_score(self):
        self.score +=1
        self.update_score()
    
    def update_score(self):
        self.clear()
        self.write(arg = f"Score: {self.score}", align = ALIGNMENT, font = FONT)
    
    def game_over(self):
        self.goto(0, 0)
        self.write(arg ="Game Over!", align = ALIGNMENT, font = FONT)

    # Day 24

    def update_score_day24(self):# changes made on day 24
        self.clear()
        self.write(arg = f"Score: {self.score}  High Score: {self.high_score}", align = ALIGNMENT, font = FONT)

    def add_score_day24(self):
        self.score +=1
        self.update_score_day24()

    # reset() will be used instead of game_over() for day 24 changes.
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.update_score_day24()


