# IB 2nd for loops
import time

nums = [6,51,61,94,351,946,5489,4,654,684]

for num in nums:
    div = num/2
    if div > 100:
        print(f"{div} is half of {num}. and it is still a large number!")
    else:
        print(num)

print("we completed all the number!")
time.sleep(3)
for x in range(0,100):
    print(x)
time.sleep(3)

print("count by twos")
for x in range (2,11,2):
    print(x)
time.sleep(3)

print("count down")
for x in range(10,0, -1):
    print(x)
    time.sleep(1)