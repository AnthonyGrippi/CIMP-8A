print("Enter 'exit' whem you\'re done. \n")
while True:
    data = input("Enter an integer to square: ")
    if data == "exit":
        break
    i = int(data)
    print(i, "squared is", i * i, "\n" )
print("The program has ended")