import turtle
from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        with open("data.txt") as score:
            self.high_score = int(score.read())
        self.penup()
        self.setposition(0, 280)
        self.score = 0
        self.hideturtle()
        self.color("white")
        self.write_score()  # call write

    def write_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align="center", font=("Courier", 12, "normal"))

    def score_point(self):
        self.score += 1
        self.check()
        self.clear()  # clear
        self.write_score()  # call write

    def game_over(self):
        self.setposition(0, 0)
        self.write(f"GAME OVER. Final Score: {self.score}", align="center", font=("Courier", 24, "normal"))
        if self.score == 0:
            self.goto(0, -30)
            self.write("YOU SUCK", align="center", font=("Courier", 24, "normal"))

    def reset(self):
        self.check()
        with open("data.txt", mode="w") as score:
            score.write(str(self.high_score))
        self.score = 0
        self.write_score()

    def check(self):
        if self.score > self.high_score:
            self.high_score = self.score
