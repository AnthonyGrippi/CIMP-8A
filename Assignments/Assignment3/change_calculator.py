print("Change Calculator\n")

again = "y"
while again.lower() == "y":
    cents = int(input("Enter number of cents (0-99): "))

    quarters = int(cents / 25)
    if quarters >= 0:
        cents -= quarters * 25
    print("Quarters:\t" + str(quarters))

    dimes = int(cents / 10)
    if dimes >= 0:
        cents -= dimes * 10
    print("Dimes:\t\t" + str(dimes))

    nickels = int(cents / 5)
    if nickels >= 0:
        cents -= nickels * 5
    print("Nickels:\t" + str(nickels))

    print("Pennies:\t" + str(cents))

    again = input("\nContinue? (y/n): ")

print("Bye!")
