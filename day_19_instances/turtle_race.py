from turtle import Turtle, Screen
import random

is_race_on = False

tim = Turtle(shape="turtle")
bob = Turtle(shape="turtle")
harriet = Turtle(shape="turtle")
chelsea = Turtle(shape="turtle")
peanut = Turtle(shape="turtle")

colors = ["blue", "green", "black", "orange", "red"]
turtles = {
    "tim": tim,
    "bob": bob,
    "harriet": harriet,
    "chelsea": chelsea,
    "peanut": peanut
}
names = []
screen = Screen()
screen.setup(width=500, height=400)  # x: -250 0 250 ; y: -200 0 200

index = 0
start = -100  # keep these values outside
for name, turtle in turtles.items():
    turtle.color(colors[index])
    turtle.penup()
    turtle.goto(x=-230, y=start)
    start += 50
    index += 1
    names.append(name)
    screen.title(f"{name.title()}")

screen.title(f', '.join(names).title())  # ', '. join all names and titles them

user_bet = screen.textinput\
(
    title="Captain William Presents: Turtle Racing",
    prompt="Choose your turtle!"
).lower()

if user_bet:
    is_race_on = True

while is_race_on:

    for name, turtle in turtles.items():
        for _ in range(3):
            rand_distance = random.randint(0, 10)
            turtle.forward(rand_distance)
        if turtle.xcor() > 220:
            is_race_on = False
            winning_turtle = name
            if winning_turtle == user_bet:
                print("You win!")
            else:
                print(f"You lose, the winner was {name}")

screen.exitonclick()
