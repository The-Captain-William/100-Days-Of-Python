# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

size_price = 0
pepperoni_price = 0
extra_cheese_price = 0
size_options = [15, 20, 25]

if size == "S":
    size_price += size_options[0]
elif size == "M":
    size_price += size_options[1]
elif size == "L":
    size_price += size_options[2]

if add_pepperoni == "Y" and size == "S":
    pepperoni_price += 2
elif add_pepperoni == "Y" and (size == "M" or size == "L"):
    pepperoni_price += 3
else:
    pass

if extra_cheese == "Y":
    extra_cheese_price += 1
else:
    pass

print(f"Your final bill is:${size_price + pepperoni_price + extra_cheese_price}.")


