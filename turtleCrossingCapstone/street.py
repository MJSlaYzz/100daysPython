from turtle import Turtle, Screen

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
ALIGNMENT = "center"
FONT = ("Arial", 35, "normal")

class Street: 
    def __init__(self):
        self.screen = Screen()
        self.screen.setup(width = 800, height = 600)
        self.screen.bgcolor("gray29")
        self.screen_y_positions = [200, 100, 0, -100, -200]
        self.draw_line()

    # draw white lines
    def draw_line(self):
        y_indes = 0
        for _ in self.screen_y_positions:
            x_index = 0
            for _ in range(7):
                new_turtle = Turtle()
                new_turtle.hideturtle()
                new_turtle.penup()
                new_turtle.color("white")
                new_turtle.speed("fastest")
                x_position = -324 + (108 * x_index)
                new_turtle.goto(x_position, self.screen_y_positions[y_indes])
                new_turtle.write(arg= "__", align= ALIGNMENT, font= FONT)
                x_index += 1
            y_indes += 1
            