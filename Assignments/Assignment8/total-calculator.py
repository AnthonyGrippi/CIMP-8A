print("The Calculator program")

while True:
    try:
        price = float(input("Enter the price: "))
        break

    except ValueError:
        print("Invalid deciman number. Please Try again.")

while True:
    try:
        quantity = int(input("Enter quntity: "))
        break

    except ValueError:
        print("Invalid integer. Please try again")

print()
print("PRICE:\t\t" + str(price))
print("QUANTITY:\t" + str(quantity))
print("TOTAL:\t\t" + str(price * quantity))