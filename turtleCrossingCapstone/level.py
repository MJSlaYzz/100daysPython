from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 20, "normal")
FONT2 = ("Arial", 40, "bold")

class Level(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.cars_speed = 0.1
        self.current_level = 1
        self.goto(-320, 240)
        self.write(arg= f"Level: {self.current_level}", align= ALIGNMENT, font= FONT)
    

    def update_level(self):
        self.clear()
        self.current_level += 1
        self.cars_speed *= 0.95
        self.write(arg= f"Level: {self.current_level}", align= ALIGNMENT, font= FONT)

    
    def game_over(self):
        self.goto(0, 25)
        self.write(arg= "Game Over!", align= ALIGNMENT, font= FONT2)
    