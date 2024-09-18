# Day 19 #

from turtle import Turtle, Screen
import random
import time
# we need a way to listen to what the user does (press a key on keyboard for example):
# the code that does that is called: Event listeners.


screen = Screen()
def higher_order_functions():
    tim = Turtle()
    def move_forward():
        tim.forward(10)

    screen.listen()
    # # with methods you haven't created (like onkey) it's recommended  to use keyword arguments instead of positional arguments.
    # def my_function(a, b, c):
    #     print(a + b + c)
    # # positional arguments:
    # my_function(1, 2, 3)
    # # keyword arguments
    # my_function(a = 1, b = 2, c = 3)

    #         listen for events, trigger a particular function.
    screen.onkey(key = "space", fun = move_forward) # why we don't use parentheses() at the end of the function? read below!
    # higher order functions: a function that can work with other functions.
    # when we use a function as an argument(something to be passed in another function) we don't add parentheses() at the end.
    # parentheses() triggers the function to happen, but what we want is this method "onkey" to listen for when the "space" bar is pressed and trigger the function then.

    # example:
    def add(n1, n2):
        return n1 + n2
    def calculator(n1, n2, func):
        return func(n1, n2)
    print(calculator(2, 3, add)) # output: 5. and we didn't use parentheses()

def turtle_control():
    tim = Turtle()
    screen.listen()
    def move_forward():
        tim.forward(10)
    def move_backward():
        tim.backward(10)
    def rotate_right():
        # tim.right(10)
        new_heading = tim.heading() - 10
        tim.setheading(new_heading)
    def rotate_left():
        # tim.left(10)
        new_heading = tim.heading() + 10
        tim.setheading(new_heading)
    def clear():
        tim.clear()
        tim.penup()
        tim.home()
        tim.pendown()

    screen.onkey(key ="w", fun = move_forward)
    screen.onkey(key ="s", fun = move_backward)
    screen.onkey(key ="d", fun = rotate_right)
    screen.onkey(key ="a", fun = rotate_left)
    screen.onkey(key ="c", fun = clear)

def turtles_race():
    # change screen dimensions:
    screen.setup(width = 500, height = 400)
    user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
    user_money = screen.textinput(title="Make your bet", prompt="How much would you like to bet?: ")
    #print(user_bet)
    is_race_on = False
    colors = ["red", "orange", "yellow", "green", "blue", "gray"]
    turtles = []
    y_positions = [-120, -80, -20, 20, 80, 120]
    for index, color in enumerate(colors):
        turtle =  Turtle(shape="turtle")
        turtles.append(turtle)
        turtle.penup()
        turtle.color(color)
        turtle.goto(x = -230, y = y_positions[index])

    if user_bet: #checks if user bet exists
        is_race_on = True

    while is_race_on:
        for turtle in turtles:
            if turtle.position()[0] >= 230: # turtle is 40 x 40 so 250 - 20 which half of the turtle
                is_race_on = False
                winning_color = turtle.pencolor() # or turtle.color()[0]
                if winning_color == user_bet:
                    print(f"You won your bet, the {winning_color} turtle won the race! and you won {user_money}$")
                else:
                    print(f"You lost your bet, the {winning_color} turtle won the race! and you lost {user_money}$")
            rand_distance = random.randint(0, 10)
            turtle.forward(rand_distance)


#*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-

#higher_order_functions()
#turtle_control()
turtles_race()
screen.exitonclick()
