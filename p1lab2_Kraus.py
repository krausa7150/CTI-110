# CTI 110
# P1LAB2
# Kraus, A
# 9/3/26  

# Fictional Store -- Pick three things.
# product_name, product_price, product_quantity.

# Hard coding sets value directly.
product_name = "Jeep Badge"
product_count = 1
product_price = 19.99

# Instead ask the user with input()
# Input
print("STORE SETUP")
print("_" * 10) # ten _ in a row
product_name = input("Enter product name: ")
product_count = input( "Enter product count: ")
product_price = input("Enter unit price: ")

# Processing
product_count = int(product_count) #Covert string to integer: "100" -> 100
product_price = float(product_price) #Convert string to float: "3.25" -> 3.25
total = product_count * product_price # Requires two numbers, returns a third number. 

# Output
print("CUSTOMER INTERFACE")
print("_" * 10) # ten _ in a row
print ("Welcome to the", product_name, "store")
print("We have", product_count, product_name, "(s) at $", product_price, "each.")
print("Your total is: $", total)
