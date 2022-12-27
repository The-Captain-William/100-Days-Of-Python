import random
from turtle import Turtle


class GeometryCalc:
    def __init__(self, turtle, sides):
        self.turtle = turtle  # input turtle now becomes an input of the class object geometry calc
        triangle = 3  # triangle is the base polygon
        repeat = True
        while repeat is True:
            self.turtle_color_random()  # call on random turtle method
            for _ in range(triangle):  # in range sides, loops
                turtle.forward(100)
                turtle.left(360/triangle)  # polygons angles are equal to 360 / num of sides
            if sides > 0:  # after triangle, checks if sides  are > 0
                triangle += 1
            if sides == triangle:  # once complete, repeat is terminated
                repeat = False

    def turtle_color_random(self):
        color_list = []
        for _ in range(3):  # pick 3 floats from 0 to 1
            color_number = random.uniform(0, 1)  # random float
            color_number = round(color_number, 2)  # round to 2 decimal places
            color_list.append(color_number)
        # self.turtle.color(color_list[0], color_list[1], color_list[2])  # assigned to rgb, alternate
        self.turtle.color(random.choice(color_list), random.choice(color_list), random.choice(color_list))
        color_list.clear()


  # function method:
# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     for _ in range(num_sides):  # num sides
#         tim.forward(100)
#         tim.right(angle)  # angle
#
#
# for shape_side_n in range(3, 10):  # in range from 3 to 10
#     tim.color(random.choice(colours))
#     draw_shape(shape_side_n)  # at 3, sides 3, at 4, sides 4, etc.


class RandomWalk:
    def __init__(self, turtle, path_length):
        self.turtle = turtle
        self.path_length = path_length

    def random_return(self):
        turtle_commands = [
            self.turtle.left(90),
            self.turtle.right(90)
        ]
        return random.choice(turtle_commands)


class RandomColor:  # honestly just a def would have been better
    def __init__(self, turtle):
        self.turtle = turtle
        color_list = []
        for _ in range(3):  # pick 3 floats from 0 to 1
            color_number = random.uniform(0, 1)  # random float
            color_number = round(color_number, 2)  # round to 2 decimal places
            color_list.append(color_number)
        # self.turtle.color(color_list[0], color_list[1], color_list[2])  # assigned to rgb, alternate
        self.turtle.color(random.choice(color_list), random.choice(color_list), random.choice(color_list))
        color_list.clear()
