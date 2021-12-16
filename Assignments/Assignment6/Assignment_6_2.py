
# open a file in th write mode (overwrite)
from os import waitpid


file = open("A:\\Python Projects\\Assignments\\Temp\\hello.txt", "w")

# write to the file
file.write("Hello World\n")
file.write("From Anthony")

# close the file
file.close()

print("This will read and then print the entire file")
with open("A:\\Python Projects\\Assignments\\Temp\\hello.txt") as file:
    for line in file:
        print(line, end="")

print("\n")

# Read the entire file as a list
print("This will read the file as list and then print 1 list item at a time")
with open("A:\\Python Projects\\Assignments\\Temp\\hello.txt") as file:
    listItems = file.readlines()
    for item in listItems:
        print(item, end="")

print("\n")

# Read and print thefile 1 line at a time
print("This will read and print the file 1 line at a time")
with open("A:\\Python Projects\\Assignments\\Temp\\hello.txt") as file:
    line = file.readline()
    print(line, end="")
    line = file.readline()
    print(line)