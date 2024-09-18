from turtle import Turtle

class PlayerTurtle(Turtle):
    def __init__(self):
        super().__init__()
        self.create_player()

    #create player method.
    def create_player(self):
        self.shape("turtle")
        self.shapesize(stretch_wid=1.5, stretch_len=1.5)
        self.penup()
        self.color("black", "dark green")
        self.reset_position()
    
    # Player movement methods.
    def move_up(self):
        self.forward(100)
    
    def reset_position(self):
        self.setheading(90)
        self.goto(0, -250)