# Alex Kraus
# CTI-110
# 9/17/26
# P2HW1
# Travel Expenses Displays and Calculations

print ("Enter budget:")
budget = int(input())
print ("Enter your travel destination:")
destination = input()
print ("Approximately, how much will you need for fuel?")
fuel_expenses = int(input())
print ("Approximately, how much will you need for accommodations/hotel?")
hotel_expenses = int(input())
Accomadations = hotel_expenses
print ("Lastly, how much will you need for food?")
food_expenses = int(input())
print("-----Travel Expenses-----") 
print(f"{"Location:":<16}{destination:<15}")
print(f"{"Budget":<15} ${budget}")
print(f"{"Fuel:":<15} ${fuel_expenses:<15}")
print(f"{"Accommodation:":<15} ${hotel_expenses:<15}")
print(f"{"Food:":<15} ${food_expenses:<15}") 
print("-" * 25)
total_expenses = fuel_expenses + hotel_expenses + food_expenses
print("" * 30)
print("Remaining Balance:", "$" + str(budget - total_expenses)) 