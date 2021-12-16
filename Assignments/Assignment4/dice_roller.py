import random

def roll_die():
    die = random.randint(1, 6)
    return die

def main():
    print("Dice Roller\n")

    again = input("Roll the dice? (y/n):\t")

    while again == "y":
        die_1 = roll_die()
        print("\nDie 1:\t" + str(die_1))

        die_2 = roll_die()
        print("Die 2:\t" + str(die_2))

        total = die_1 + die_2
        print("Total: " + str(total))

        if die_1 == 1 and die_2 == 1:
            print("Snake eyes!")

        elif die_1 == 6 and die_2 == 6:
            print("Boxcars!")

        again = input("\nRoll the dice? (y/n):\t")


if __name__ == "__main__":
    main()