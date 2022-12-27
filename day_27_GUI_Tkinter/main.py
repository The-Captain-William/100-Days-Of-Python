import tkinter
import tkinter as tk

main_window = tk.Tk()
main_window.title("Captain William Presents: Miles to Kilometers Converter")
# main_window.minsize(width=250, height=150)
main_window.config(pady=30, padx=30)

FONT = ("Arial", 24, "bold")


#  layout
# 1 2 3
# 1 2 3
# 1 2 3
m = tk.DoubleVar()
m.set(0)
km = tk.DoubleVar()
km.set(0)


def convert():
    k = m.get() * 1.609344
    km.set(round(k, 2))
    equal_to_label.config(text=f"Is equal to {km.get()} Km", font=FONT)
    print(k, km.get())

#  m to km converter

# mile entry box
mile_to_km_entry = tk.Entry()
mile_to_km_entry.grid(column=2, row=2)
mile_to_km_entry.config(font=FONT, width=10, textvariable=m)


# mile label
miles_label = tk.Label(text="Miles", font=FONT)
miles_label.grid(column=3, row=2)


# "equal to" dynamic label
equal_to_label = tk.Label(text=f"Is equal to {km.get()} Km", font=FONT)
equal_to_label.grid(column=2, row=3)


# calc box
calc_box = tk.Button(text="Calculate", font=FONT, command=convert)
calc_box.grid(column=2, row=4)

main_window.mainloop()

# time thus far 223