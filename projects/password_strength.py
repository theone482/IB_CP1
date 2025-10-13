# IB 2nd password strength checker
# tell them thge reciermemnctes for password
print("make a psssword that 1.Has 8 characters\t 2. Has at least one lowercase\t 3. Has one uppercase\t 4. Has at lest one number\t 5.Has one special character\t")
strength_score = 0
one = 1
#make a input called password
password = input("please write you password here: ")
#if password== len 8 print you go the leng6th right
if len(password) >= 8:
    print("good job you got 8 or more character in your password")
    strength_score + 1
else:
    print("you should put more characters")
#if password has uppercase letter print you have uppercode good
if password >= "A" and password <= "Z":
    print("your password had a uppercase good")
    strength_score + one
else:
    print("you should put a uppercase in your password")
# if password has under case print you have lower csae
if password >= "a" and password <="z":
    print("You have a lowercase good job")
    strength_score + one
else:
    print("put a lowercase letter")
# if password has nunber primt good job oyu bhave number in itH
if password >= "0":
    print("you have a number great")
    strength_score + one
else:
    print("you don't have a a number")
# if password has specil character then print you got it
if password == ["!@#$%^&*()_-+,=[]`~;<>?."]:
    print("you have a special caracter good.")
# if password has all five print your password is very strong 5/5
if strength_score == 5:
    print(f"you have a very strong password, strength score == {strength_score}")
elif strength_score == 4:
    print("hi")
elif strength_score == 3:
    print("hi")
elif strength_score == 2:
    print("hi")
elif strength_score == 1:
    print("hi")
else:
    print("error try again")
# if not print how many you got right 
