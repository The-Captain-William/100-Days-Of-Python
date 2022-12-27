from turtle import Turtle

FONT = "Courier"
FONT_SIZE = 80
FONT_TYPE = "normal"
ALIGN = "center"


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.l_score = 0
        self.r_score = 0
        self.goto(0, 200)

    def add_score_l(self):
        self.l_score += 1
        self.write_score()

    def add_score_r(self):
        self.r_score += 1
        self.write_score()


    def write_score(self):
        self.clear()
        self.write(f"{self.l_score}         {self.r_score}",
                   align=ALIGN, font=(FONT, FONT_SIZE, FONT_TYPE))


