from turtle import Turtle
import random

class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
    
    def create_car(self, car_index_location):
        random_colors = ("cornflower blue", "dark olive green", "saddle brown", "medium purple", "VioletRed2", "LightCyan4", "medium sea green", "medium orchid")
        random_position = (150, 50, -50, -150)
        self.shape("square")
        self.penup()
        self.shapesize(stretch_len = 1.5, stretch_wid = 1)
        self.color(random.choice(random_colors))
        # random_y_position = random.choice(random_position)
        random_y_position = random_position[car_index_location]
        if random_y_position == 150 or random_y_position == -50: # cars coming from the left
            self.goto(-400, random_y_position)
            self.setheading(0)
        elif random_y_position == 50 or random_y_position == -150: # cars coming from the right
            self.goto(400, random_y_position)
            self.setheading(180)
        self.showturtle()
    
    def moving_car(self):
        self.forward(10)

        