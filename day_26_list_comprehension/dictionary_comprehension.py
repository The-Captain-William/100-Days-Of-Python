import random
import pandas
#  new_dict = {new_key: new_value for item in list}

# adding items from previous dictionary called "dict" in new dictionary
#  new_dict = {new_key :new_value for (key,value) in dict.items()}

# adding items from previous dictionary called "dict" in new dictionary if condition met
#  new_dict = {new_key :new_value for (key,value) in dict.items() if 'condition'}

names = ["beth", "alex", "caroline", "dave"]

#  assigning name as key, and randomly generated value
rand_value = {name: random.randint(0, 6) for name in names}
print(rand_value)

#  creating a new dictionary from another dictionary, filtering # 👀 - don't forget .items() for dict
passed_students = {name: score for (name, score) in rand_value.items() if score > 3}
print(passed_students)

sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
result = {word: len(word) for word in sentence.split()}  # word w.r.t 'word' vs 'w' 'o' 'r' 'd'
print(result)

weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}


#  👀 note that the new value is having operations performed on it in the comprehension,
#  vs having a separate variable for that value.
weather_f = {weather: ((value * 9/5) + 32) for (weather, value) in weather_c.items()}

print(weather_f)

