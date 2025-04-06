from turtle import Screen, Turtle
from .border import Border
import snake_game.configs as configs


class GameScreen:
    def __init__(self) -> None:
        self.screen = Screen()
        self.borders = []
        self.setup_screen()

    def setup_screen(self) -> None:
        self.screen.setup(configs.SCREEN_HEIGHT, configs.SCREEN_HEIGHT)
        self.screen.bgcolor('black')
        self.screen.title('Snake Game')
        self.screen.tracer(0)
        self.screen.listen()
        self.setup_borders()

    def setup_borders(self) -> None:
        self.borders = [
            Border(position=(configs.GAME_WIDTH // 2, 0), head_direction=0),
            Border(position=(-configs.GAME_WIDTH // 2, 0), head_direction=0),
            Border(position=(0, configs.GAME_WIDTH // 2), head_direction=90),
            Border(position=(0, -configs.GAME_WIDTH // 2), head_direction=90),
        ]

    def get_screen(self) -> Screen:
        return self.screen
