# Modules:
from turtle import Turtle
# Constants:
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGH = 0
LEFT = 180
STARTING_POSITIONS = [(0, 0),(-20, 0),(-40, 0)]
class Snake:

    def __init__(self):
        self.snake_parts = []
        self.create_snake()
        self.head = self.snake_parts[0]
        self.can_change_direction = True # to prevent player from pressing two buttons at the same time.

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        new_part = Turtle("square")
        if position == STARTING_POSITIONS[0]:
            new_part.color("lawn green")
        else:
            new_part.color("lime green")
        new_part.penup()
        new_part.setposition(position)
        self.snake_parts.append(new_part)
            
    def extend(self):
        self.add_segment(self.snake_parts[-1].position())

    def move(self):
        # start is the number to start the range from.
        # stop is where the range going to end.
        # step is how we are going to get from start to stop.
        # we need a way to move the snake, so instead of the normal way of moving each segment forward, we will just control the first one,
        # and make the rest of the segments follow it.
        # This is the range function in C language so we can not write it with this keywords so we care using it to visualize it only.
        # for segment_number in range(start = 3, stop = 0, step = -1):
        #for segment_number in range(start = len(snake_parts) - 1, stop = 0, step = -1):
        for segment_number in range(len(self.snake_parts) - 1, 0, -1):
            new_x =  self.snake_parts[segment_number - 1].xcor() # get x position of previous segment/snake part
            new_y =  self.snake_parts[segment_number - 1].ycor() # get y position of previous segment/snake part
            self.snake_parts[segment_number].goto(new_x, new_y) # send the current segment/snake part to the x and y position of the previous segment.
        self.head.forward(MOVE_DISTANCE)

    def teleport_to_opposite_side(self):
        # snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280
        if self.head.xcor() > 280:
            self.head.goto(-280, self.head.ycor())
        elif self.head.xcor() < -280:
            self.head.goto(280, self.head.ycor())
        elif self.head.ycor() > 280:
            self.head.goto(self.head.xcor(), -280)
        elif self.head.ycor() < -280:
            self.head.goto(self.head.xcor(), 280)


    def move_snake_up(self):
        if self.head.heading() != DOWN and self.can_change_direction:
            self.head.setheading(UP)
            self.can_change_direction = False
    def move_snake_down(self):
        if self.head.heading() != UP and self.can_change_direction:
            self.head.setheading(DOWN)
            self.can_change_direction = False
    def move_snake_right(self):
        if self.head.heading() != LEFT and self.can_change_direction:
            self.head.setheading(RIGH)
            self.can_change_direction = False
    def move_snake_left(self):
        if self.head.heading() != RIGH and self.can_change_direction:
            self.head.setheading(LEFT)
            self.can_change_direction = False
    
    # reset() will be used for day 24 changes.
    def reset(self):
        for snake_part in self.snake_parts:
            snake_part.hideturtle()
        self.snake_parts.clear()
        self.create_snake()
        self.head = self.snake_parts[0]


    
