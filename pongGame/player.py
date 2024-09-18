from turtle import Turtle
MOVE_DISTANCE = 20
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

class Player(Turtle):
    def __init__(self, paddle_position):
        super().__init__()
        self.x_position = paddle_position * ((SCREEN_WIDTH/2) - 20)
        self.y_position = 0
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.color("white")
        #self.speed("fastest")
        self.goto(self.x_position, self.y_position)
        
    
    def move_up(self):
        if self.ycor() < (SCREEN_HEIGHT/2) - 55:
            new_y = self.ycor() + MOVE_DISTANCE
            self.goto(self.xcor(), new_y)

    def move_down(self):
        if self.ycor() > -(SCREEN_HEIGHT/2) + 60:
            new_y = self.ycor() - MOVE_DISTANCE
            self.goto(self.xcor(), new_y)