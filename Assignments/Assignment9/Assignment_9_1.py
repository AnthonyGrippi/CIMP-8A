import math as m

num1 = int(input("Input a number: "))
num2 = int(input("Input another number: "))

print()

# the power function
print(str(num1) + " to the power of " + str(num2) + " is " + str(m.pow(num1, num2)))

# the square toot function
print("The square root of " + str(num1) + " is " + str(m.sqrt(num1)))

# the ceiling function
print("The nearest integer (rounded up) to " + str(num1/num2) + " is " + str(m.ceil(num1/num2)))

# the floor function
print("The nearest integer (rounded up) to " + str(num1/num2) + " is " + str(m.floor(num1/num2)))

# calculate the area of the curcle using the pi function
print("The are of the circle with radius " + str(num1) + " is: " + str(m.pi * num1**2))
