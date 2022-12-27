# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
true_str = "true"
love_str = "love"
true_list = []
love_list = []

for char in true_str:
    for letter in name1.lower():
        if char == letter:
            true_list.append(letter)
    for letter2 in name2.lower():
        if char == letter2:
            true_list.append(letter2)

for char2 in love_str:
    for letter in name1.lower():
        if char2 == letter:
            love_list.append(letter)
    for letter2 in name2.lower():
        if char2 == letter2:
            love_list.append(letter2)

love_score = (len(true_list) * 10) + len(love_list)

if 10 < love_score < 40:
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif 40 <= love_score <= 50:
    print(f"Your score is {love_score}, you are alright together.")
elif love_score > 90:
    print(f"Your score is {love_score}, you go together like coke and mentos.")
else:
    print(f"Your score is {love_score}.")


# print(true_list, love_list)
# print(len(true_list), len(love_list))

