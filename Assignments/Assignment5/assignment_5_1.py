
# create an empty list
items = []

# create s a list with repreating values
counts = [0] * 3            # same as [0, 0, 0]

# creates a list with items loaded
cars = ["Porsche", "Ford", "Mercedes"]

print("The second car in the list is a " + cars[1])

# update the second car in the list
cars[1] = "BMW"
print("After update, the second car is the list is now a " + cars[1])

# add a new car to the end of the list
cars.append("Lexus")
print("A new car was added to the end of the list: " + cars[len(cars) - 1])

# insert a new car int othe 2nd position of the list
cars.insert(1, "Honda")
print("After insert, the car in the list is now a " + cars[1])

# remove a car from the list = by value
cars.remove("Porsche")
print("The list element was deleted so the second car in the list is now a " + cars[1])

# remove a car from the list = by index
cars.pop(1)
print("The car in the second position was deleted...")
print("The car in the second position is now a " + cars[1])

print()

# process to find a car in the list
car = "Honda"
if car in cars:
    print("There is a " + car + " in the list")

print()

print("The list contains " + str(len(cars)) + " item in the list")

# process to display all cars in the list
print("Processing with a for loop")
for car in cars:
    print("\t", car)

print()

print("Processing with a while loop")
i = 0
while i < len(cars):
    print("\t", cars[i])
    i += 1