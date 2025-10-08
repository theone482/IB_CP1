# Ib 2nd rock paper scissors game
import random

aiwons = 0
playerwons = 0

while True:
    print("\n1 is Rock, 2 is Paper, 3 is Scissors")
    print("4 to Quit Game, 5 to Show Wins")
    player = input("What do you pick (1, 2, 3, 4, 5): ")

    if player == "4":
        print("Thanks for playing!")
        break

    if player == "5":
        print(f"Computer wins: {aiwons} | Player wins: {playerwons}")
        continue

    if player not in ["1", "2", "3"]:
        print("Invalid choice. Try again.")
        continue

    ai = random.randint(1, 3)

    # Show choices
    choices = { "1": "Rock", "2": "Paper", "3": "Scissors" }
    print(f"You chose {choices[player]}, Computer chose {choices[str(ai)]}")

    # Game logic
    if str(ai) == player:
        print("It's a tie! Try again.")
    elif (player == "1" and ai == 3) or (player == "2" and ai == 1) or (player == "3" and ai == 2):
        print("You won!")
        playerwons += 1
    else:
        print("💻 The computer won.")
        aiwons += 1
