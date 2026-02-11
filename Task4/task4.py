print("this is Task4")

import random
choices =["rock","paper","scissors"]

while True:
 players = int(input("enter the number of players (1 or 2): "))
 if players == 1:
    user = input("Enter rock, paper, or scissors: ")
    computer = random.choice(choices)
    print("Computer chose:", computer)

 elif players == 2:
    user = input("Enter rock, paper, or scissors: ").lower().strip()
    computer = input("Player 2 - enter rock, paper, or scissors: ").lower().strip()


 else:
    print("Invalid number of players")

 if user == computer:
    print("It's a tie!")

 elif (user == "rock" and computer == "scissors") or \
     (user == "scissors" and computer == "paper") or \
     (user == "paper" and computer == "rock"):
    print("User/Player 1 wins!")

 else:
    print("Computer/Player 2 wins!")

 again = input("Do you want to play again? (yes/no): ").lower()
 if again == "no":
        print("Thanks for playing!")
        break
