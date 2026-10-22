import random

# --- STARTING VARIABLES ---
miles_traveled = 0
goal_miles = 50
fuel = 100
condition = 100  # Vehicle health (0 = broken down)
trail_points = 0  # Reward points earned during the run
repair_kits = 1   # One-time use Trail Repair Kit & Jerry Can

# --- MOUNTAIN WOODS BANNER (Made with dashes and text symbols) ---
print("--------------------------------------------------------")
print("            /\\        /\\        /\\                      ")
print("           /  \\      /  \\      /  \\     /\\              ")
print("          /    \\    /    \\    /    \\   /  \\             ")
print("   ^  ^  /------\\  /------\\  /------\\ /----\\  ^  ^      ")
print("  /|\\/|\\         \\/        \\/        \\       /|\\/|\\     ")
print("   |  |    [o===o] MOUNTAIN TRAIL 4X4 [o===o] |  |      ")
print("--------------------------------------------------------")
print("Goal: Survive 50 miles of tight mountain woods trail!")
print("Customize your rig, manage tire PSI, and climb the Leaderboard.\n")

# 1. Ask for the player's name
driver_name = input("Enter your Driver Name for the Leaderboard: ")
if driver_name == "":
    driver_name = "Trail Boss"

# 2. Customize Vehicle Color
print("\n--- CHOOSE YOUR RIG COLOR ---")
print("1. Red (Classic Trail Red)")
print("2. Sarge Green")
print("3. Hydro Blue")
print("4. Sting-Gray")
color_choice = input("Pick a color (1-4): ")

if color_choice == "2":
    rig_color = "Sarge Green"
elif color_choice == "3":
    rig_color = "Hydro Blue"
elif color_choice == "4":
    rig_color = "Sting-Gray"
else:
    rig_color = "Red"

# 3. Choose Vehicle / Generation (Size affects trail damage and fuel!)
print("\n--- CHOOSE YOUR OFF-ROAD RIG ---")
print("1. Jeep Wrangler TJ 2-Door (Short wheelbase: Nimble, -2% damage on tight trails)")
print("2. Jeep Wrangler JK Unlimited (Mid-size 4-Door: Balanced, standard wear & fuel)")
print("3. Jeep Wrangler JLU 4-Door (Modern Overlander: Stable, +2% damage on tight trees)")
print("4. Jeep Gladiator JT Pickup (Long wheelbase: High belly-drag risk! +6% damage, +3% gas)")
print("5. Toyota Tacoma TRD Off-Road (Wide full-bed: Heavy trail risk! +5% damage, +2% gas)")
rig_choice = input("Select your vehicle (1-5): ")

if rig_choice == "1":
    rig_name = "Jeep Wrangler TJ 2-Door"
    size_damage_mod = -2
    size_fuel_mod = 0
elif rig_choice == "2":
    rig_name = "Jeep Wrangler JK Unlimited"
    size_damage_mod = 0
    size_fuel_mod = 0
elif rig_choice == "4":
    rig_name = "Jeep Gladiator JT"
    size_damage_mod = 6
    size_fuel_mod = 3
elif rig_choice == "5":
    rig_name = "Toyota Tacoma TRD"
    size_damage_mod = 5
    size_fuel_mod = 2
else:
    rig_name = "Jeep Wrangler JLU"
    size_damage_mod = 2
    size_fuel_mod = 0

full_rig = f"{rig_color} {rig_name}"

# 4. Idea 3: Air Down Tires Option
print(f"\nYour {full_rig} is lined up at the trailhead!")
air_choice = input("Air down tires to 15 PSI for better rock grip? (-4% damage, +2% gas per turn) (y/n): ")

if air_choice == "y" or air_choice == "Y":
    aired_down = True
    print("-> Psssshhhh! Tires aired down to 15 PSI. Sidewalls are flexing nicely!\n")
else:
    aired_down = False
    print("-> Keeping street PSI (35 PSI). Watch out for sharp rocks and wheel slip!\n")

