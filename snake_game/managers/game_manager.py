import time

from snake_game.models.game_screen import GameScreen
from snake_game.models.snake import Snake
from snake_game.models.food import Food
from snake_game.models.scoreboard import Scoreboard
from collision_manager import CollisionManager


class GameManager:
    def __init__(self) -> None:
        self.game_screen = GameScreen()
        self.snake = Snake()
        self.food = Food()
        self.scoreboard = Scoreboard()
        self.collision_manager = CollisionManager(self.snake, self.food)

        self.is_game_over = False

        self.setup_controls()

    def setup_controls(self) -> None:
        self.game_screen.get_screen().onkey(self.snake.right, 'd')
        self.game_screen.get_screen().onkey(self.snake.up, 'w')
        self.game_screen.get_screen().onkey(self.snake.left, 'a')
        self.game_screen.get_screen().onkey(self.snake.down, 's')
        self.game_screen.get_screen().onkey(self.restart_game, 'e')

    def update(self) -> None:
        if self.is_game_over:
            return

        self.snake.move()
        time.sleep(0.1)

        if self.collision_manager.snake_ate_food():
            self.scoreboard.increase_score()
            self.snake.expand()
            self.food.relocate()

        if self.collision_manager.snake_hit_wall() or self.snake.collided_with_tail():
            self.end_game()

    def end_game(self) -> None:
        self.is_game_over = True
        self.scoreboard.game_over()

    def restart_game(self) -> None:
        if not self.is_game_over:
            return

        self.scoreboard.set_score(0)
        self.snake.reset()
        self.game_screen.get_screen().clear()
        self.__init__()

    def run(self) -> None:
        while True:
            self.update()
            self.game_screen.get_screen().update()
