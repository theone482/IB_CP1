# IB 2nd password strength checker
# tell them the reciermemnctes for password
print("make a psssword that 1.Has 8 characters\t 2. Has at least one lowercase\t 3. Has one uppercase\t 4. Has at lest one number\t 5.Has one special character\t")
score_strength = 0
#make a input called password
password = input("please write you password here: ")
#if password== len 8 print you go the length right
if len(password) >= 8:
    print("good job you got 8 or more character in your password")
    score_strength += 1
else:
    print("you should put more characters")
#if password has uppercase letter print you have uppercode good
if password >= "A" and password <= "Z":
    print("your password had a uppercase good")
    score_strength += 1
else:
    print("you should put a uppercase in your password")
# if password has under case print you have lower csae
if password <= "a" and password <="z":
    print("You have a lowercase good job")
    score_strength += 1
else:
    print("put a lowercase letter")
# if password has nunber print good job you have number in it
if password >= "0":
    print("you have a number great")
    score_strength += 1
else:
    print("you don't have a a number")
# if password has special character then print you got it
if password >= ("!@#$%^&*()_-+,=[]`~;<>?."):
    print("you have a special caracter good.")
    score_strength += 1
else:
    print("you should put a special characters")
# if password has all five print your password is very strong 5/5
# # if not print how many you got right 
if score_strength == 5:
    print(f"you have a very strong password, strength score == {score_strength}")
elif score_strength == 4:
    print(f"You have a strong password, strength score = {score_strength}")
elif score_strength == 3:
    print(f"You havr a moderate password, strength score = {score_strength}")
elif score_strength == 2:
    print(f"hYou have a weak password, strength score = {score_strength}")
elif score_strength == 1:
    print(f"You have a weak password, strength score = {score_strength}")
else:
    print("error try again")

