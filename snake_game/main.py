import time
from turtle import Screen
from snake_game.classes.snake import Snake


def set_screen():
    screen = Screen()
    screen.setup(500, 500)
    screen.bgcolor("black")
    screen.title("Snake Game")
    screen.tracer(0)
    screen.listen()
    return screen


def set_controllers(snake, screen):
    screen.onkey(snake.right, "d")
    screen.onkey(snake.up, "w")
    screen.onkey(snake.left, "a")
    screen.onkey(snake.down, "s")


def main():
    screen = set_screen()
    snake = Snake()
    set_controllers(snake=snake, screen=screen)

    game_is_on = True
    while game_is_on:
        snake.move()
        screen.update()
        time.sleep(0.07)



    screen.exitonclick()


if __name__ == "__main__":
    main()