# CTI 110 
# P1W1 - Math
# Kraus, A
# 9/8/26
# Do some math processing

# Part 1 - Exponents

# Part 2 - ADDITION SUBTRACTION
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
