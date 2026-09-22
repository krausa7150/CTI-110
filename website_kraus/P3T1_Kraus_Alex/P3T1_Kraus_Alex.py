# Alex Kraus
# P3T1 - Warmup with IF statements
# 09/22/26
# CTI 110

# main () -- this is the programs starting point.
# You dont need to use it, it is very good idea.
def main():
    # Part 1 - Level Check
    print("Hello and welcome to the dungeon!")
level = int(input("What level are you? "))
if level >= 21:
    print("You can enter the boss fight. ")
else:
    print("Try leveling up first. HAHAHAHAHA....")

# Part 2 - List your ~potions~!
print("Time to enter the boss fight!")
potions = int(input("How many health potions did you bring? "))
if potions == 0:
    print("It is dangerous to go alone with potions. ")
elif potions == 1:
    print(f"You have {potions} health potion ")
elif potions == 1:
    print(f"You have {potions} health portions. "))
else:
    print(f"How did you get {potions}!!! That is less than zero! ")

# Part 3 - Boss Battle
print ("You are facing the DELUXE KAREN")
print ("This will be a hard fight..." )
if level >= 25:
    # You are tough enough to hit him!
    if potions > 3:
        print("It takes three potions to get him to low health!! ")
        print("****VICTORY****")
    else: 
        print("You ran out of healing before he is weakend... ")
        print("****GAME OVER**** ")
else: 
    print("His armor is too strong!!! ")
    print("****GAME OVER**** ")
# At the bottom -- start the program
main()
