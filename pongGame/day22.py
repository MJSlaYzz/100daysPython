# Day 22 #

from turtle import Screen
import time

from ball import Ball
from player import Player
from score import Score, Mid_Line
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


screen = Screen()
screen.bgcolor("black")
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.title("Pong")
screen.tracer(0) #turning off tracer

background = Mid_Line()
score = Score()
player1 = Player(-1)
player2 = Player(1)
ball = Ball()
screen.listen()
screen.onkeypress(key="w", fun= player1.move_up)
screen.onkeypress(key="s", fun= player1.move_down)

screen.onkeypress(key="Up", fun= player2.move_up)
screen.onkeypress(key="Down", fun= player2.move_down)

game_is_on = True
while game_is_on:
    round_speed = round(ball.move_speed,5)
    time.sleep(round_speed)
    screen.update()
    ball.move_ball()
    
    # detect collation with wall
    if ball.ycor() > 280:
        ball.speed_on_y = -10
    elif ball.ycor() < -280:
        ball.speed_on_y = 10

    
    # detect collation with paddles
    if ball.distance(player1) < 50 and ball.xcor() < -320:
        ball.speed_on_x = 10
        ball.bounce_ball_x()
        print(round_speed)
    elif ball.distance(player2) < 50 and ball.xcor() > 320:
        ball.speed_on_x = -10
        ball.bounce_ball_x()
        print(round_speed)

    
    # detect collation with goal
    if ball.xcor() > 380:
        ball.reset_ball()
        score.update_score(player_score=1)
    elif ball.xcor() < -380:
        ball.reset_ball()
        score.update_score(enemy_score=1)
    
      
    
    #screen.exitonclick()