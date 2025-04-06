from snake_game.models.snake_body import SnakeBody

NORTH = 90
WEST = 180
SOUTH = 270
EAST = 0
MOVEMENT_DISTANCE = 20
STARTING_X_POS = [(0, 0), (-20, 0), (-40, 0)]


class Snake:
    def __init__(self) -> None:
        self.body = []
        self.create_snake()
        self.head = self.body[0]

    def create_snake(self) -> None:
        for position in STARTING_X_POS:
            self.add_body(position)

    def reset(self) -> None:
        self.body = []
        self.create_snake()

    def add_body(self, position: (float, float)) -> None:
        new_body = SnakeBody()
        new_body.goto(position)
        self.body.append(new_body)

    def move(self) -> None:
        for i in range(len(self.body) - 1, 0, -1):
            x_pos = self.body[i - 1].xcor()
            y_pos = self.body[i - 1].ycor()
            self.body[i].goto(x_pos, y_pos)
        self.head.forward(MOVEMENT_DISTANCE)

    def expand(self) -> None:
        tail = self.body[-1]
        self.add_body(tail.position())

    def collided_with_tail(self) -> bool:
        tails = self.body[1:]
        for tail in tails:
            if self.head.distance(tail.position()) < 10:
                return True
        return False

    def up(self) -> None:
        if not self.head.heading() == SOUTH:
            self.head.setheading(NORTH)

    def left(self) -> None:
        if not self.head.heading() == EAST:
            self.head.setheading(WEST)

    def right(self) -> None:
        if not self.head.heading() == WEST:
            self.head.setheading(EAST)

    def down(self) -> None:
        if not self.head.heading() == NORTH:
            self.head.setheading(SOUTH)
