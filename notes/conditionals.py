# IB end conditions
import random
monster_hp = 30
dmg_modifier = 2
atack_bounds = 3
player_hp = 25

roll = random.randint(1,20)

if roll == 20:
    print(f"You rolled a crit! double your damage.")
    atack = random.randint(1,8) + dmg_modifier
    monster_hp -= atack
    print(f"you did {atack} damage to monster!")
elif roll+atack_bounds > 10:
    print(f"You hit!")
    atack = random.randint(1,8) + dmg_modifier
    monster_hp -= atack

    print(f"you did {atack} damge to monster!")
elif roll <= 10:
    if roll ==1:
        print(f"you roll a critical failure! the moster gets a free attack!")
        damage = (random.randint(1,10) +2)
        player_hp -= damage
        print(f"you took {damage} you now have {player_hp} HP.")
    else:
        print(f"you missed!")
else:
    print("that should be possible")

print("your turn is over.") 

if True:
    print("this makes more sense")
else:
    print("I don't know how we got here")

if False:
    print("I don't know how we got here")
else:
    print("This ,makes more sense")

if monster_hp and monster_hp > 0:
    print("It is the moster turn")
else:
    print("the moster is dead")
