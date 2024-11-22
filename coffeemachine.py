

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def total_amount(quaters,dimes,nickels,pennies):
    total = (quaters * 0.25) + (dimes * 0.10) + (nickels * 0.05) + (pennies * 0.01)
    return total


#GLOBALS
MONEY = 0

# report . this gives info about ingredients and money input

def report():

    for key,value in resources.items():
        print(f"{key}:{value}")

    print(f"balance = {MONEY}")

#global variables
MONEY_total = 0



# main loop and user input
machine_exit = True


while machine_exit == True:

    user_input  = input("commands to use \n off/on \n exist \n report \n What would you like? espresso/latte/cappuccino :").lower()


    if user_input == "exit":
        print("Vist again 😇 ")
        machine_exit = False
    #drinks and the money
    elif user_input == "espresso":
        if resources["water"] >= MENU["espresso"]["ingredients"]["water"] and resources["coffee"] >= MENU["espresso"]["ingredients"]["coffee"]:

            quarters = float(input("how many quarters ? $ "))
            dimes = float(input("how many dimes ? $"))
            nickels = float(input("how many nickels ? $"))
            pennies = float(input("how many pennies ? $"))

            money_given = float(total_amount(quarters, dimes, nickels, pennies))

            if money_given == 1.5:
                print("enjoy your espresso . 😀")
                MONEY += money_given

            elif money_given > 1.5:
                money_given = money_given - 1.5

                MONEY += money_given
                print(f"you exchange is {money_given:.2f}$")
                print("enjoy your espresso . 😀")

            else:
                print("not enough money ")

            resources["water"] -= 50
            resources["coffee"] -= 18
        else:
            print("there are not enough resources")

    elif user_input == "latte":
        if resources["water"] >= MENU["latte"]["ingredients"]["water"] and resources["milk"] >= MENU["latte"]["ingredients"]["milk"]  and resources["coffee"] >= MENU["latte"]["ingredients"]["coffee"]:
            quarters = float(input("how many quarters ? $"))
            dimes = float(input("how many dimes ? $"))
            nickels = float(input("how many nickels ? $"))
            pennies = float(input("how many pennies ? $"))

            money_given = total_amount(quarters,dimes,nickels,pennies)

            if money_given == 2.5:
                print("enjoy your latte . 😀")
                MONEY += money_given

            elif money_given > 2.5:
                money_given = money_given - 2.5
                MONEY += money_given
                print(f"you exchange is {money_given:.2f}$")
                print("enjoy your latte . 😀")

            else:
                print("not enough money ")


            #resources reduction
            resources["water"] -= 200
            resources["milk"] -= 150
            resources["coffee"] -= 24

        else:
            print("there are not enough resources .")

    elif user_input == "cappuccino":
        if resources["water"] >= MENU["cappuccino"]["ingredients"]["water"] and resources["milk"] >= MENU["cappuccino"]["ingredients"]["milk"] and resources["coffee"] >= MENU["cappuccino"]["ingredients"]["coffee"]:

            quarters = float(input("how many quarters ? $"))
            dimes = float(input("how many dimes ? $"))
            nickels = float(input("how many nickels ? $"))
            pennies = float(input("how many pennies ? $"))

            money_given = float(total_amount(quarters, dimes, nickels, pennies))

            if money_given == 3.0:
                print("enjoy your cappuccino . 😀")
                MONEY += money_given

            elif money_given > 3.0:

                money_given = money_given - 3.0
                money_given = round(money_given, 2)
                MONEY += 3.0
                print(f"you exchange is {money_given:.2f}$.")
                print("enjoy your cappuccino . 😀")

            else:
                print("not enough money ")

            #resources deduction
            resources["water"] -= 250
            resources["milk"] -= 100
            resources["coffee"] -= 24



    elif user_input == "off":
        print("Turning off the coffee machine .")
        machine_exit = False


    elif user_input == "report":
        report()


    else:
        print("Please enter a valid option .")
