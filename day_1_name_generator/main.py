 # My response

# city_question = str("What is the city you grew up in?")
# pet_question = str("What is the name of your favorite pet?")
# city_answer = str(input())
# pet_answer = str(input())
# print(city_question,city_answer)
# print(pet_question,pet_answer)
# band_name = f"Your new band name is {city_answer} {city_question}"

 # Professors response
# print("Welcome to the Band Name Generator.")
# street = input("What's name of the city you grew up in?\n")  # values already stored in input
# pet = input("What's your pet's name?\n")
# print("Your band name could be " + street + " " + pet)  # my method of formatted strings is cleaner

# Best response
print("Welcome to the Band Name Generator.")
street = input("What's the name of the city you grew up in?\n") #note that \n is inside the string
pet = input("What's the name of your favorite pet?\n")
print(f"Your band name could be {street} {pet}")