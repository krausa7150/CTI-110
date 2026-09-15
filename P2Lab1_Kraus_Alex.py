# Alex Kraus
# CTI 110
# 09/15/26
# P2Lab1
# Get Radius, Calculate, Display Radius, Circumference, and Area

PI = 3.14159
radius = float(input("What is the radius of the circle? "))
print(f"The radius is {radius:.1f}.")

# Calculation -- find diameter, circumference, and area
# diameter = 2*r, circumference = 2*pi*r, area = pi*r*r
diameter = 2 * radius
circumference = 2 * PI * radius
area = PI * radius * radius

#Output -- .1f, .2f, 3.f
print(f"The diameter is {diameter:.1f}.")
print(f"The circumference is {circumference:.2f}")
print(f"The area is {diameter:.3f}")   
