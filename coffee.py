from main import MENU, resources

def print_report():
    """Prints the current resource values."""
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${profit:.2f}")

def check_resources(drink):
    """Check if there are enough resources to make the selected drink."""
    for ingredient, amount in MENU[drink]["ingredients"].items():
        if resources[ingredient] < amount:
            print(f"Sorry, there is not enough {ingredient}.")
            return False
    return True

def process_coins():
    """Prompt the user to insert coins and calculate the total amount."""
    print("Please insert coins.")
    quarters = int(input("Quarters: ")) * 0.25
    dimes = int(input("Dimes: ")) * 0.10
    nickels = int(input("Nickels: ")) * 0.05
    pennies = int(input("Pennies: ")) * 0.01
    return quarters + dimes + nickels + pennies

def make_coffee(drink):
    """Deduct resources and update profit after successful purchase."""
    global profit
    for ingredient, amount in MENU[drink]["ingredients"].items():
        resources[ingredient] -= amount
    profit += MENU[drink]["cost"]
    print(f"Here is your {drink}☕☕. Enjoy!❤😎")

# Main program
profit = 0.0

while True:
    user_input = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if user_input == "off":
        break  # Turn off the coffee machine

    elif user_input == "report":
        print_report()

    elif user_input in MENU:
        if check_resources(user_input):
            coins_inserted = process_coins()
            if coins_inserted < MENU[user_input]["cost"]:
                print("Sorry, that's not enough money. Money refunded.")
            else:
                change = coins_inserted - MENU[user_input]["cost"]
                if change > 0:
                    print(f"Here is ${change:.2f} in change.")
                make_coffee(user_input)

    else:
        print("Invalid input. Please enter a valid option.")
