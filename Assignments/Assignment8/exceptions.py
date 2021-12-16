import sys

# Prompt for the filename
filename = input("Enter the OS filename: ")

OS = []

try:
    with open("A:\\Python Projects\\Assignments\\Assignment8\\Temp" + filename) as file:
        for line in file:
            # add the OS to the list
            line = line.replace("\n", "")
            OS.append(line)
except FileNotFoundError as e:
    # Display File not found error
    print("FileNotFoundError", e)
    sys.exit()
except OSError as e:
    # Display an error reading file message
    print("OSError", e)
except Exception as e:
    # Display a generic error message
    print(type(e), e)
    sys.exit()