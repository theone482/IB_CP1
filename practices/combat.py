# IB 2nd cobat program
import random
name = input("What is your name: ").strip().title()
fighter = input("1 if you are fighter\t 2 if you are a mage\t 3 if you are a rouge\t what are you: ")
monster_hp = 35
atack_bounds = 3
damage_bounds = 4
stat_one = random.randint(1,20) +random.randint(1,20) +random.randint(1,20)
stat_two = random.randint(1,8) +random.randint(1,8) +random.randint(1,8)
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

