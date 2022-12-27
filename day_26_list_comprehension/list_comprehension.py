numbers = [1, 2, 3]
new_list = [n + 1 for n in numbers]  # new_list = [new_item for item in (other) list]
print(new_list)

name = "Angela"
str_list = [letter for letter in name]  # split
print(str_list)

range_list = [n * 2 for n in range(1, 5)]  # encapsulate value source in list
print(range_list)


names = ["beth", "alex", "caroline", "dave"]

four_letter_names = [name for name in names if len(name) <= 4]  # name for name == transcribe value
print(four_letter_names)

all_capitals = [name.swapcase() for name in names if len(name) > 4]  # item.method for name
print(all_capitals)


numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# 🚨 Do Not Change the code above 👆

squared_numbers = [number * number for number in numbers]
print(squared_numbers)

even_numbers = [number for number in numbers if number % 2 == 0]
print(even_numbers)
