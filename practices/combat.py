# IB 2nd cobat program
import random
name = input("What is your name: ").strip().title()
fighter = input("1 if you are fighter\t 2 if you are a mage\t 3 if you are a rouge\t what are you: ")
monster_hp = 35
atack_bounds = 3
damage_bounds = 4
wild_attck = random.randint(1,10)
stat_one = random.randint(1,20) +random.randint(1,20) +random.randint(1,20)
stat_two = random.randint(1,8) +random.randint(1,8) +random.randint(1,8)
while True:
    if fighter == "1":
        figh_hp = 30
        figh_def = 14
        figh_atack = stat_one + atack_bounds
        figh_dam = stat_two + damage_bounds
        print(f"Your stats:\t fighter attack = {figh_atack}, fighter damage = {figh_dam}, fighter health = {figh_hp}, and fighter defense = {figh_def}")
    elif fighter == "2":
        figh_hp = 20
        figh_def = 16
        figh_atack = stat_one + atack_bounds
        figh_dam = stat_two + damage_bounds
        print(f"Your stats:\t mage attack = {figh_atack}, mage damage = {figh_dam}, mage health = {figh_hp}, and mage defense = {figh_def}")
    elif fighter == "3":
        figh_hp = 25
        figh_def = 15
        figh_atack = stat_one + atack_bounds
        figh_dam = stat_two + damage_bounds
        print(f"Your stats:\t rouge attack = {figh_atack}, rouge damage = {figh_dam}, rouge health = {figh_hp}, and rouge defense = {figh_def}")
    else:
        print("sorry error try again")

    turn = random.randint(1,2)
    while True:
        if turn == 1:
            print("It is your turn")
            atack = input("what attack do you want to do 1. A norma attack 2. wild attack(you can double the damage but oyu will also take damage) 3. drink a healing potion(9 health) 4.Flee(You may or may not get away) 5.defense: ")
            if atack == "1":
                monster_hp -= figh_atack
                print(f"the monster now has {monster_hp} health")
            elif atack == "2":
                monster_hp -= figh_atack *2
                figh_hp -= wild_attck
                print(f"the monster now has {monster_hp} health")
                print(f"You now have {figh_hp} health")
            elif atack == "3":
                figh_hp += 9
                print(f"player health is now {figh_hp}")
            if monster_hp <= 0 and figh_hp >= 1:
                print("Monster died, you won")
                break
            elif figh_hp <= 0 and monster_hp >= 1:
                print("You died, Monster won")
                break
            elif monster_hp <= 0 and figh_hp <= 0:
                print("you both died no one won")
                break
        elif turn == 2:
            print("it is the monster turn")
