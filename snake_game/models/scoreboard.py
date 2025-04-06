from turtle import Turtle
import snake_game.configs as configs

ALIGNMENT = "center"
FONT = ("Arial", 16, "normal")
SCORE_POSITION = (0, configs.GAME_HEIGHT // 2 + 10)


class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.score = 0
        self.penup()
        self.color("white")
        self.hideturtle()
        self.goto(SCORE_POSITION)
        self.display_score()

    def display_score(self) -> None:
        self.clear()
        self.write(arg=f'Score: {self.score}', align=ALIGNMENT, font=FONT)

    def game_over(self) -> None:
        self.goto(0, 0)
        self.write(arg='GAME OVER', align=ALIGNMENT, font=FONT)
        self.goto(0, -15)
        self.write(arg='PRESS E TO RESTART', align=ALIGNMENT, font=('Arial', 10, 'normal'))

    def increase_score(self) -> None:
        self.score += 1
        self.display_score()

    def set_score(self, score) -> None:
        self.score = score
