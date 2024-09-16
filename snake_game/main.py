import time
from turtle import Screen
from snake_game.classes.snake import Snake


screen = Screen()
screen.setup(500, 500)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
screen.listen()


snake = Snake()
screen.onkey(snake.right, "d")
screen.onkey(snake.up, "w")
screen.onkey(snake.left, "a")
screen.onkey(snake.down, "s")

while True:
    snake.move()
    screen.update()
    time.sleep(0.07)


screen.exitonclick()

if __name__ == "__main__":
    main()