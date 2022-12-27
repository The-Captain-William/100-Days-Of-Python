import turtle
import pandas

# coordinate functionality
# def get_mouse_click(x, y):
#     print(x, y)
#
#
# turtle.onscreenclick(get_mouse_click)
#
# turtle.mainloop()  #

screen = turtle.Screen()
screen.title("Captain William Presents: U.S STATES GAME")
country = "blank_states_img.gif"
screen.addshape(country)
turtle.shape(country)

all_states = pandas.read_csv("50_states.csv")
x_coor = all_states["x"]
y_coor = all_states["y"]
# print(states[states["state"] == "Texas"])
# print(state_series)
#  title of window; prompt in side window
correct = 0
states_num = 50
guessed_states = []
missing_states = []
while states_num > 0:
    total = f"{correct}/{len(all_states['state'])}"
    results = f"Results: {total}, Your score is: {(correct/50) * 100}%!"

    answer_state = screen.textinput(title="Guess the state.",
                                    prompt=f"Name a State. {total} Correct."
                                           f" {states_num} tries remaining")
    if answer_state is not None:
        for actual_state in all_states["state"]:
            if answer_state == actual_state.lower():
                guessed_states.append(actual_state)
                correct += 1
                state_row = all_states[all_states["state"] == actual_state]
                state_turtle = turtle.Turtle()
                state_turtle.hideturtle()
                state_turtle.penup()
                state_turtle.color("black")
                state_turtle.goto(int(state_row.x), int(state_row.y))
                state_turtle.write(arg=actual_state)
        states_num -= 1
    else:
        states_num = 0
        screen.title(titlestring=results)
        ending_screen = turtle.Turtle()
        ending_screen.hideturtle()
        ending_screen.color("black")
        ending_screen.penup()
        ending_screen.goto(0, -300)
        ending_screen.write(arg=results, font=("Arial", 24, "normal"), align="center")

all_states_list = all_states["state"].to_list()
missing_states_2 = [state for state in all_states_list if state not in guessed_states]
states_to_learn_dict = {"Missing states": missing_states_2}
pandas.DataFrame(states_to_learn_dict).to_csv("States to Learn.csv")

screen.exitonclick()
