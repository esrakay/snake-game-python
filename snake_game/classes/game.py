import time
from turtle import Screen
from snake_game.classes.snake import Snake


class Game:
    def __init__(self):
        self.screen = Screen()
        self.set_screen()
        self.snake = Snake()
        self.set_events()

    def set_screen(self):
        self.screen.setup(500, 500)
        self.screen.bgcolor("black")
        self.screen.title("Snake Game")
        self.screen.tracer(0)
        self.screen.listen()

    def set_events(self):
        self.screen.onkey(self.snake.right, "d")
        self.screen.onkey(self.snake.up, "w")
        self.screen.onkey(self.snake.left, "a")
        self.screen.onkey(self.snake.down, "s")

    def start_game(self):
        while True:
            print('hi')
            self.snake.move()
            self.screen.update()
            time.sleep(0.07)

        self.screen.exitonclick()
