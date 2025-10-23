# IB 2nd password strength checker
import string
# tell them the reciermemnctes for password
print("make a password that 1.Has 8 characters\t 2. Has at least one lowercase\t 3. Has one uppercase\t 4. Has at lest one number\t 5.Has one special character\t")
score_strength = 0
#make a input called password
password = input("please write you password here: ")
#if password== len 8 print you go the length right
if len(password) >= 8:
    print("Good job! Your password has 8 or more characters.")
    score_strength += 1
else:
    print("Your password should have at least 8 characters.")
#if password has uppercase letter print you have uppercode good
if any(char.isupper() for char in password):
    print("Your password contains an uppercase letter.")
    score_strength += 1
else:
    print("Add at least one uppercase letter.")
# if password has under case print you have lower csae
if any(char.islower() for char in password):
    print("Your password contains a lowercase letter.")
    score_strength += 1
else:
    print("Add at least one lowercase letter.")
# if password has nunber print good job you have number in it
if any(char.isdigit() for char in password):
    print("Your password contains a number.")
    score_strength += 1
else:
    print("Add at least one number.")
# if password has special character then print you got it
special_characters = string.punctuation
if any(char in special_characters for char in password):
    print("Your password contains a special character.")
    score_strength += 1
else:
    print("Add at least one special character.")
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

