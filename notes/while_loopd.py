# IB 2md while loop notes

#for nums in range(1,21):
    #print(nums)

#num = 1
#while num <= 20:
    #print(num)
    #numt = 1

import time
import random

# infinite loop part 1
#num = 1
#break_point = random.randint(1,20)
#while num <= 20:
    #print(num)
   # time.sleep(.10)
    #if num == 6:
        #break
    #num += 1

#print("the loop is over")

# infinite loop part 2
#num = 1
#break_point = random.randint(1,20)
#while num <= 20:
    #print(num)
    #time.sleep(.10)
    #if num == break_point:
        #break
    #num += 1
#else:
    #print("this loop exited by meeting the condition!")

#print("the loop is over")

# infinite loopp part 3
num = 0
break_point = random.randint(1,30)
while num < 20:
    num += 1
    if num == break_point:
        break
    elif num%2 != 0:
        continue
    print(num)
    time.sleep(.10)
else:
    print("this loop exited by meeting the condition!")

print("the loop is over")