# Alex Kraus
# CTI 110
# 10/08/26
# P4Lab2

#warm ups
for number in (1,2,3,4):
    print(number)
for number in range (5):
    print (number)
for beer in range(99,0,-1):

# validate (loop) - number must be 0 and 12
    while multiplier < 0 or multiplier > 12: 
     print("That is not a valid answer." )
    multiplier = int(input("Enter a number 0-12: "))

# print the times table header
print("Multiplication Table")
print ("-"*20)
# print the times table loop
for number in range(1, 13):
    
#print(multiplier, "*", number, "=", number*multiplier)
print(f"{multiplier}*{number}= {number*})

# ask if they want repeat
again = input ("Run again? (yes/no)")