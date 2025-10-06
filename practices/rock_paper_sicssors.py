# Ib 2nd rock paper sicssors game
import random

while True:
    print("1 is rock, 2 is paper and 3 is sicssors and 4 is to quit game, 5 to show me the wins of th computer and me")
    player = input("what do you pick 1,2,3,4,5: ")
    ai = random.randint(1,3)
    aiwons = 1
    playerwons = 1
    

    if ai == 1 and player == "1" :
        print("Tie try again")
    elif ai == 2 and player == "1":
        print("The Computer won")
        aiwons += 1
    elif ai == 3 and player == "1":
        print("You won")
        playerwons+= 1
    elif ai == 1 and player == "2":
        print("You won")
        playerwons+= 1
    elif ai == 2 and player == "2":
        print("Tie try again")
    elif ai == 3 and player == "2":
        print("The computer won")
        aiwons+= 1
    elif ai == 1 and player == "3":
        print("the computer won")
        aiwons.append()
    elif ai == 2 and player == "3":
        print("you won")
        playerwons.append()
    elif ai == 3 and player == "3":
        print("Tie try again")
    if player == "5":
        print(f" the computer wins:{aiwons} and player wins:{playerwons}")
    if player == "4":
        break