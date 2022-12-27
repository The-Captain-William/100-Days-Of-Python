from turtle import Screen
from paddle import Paddle
from ball import Ball
from score_board import ScoreBoard
import time

# TODO: Make a Screen ✅
# TODO: Create and move a paddle ✅
# TODO: Create another paddle ✅
# TODO: Create a ball and make it move ✅
# TODO: Detect collision with wall and bounce ✅
# TODO: Detect collision with paddle  ✅
# TODO: Detect when paddle misses ✅
# TODO Keep score ✅


PADDLE_ONE_UP = "Up"
PADDLE_ONE_DOWN = "Down"
PADDLE_TWO_UP = "w"
PADDLE_TWO_DOWN = "s"


# initialize screen start

screen = Screen()
screen.setup(width=900, height=700)
screen.title(titlestring="Captain William Presents: PONG")
screen.bgcolor("black")
screen.listen()
screen.tracer(0)  # no update

# paddle

paddle_1 = Paddle()
paddle_1.setposition(-400, 0)  # left

paddle_2 = Paddle()
paddle_2.setposition(400, 0)  # right

# ball

ball = Ball()
ball.speed("slow")



# initialize screen end

# scoreboard
score_p1 = ScoreBoard()
score_p1.write_score()

screen.tracer(1)  # update // this is so the paddle does not flip in front of viewer on game start

# paddle keybinds

screen.onkeypress(paddle_1.up, PADDLE_ONE_UP)
screen.onkeypress(paddle_1.down, PADDLE_ONE_DOWN)

screen.onkeypress(paddle_2.up, PADDLE_TWO_UP)
screen.onkeypress(paddle_2.down, PADDLE_TWO_DOWN)
game_on = True


while game_on is True:
    time.sleep(0.01)
    ball.initial_v()
    print(ball.pos())
    if ball.ycor() > 330 or ball.ycor() < - 330:
        print("contact_wall")
        ball.bounce_y()

    if ball.distance(paddle_2) < 40 and ball.xcor() > 380 or ball.distance(paddle_1) < 40 and ball.xcor() < -380:
        ball.bounce_x()
        print("contact")
    elif ball.xcor() > 450 or ball.xcor() < -450:
        if ball.xcor() > 450:
            print("confirm")
            score_p1.add_score_l()
        elif ball.xcor() < -450:
            score_p1.add_score_r()
        ball.reset_ball()




screen.exitonclick()


