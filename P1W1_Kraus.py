# CTI 110 
# P1W1 - Math
# Kraus, A
# 9/8/26
# Do some math processing

# Part 1 - Exponents
print("-----Calculating Exponents-----")
print("n") # 2 newlines
base = int(input("Enter integar as a base value: "))
exponent = int(input("Enter integar as an exponent value: "))
result = base ** exponent # example, (3 ** 2) is 3 squared
print(f"{base} to the {exponent} power is {result}!!")

# Part 2 - ADDITION SUBTRACTION
print("-----Calculating Addition and Subtraction-----") 
print("n") # 2 newlines
# 3 numbers, start, add_this, sub_this
start = int(input("Enter a starting number: "))
#print("you typed: ", start)
add_this = int(input("Enter a number to add: "))
sub_this = int(input("Enter a number to subtract: "))   
# Calculate the answer
answer = start + add_this - sub_this
# Print the answer
print()
print() # That gives a 2 newlines, so would print("\n\n")
# Should look like: "10 + 4 is equal to 12"
print(start, "+", add_this, "-", sub_this, "is equal to", answer)
print(f"{start} + {add_this} - {sub_this} is equal to {answer}")
