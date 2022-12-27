from turtle import Turtle
import random


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.setposition(0, 0)
        self.x_move = 10
        self.y_move = 10

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)  # dynamic x instead of "set -350" or "set 350"

    def move_alt(self):
        self.goto(self.xcor() + self.x_move * -1, self.ycor() + self.y_move * -1)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1

    def initial_v(self):
        choices = [self.move(), self.move()]
        choice = random.choice(choices)
        return choice

    def reset_ball(self):
        self.hideturtle()
        self.setposition(0, 0)
        if self.pos() == (0, 0):
            self.showturtle()


