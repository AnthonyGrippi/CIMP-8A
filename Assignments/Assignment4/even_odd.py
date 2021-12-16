def display_message():
    print("Even or Odd Checker\n")


def even_odd(number):
    if number % 2 == 0:
        print("This is an even number.")
    else:
        print("This is an odd number.")


def main():
    display_message()

    number = int(input("Enter an integer:\t"))

    even_odd(number)


if __name__ == "__main__":
    main()