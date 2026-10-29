# Alex Kraus
# CTI 110
# 10/29/26
# P5Lab-purchase and change

# Put other functions
import random
def disperse_change(amount):
    pass
# Print out the change needed.
    print(f"Change is: ${amount:.2f}")
    print()
    # Put p3lab code here:
    # Example 2 - with coins!!!
    cents = round(amount * 100) # Convert to cents, round correctly
    print("That's", cents, "cents.")

    # For each currency type:
    # - cents // [currency] gives you many currency
    # - cents % [currency] gives you left over cents
    dollars = cents // 100
    cents = cents % 100
    # If statement - do not show of zero, use singular or plural otherwise 
    if dollars == 0:
        pass
    if dollars == 1:
        print("1 dollar")
    if dollars > 1:
        print(dollars, "dollars")

    # quarters
    quarters = cents // 25
    cents = cents % 25

    if quarters == 0:
        pass
    if quarters == 1:
        print("1 quarter")
    if quarters > 1:
        print(quarters, "quarters")
        
    # dimes
    dimes = cents // 10
    cents = cents % 10

    if dimes == 0:
        pass
    if dimes == 1:
        print("1 dime")
    if dimes > 1:
        print(dimes, "dimes")
        
    # nickels
    nickles = cents // 5
    cents = cents % 5

    if nickles == 0:
        pass
    if nickles == 1:
        print("1 nickel")
    if nickles > 1:
        print(nickles, "nickels")
        print("1 nickel")
    if nickles > 1:
        print(nickles, "nickels")

    # pennies
    pennies = cents // 1
    cents = cents % 1

    if pennies == 0:
        pass
    if pennies == 1:
        print("1 penny")
    if pennies > 1:
        print(pennies, "pennies")

# Main
def main():
    cost = 0.0
    amount_paid = 0.0
    change_owed = 0.0
    print("Welcome to the self-checkout sim: ")
    cost = round(random.uniform(0.01, 100.00), 2)
    print(f"You owe: ${cost:.2f}")
    amount_paid = float(input("How much money do you put in the self checkout? $"))

    change_owed = amount_paid - cost

    print("Here is your change: ")
    disperse_change(change_owed)


# Last line - start program
main()
