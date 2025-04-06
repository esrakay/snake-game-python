import snake_game.configs as configs
from snake_game.models.snake import Snake
from snake_game.models.food import Food

X_BORDER_LIMIT = configs.GAME_WIDTH // 2 - 20
Y_BORDER_LIMIT = configs.GAME_HEIGHT // 2 - 20
DISTANCE_LIMIT = 15


class CollisionManager:
    def __init__(self, snake: Snake, food: Food) -> None:
        self.snake = snake
        self.food = food

    def snake_ate_food(self) -> bool:
        return self.snake.head.distance(self.food.position()) < DISTANCE_LIMIT

    def snake_hit_wall(self) -> bool:
        x, y = self.snake.head.xcor(), self.snake.head.ycor()
        return abs(x) > X_BORDER_LIMIT or abs(y) > Y_BORDER_LIMIT
