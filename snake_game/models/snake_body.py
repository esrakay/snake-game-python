from turtle import Turtle


class SnakeBody(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.shape("square")
        self.penup()
        self.color("white")
