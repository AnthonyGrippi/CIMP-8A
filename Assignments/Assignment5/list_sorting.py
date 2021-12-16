cars = ["Porsche", "Ford", "Mercedes"]

print("Unsorted List")
for car in cars:
    print(car)

print()
print("Sorted List - Ascending")
cars.sort()
for car in cars:
    print(car)

print()
print("Sorted List - Decending")
cars.sort()
cars.reverse()
for car in cars:
    print(car)

cars = ["Porsche", "Ford", "Mercedes", "Porsche", "BMW"]

print()
print("The Porsche occurs " + str(cars.count("Porsche")) + " times")