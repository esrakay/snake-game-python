from turtle import Turtle
import snake_game.configs as configs


class Border(Turtle):
    def __init__(self, position: (int, int) = (0, 0), head_direction: int = 0) -> None:
        super().__init__()
        self.shape('square')
        self.color('green')
        self.setheading(head_direction)
        self.shapesize(configs.GAME_WIDTH // 20, 0.01)
        self.penup()
        self.goto(position)

