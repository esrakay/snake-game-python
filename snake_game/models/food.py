from turtle import Turtle
import snake_game.configs as configs
import random

MAX_X_POS = configs.GAME_WIDTH // 2 - 20
MAX_Y_POS = configs.GAME_HEIGHT // 2 - 20


class Food(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.shape('circle')
        self.color('green')
        self.penup()
        self.shapesize(0.5, 0.5)
        self.speed("fastest")
        self.relocate()

    def relocate(self) -> None:
        random_x = random.randint(-MAX_X_POS, MAX_X_POS)
        random_y = random.randint(-MAX_Y_POS, MAX_Y_POS)
        self.goto(random_x, random_y)
