import tkinter as tk
from tkinter import messagebox
from password_gen import password_generator
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def password_input():
    pw_gen = password_generator()
    password_box.delete(0, tk.END)
    password_box.insert(0, pw_gen)
    pyperclip.copy(pw_gen)
    password_refresh()


def password_refresh():
    generate_password.config(text="        Copied        ")
    window.after(3000, password_check)


def password_check():
    generate_password.config(text="Generate Button")


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_button():
    new_data = {
        website_box.get().title(): {
            "email": user_box.get().title(),
            "password": password_box.get()
        }
    }

    if len(user_box.get()) == 0 or len(website_box.get()) == 0 or len(password_box.get()) == 0:  # if any have len 0
        messagebox.showinfo(title="Oops", message="Fields cannot be empty!")
    else:  # next step, ask if okay
        is_okay = messagebox.askokcancel(title=website_box.get(), message=f"Website: {website_box.get()}\n"
                                                                          f"Email: {user_box.get()}\n"
                                                                          f"Password: {password_box.get()}\n"
                                                                          f"\n Is this correct?")
        if is_okay is True:
            # 👀 keep in mind DATA_FILE is the file object,
            # where DATA is the contents of the file as an object
            try:
                with open("data.json", mode="r") as data_file:  # r mode
                    data = json.load(data_file)  # loading pre-existing .json file # reading old data
                    data.update(
                        new_data)  # update w/ new data found in dynamic dictionary # updating old data w new data
            except FileNotFoundError:
                # 👀 if file not found, make a data.json file and import it as data_file file object,
                # and use new_data as the contents of said file.
                with open("data.json", mode="w") as data_file:
                    json.dump(new_data, data_file, indent=4)
            else:
                # if no error, it is assumed file is located.
                # Read old file contents, update with new contents, and write new contents to old file
                # the bottom portion is the writing new contents to old file part
                # the reading contents and updating contents parts are the steps above under the try block
                with open("data.json", mode="w") as data_file:
                    json.dump(data, data_file, indent=4)  # dump # saving updated data


                for item in container[1:]:
                    item.delete(0, tk.END)
            refresh()  # refresh func


def refresh():
    add.config(text="Information Saved")
    window.after(3000, check)


def check():
    add.config(text="Add")

# ---------------------------- SEARCH ------------------------------- #


def search_button():
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
            if website_box.get().title() in data:
                entry = website_box.get().title()
                user_box.delete(0, tk.END)
                password_box.delete(0, tk.END)
                user_box.insert(0, data[entry]["email"])
                password_box.insert(0, data[entry]["password"])
            else:
                messagebox.showwarning(message="No website with that name on file.", title="Oops!")
    except FileNotFoundError:
        messagebox.showwarning(message="No websites saved yet!", title="Oops!")


# ---------------------------- UI SETUP ------------------------------- #


GREY = "#444444"
BLACK = "#171717"
RED = "#DA0037"
CREAM = "#EDEDED"

# window
window = tk.Tk()
window.title("Captain William Presents: Password Generator")
window.config(padx=50, pady=50, bg=BLACK)
window.minsize(width=200, height=200)
window.iconbitmap("favicon.ico")

# canvas
main_img = tk.PhotoImage(file="society.png")
canvas = tk.Canvas(width=336, height=436, borderwidth=0, bg=BLACK, border=0,
                   highlightthickness=0)  # canvas width and length
canvas.grid(column=1, row=0, pady=20, columnspan=4)
canvas.create_image(168, 218, image=main_img)  # x, y w.r.t placement not image size
# text

website = tk.Label(text="Website:")
website.grid(column=1, row=1)
website.config(bg=BLACK, fg=CREAM)

user = tk.Label(text="Email/Username:")  # can we make this flush?
user.grid(column=1, row=2)
user.config(bg=BLACK, fg=CREAM)

password = tk.Label(text="Password:")
password.grid(column=1, row=3)
password.config(bg=BLACK, fg=CREAM)

# text boxes

website_box = tk.Entry(width=34)
website_box.grid(column=2, row=1, columnspan=2, ipadx=1)
website_box.focus()
website_box.config(bg=GREY, fg=CREAM)

user_box = tk.Entry(width=50)
user_box.grid(column=2, row=2, columnspan=3)
user_box.insert(0, "theavenger16@gmail.com")
user_box.config(bg=GREY, fg=CREAM)

password_box = tk.Entry(width=34)
password_box.grid(column=2, row=3, columnspan=2, ipadx=1)
password_box.config(bg=GREY, fg=CREAM)

container = [user_box, website_box, password_box]

# button(s)
generate_password = tk.Button(text="Generate Button", command=password_input)
generate_password.grid(column=4, row=3)
generate_password.config(bg=RED, fg=CREAM)

add = tk.Button(text="Add", width=40, command=save_button)
add.grid(column=2, row=5, columnspan=3, ipadx=9)
add.config(bg=RED, fg=CREAM)

search = tk.Button(text="Search", command=search_button)
search.grid(column=4, row=1, ipadx=25)
search.config(bg=RED, fg=CREAM)


window.mainloop()
