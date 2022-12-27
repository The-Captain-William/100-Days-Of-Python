import tkinter as tk
import pandas as pd
import random

card = False

BACKGROUND_COLOR = "#B1DDC6"
FRONT_CARD_COLOR = "#FFFFFF"
CARD_BACK_COLOR = "#91C2AF"

HANZI_DEFAULT_FONT = ("Ariel", 150, "bold")
HANZI_SMALLER_FONT = ("Ariel", 100, "bold")
DEFINITION_LARGE_FONT = ("Ariel", 20, "bold")
DEFINITION_SMALL_FONT = ("Ariel", 17, "bold")

# ------- CSV FILES ------- #
to_learn_1000 = pd.read_csv("data/first_1000_chars.csv")

# ------- FUNCTIONS -------#

# functions can be called all over the place, classes can-not
# we call this function after hanzi and pinyin have been created

current_card = random.choice(to_learn_1000.values)


def flip():
    card_flip()
    root.after(2000, card_flip)


def flow():
    card_flip()
    root.after(2000, next_card)


def next_card():
    global current_card
    current_card = random.choice(to_learn_1000.values)

    if len(current_card[1]) > 2:  # if hanzi more than 2 char
        hanzi.config(font=HANZI_SMALLER_FONT)
    else:
        hanzi.config(font=HANZI_DEFAULT_FONT)

    flash_card.create_image(400, 263, image=flash_front_img)
    hanzi.config(text=current_card[1], bg=FRONT_CARD_COLOR)
    pinyin.config(text=current_card[0], bg=FRONT_CARD_COLOR)
    definition.config(text='', bg=FRONT_CARD_COLOR)
    global card
    card = False


def card_flip():
    global card
    if card is False:
        flash_card.create_image(400, 263, image=flash_back_img)
        hanzi.config(bg=CARD_BACK_COLOR)
        pinyin.config(bg=CARD_BACK_COLOR)
        split = str(current_card[2]).split(", ")  # splits into list
        definition_list = ""
        if len(split) > 5:  # if more than 5 words # (regular words)
            definition.config(font=DEFINITION_SMALL_FONT)  # make small font
            for word in split[0:3]:
                definition_list += f'{word}, '  # only add the first 4
            definition.config(text=definition_list, bg=CARD_BACK_COLOR)
        else:
            definition.config(text=current_card[2], font=DEFINITION_LARGE_FONT, bg=CARD_BACK_COLOR)
        card = True
    else:
        flash_card.create_image(400, 263, image=flash_front_img)
        hanzi.config(bg=FRONT_CARD_COLOR)
        pinyin.config(bg=FRONT_CARD_COLOR)
        definition.config(text='', bg=FRONT_CARD_COLOR)
        card = False


def remove_from_stack(n):
    # will either ask or have assigned a number
    to_learn_1000.remove(current_card)
    sorted_data = pd.DataFrame(to_learn_1000)
    sorted_data.to_csv("words to learn.csv")


def know_card():
    # prompt to ask what rating is
    # temporarily cover up card info then dissapear
    pass


def dont_know_card():
    # know rating is zero
    dont_know_df = pd.DataFrame
    dont_know_df.insert(current_card)

    pass


# ------- UI ------- #

# // root window //

root = tk.Tk()
root.title("Captain William Presents: 中国 Flashcard Game")
root.iconbitmap("images/chinese_food.ico")
root.config(background=BACKGROUND_COLOR, padx=50, pady=50)
root.minsize(width=880, height=725)
root.maxsize(width=880, height=725)

# flashcard front and back images
flash_front_img = tk.PhotoImage(file="images/card_front.png")  # 👀 note the directory format folder/--/--
flash_back_img = tk.PhotoImage(file="images/card_back.png")

# flashcard canvas
flash_card = tk.Canvas(width=800, height=526, bg=BACKGROUND_COLOR, borderwidth=0, border=0, highlightthickness=0)
flashcard_front = flash_card.create_image(400, 263, image=flash_front_img)
flash_card.grid(row=0, column=0, columnspan=4, rowspan=3)

# // labels //


# hanzi
hanzi = tk.Label(font=("Ariel", 150, "bold"), borderwidth=0, bg=FRONT_CARD_COLOR)
hanzi.grid(row=0, column=0, columnspan=4)

# pinyin
pinyin = tk.Label(font=("Ariel", 40, "normal"), borderwidth=0, bg=FRONT_CARD_COLOR)
pinyin.grid(row=1, column=0, columnspan=4)

# definition
definition = tk.Label(font=DEFINITION_LARGE_FONT, borderwidth=0, bg=FRONT_CARD_COLOR)
definition.grid(row=2, column=0, columnspan=4)

# // buttons //

# no
x_button_img = tk.PhotoImage(file="images/wrong.png")
x_button = tk.Button(image=x_button_img, borderwidth=0, border=0, highlightthickness=0,
                     bg=BACKGROUND_COLOR, command=next_card)
x_button.grid(row=3, column=0)

# yes
check_button_img = tk.PhotoImage(file="images/right.png")
check_button = tk.Button(image=check_button_img, borderwidth=0, border=0,
                         highlightthickness=0, bg=BACKGROUND_COLOR, command=next_card)
check_button.grid(row=3, column=3)

# flip
flip_button_img = tk.PhotoImage(file="images/rotate.png")
flip_button = tk.Button(image=flip_button_img, borderwidth=0, border=0,
                        highlightthickness=0, bg=BACKGROUND_COLOR, command=flip, highlightcolor=BACKGROUND_COLOR)
flip_button.grid(row=3, column=1, columnspan=2)
next_card()

root.mainloop()
