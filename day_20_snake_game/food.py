from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):  # what is innate to food
        super().__init__()  # is everything innate to Turtle
        self.penup()
        self.shape("circle")
        self.shapesize(stretch_wid=.5, stretch_len=.5)
        self.color("white")
        self.speed("fastest")

    def refresh(self):
        random_x = random.randint(-270, 270)
        random_y = random.randint(-270, 270)
        self.goto(random_x, random_y)