

OS = ["Mac OS", "Windows", "Android", "Linux"]

# Open the file in overwtrite mode
with open("A:\\Python Projects\\Assignments\\Temp\\os.txt", "w") as file:
    # write 1 element at a time
    for item in OS:
        file.write(item + "\n")
    
new_OS = []
# open the file in read(default) mode
with open("A:\\Python Projects\\Assignments\\Temp\\os.txt") as file:
    # read 1 element at a time
    for line in file:
        line = line.replace("\n", "")
        new_OS.append(line)

print(new_OS)