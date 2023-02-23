import random

# Define the options
options = ["rock", "paper", "scissors"]

# Define a function to get the user's choice
def get_user_choice():
    while True:
        user_choice = input("Choose rock, paper, or scissors: ")
        if user_choice in options:
            return user_choice
        else:
            print("Invalid choice. Please try again.")

# Define a function to get the computer's choice
def get_computer_choice():
    return random.choice(options)

# Define a function to determine the winner
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    elif user_choice == "rock":
        if computer_choice == "paper":
            return "computer"
        else:
            return "user"
    elif user_choice == "paper":
        if computer_choice == "scissors":
            return "computer"
        else:
            return "user"
    elif user_choice == "scissors":
        if computer_choice == "rock":
            return "computer"
        else:
            return "user"

# Main game loop
while True:
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    print(f"You chose {user_choice} and the computer chose {computer_choice}.")
    winner = determine_winner(user_choice, computer_choice)
    if winner == "tie":
        print("It's a tie!")
    else:
        print(f"The {winner} wins!")
    play_again = input("Do you want to play again? (y/n): ")
    if play_again.lower() != "y":
        break