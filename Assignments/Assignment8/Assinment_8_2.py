import sys
import os

filename = input("Enter the OS filename: ")
OS = []

try:
    with open(filename) as file:
        try:
            if os.stat(filename).st_size == 0:
                raise ValueError("The file is empty")
            for line in file:
                 line = line.replace("\n", "")
                 OS.append(line)
        except Exception as e:
            print(type(e), e)
            sys.exit()
        finally:
            file.close()

except FileNotFoundError as e:
    print(type(e), e)
    sys.exit()