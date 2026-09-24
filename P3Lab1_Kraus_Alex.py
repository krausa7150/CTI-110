# Alex Kraus
# CTI 110
# 9/24/26
# P3Lab1 - Making change

# Example 1 -- with potions
hp = int(input("How many hit points of damage (1-100): "))
print ("You took ", hp, "Damage!")
large = hp // 25         # each potion heals 25
hp = hp % 25            # some damage left over

print("Drank" , large, "large potions.")
print("Damage remaining: ", hp)

# Small potions heal 5
small = hp // 5
hp = hp % 5

print("Drank", small, "small potions.")
print("Damage remaining: ", hp)

# Example 2 - with coins!!!
amount = float(input("Enter dollars and cent (ex: 2.91): "))
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