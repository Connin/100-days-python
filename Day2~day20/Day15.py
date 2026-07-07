MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
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
    "coffee": 80,
    "money": 0
}
QUARTER = 0.25
DIME = 0.1
NICKLES = 0.05
PENNIES = 0.01

usermoney ={ 
'quarter' : 0,
'dime' : 0,
'nickles' : 0,
'pennies' : 0
    }

userinput = ""

import sys
#TODO ask how many coins

def askcoin():
    usermoney['quarter'] = int(input("quarter? "))
    usermoney['dime'] = int(input("dime? "))
    usermoney['nickles'] = int(input("nickles? "))
    usermoney['pennies'] = int(input("pennies? "))

def summoney(usermoney):
    summ = 0
    summ = usermoney['quarter'] * QUARTER + usermoney['dime'] * DIME + usermoney['nickles'] * NICKLES + usermoney['pennies'] * PENNIES
    return summ
    
#TODO When the user enters “report” to the prompt, a report should be generated that shows input: order,  output:

def report():
    print(f"Water:{resources['water']}ml")
    print(f"Milk:{resources['milk']}ml")
    print(f"Coffee:{resources['coffee']}g")
    print(f"Money:{resources['money']}$")

#TODO check resource sufficient
# input: resource and coffeename output: boolean
def checkresource(resources, userinput):
    for item in MENU[userinput]["ingredients"]:
        if MENU[userinput]["ingredients"][item] > resources[item]:
            return False
        elif MENU[userinput]["ingredients"][item] < resources[item]:
            continue
    return True

#TODO calculate coin input:number of coins output:sum
def summoney(usermoney):
    summ = 0
    summ = usermoney['quarter'] * QUARTER + usermoney['dime'] * DIME + usermoney['nickles'] * NICKLES + usermoney['pennies'] * PENNIES
    return summ
#TODO Check transaction successful? input:sum, coffee output:boolean and change

def checktrans(summ, MENU):
    if summ >= MENU[userinput]["cost"]:
        print("success")
        return True
    else:
        print("fail")
        return False
#TODO Perform transaction input:sum, coffee output: change, and resourceaddition

def perftrans(summ, MENU):
    coin_change = summ - MENU[userinput]["cost"]
    resources["water"] -= MENU[userinput]["ingredients"]["water"]
    resources["milk"] -= MENU[userinput]["ingredients"]["milk"]
    resources["coffee"] -= MENU[userinput]["ingredients"]["coffee"]    
    resources["money"] += MENU[userinput]["cost"]
    print(f"Here is yout change {round(coin_change, 2)}")
    return coin_change


#TODO make coffee input: resource, coffee output: resource including money

#TODO ask user input 

#
while True:
    userinput = input("what would you like? (espresso/latte/cappuccino): ").lower()
    print(userinput)
    if userinput == "off":
        sys.exit()
    elif userinput == "report":
        report()
        continue
    
    if checkresource(resources, userinput) == False:
        print("Not enough item")
        continue
    else:
        askcoin()
        summ = summoney(usermoney)
        transaction_ok = checktrans(summ, MENU)
        if transaction_ok == True:
            perftrans(summ, MENU)
        elif transaction_ok == False:
            print("Not enough money")
