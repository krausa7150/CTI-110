# Alex Kraus
# 09/10/26
# P1HW2
# Travel Budgets

print ("Enter budget:")
budget = int(input())
print ("Enter your travel destination:")
destination = input()
print ("Approximately, how much will you need for fuel?")
fuel_expenses = int(input())
print ("Approximately, how much will you need for accommodations/hotel?")
hotel_expenses = int(input())
print ("Lastly, how much will you need for food?")
food_expenses = int(input())
print("-----Travel Expenses-----") 
print("Location:", destination)
print("Initial Budget:", "$" + str(budget))
print("" * 30)
print("Fuel:", "$" + str(fuel_expenses))
print("Accommodation:", "$" + str(hotel_expenses))
print("Food:", "$" + str(food_expenses)) 
total_expenses = fuel_expenses + hotel_expenses + food_expenses
print("" * 30)
print("Remaining Balance:", "$" + str(budget - total_expenses)) 