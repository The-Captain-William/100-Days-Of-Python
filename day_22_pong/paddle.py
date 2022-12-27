from turtle import Turtle
import random


class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.setheading(90)
        self.shapesize(stretch_wid=1, stretch_len=4)

    def up(self):
        self.forward(20)

    def down(self):
        self.backward(20)


