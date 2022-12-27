from coffee_functions import *
from coffee_functions import check_values

# TODO 1 Make 3 hot flavors given the specified quantities of ingredients
# TODO 1.1 make a loop to prevent hanging when given incorrect entry
# TODO 2 make coin functionality with pennies, nickels, dimes, and quarters
# TODO 3 reporting function to show the resources available in the machine
# TODO 4 check resources as order is created (limited resource functionality)
# TODO 5 money check and change functionality


# introduction, choose a drink functionality when machine is on
print("Captain William Presents: Coffee Machine")

machine_on = True
while machine_on is True:
    welcome_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()  # basic input
    if welcome_choice == 'report':  # will catch report and print resources
        print(resources)
    else:
        drink = welcome_order_prompt(welcome_choice)  # maps user entry to MENU key; producing key values
        if check_values(drink["ingredients"]) is True:  # will pull up {ingredient:val} out of ingredients:{val}
            drink_name = welcome_choice.title()  # stores drink name
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]) is True:
                make_coffee(drink_name, drink["ingredients"])
