from turtle import Turtle, Screen

tim = Turtle()

screen = Screen()
screen.listen()


def move_forwards():
    tim.forward(10)


def move_forwards_10():
    tim.forward(100)


def move_backwards():
    tim.back(10)


def rotate_left():
    tim.left(10)


def rotate_right():
    tim.right(10)


def clear():
    tim.clear()
    tim.penup()
    tim.setposition(0, 0)
    tim.pendown()


screen.onkeypress(key="w", fun=move_forwards)  # no () for fun that operates as an argument for turtle
screen.onkeypress(key="s", fun=move_backwards)
screen.onkeypress(key="q", fun=rotate_left)
screen.onkeypress(key="e", fun=rotate_right)
screen.onkey(key="c", fun=clear)

screen.exitonclick()
