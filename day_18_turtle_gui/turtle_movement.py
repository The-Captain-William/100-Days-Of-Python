import random

from custom_class import GeometryCalc, RandomWalk, RandomColor
from turtle import Turtle, Screen
tim = Turtle()
tim.shape("turtle")
tim.pensize(2)

# # geom_calc = GeometryCalc(sides=20, turtle=tim)
# directions = [0, 90, 180, 270]

# for _ in range(200):
#     tim.forward(30)
#     tim.setheading(random.choice(directions))
#     RandomColor(tim)

tim.speed(0)
for _ in range(int(360/5)):
    tim.circle(radius=100)
    tim.left(10)
    RandomColor(tim)

screen = Screen()
screen.exitonclick()
