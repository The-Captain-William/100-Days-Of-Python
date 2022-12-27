import pandas

# data frame from csv file
squirrel_data_2018 = pandas.read_csv("squirrel_count.csv")

# Unique ID (Primary Key) for squirrel
unique_id = squirrel_data_2018["Unique Squirrel ID"]

# Testing counts of all black squirrels
# Unique ID where primary fur color is also black, then count
# 👀 remember to initialize w/ () # Primary Key Count
print(unique_id[squirrel_data_2018["Primary Fur Color"] == "Black"].count())

colors = ["Black", "Cinnamon", "Gray"]  # different colors

# color key: (primary fur color == color from colors list).count() for every color in colors list

# dictionary with lists as key values
# list comprehension
# 1  "color" for every color in colors
# 2 get count of all squirrels with this "color", for every "color" in colors
color_dict_r = {"Color": [color for color in colors],# 1
                "Count": [unique_id[squirrel_data_2018["Primary Fur Color"] == color].count() for color in colors]}  # 2

# test print
print(color_dict_r)

# convert to dataframe
data = pandas.DataFrame(color_dict_r)

# data to csv
data.to_csv("2018 Primary Color Count.csv")
