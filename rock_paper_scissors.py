# mini game: rock, paper, scissors- 1st draft

# 1. Invite user to play. Receive raw input: rock, paper, scissors or quit.
# 	(Confirm valid input)
# 2. Generate random choice for computer.
# 3. Compare choices and display result.
# 4. Offer another round and keep a tally.

# syntax issues


user_choice = ""

request_player_input = "Please type: 'rock', 'paper' or 'scissors', 'score' for the score or 'quit' to leave. "


# Function to take in the user's choice
def player_input():
    player_selection = raw_input(request_player_input)
    # This loop verifies that the input is correct
    while player_selection not in ["rock", "paper", "scissors", "score", "quit"]:
        player_selection = raw_input("Oops, let's try that again.\n" + request_player_input)

    # This conditional allows the player to exit at any time and close the program
    if player_selection == "quit":
        exit()
    else:
        return player_selection


# Updates the wins count and displays a win message
def victory():
    print "Congrats, you won!"
    return 1


# Updates the losses count and displays a message
def defeat():
    print "Sorry, you lost. Better luck next time!"
    return 1


# Updates the ties count and displays a message
def tie():
    print "It's a tie!"
    return 1


def display_score():
    print ("Wins so far: " + str(wins) + ", losses: " + str(losses) + ", ties: " + str(ties) + ".")


# This displays the current score and offers the choice of another round
def keep_playing():
    print ("Wins so far: " + str(wins) + ", losses: " + str(losses) + ", ties: " + str(ties) + ".")
    print "Do you want to play again? "
    return player_input()


# def main():



    wins = losses = ties = 0
    print "Beginning of main. Wins: " + str(wins) + ", losses: " + str(losses) + ", ties: " + str(ties)
    print "Hi!"

    print "Welcome to Rock, Paper, Scissors!"

    # First off we take in the player's choice
    user_choice = player_input()

    # In case the player is interested in the score:
    if user_choice == "score":
        user_choice = keep_playing()
    # By this point, the quit and score options have both been considered. On to the game!
    while user_choice in ["rock", "paper", "scissors", "score"]:

        # Here we generate the program's choice
        import random
        roshambo = ["rock", "paper", "scissors"]
        computer_choice = random.choice(roshambo)

        # Displaying both choices to the player
        if (user_choice != "score"):
            print "You chose " + user_choice + " and Python chose " + computer_choice + "."

        # This conditional handles the actual game, first handling the tie scenario...
        if user_choice == computer_choice:
            ties += tie()
            print " Ties: " + str(ties)

        # ...and then all the others individually:
        elif user_choice == "rock":
            if computer_choice == "paper":
                losses += defeat()
                print " Losses: " + str(losses)
            else:
                wins += victory()
                print " Wins: " + str(wins)

        elif user_choice == "paper":
            if computer_choice == "rock":
                wins += victory()
                print " Wins: " + str(wins)
            else:
                losses += defeat()
                print " Losses: " + str(losses)

        elif user_choice == "scissors":
            if computer_choice == "rock":
                losses += defeat()
                print " Losses: " + str(losses)
            else:
                wins += victory()
                print " Wins: " + str(wins)

        # Once each round is up, the player is offered the choice to play again. If player chooses to remain in the game,
        # Wether or not they've looked at the score, they'll be returned to the game loop when they've selected their weapon.
        user_choice = keep_playing()

# if __name__ == "__main__":
#     main()
