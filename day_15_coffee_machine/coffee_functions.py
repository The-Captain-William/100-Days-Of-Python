from dictionaries import *

profit = 0

def welcome_order_prompt(drink_input):
    """
    the welcome order prompt is a function that takes the drink input. It's primary function is to map the drink input
    to the keys in the MENU dictionary. It will return the dictionary nested inside that dictionary, which is a
    collection of two keys, one called ingredients, the other called cost.
    "ingredients" is another dictionary with water, coffee, and milk keys. cost is a simple numerical value
    TLDR; key_values == dictionary[key_input]
    """
    global machine_on
    if drink_input == 'espresso' or drink_input == 'latte' or drink_input == 'cappuccino':
        drink = MENU[drink_input]  # pulls up {ingredients:{val}, price:val}
        return drink
    elif drink_input == 'off':
        print("Shutting down.")
        machine_on = False
        exit()
    else:
        print("Entry not recognized, please try again")
        pass

#  the welcome order prompt is a function that takes the drink input. It's primary function is to map the drink input
#  to the keys in the MENU dictionary. It will return the dictionary nested inside that dictionary, which is a
#  collection of two keys, one called ingredients, the other called cost.
#  "ingredients" is another dictionary with water, coffee, and milk keys. cost is a simple numerical value
#  TLDR; key_values == dictionary[key_input]


def check_values(order_ingredients):
    """
    check values checks the key values of one dictionary and compares them against the "resources" dictionary, and
    returns true when order can be made. by default, it goes one level. use order_ingredients[dict]
    if your ingredients are in another dictionary (for example if the values are in a nested dictionary).
    """
    for item in order_ingredients:  # placeholder key and dictionary # for water/milk/coffee in {}
        if order_ingredients[item] > resources[item]:  # will check key value vs key value
            # ** important -> dict[key] == key_val
            print(f"Sorry, there is not enough {item}. Please select another drink.")
            return False
        else:
            return True


def process_coins():
    """Returns total calculated from coins inserted"""
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25  # note how total is defined with the first input
    total += int(input("how many dimes?: ")) * 0.10
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total


def is_transaction_successful(money_received, drink_cost):
    """
    Will check to see if the money received is greater than or equal to the drink cost.
    Drink cost is denoted by drink["cost"]
    Subtraction encapsulated by round function.
    """
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)  # 2 decimal places .00
        global profit  # ⭐ tell function I want to source global variable
        profit += drink_cost
        print(f"Thank you for your purchase. Your change is ${change}")
        return True
    else:
        print("That's not enough money. Money refunded.")
        return False


def make_coffee(drink_name_input, order_ingredients):
    """
    Will identify the different values given a key that can be found in either dictionary,
    and subtract one value from another. The result is stored in the "resources" dictionary.
    """
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]  # ⭐ *** important *** for every item in order ingredients,
        # look into resources of that same item and subtract values, take [keyval] from dict 1 and subtract [keyval]
        # from dict 2
    print(f"Here is your {drink_name_input} ☕ ")