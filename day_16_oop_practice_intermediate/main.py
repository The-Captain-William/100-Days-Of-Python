from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

is_on = True

# coffee_maker.report()   # reports ingredients
# money_machine.report()  # reports funds

while is_on is True:
    options = menu.get_items()  # textual but not printed info
    choice = input(f"What would you like? ({options})")  # options just displays textual information
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_maker.report()  # will call up if true
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink) is True:  # returns true or false
            if money_machine.make_payment(drink.cost) is True: # returns true if input amount is equal to drink cost amount
                coffee_maker.make_coffee(drink)
