import tkinter as tk

window = tk.Tk()  # similar to screen in Turtle # 👀 don't forget to initialize with ()
window.title("GUI Program")
window.minsize(width=500, height=300)  # will cause to scale with interface


def button_clicked():
    collect_text = input_gui.get()
    label.config(text=collect_text)  # button changes name to assigned text
    print("*clicked*")


label = tk.Label(text="Label", font=("Arial", 24, "bold"))  # font is a tuple
label.pack()  # will center if no argument ; needed to "pack" the item onto the screen

button = tk.Button(text="Click", command=button_clicked)
button.pack()

input_gui = tk.Entry(width=10)  # entry assigns value to predefined variable
input_gui.pack()

# label_ye = tk.Label(text="Ye Ye", font=("Arial", 24, "italic"))
# label_ye.grid(column=0, row=0)

window.mainloop()  # keeps window on screen # end of code



