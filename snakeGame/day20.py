    # Day 20 #
def snake_game_day20():

    from turtle import Screen
    from snake import Snake
    import time

    screen = Screen()
    # change screen dimensions:
    screen.setup(width = 600, height = 600)
    screen.bgcolor("black")
    screen.title("My Snake Game")
    screen.tracer(0) #turning off tracer

    snake = Snake()
    screen.listen()
    screen.onkey(snake.move_snake_up, "Up")
    screen.onkey(snake.move_snake_down, "Down")
    screen.onkey(snake.move_snake_right, "Right")
    screen.onkey(snake.move_snake_left, "Left")

    game_is_on = True
    while game_is_on:
        # we delay the screen for 0.1 second then update the screen and every time the screen refresh move forward.
        screen.update() #update the animation after all the snake segments have been moved to get a smooth animation.
        time.sleep(0.1) # adds a 0.1 second delay.

        snake.move()

    screen.exitonclick()


def snake_game_day21():
    # Day 21 #
    from turtle import Screen
    from snake import Snake
    from food import Food
    from scoreboard import Scoreboard
    import time

    screen = Screen()
    # change screen dimensions:
    screen.setup(width = 600, height = 600)
    screen.bgcolor("black")
    screen.title("My Snake Game")
    screen.tracer(0) #turning off tracer

    snake = Snake()
    food = Food()
    scoreboard = Scoreboard()
    screen.listen()
    screen.onkey(snake.move_snake_up, "Up")
    screen.onkey(snake.move_snake_down, "Down")
    screen.onkey(snake.move_snake_right, "Right")
    screen.onkey(snake.move_snake_left, "Left")

    game_is_on = True
    hard_core = False # if card core is false then snake can go through the wall
    while game_is_on:
        # we delay the screen for 0.1 second then update the screen and every time the screen refresh move forward.
        screen.update() #update the animation after all the snake segments have been moved to get a smooth animation.
        time.sleep(0.1) # adds a 0.1 second delay.
        snake.can_change_direction = True # player can change direction.
        snake.move()
        # Detect collision with food
        if snake.head.distance(food) < 15: #food is  10x10
            food.refresh()
            snake.extend()
            scoreboard.add_score()
        
        # Detect collision with wall.
        if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
            if(not hard_core):
                snake.teleport_to_opposite_side()
            else:
                print("Game Over!")
                scoreboard.game_over()
                game_is_on = False

        # Detect collision with wall.

        # code without slicing:
        # for segment in snake.snake_parts:
        #     if segment == snake.head:
        #         pass
        #     else:
        #         if snake.head.distance(segment) < 10:
        #             game_is_on = False
        #             scoreboard.game_over()

        # code with slicing:
        for segment in snake.snake_parts[1:]:
            if snake.head.distance(segment) < 10:
                    game_is_on = False
                    scoreboard.game_over()
                
    screen.exitonclick()

def snake_game_day24():
    # Day 24 #
    from turtle import Screen
    from snake import Snake
    from food import Food
    from scoreboard import Scoreboard
    import time
    import os
    screen = Screen()
    # change screen dimensions:
    screen.setup(width = 600, height = 600)
    screen.bgcolor("black")
    screen.title("My Snake Game")
    screen.tracer(0) #turning off tracer

    ABSOLUTE_PATH = "/road_to_programming/GitHub/100daysPython"
    global game_is_on


    def turn_game_off():
        print("escape called!")
        global game_is_on
        game_is_on = False
        return game_is_on
    
    def high_score_file():
        # check if high score file exist
        # Writing to a file

        # Relative path
        relative_path = os.path.join("FilesDirectoriesPaths", "high_score.txt")
        print(f"Relative path: {relative_path}")
        if not os.path.exists(relative_path):
            with open(ABSOLUTE_PATH, "w") as file: # can use absolute path
                file.write(f"High Score = {scoreboard.high_score}")
        else:
            with open("FilesDirectoriesPaths/high_score.txt", "r") as file: # can use relative path
                contents = file.read()
            # Extract the high score number from the file contents
            # Assuming the format is "High Score = <number>"
            high_score_str = contents.split(" = ")[1]
            high_score = int(high_score_str)
            # Update the scoreboard high score
            if high_score > scoreboard.high_score:
                scoreboard.high_score = high_score
            else:
                high_score = scoreboard.high_score
                with open("FilesDirectoriesPaths/high_score.txt", "w") as file:
                    file.write(f"High Score = {high_score}")
                    
            print(f"High score from file: {high_score}")


    snake = Snake()
    food = Food()
    scoreboard = Scoreboard()
    high_score_file()
    scoreboard.update_score_day24() # used because the init function in scoreboard uses the day 21 update function.
    screen.listen()
    screen.onkey(snake.move_snake_up, "Up")
    screen.onkey(snake.move_snake_down, "Down")
    screen.onkey(snake.move_snake_right, "Right")
    screen.onkey(snake.move_snake_left, "Left")
    screen.onkey(turn_game_off, "Escape")
    
    
    game_is_on = True
    hard_core = False # if card core is false then snake can go through the wall
    
    while game_is_on:
        # we delay the screen for 0.1 second then update the screen and every time the screen refresh move forward.
        screen.update() #update the animation after all the snake segments have been moved to get a smooth animation.
        time.sleep(0.1) # adds a 0.1 second delay.
        snake.can_change_direction = True # player can change direction.
        snake.move()
        # Detect collision with food
        if snake.head.distance(food) < 15: #food is  10x10
            food.refresh()
            snake.extend()
            scoreboard.add_score_day24()
        
        # Detect collision with wall.
        if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
            if(not hard_core):
                snake.teleport_to_opposite_side()
            else:
                #print("Game Over!")
                scoreboard.reset()
                snake.reset()
                #game_is_on = False

        # Detect collision with snake's tail.
        for segment in snake.snake_parts[1:]:
            if snake.head.distance(segment) < 10:
                    scoreboard.reset()
                    snake.reset()
                    #game_is_on = False
                    #scoreboard.game_over()

    high_score_file()
    screen.exitonclick()


snake_game_day24()