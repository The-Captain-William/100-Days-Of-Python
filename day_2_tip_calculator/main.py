# my method, time start 2:08 PM - End 3:36 - Polish 4:10   # update this with a custom exception class
# valid = False
# while not valid:  # "not valid" == "valid == False"
#     print("Welcome to the tip calculator")
#     try:
#         total = float(input("What was the total bill? "))
#         people = int(input("How many people to split the bill? "))
#         percent = (float(input("What percentage tip would you like to give? 10, 12, or 15? "))) / 100
#         error_message = "Incorrect tip amount or number of people, please try again"
#         x = [0.1, 0.12, 0.15]
#         for number in x:  # need to come out of this for loop, if I place an error message in else: it will repeat
#             if number == percent and people >= 1:
#                 print(f"The total tip for {people} is: {(percent * total) / people}")
#                 print("Thank you and have a great day")
#                 valid = True
#                 break
#             else:
#                 pass  # get out of the for loop, so we don't have x number of error messages
#         if not valid:
#             print(error_message)
#     except ValueError:
#         print("Invalid Value")

# modified method #
# my method, time start 2:08 PM - End 3:36 - Polish 4:10   # update this with a custom exception class

valid = False
while not valid:  # "not valid" == "valid == False"
    print("Welcome to the tip calculator")
    try:
        total = float(input("What was the total bill? "))
        people = int(input("How many people to split the bill? "))
        percent = (float(input("What percentage tip would you like to give? 10, 12, or 15? "))) / 100
        error_message = "Incorrect tip amount or number of people, please try again"
        x = [0.1, 0.12, 0.15]
        for number in x:  # need to come out of this for loop, if I place an error message in else: it will repeat
            if number == percent and people >= 1:
                bill_per_person = ((percent * total) / people)
                final_amount = round(bill_per_person, ndigits=2)
                print(f"The total tip for {people} is: ${final_amount}")
                print("Thank you and have a great day")
                valid = True
                break
            else:
                pass  # get out of the for loop, so we don't have x number of error messages
        if not valid:
            print(error_message)
    except ValueError:
        print("Invalid Value")

# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇



