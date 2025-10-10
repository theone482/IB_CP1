# IB 2nd password strength checker
# tell them thge reciermemnctes for password
print("make a psssword that 1.Has 8 characters\t 2. Has at least one lowercase\t 3. Has one uppercase\t 4. Has at lest one number\t 5.Has one special character\t")
#make a input called password
password = input("please write you password here: ")
#if password== len 8 print you go the leng6th right
if len(password) >= 8:
    print("good job you got 8 or more character in your password")
else:
    print("you should put more characters")
#if password has uppercase letter print you have uppercode good
if password == "A" or "B" or "C" or "D" or "E" or "F" or "G" or "H"or "I" or "J" or "K" or "L" or "M" or "N" or"O" or "P" or "Q" or "R" or "S" or "T" or "U" or "V" or "W" or "X" or "Y" or "Z":
    print("your password had a uppercase good")
else:
    print("you should put a uppercase in your password")
# if password has under case print you have lower csae
if password == "hi":
    print("hi")
# if password has nunber primt good job oyu bhave number in it
# if password has specil character then print you got it
# if password has all five print your password is very strong 5/5
# if not print how many you got right 
