# Ib 2nd rock paper sicssors game
import random
print("1 is rock, 2 is paper and 3 is sicssors")
player = input("what do you pick 1,2,3: ")
ai = random.randint(1,3)
if ai == 1:
    print("The ai choose rock")
if ai == 2:
    print("the ai choose paper")
if ai == 3:
    print("The ai choose sicssors")
if player == "1" and ai == 2:
    print("the ai won")