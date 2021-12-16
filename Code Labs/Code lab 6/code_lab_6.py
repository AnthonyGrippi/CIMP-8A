import card_tester as deck
import db

# ================================================================ # 
# welcome_message prints the welcome message to the game
# **************************************************************** #
# Parameters:
# Returns:
# ================================================================ # 
def welcome_message():

    print("BLACKJACK!")
    print("Blackjack payout is 3:2")
    print("Enter \'x\' for bet to exit\n")

# ================================================================ # 
# play_player_hand prompts the user to hit or stand, adds a card
# depending on players choice if you bust you lose.
# **************************************************************** #
# Parameters: List deck_of_cards[], List hand[]
# Returns: List hand[]
# ================================================================ # 
def play_player_hand(deck_of_cards, hand):

    while True:
        player_choice = input("Hit or Stand? (h / s):")
        print()

        if player_choice.lower() == "h":
            deck.add_card(hand, deck.deal_card(deck_of_cards))
            display_cards(hand, "YOUR CARDS: ")

            if deck.calculate_hand_points(hand) > 21:
                break

        elif player_choice.lower() == "s":
            break

        else:
            print("Not a valid choice, please try again.")

    return hand

# ================================================================ #
# starting_money validates the starting amount the player inputted
# between 5 to 10,000 inputing invalid data prompts the
# the user to try again
# **************************************************************** #
# Parameters: float starting_player_amount
# Returns: float starting_player_amount
# ================================================================ #
def get_starting_amount():

    player_money = db.read_money()
    if player_money < 5:
        print("You don't have enough to play, resetting back to 1000.")
        player_money = 1000
        db.write_money(player_money)

    print("Money", player_money)
    print()
    return player_money
# ================================================================ #
# player_bet propmts the user to place a valid bet 
# where 5 <= bet < 1000 and bet <= current_money
# prompt the user to enter valid data again if they did not
# **************************************************************** #
# Parameters: float float bet_amount, float current_money
# Returns: float bet_amount
# ================================================================ #   
def player_bet(current_money):

    while True:
        bet_amount = 0
        bet_amount = input("Bet amount: ")

        if str(bet_amount) == "x":
            break
        
        if float(bet_amount) == 5 and current_money == 5:
            print("check bet")

        if float(bet_amount) < 5:
            print("The minimum bet is 5.")

        elif float(bet_amount) > 1000:
            print("The maximum bet it 1,000.")

        elif float(bet_amount) > float(current_money):
            print("You don't have enough money to make that bet")

        return bet_amount
    return bet_amount

# ================================================================ #
# display_cards displays the hand of eithe the dealer or player
# **************************************************************** #
# Parameters: List hand[], String Title
# Returns: 
# ================================================================ #   
def display_cards(hand, title):

    print(title.upper())
    for card in hand:
        print(deck.display_card(card))
    print()

# ================================================================ #
# display_outcome displays the outcome of the round, the player
# either loses, wins or get BlackJack depending on the cards drawn
# **************************************************************** #
# Parameters: Int player_points, List player_hand[], Int deler_points
# List dealer_hand[], Float bet_amount, Float current_money
# Returns: float current_money
# ================================================================ #   
def display_outcome(player_points, player_hand, dealer_points, dealer_hand, bet_amount, current_money):

    if player_points > 21:
        print("Sorry, you busted. You lose.")
        current_money -= float(bet_amount)

    elif player_points == 21 and len(player_hand) == 2:

        if dealer_points == 21 and len(dealer_hand) == 2:
            print("Bad luck, you both got a BlackJack! Nobody wins.")

        else:
            print("BLACKJACK")
            current_money += float(bet_amount) * 1.5

    elif dealer_points == 21 and len(dealer_hand) == 2:
        print("The dealer got a BlackJack, you Lose.")
        current_money -= float(bet_amount)

    elif dealer_points > 21:
        print("The dealer busted, you won!")
        current_money += float(bet_amount)

    elif player_points > dealer_points:
        print("You won!")
        current_money += float(bet_amount)
        
    elif dealer_points > player_points:
        print("You lose.")
        current_money -= float(bet_amount)

    else:
        print("You and the dealer pushed.")

    return current_money

def main():

    welcome_message()

    current_money = get_starting_amount()


    while True:

        bet_amount = player_bet(current_money)
        if bet_amount == "x":
            break
        print()
        
        deck_of_cards = deck.get_deck()
        deck.shuffle(deck_of_cards)

        dealer_hand = deck.get_empty_hand()
        player_hand = deck.get_empty_hand()

        deck.add_card(player_hand, deck.deal_card(deck_of_cards))
        deck.add_card(dealer_hand, deck.deal_card(deck_of_cards))
        deck.add_card(player_hand, deck.deal_card(deck_of_cards))

        display_cards(dealer_hand, "DEALER'S SHOW CARD:")
        display_cards(player_hand, "YOUR CARDS:")

        player_hand = play_player_hand(deck_of_cards, player_hand)

        deck.add_card(dealer_hand, deck.deal_card(deck_of_cards))
        if deck.calculate_hand_points(player_hand) <= 21:

            while deck.calculate_hand_points(dealer_hand) < 17:

                deck.add_card(dealer_hand, deck.deal_card(deck_of_cards))
        
        display_cards(dealer_hand, "DEALER'S CARDS:")

        # Display points
        dealer_points = deck.calculate_hand_points(dealer_hand)
        player_points = deck.calculate_hand_points(player_hand)
        print("YOUR POINTS:\t\t", player_points)
        print("DEALER'S POINTS:\t", dealer_points)
        print()

        current_money = display_outcome(player_points, player_hand, dealer_points, dealer_hand, bet_amount, current_money)

        print("Money: ", round(current_money, 2))
        print()

        db.write_money(current_money)

        if current_money < 5:
            print("You are out of money.")
            break

        play_again = input("Play again? (y / n): ")

        if play_again.lower() != "y":
            print("Come agin soon.")
            break

    print("Bye!")

if __name__ == "__main__":
       main()
