from snake_game.classes.snake_body import SnakeBody

NORTH = 90
WEST = 180
SOUTH = 270
EAST = 0
MOVEMENT_DISTANCE = 20
STARTING_X_POS = [(0, 0), (-20, 0), (-40, 0)]


class Snake:
    def __init__(self):
        self.body = []
        self.create_snake()
        self.head = self.body[0]

    def create_snake(self):
        for position in STARTING_X_POS:
            self.add_body(position)

    def add_body(self, position):
        new_body = SnakeBody()
        new_body.goto(position)
        self.body.append(new_body)

    def move(self):
        for i in range(len(self.body) - 1, 0, -1):
            x_pos = self.body[i - 1].xcor()
            y_pos = self.body[i - 1].ycor()
            self.body[i].goto(x_pos, y_pos)
        self.head.forward(MOVEMENT_DISTANCE)

    def expand(self):
        tail = self.body[-1]
        self.add_body(tail.position())

    def up(self):
        if not self.head.heading() == SOUTH:
            self.head.setheading(NORTH)

    def left(self):
        if not self.head.heading() == EAST:
            self.head.setheading(WEST)

    def right(self):
        if not self.head.heading() == WEST:
            self.head.setheading(EAST)

    def down(self):
        if not self.head.heading() == NORTH:
            self.head.setheading(SOUTH)
