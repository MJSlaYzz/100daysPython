from turtle import Turtle
import random
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("square")
        self.color("red")
        self.goto(0, 0)
        self.move_speed = 0.05
        self.speed_on_x = 10
        self.speed_on_y = 10
        self.random_direction()

    def random_direction(self):
        random_x = random.choice([10, -10])
        random_y = random.choice([10, -10])

        self.speed_on_x = random_x
        self.speed_on_y = random_y


    def move_ball(self):
        new_x = self.xcor() + self.speed_on_x
        new_y = self.ycor() + self.speed_on_y
        self.goto(new_x, new_y)
    
    def bounce_ball_y(self):
        print("bounce_ball_y Called!")
        #self.speed_on_y *= -1
            
    
    def bounce_ball_x(self):
        self.move_speed *= 0.95
        #print("bounce_ball_x Called!")
        #self.speed_on_x *= -1
            
    
    def reset_ball(self,):
        self.move_speed = 0.05
        self.goto(0, 0)
        self.bounce_ball_x()
