# Day 23 #

# Capstone Project - Turtle Crossing Game

from turtle import Screen
import time
from street import Street
from playerTurtle import PlayerTurtle
from car import Car
from level import Level
import random



screen = Screen()
screen.tracer(0)
cars_amount = 10

street = Street()
car = Car()
car_list = []
player = PlayerTurtle()
level = Level()

screen.listen()
screen.onkey(fun = player.move_up, key = "Up")

def create_cars():
    for _ in range(1):
        random_y_position = random.randint(0,3)
        #print(random_y_position)
        new_car = Car()
        new_car.create_car(random_y_position)
        car_list.append(new_car)

         
create_cars()
cars_creation_delay = 0
game_is_on = True
while game_is_on:
    cars_creation_delay += 1.
    if cars_creation_delay >= cars_amount: # used to equal 10
        create_cars()
        cars_creation_delay = 0

    for c in car_list:
        c.moving_car()
        if c.distance(player) < 20:
            level.game_over()
            game_is_on = False
        if c.xcor() > 410 or c.xcor() < -410:
            c.hideturtle()
            car_list.remove(c)
            #print("a car got removed!")

    if player.ycor() >= 250:
        level.update_level()
        player.reset_position()
        if cars_amount > 5:
            cars_amount -= 1
        print(level.cars_speed)
    
    screen.update()
    time.sleep(round(level.cars_speed,5))
    
screen.exitonclick()
        