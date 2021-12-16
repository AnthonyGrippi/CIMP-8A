import random


# Get a random number between 1 and 9
randomNum = random.randint(1,9)
yourGuess = 3
count = 0


# Continue guessing until the giess is correct or the user types "exit"
while yourGuess != randomNum and yourGuess != "exit":
    yourGuess = input("Enter a gues between 1 to 9 or exit to end the game. ")

    # If the user types "exit", end the application
    if yourGuess == "exit":
        break

    # Cast the user's guess to an integer so it
    # can be used in the comparison below
    yourGuess = int(yourGuess)
    count += 1

    if yourGuess < randomNum:
        print("Too Low")

    elif yourGuess > randomNum:
        print("Too high")

    else:
        print("Right!!")
        print("You took only" , count , "tries")

input() # This will pause the app from exiting when running from command line.
