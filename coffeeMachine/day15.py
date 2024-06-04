# Day 15 #

# Setup Local Development Environment & Coffee Machine Project
# IDE: Integrated Development Environment


# Coffee Machine:
# 1. Makes 3 hot flavours
# Type: Espresso - Latte - Cappuccino
# Price: 1.50$ - 2.50$ - 3.00$
# Water: 50ml - 200ml  - 250ml
# Coffee: 18g - 24g - 24g
# Milk: 0ml - 150ml - 100ml

# 1- Starting resources:
# Water: 300ml
# Coffee: 200ml
# Milk: 100g

# 2- Coin Operated
# Penny - 1 cent - 0.01$
# Nickel - 5 cents - 0.05$
# Dime - 10 cents - 0.10$
# Quarter - 25 cents - 0.25$

# 3- Program Requirements
# - Print report.
# - check resources sufficient ?
# - Process coins
# - Check transaction successful ?
# - Make Coffee

from coffeeMachineData import MENU, resources
# from os import system
machineIsOn = True
total_money = 0
remaining_resources = resources.copy()

def take_user_input(user_input):
    """Checks users input and return whether it's true or false"""
    # print(remaining_resources)
    if user_input == "report":
        print(f"Water: {remaining_resources['water']} ml")
        print(f"Milk: {remaining_resources['milk']} ml")
        print(f"Coffee: {remaining_resources['coffee']} mg")
        print(f"Money : {total_money} $")
        return False
    elif user_input in MENU:
        # print(f"it's in menu: {MENU[user_input]}")
        return True
    else:
        print("Wrong input")
        return False

def check_resources(user_input):
    """Checks whether the machine has enough resources or not and return True or False"""
    product = MENU[user_input]
    resources_available = True
    print(f"remaining_resources['water'] = {remaining_resources['water']}")
    if remaining_resources['water'] < product['ingredients']['water']:
        print("Sorry, there is no enough water.")
        resources_available = False
    if user_input != "espresso" and remaining_resources['milk'] < product['ingredients']['milk']:
        print("Sorry, there is no enough milk.")
        resources_available = False
    if remaining_resources['coffee'] < product['ingredients']['coffee']:
        print("Sorry, there is no enough coffee.")
        resources_available = False
    return resources_available
    
def change_resources(user_input, remaining_res, not_enough_money):
    """Changes the amount of resources depending on user's order and returns the remaining resources"""
    if not not_enough_money:
        product = MENU[user_input]
        remaining_res['water'] -= product['ingredients']['water']
        if user_input != "espresso":
            remaining_res['milk'] -= product['ingredients']['milk']
        remaining_res['coffee'] -= product['ingredients']['coffee']
    return remaining_res
    

def process_money(user_input):
    """Processing the coins, print the remaining change if there's any and returns the total coins"""
    product_price = MENU[user_input]['cost']
    print(f"That will cost {product_price}$")
    print("Please insert coins.")
    quarter = 0.25 * int(input("How many quarters: "))
    dime = 0.10 * int(input("How many dimes: "))
    nickel = 0.05 * int(input("How many nickels: "))
    penny = 0.01 * int(input("How many pennies: "))

    total_coins = round(quarter + dime + nickel + penny, 2)
    print(f"You paid {total_coins}$")
    remaining_res = {}
    if total_coins == product_price:
        print(f"Here's your {user_input}, Enjoy!")
        remaining_res = change_resources(user_input, remaining_resources, False)
        return total_coins, remaining_res
    elif total_coins > product_price:
        change = round(total_coins - product_price, 2)
        print(f"Here's {change}$ in change.")
        print(f"Here's your {user_input}, Enjoy!")
        remaining_res = change_resources(user_input, remaining_resources, False)
        return (total_coins - change), remaining_res
    else:
        print(f"Sorry, that's not enough money. {total_coins}$ has been refunded")
        remaining_res = change_resources(user_input, remaining_resources, True)
        return 0, remaining_res


def coffee_machine(all_money):
    """The coffee machine program, will keep running unless it's turned off"""
    extra_money = 0
    remaining_res = remaining_resources
    machine_status = True
    user_input = input("What would you Like? (espresso/latte/cappuccino): ").lower()
    if user_input == "off":
        print("Machine is turning off!")
        machine_status = False
    else:
        if take_user_input(user_input) and check_resources(user_input):
            extra_money, remaining_res = process_money(user_input)
    all_money += extra_money
    return round(all_money,2), remaining_res, machine_status

while machineIsOn:
    total_money, remaining_resources, machineIsOn = coffee_machine(total_money)
