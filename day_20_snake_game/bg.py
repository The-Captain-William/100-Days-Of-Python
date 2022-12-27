from turtle import Turtle


class BG(Turtle):
    def __init__(self):
        super().__init__()
        self.speed("fastest")
        self.penup()
        self.shape("square")
        self.color("black")
        self.shapesize(stretch_len=30, stretch_wid=30)
