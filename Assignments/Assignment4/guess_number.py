import random

def display_title():
    print("Guess the number\n")
    print("I'm thinging of a number from 1 to 10\n")


def play_game():
    ran_number = random.randint(1, 10)
    your_guess = 11
    count = 0

    while your_guess != ran_number:
        your_guess = int(input("Your guess:\t"))
        count += 1

        if your_guess < ran_number:
            print("Too low.")
        
        if your_guess > ran_number:
            print("Too high.")
        
        if your_guess == ran_number:
            print("You guessed it in " + str(count) + " tries\n")


def main():
    choice = "y"
    display_title()

    while choice.lower() == "y":
        play_game()
        choice = input("Would you like to play again? (y/n): ")

    print("Bye!")

if __name__ =="__main__":
    main()