# --- MAIN GAME LOOP ---
# Keep looping while under 50 miles, with gas in the tank, and rig still running
while miles_traveled < goal_miles and fuel > 0 and condition > 0:
    
    # Display the dashboard every turn
    print("--------------------------------------------------------")
    print(f"Rig: {full_rig} | Repair Kits: {repair_kits}")
    print(f"Miles: {miles_traveled}/{goal_miles} | Fuel: {fuel}% | Condition: {condition}% | Points: {trail_points}")
    
    # Pick a random trail obstacle using a number from 1 to 3
    obstacle_number = random.randint(1, 3)
    if obstacle_number == 1:
        obstacle = "Deep Mud Pit"
    elif obstacle_number == 2:
        obstacle = "Jagged Boulder Field"
    else:
        obstacle = "Tight Timber Mountain Climb"
        
    print(f"\nAHEAD IN THE WOODS: {obstacle}!")
    print("1. Shift into 4-Lo and crawl (Safe, burns more gas, +100 pts)")
    print("2. Floor it in 2-High (Fast, heavy damage risk, +200 pts)")
    print("3. Take the tight woods bypass (Low damage, slow gain, +50 pts)")
    print(f"4. Pull over & use Trail Repair Kit + Jerry Can ({repair_kits} left: +25% Cond, +15% Fuel)")
    
    # Ask the player what they want to do
    choice = input("Choose your action (1, 2, 3, or 4): ")
    print("")
    
    # Calculate tire PSI modifiers for this turn
    if aired_down == True:
        psi_damage_mod = -4
        psi_fuel_mod = 2
    else:
        psi_damage_mod = 0
        psi_fuel_mod = 0

    # --- CHECK PLAYER CHOICE ---
    if choice == "1":
        # 4-Lo is safe for crawling, but burns extra gas
        miles_gained = random.randint(7, 11)
        fuel_used = random.randint(13, 18) + size_fuel_mod + psi_fuel_mod
        damage = random.randint(1, 6) + size_damage_mod + psi_damage_mod
        if damage < 0:
            damage = 0
            
        miles_traveled = miles_traveled + miles_gained
        fuel = fuel - fuel_used
        condition = condition - damage
        trail_points = trail_points + 100
        
        print(f"You shifted your {full_rig} into 4-Lo and crawled over the {obstacle}!")
        print(f"+{miles_gained} miles | -{fuel_used}% fuel | -{damage}% wear | +100 Trail Points")
        
    elif choice == "2":
        # Flooring it gets more miles and points, but bigger rigs take a beating
        miles_gained = random.randint(12, 17)
        fuel_used = random.randint(10, 15) + size_fuel_mod + psi_fuel_mod
        damage = random.randint(15, 28) + size_damage_mod + psi_damage_mod
        if damage < 0:
            damage = 0
            
        miles_traveled = miles_traveled + miles_gained
        fuel = fuel - fuel_used
        condition = condition - damage
        trail_points = trail_points + 200
        
        print(f"You floored your {full_rig} through the {obstacle}! Mud and rocks flew everywhere.")
        print(f"+{miles_gained} miles | -{fuel_used}% fuel | -{damage}% damage | +200 Trail Points")
        
    elif choice == "3":
        # Detour saves the rig, though wider/longer trucks still risk tree branch scrapes
        miles_gained = random.randint(4, 7)
        fuel_used = random.randint(7, 11) + size_fuel_mod + psi_fuel_mod
        damage = size_damage_mod + psi_damage_mod
        if damage < 0:
            damage = 0
            
        miles_traveled = miles_traveled + miles_gained
        fuel = fuel - fuel_used
        condition = condition - damage
        trail_points = trail_points + 50
        
        print(f"You squeezed your {full_rig} through the narrow woods bypass around the {obstacle}.")
        print(f"+{miles_gained} miles | -{fuel_used}% fuel | -{damage}% branch scrapes | +50 Trail Points")
        
    elif choice == "4":
        # Idea 1: Trail Repair Kit & Spare Jerry Can
        if repair_kits > 0:
            repair_kits = repair_kits - 1
            condition = condition + 25
            fuel = fuel + 15
            if condition > 100:
                condition = 100
            if fuel > 100:
                fuel = 100
            print(f"You pulled your {full_rig} onto a flat rock, wrenched on the suspension, and dumped in the Jerry Can!")
            print("+25% Condition | +15% Fuel | 0 miles gained this turn.")
        else:
            print("You already used your Trail Repair Kit and Jerry Can! You wasted 3% fuel looking in the trunk.")
            fuel = fuel - 3
            
    else:
        # If the user types something other than 1, 2, 3, or 4
        print("Invalid gear selection! You idled on the trail and wasted 5% fuel.")
        fuel = fuel - 5

# --- CLEAN UP STATS FOR FINAL DISPLAY ---
# Keep fuel and condition from showing negative numbers on the final scoreboard
if fuel < 0:
    fuel = 0
if condition < 0:
    condition = 0

total_gas_used = 100 - fuel

