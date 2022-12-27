from turtle import Turtle


class Snake:
    def __init__(self):
        self.colors = ["black", "yellow", "red"]
        self.snake_head = Turtle("square")  # all values w.r.t self
        self.snake_body = Turtle("square")
        self.snake_body_cont = Turtle("square")

        self.snake_head.penup()
        self.snake_body.penup()
        self.snake_body_cont.penup()

        self.snake_head.color("green")
        self.snake_body.color("Yellow")
        self.snake_body_cont.color("red")

        self.snake_unit = [self.snake_head, self.snake_body, self.snake_body_cont]
        self.snake_unit_default = [self.snake_head, self.snake_body, self.snake_body_cont]  # 1 2 3

        # alignment
        position_of_head = self.snake_head.pos()
        self.snake_body.setposition(position_of_head[0] - 20, position_of_head[1])
        self.snake_body_cont.setposition(position_of_head[0] - 40, position_of_head[1])
        self.snake_body_cont.pos()

    def add_segment(self):
        new_segment = Turtle("square")
        new_segment.penup()
        new_segment.color(self.colors[0])
        new_segment.goto(self.snake_body_cont.pos())  # won't go from center to tail
        color = self.colors[0]
        self.colors.pop(0)
        self.colors.append(color)
        self.snake_unit.append(new_segment)  # note only this is w.r.t itself and the rst is not an attribute

    def move(self):  # .self method will do this once. while loop in main will keep it going
        for index_num in range(len(self.snake_unit) - 1, 0, -1):  # for index in start, stop, step
            new_x = self.snake_unit[index_num - 1].xcor()  # // step == how to go from start to stop
            new_y = self.snake_unit[index_num - 1].ycor()  # range(index 2, to zero, going down 1)
            self.snake_unit[index_num].goto(new_x, new_y)

        self.snake_unit[0].forward(20)  # same as snake_head.forward(20)

        #  2 1 0 from 2 to 1, stop at zero
        #  0 1 2
        #  Remember range does not include 0 here, so the head is not affected.

    def reset(self):
        for seg in self.snake_unit[3:]:  # all but 0 1 2
            seg.hideturtle()  # hide from player
        del self.snake_unit[3:]  # delete from list
        self.snake_head.setposition(0, 0)

    def upright(self):
        self.snake_head.setheading(0)

    def up(self):
        if self.snake_head.heading() == 270:
            pass
        else:
            self.upright()  # orientation w.r.t screen
            self.snake_head.setheading(90)

    def left(self):
        if self.snake_head.heading() == 0:
            pass
        else:
            self.upright()
            # self.snake_head.setheading(0)
            self.snake_head.left(180)

    def down(self):
        if self.snake_head.heading() == 90:
            pass
        else:
            self.upright()
            # self.snake_head.setheading(0)
            self.snake_head.left(270)

    def right(self):
        if self.snake_head.heading() == 180:
            pass
        else:
            self.upright()
            # self.snake_head.setheading(0)
            self.snake_head.right(0)

    # screen time input function accepts movement method, movement method calls upright function / method
