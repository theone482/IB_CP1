# IB 2nd List notes
import random

names = ["Alex", "Katie", "Cora", "Andrew", "Jake", "Eric", 5,3.14, False]

print(names)
print(names[3])
#print(names[random.randint(1,len(names))])
print(random.choice(names))
names[-1] = "Xavier"
names.extend(["Treyson", "Tia"]) 
names += ["Joseph", "Israel", "Zee"]
names.remove(3.14)
number = names.index(5)
names.insert(3, "vienna")
names.pop(number)
print(names)

board = [[1,2,3],
        [4,5,6],
        [7,8,9]]

board[1][1] = "X"
print(board)
#list (changable, ordered0)
#tuple (not changable, ordered)
classes = ("bard", "monk", "barbarian", "paladin")

# Set (changable, unordered)
fruit = {"apple", "orange", "strawberry", "kiwi"}
print(fruit)