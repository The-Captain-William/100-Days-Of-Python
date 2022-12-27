import random
from turtle import Turtle

STARTING_MOVE_DISTANCE = 0.1
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        COLORS_R = []
        for _ in range(3):  # rgb from .20 to 1.0
            COLORS_R.append(random.uniform(.20, 1.0))
        self.color(COLORS_R[0], COLORS_R[1], COLORS_R[2])
        self.shape("square")
        self.setheading(180)
        self.shapesize(stretch_wid=1, stretch_len=2)  # 2 * 20 = 40
        self.penup()
        self.goto(650, 300)   # 600 x 600; offset
        self.speed(1)  # slowest speed

    def spawn(self):
        rand_x_val = random.randint(330, 2200)
        rand_y_val = random.randrange(-200, 260, 10)
        self.goto(rand_x_val, rand_y_val)

    def nextlevel(self, score):
        score = STARTING_MOVE_DISTANCE + score/10  # moves by 0.1 units + score/10
        self.forward(score)


