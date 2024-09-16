from snake_body import SnakeBody

NORTH = 90
WEST = 180
SOUTH = 270
EAST = 0
MOVEMENT_DISTANCE = 20
STARTING_X_POS = [0, -20, -40]


class Snake:
    def __init__(self):
        self.body = []
        self.create_snake()
        self.head = self.body[0]

    def create_snake(self):
        for i in range(3):
            new_body = SnakeBody()
            new_body.goto(STARTING_X_POS[i], 0)
            self.body.append(new_body)

    def move(self):
        for i in range(len(self.body) - 1, 0, -1):
            x_pos = self.body[i - 1].xcor()
            y_pos = self.body[i - 1].ycor()
            self.body[i].goto(x_pos, y_pos)
        self.head.forward(MOVEMENT_DISTANCE)

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
