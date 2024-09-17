import time
from turtle import Screen
from snake_game.classes.snake import Snake
from snake_game.classes.food import Food
from snake_game.classes.scoreboard import Scoreboard


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


def has_collided(snake, food):
    if snake.head.distance(food.position()) < 15:
        return True
    return False


def hit_wall(snake):
    if snake.head.xcor() > 230 or snake.head.xcor() < -230 or snake.head.ycor() > 230 or snake.head.ycor() < -230:
        return True
    return False


def main():
    screen = set_screen()
    snake = Snake()
    food = Food()
    scoreboard = Scoreboard()
    set_controllers(snake=snake, screen=screen)

    game_is_on = True
    while game_is_on:
        snake.move()
        screen.update()
        time.sleep(0.1)

        if has_collided(snake, food):
            scoreboard.increase_score()
            snake.expand()
            food.relocate()

        if hit_wall(snake):
            game_is_on = False
            scoreboard.game_over()


    screen.exitonclick()


if __name__ == "__main__":
    main()
