# IB 2nd random number notes
import random

#exampkes of random numnbers
print(random.random()) # float between 0 and 1
print(random.randint(1, 100)) 


name = input("what is your name: \n").strip().title()

#random stat creater D&D
stat_one = random.randint(1,6) +random.randint(1,6) +random.randint(1,6)
stat_two = random.randint(1,6) +random.randint(1,6) +random.randint(1,6)
stat_three = random.randint(1,6) +random.randint(1,6) +random.randint(1,6)
stat_four = random.randint(1,6) +random.randint(1,6) +random.randint(1,6)
stat_five = random.randint(1,6) +random.randint(1,6) +random.randint(1,6)
stat_six = random.randint(1,6) +random.randint(1,6) +random.randint(1,6)
stat_seven = random.randint(1,6) +random.randint(1,6) +random.randint(1,6)

print(f"Your stat options are: {stat_one}, {stat_two}, {stat_five}, {stat_six}, {stat_five}, {stat_three}, {stat_seven}")

strength = int(input("which stat are you making your strength: "))