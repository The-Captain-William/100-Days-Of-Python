import random
from turtle import Turtle, Screen
from random import Random
# from colorgram import colorgram
#
# hirst_colors = colorgram.extract('image.jpg', 16)
# color_list = []
#
# for color in hirst_colors:
#     color_list.append((color.rgb[0], color.rgb[1], color.rgb[2]))
#
#
# print(color_list)
brush = Turtle()
brush.ht()  # hide
brush.penup()  # no lines
brush.setposition(-250, 0)  # if there is a dot every 50 units, for 10 dots, that's 500 units squared
screen = Screen()           # origin w.r.t square is 250 units
screen.colormode(255)

color_list = [(182, 7, 46), (156, 95, 30), (23, 95, 185), (192, 157, 92), (246, 215, 52), (218, 145, 175),
              (178, 200, 6), (237, 242, 238), (67, 154, 95), (244, 234, 239), (125, 43, 125), (72, 55, 49),
              (81, 56, 51), (65, 146, 91)]

brush.speed(0)
set_pos = 50  # set pos outside loop
for _ in range(10):  # 10
    for _ in range(10):  # 10
        brush.forward(50)
        brush.dot(30, random.choice(color_list))
    brush.setposition(-250, set_pos)  # position -250 x, 50 y
    set_pos += 50  # repeat + 50 y every loop

screen.exitonclick()
