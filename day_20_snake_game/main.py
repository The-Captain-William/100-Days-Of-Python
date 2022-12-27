from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

screen = Screen()
screen.listen()

screen.setup(width=600, height=600)
screen.bgcolor(0.27, 0.30, 0.30)
screen.title("Captain William Presents: SNAKE GAME")

screen.tracer(0)  # no refresh

snake = Snake()
score_board = ScoreBoard()
food = Food()
food.refresh()

screen.onkey(snake.up, "Up")
screen.onkey(snake.left, "Left")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")

game_is_on = True

while game_is_on is True:
    screen.update()  # turn on, run loop, refresh
    time.sleep(.05)  # sleep only .1 second once before and after all 3 units move
    snake.move()

    if snake.snake_head.distance(food) < 15:
        food.refresh()
        snake.add_segment()
        score_board.score_point()

    head = snake.snake_head

    # bounding box collision
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        # game_is_on = False
        # score_board.clear()
        # score_board.game_over()
        score_board.reset()
        snake.reset()

    # tail collision
    # for segment in snake.snake_unit:
    #     if segment == snake.snake_head:
    #         pass
    #     elif snake.snake_head.distance(segment) < 10:  # if distance of head < 10 pix
    #         game_is_on = False
    #         score_board.game_over()

    # tail collision simplified
    for segment in snake.snake_unit[1:]:  # in list from index range 1 -> end
        if snake.snake_head.distance(segment) < 10:
            score_board.reset()
            snake.reset()
            # game_is_on = False
            # score_board.game_over()

screen.exitonclick()
