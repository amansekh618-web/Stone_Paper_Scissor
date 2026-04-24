# stone_paper_scissors.py

import random

# Function to get computer choice
def get_computer_choice():
    choices = ["stone", "paper", "scissors"]
    return random.choice(choices)

# Function to decide winner
def decide_winner(user, computer):
    if user == computer:
        return "Draw"
    
    elif (user == "stone" and computer == "scissors") or \
         (user == "paper" and computer == "stone") or \
         (user == "scissors" and computer == "paper"):
        return "User"
    
    else:
        return "Computer"

# Main game function
def play_game():
    print("Stone Paper Scissors Game")
    print("--------------------------")
    
    while True:
        user_choice = input("Enter stone, paper, or scissors: ").lower()
        
        if user_choice not in ["stone", "paper", "scissors"]:
            print("Invalid input. Please try again.")
            continue
        
        computer_choice = get_computer_choice()
        
        print("Computer chose:", computer_choice)
        
        result = decide_winner(user_choice, computer_choice)
        
        if result == "Draw":
            print("Result: It's a draw!")
        elif result == "User":
            print("Result: You win!")
        else:
            print("Result: Computer wins!")
        
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print("Game Over")
            break

# Run the program
play_game()