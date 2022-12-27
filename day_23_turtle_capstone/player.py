import random
from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()  # ❓ why this?
        self.color("White")
        self.penup()
        self.goto(STARTING_POSITION)
        self.shape("turtle")
        self.setheading(90)

    def move(self):
        self.forward(MOVE_DISTANCE)

    def orient(self):
        self.setheading(90)

    def move_up(self):
        self.orient()
        self.move()

    def start(self):
        self.goto(STARTING_POSITION)

    def move_left(self):
        self.orient()
        self.setheading(180)
        self.move()

    def move_right(self):
        self.orient()
        self.setheading(0)
        self.move()

    def move_down(self):
        self.orient()
        self.setheading(270)
        self.move()

    def sayings(self):
        sayings = ["aw yee", "yip yip", "sheee", "lets get this bread", "aint nothin to it but to do it",
                   "LIGHT-WEIGHT BABAAYYY"]
        self.clear()
        self.write(random.choice(sayings))

