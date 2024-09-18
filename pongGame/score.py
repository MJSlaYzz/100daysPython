from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 30, "normal")

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.player_current_score = 0
        self.enemy_current_score = 0
        self.player_score()
        self.enemy_score()
    def player_score(self):
        self.penup()
        self.color("white")
        self.speed("fastest")
        self.hideturtle()

        self.x_position = -40
        self.y_position = 250

        self.goto(self.x_position, self.y_position)
        self.write(arg=f"{self.player_current_score}",align= ALIGNMENT ,font= FONT)
        
    def enemy_score(self):
        self.penup()
        self.color("white")
        self.speed("fastest")
        self.hideturtle()

        self.x_position = 40
        self.y_position = 250

        self.goto(self.x_position, self.y_position)
        self.write(arg=f"{self.enemy_current_score}",align= ALIGNMENT ,font= FONT)
    
    def update_score(self, player_score = 0, enemy_score = 0):
        self.player_current_score += player_score
        self.enemy_current_score += enemy_score
        self.clear()
        self.player_score()
        self.enemy_score()

class Mid_Line(Turtle):
    def __init__(self):
        super().__init__()
        self.draw_mid_line()

    def draw_mid_line(self):
        self.penup()
        self.color("white")
        self.speed("fastest")
        self.hideturtle()

        self.x_position = 0
        self.y_position = -300
        while True:
            if self.position()[1] < 300:
                self.goto(self.x_position, self.y_position)
                self.write(arg="'",align= ALIGNMENT ,font= FONT)
                self.y_position += 25
            else:
                break