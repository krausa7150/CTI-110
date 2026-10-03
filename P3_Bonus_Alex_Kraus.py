# Alex Kraus
# 10/01/2026
# M3BONUS - Let's Make A Deal
# A short text adventure with a buzzer round

# ------------------- ROOMS -------------------

def end_room():
    print("The game ends.")

def box_room():
    print("You open the mystery box.")
    print("Inside is a rubber chicken wearing sunglasses.")
    print("You win: one stylish rubber chicken!")
    end_room()

def door1():
    print("Door 1 swings open.")
    print("A goat looks at you. It is chewing your ticket!")
    print("You win: one goat.")

    print("What do you do?")
    print("1: Keep the goat")
    print("2: Open the mystery box")
    print("3: Run for the exit")
    choice = input("Choose: ")

    if choice == "1":
        print("You keep the goat. It seems happy.")
        end_room()
    elif choice == "2":
        box_room()
    elif choice == "3":
        print("You sprint out of the room.")
        end_room()
    else:
        print("That is not an option.")
        end_room()

def door2():
    print("Door 2 swings open.")
    print("Lights flash. A small red car rolls out!")
    print("You win: a car.")
    end_room()

def door3():
    print("Door 3 swings open.")
    print("A briefcase sits on a stool.")
    print("You win a briefcase.")

    print("The host smiles. Time for the Buzzer Round.")
    print("The first 40 seconds pay the base rate.")
    print("Every second over 40 pays 1.5 times the base rate.")

    seconds = float(input("How many seconds did you hold the buzzer? "))
    rate = float(input("Dollars per second: "))

    if seconds > 40:
        bonus_seconds = seconds - 40
        base_pay = 40 * rate
        bonus_pay = bonus_seconds * (rate * 1.5)
    else:
        bonus_seconds = 0
        base_pay = seconds * rate
        bonus_pay = 0

    total = base_pay + bonus_pay

    print("------------ PRIZE RECEIPT ------------")
    print(f"{'Prize:':<20}Briefcase")
    print(f"{'Seconds held:':<20}{seconds:.2f}")
    print(f"{'Bonus seconds:':<20}{bonus_seconds:.2f}")
    print(f"{'Base pay:':<20}${base_pay:.2f}")
    print(f"{'Bonus pay:':<20}${bonus_pay:.2f}")
    print(f"{'Total winnings:':<20}${total:.2f}")
    print("---------------------------------------")

    end_room()

# ------------------- START ROOM -------------------

def start():
    print("========================================")
    print("     WELCOME TO LET'S MAKE A DEAL")
    print("========================================")

    choice = input("Pick a door (1, 2, or 3): ")

    if choice == "1":
        door1()
    elif choice == "2":
        door2()
    elif choice == "3":
        door3()
    else:
        print("That is not a door.")
        start()

# ------------------- RUN GAME -------------------

start()