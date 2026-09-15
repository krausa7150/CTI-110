# Alex Kraus
# CTI 110  
# 9/15/26
# P2Lab2 - Directories

# Car directory that lets us see mpg
# From that mpg, find gallons burned per X miles.

cars = {
    "Camaro": 18.21,
    "Prius": 52.36,
    "Model S": 110,
    "Silverado": 26,
}
print(cars)
car_keys = cars.keys()
print(car_keys)
# Choose car
car=input("Enter a vehicle to see its mpg: ")
mpg = cars[car]
print(f"The MPG of {car} is {mpg} miles per gallon. ")
# Ask user for miles, output gas used
miles = float(input("How many miles will drive? "))
gallons_used = miles / mpg # miles divided by miles per gallon gives units in gallons
print(f"Driving {car} for {miles} miles will use {gallons_used:.2f} gallons of gas.")