from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 16, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color("white")
        self.hideturtle()
        self.goto(0, 220)
        self.display_score()

    def display_score(self):
        self.clear()
        self.write(arg=f'Score: {self.score}', align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(arg='GAME OVER', align=ALIGNMENT, font=FONT)


    def increase_score(self):
        self.score += 1
        self.display_score()