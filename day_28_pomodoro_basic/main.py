import tkinter as tk
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"  # hex codes
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK = "Work"
BREAK = "Break"
TIME_START = "00:00"
TIMER_LABEL = "Timer"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20


# ---------------------------- GLOBAL VARIABLES ------------------------------- #
reps = 1
count_mechanism = None

# ---------------------------- TIMER RESET ------------------------------- #


# noinspection PyTypeChecker
def timer_reset():
    window.after_cancel(count_mechanism)
    global reps
    reps = 1
    canvas.itemconfig(timer_text, text=TIME_START)
    check_mark.config(text='')
    timer_label.config(text=TIMER_LABEL)

# ---------------------------- TIMER MECHANISM ------------------------------- # 


def start_timer():
    global reps
    work_sec = WORK_MIN * 60
    break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps % 8 == 0:  # 4 breaks, 4 pomodoros
        timer_label.config(text=BREAK, fg=RED)
        count_down(long_break_sec)
    elif reps % 2 != 0:  # if 1, 3, 5
        timer_label.config(text=WORK, fg=GREEN)
        count_down(work_sec)
        if reps != 1:
            check = "✔" * math.ceil(reps / 3)  # 3/3 = 1, 5/3 ~ 2, 7/3 ~ 3, etc.
            check_mark.config(text=check)
    elif reps % 2 == 0:
        timer_label.config(text=BREAK, fg=PINK)
        count_down(break_sec)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):  # takes int
    count_minute = math.floor(count / 60)  # math module
    count_second = count % 60  # remainder = seconds; recall modulo = 'remainder of count / 60'
    if count_second <= 9:  # ❓ I think this checks to see if 0 remainder OR 0 times it can divide ex:(120 % 60 = 2 R 0)
        count_second = f"0{count_second}"  # replace with fstring if sec is 0 or less than 10.
        # this works because loop depends on 'count'
    canvas.itemconfig(timer_text, text=f"{count_minute}:{count_second}")  # 👀
    # configs canvas item dubbed "timer_text", modifies 'text' kwarg
    if count > 0:
        global count_mechanism  # call global, then assign value
        count_mechanism = window.after(1000, count_down, count - 1)  # after 1s, call count_down(), with argument "count - 1"
    elif count == 0:
        global reps
        reps += 1
        start_timer()  # will re-initialize pomodoro

    # everything w.r.t seconds because window is checking every second. Plus it looks cleaner and has more purpose.


# ---------------------------- UI SETUP ------------------------------- #

# window


window = tk.Tk()  # module / class
window.title("Captain William Presents: Pomodoro Timer")
window.config(padx=100, pady=50, bg=YELLOW)  # this will expand the window around the canvas
window.minsize(width=220, height=224)

# label
timer_label = tk.Label(text=TIMER_LABEL, font=(FONT_NAME, 35, "bold"), fg=GREEN, borderwidth=0, bg=YELLOW)
timer_label.grid(column=1, row=1)


# checkmark
check_mark = tk.Label(bg=YELLOW, borderwidth=0, fg=GREEN)
check_mark.grid(column=1, row=4)

# canvas
canvas = tk.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)  # even numbers
tomato = tk.PhotoImage(file="tomato.png")  # needed to create file object
canvas.create_image(100, 112, image=tomato)  # exact origin since we are using even numbers; still had to shift
canvas.grid(column=1, row=2)
timer_text = canvas.create_text(100, 130,  # args are x,y, kwargs are kwargs associated with method. Note same canvas.
                                text=TIME_START,
                                fill="white",
                                font=(FONT_NAME, 35, "bold"),  # always tuple with this module collection
                                )
# note that you can apply multiple methods on the same canvas, and they all work synergistically
# note that the x and y is w.r.t the canvas and not a traditional cartesian plane. the max height of the image is y = 0

# buttons
start_button = tk.Button(text="start", command=start_timer)  # call function with no parameters
start_button.grid(column=0, row=3)

restart_button = tk.Button(text="restart", command=timer_reset)
restart_button.grid(column=2, row=3)

window.mainloop()
