from turtle import Screen

from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

#  player
player = Player()

#  screen
screen = Screen()
screen.listen()
screen.onkeypress(player.move_up, "Up")
screen.onkeypress(player.move_left, "Left")
screen.onkeypress(player.move_right, "Right")
screen.onkeypress(player.move_down, "Down")
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)


# score
score = Scoreboard()
score.refresh_score()

# cars
CARS = 100
traffic = {num: CarManager() for num in range(CARS)}  # dictionary comprehension.
for num in range(CARS):
    traffic[num].spawn()

#  game start
game_is_on = True
while game_is_on:
    if player.ycor() >= 320:
        player.start()
        score.point()
        score.refresh_score()
        player.sayings()

    for num in range(CARS):
        traffic[num].nextlevel(score.score)  # dictionary[key].method // calling a dictionary item like this is the same
        if traffic[num].xcor() <= -330:      # as using the item itself.
            traffic[num].spawn()
        if traffic[num].distance(player.pos()) < 25:
            score.game_over()
            game_is_on = False
    screen.update()

screen.exitonclick()

