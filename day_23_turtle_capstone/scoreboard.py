from turtle import Turtle
FONT = ("Courier", 24, "normal")
FONTG = ("Courier", 20, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.setposition(0, 250)
        self.score = 0
        self.hideturtle()
        self.color("White")

    def point(self):
        self.score += 1

    def refresh_score(self):
        self.clear()
        self.write(f"Score: {self.score}", font=FONT, align="center")

    def game_over(self):
        self.clear()
        self.write(f"GAME OVER. Your Final Score was {self.score}", font=FONTG, align="center")