# --- END OF GAME & BRAGGING RIGHTS REPORT ---
print("\n--------------------------------------------------------")
print("      /\\  /\\   TRAIL REPORT & BRAGGING RIGHTS   /\\  /\\  ")
print("-----/--\\/--\\----------------------------------/--\\/--\\-")

if miles_traveled >= goal_miles and fuel > 0 and condition > 0:
    print(f"STATUS: VICTORY! {driver_name}'s {full_rig} conquered the mountain!")
    
    # Calculate bonus points for remaining fuel, condition, and bigger rig difficulty bonus
    bonus_points = (fuel * 5) + (condition * 10) + (size_damage_mod * 25)
    final_score = trail_points + bonus_points
    
    # Determine Bragging Rights Badge based on condition and gas left
    if condition >= 80 and fuel >= 25:
        badge = "LEGENDARY TRAIL MASTER (Trail Rated Gold Badge)"
    elif condition >= 55:
        badge = "SEASONED OVERLANDER (Trail Rated Silver Badge)"
    else:
        badge = "MUDDY SURVIVOR (Trail Rated Bronze Badge)"
else:
    if fuel == 0:
        print(f"STATUS: GAME OVER - {driver_name}'s {full_rig} ran out of gas deep in the woods!")
    else:
        print(f"STATUS: GAME OVER - {driver_name}'s {full_rig} snapped an axle! Calling for a winch recovery.")
    
    final_score = trail_points
    badge = "STRANDED ROOKIE (Needs a Tow Strap)"

# Final Bragging Rights Scoreboard
print("--------------------------------------------------------")
print(f"Driver Name           : {driver_name}")
print(f"Custom Trail Rig      : {full_rig}")
print(f"Tires Aired Down      : {aired_down}")
print(f"Total Distance Driven : {miles_traveled} miles")
print(f"Net Gas Depleted      : {total_gas_used}% (Remaining Fuel: {fuel}%)")
print(f"Remaining Condition   : {condition}%")
print(f"Final Trail Score     : {final_score} points")
print(f"Earned Reward Rank    : {badge}")
print("--------------------------------------------------------")

# --- MOUNTAIN TRAIL LEADERBOARD ---
print("\n========================================================")
print("        MOUNTAIN WOODS OVERLANDING LEADERBOARD          ")
print("========================================================")

# Rival NPC scores and rigs to beat
score_1 = 1850
name_1 = "Rubicon_Rick (Red Jeep Wrangler JLU)"

score_2 = 1550
name_2 = "Moab_Mike (Sarge Green Wrangler TJ)"

score_3 = 1200
name_3 = "Muddy_Maya (Sting-Gray Tacoma TRD)"

score_4 = 650
name_4 = "Stock_Sam (Hydro Blue Gladiator JT)"

player_entry = f"{driver_name} ({full_rig}) [YOU]"

# Compare final_score to place the player in the exact right rank
if final_score >= score_1:
    print(f"1st Place: {player_entry} - {final_score} pts [NEW TRAIL RECORD!]")
    print(f"2nd Place: {name_1} - {score_1} pts")
    print(f"3rd Place: {name_2} - {score_2} pts")
    print(f"4th Place: {name_3} - {score_3} pts")
    print(f"5th Place: {name_4} - {score_4} pts")
elif final_score >= score_2:
    print(f"1st Place: {name_1} - {score_1} pts")
    print(f"2nd Place: {player_entry} - {final_score} pts")
    print(f"3rd Place: {name_2} - {score_2} pts")
    print(f"4th Place: {name_3} - {score_3} pts")
    print(f"5th Place: {name_4} - {score_4} pts")
elif final_score >= score_3:
    print(f"1st Place: {name_1} - {score_1} pts")
    print(f"2nd Place: {name_2} - {score_2} pts")
    print(f"3rd Place: {player_entry} - {final_score} pts")
    print(f"4th Place: {name_3} - {score_3} pts")
    print(f"5th Place: {name_4} - {score_4} pts")
elif final_score >= score_4:
    print(f"1st Place: {name_1} - {score_1} pts")
    print(f"2nd Place: {name_2} - {score_2} pts")
    print(f"3rd Place: {name_3} - {score_3} pts")
    print(f"4th Place: {player_entry} - {final_score} pts")
    print(f"5th Place: {name_4} - {score_4} pts")
else:
    print(f"1st Place: {name_1} - {score_1} pts")
    print(f"2nd Place: {name_2} - {score_2} pts")
    print(f"3rd Place: {name_3} - {score_3} pts")
    print(f"4th Place: {name_4} - {score_4} pts")
    print(f"5th Place: {player_entry} - {final_score} pts")

print("========================================================")