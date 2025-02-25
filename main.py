from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

is_on = True

coffee_maker = CoffeeMaker()
menu = Menu()
money_machine = MoneyMachine()

while is_on:

    print("What would you like?")
    print("Espresso: $1.50")
    print("Latte: $2.50")
    print("Cappuccino: $3.00")
    user_selection = input("Please type 'espresso', 'latte', or 'cappuccino': ").lower()

    if user_selection == "off":
        is_on = False
        break

    elif user_selection == "report":
        coffee_maker.report()

    elif user_selection not in menu.get_items():
        print("Please make a valid selection.")
        continue

    else:
        drink = menu.find_drink(user_selection)
        if coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
